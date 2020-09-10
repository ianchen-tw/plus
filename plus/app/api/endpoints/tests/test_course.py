import random
from typing import Generator

import pytest

from app.testutil import fakeChinese, filter_dict


# -- helper functions
def gen_course_data_nctu():
    def gen_exp(s):
        return {"kind": "nctu", "value": s}

    pids = [f"DCP{i}" for i in range(1000, 2000, 5)]
    sems = [f"{i}{j}" for i in range(106, 109) for j in "ABX"]
    teachers = [fakeChinese.name() for i in range(200)]
    timeslot_exps = [gen_exp(e) for e in ["1A5CD", "2CDX", "3GH4E"]]

    courses = []
    for pid in pids:
        courses.append(
            {
                "permanent_id": pid,
                "credit": random.choice([i for i in range(1, 4)]),
                "semester": random.choice(sems),
                "hours": random.choice([3, 4, 5, 6]),
                "teacher": random.choice(teachers),
                "timeslots": random.choice(timeslot_exps),
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


# -- API test:
def test_create_course_success(client, courses):
    course = courses.pick()

    res = client.post("/course/", json=course)

    assert res.status_code == 200


def test_create_course_return_provided_fields(client, courses):
    course = courses.pick()

    course["timeslots"] = {"kind": "nctu", "value": "2AB3E"}
    response = client.post("/course/", json=course)
    assert response.status_code == 200
    res = response.json()

    course_ans = dict(**course)
    del course_ans["timeslots"]
    assert course_ans == filter_dict(course_ans, res)
    timeslots = res["timeslots"]
    assert len(timeslots) == 3


def test_create_duplicated_courses_also_success(client, courses):
    course = courses.pick()

    res = client.post("/course/", json=course)
    assert res.status_code == 200
    ret_course1 = res.json()

    res = client.post("/course/", json=course)
    assert res.status_code == 200
    ret_course2 = res.json()

    assert ret_course1 == ret_course2


def test_create_course_with_existing_permanent_id_would_fail(client, courses):
    course = courses.pick()

    res = client.post("/course/", json=course)
    assert res.status_code == 200
    res.json()

    course["credit"] = course["credit"] + 1
    res = client.post("/course/", json=course)
    assert res.status_code == 409


def test_read_course_by_id(client, courses):
    course = courses.pick()

    res = client.post("/course/", json=course)
    assert res.status_code == 200
    course = res.json()

    res = client.get(f"/course/{course['id']}")
    assert res.status_code == 200
    assert course == filter_dict(res.json(), course)


def test_update_course(client, courses):
    course_create = courses.pick()
    course_create["credit"] = 3
    course_create["timeslots"] = {"kind": "nctu", "value": "1AB"}
    # Ensure course exists
    response = client.post("/course/", json=course_create)
    assert response.status_code == 200
    original_course = response.json()
    assert course_create["permanent_id"] == original_course["permanent_id"]

    course_id = original_course["id"]
    # Update course
    course_patch = course_create.copy()
    course_patch["credit"] = 999
    course_patch["timeslots"] = {"kind": "nctu", "value": "1A2CD"}
    # Ensure update course return the updated info
    response = client.patch(f"/course/{course_id}", json=course_patch)
    assert response.status_code == 200
    updated_course = response.json()
    assert len(updated_course["timeslots"]) == 3
    assert updated_course["timeslots"][1]["code"] == "C"

    # Get info from updated course to make sure it has been updated
    client.get(f"/course/{course_id}")
    assert response.status_code == 200
    assert response.json()["credit"] == 999


def test_delete_courses(client, courses):
    course_create = courses.pick()

    # Could delete course
    response = client.post("/course/", json=course_create)
    assert response.status_code == 200

    course_id = response.json()["id"]
    response = client.delete(f"/course/{course_id}")
    assert response.status_code == 200

    course = course_create.copy()
    del course["timeslots"]

    least_info = {**course, "id": course_id}
    assert least_info == filter_dict(least_info, response.json())

    # Delete Course not in database would return 404
    try_id, nonexist_id_found = 1, False
    while not nonexist_id_found:
        res = client.get(f"/course/{try_id}")
        if res.status_code == 404:
            nonexist_id_found = True
            res_del = client.delete(f"/course/{try_id}")
            assert res_del.status_code == 404
        try_id += 5
