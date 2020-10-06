import random
from typing import Dict, Generator

import pytest

from app.testutil import fakeChinese


# -- helper functions
# TODO: write a custom faker provider for course
# https://github.com/joke2k/faker#how-to-create-a-provider
def gen_course_data_nctu():
    def _timelocations():
        timeslots = ["1A5CD", "2CDX", "3GH4E", "4G"]

        # M-b09: 管理一館地下室
        locations = ["EC012", "F210", "M-b09", "AB101"]
        return [
            {"time": {"kind": "nctu", "value": ts}, "location": loc}
            for (ts, loc) in zip(timeslots, locations)
        ]

    def _course_names():
        return [
            ("Characterization and Analysis of Polymer", "高分子定性與分析"),
            ("Socio-cultural history of France", "法國社會文化史"),
            ("Formal Languages and Theory of Computation", "正規語言與計算理論(英文授課)"),
            ("Modern China: Cross-strait relations Globalization", "當代中國：全球化下的兩岸關係"),
            ("Power Semiconductor Devices - Physics and Technology", "高功率半導體元件物理與技術"),
            ("Advanced Eletrocardiology", "進階心臟電氣學"),
            ("Self-Active I-Learning", "自主學習課程"),
        ]

    def _dep_names():
        return [
            ("Institute of Electronics", "電子研究所"),
            ("College of Electrical Engineering", "電機共同課程"),
            ("Department of Applied Mathematics", "應用數學系"),
        ]

    pids = [
        f"{dep}{i}" for dep in ["DEE", "DEP", "IOE", "IME"] for i in range(1000, 1500, 5)
    ]
    [f"{i}{j}" for i in range(106, 109) for j in "ABX"]

    courses = []
    for pid in pids:
        en_name, zh_name = random.choice(_course_names())
        en_dep, zh_dep = random.choice(_dep_names())
        ctype = random.choice(["必修", "選修"])
        sem = random.choice([f"{i}{j}" for i in range(106, 109) for j in "ABX"])
        timelocations = [random.choice(_timelocations())]
        courses.append(
            {
                "permanent_id": pid,
                "credit": random.randint(1, 3),
                "semester": sem,
                "hours": random.randint(1, 6),
                "teacher": fakeChinese.name(),
                "en_name": en_name,
                "zh_name": zh_name,
                "course_number": random.randint(1000, 9000),
                "department_en": en_dep,
                "department_zh": zh_dep,
                "course_type": ctype,
                "time_locations": timelocations,
                "department_zh": zh_dep,
                "department_en": en_dep,
            }
        )
    return courses


@pytest.fixture(scope="module")
def courses() -> Generator:
    class DummyCourses:
        def __init__(self, courses):
            self.courses = courses

        def pick(self):
            return random.choice(self.courses)

    yield DummyCourses(gen_course_data_nctu())


@pytest.mark.unit
def test_gen_course(courses):
    for i in range(10):
        courses.pick()


# -- Helper


def post_course_and_assert_ret_code(client, course: Dict, ret_code: int):
    # helper function, hide this code frame in pytest
    __tracebackhide__ = True
    res = client.post("/course/", json=course)
    assert res.status_code == ret_code
    return res


# -- API test:
@pytest.mark.api
def test_create_course_success(client, courses):
    course = courses.pick()
    post_course_and_assert_ret_code(client, course, 200)


@pytest.mark.api
def test_create_duplicated_courses_also_success(client, courses):
    course = courses.pick()
    ret_course1 = post_course_and_assert_ret_code(client, course, 200).json()
    ret_course2 = post_course_and_assert_ret_code(client, course, 200).json()

    assert ret_course1 == ret_course2


@pytest.mark.api
def test_create_course_with_existing_permanent_id_would_fail(client, courses):
    course = courses.pick()
    post_course_and_assert_ret_code(client, course, 200)

    course["credit"] = int(course["credit"]) + 1
    post_course_and_assert_ret_code(client, course, 409)


@pytest.mark.api
def test_read_course_by_id(client, courses):
    course = courses.pick()

    ret_course = post_course_and_assert_ret_code(client, course, 200).json()

    res = client.get(f"/course/{ret_course['id']}")
    assert res.status_code == 200
    assert res.json()["course_number"] == str(course["course_number"])


@pytest.mark.api
def test_update_course(client, courses):
    course_create = courses.pick()
    course_create["credit"] = 3

    # Ensure course exists
    ret_course = post_course_and_assert_ret_code(client, course_create, 200).json()
    assert course_create["permanent_id"] == ret_course["permanent_id"]

    course_id = ret_course["id"]

    # Update course
    course_patch = course_create.copy()
    course_patch["credit"] = 999
    # Ensure update course return the updated info
    res = client.patch(f"/course/{course_id}", json=course_patch)
    assert res.status_code == 200

    # Get info from updated course to make sure it has been updated
    res = client.get(f"/course/{course_id}")
    assert res.json()["credit"] == "999"


@pytest.mark.api
def test_delete_noexist_course_would_fail(client):
    # Delete Course not in database would return 404
    try_id, nonexist_id_found = 1, False
    while not nonexist_id_found:
        res = client.get(f"/course/{try_id}")
        if res.status_code == 404:
            nonexist_id_found = True
            res_del = client.delete(f"/course/{try_id}")
            assert res_del.status_code == 404
        try_id += 5


@pytest.mark.api
def test_delete_courses(client, courses):
    course_create = courses.pick()

    course_id = post_course_and_assert_ret_code(client, course_create, 200).json()["id"]

    response = client.delete(f"/course/{course_id}")
    assert response.status_code == 200
