import random
from typing import List

from app.testutil import fakeChinese, filter_dict

# -- helper functions


def get_timeslot_ids_nctu(client, s: str) -> List[int]:
    res = client.post("/timeslot/translate", json={"kind": "nctu", "value": s})
    timeslots = res.json()
    return [t["id"] for t in timeslots]


def gen_course_data_nctu(client):
    pids = ["DCP1138", "ZW987", "AC123", "SJ618"]
    sems = [f"{i}{j}" for i in range(106, 109) for j in "ABX"]
    teachers = [fakeChinese.name() for i in range(4)]
    timeslot_codes = ["1A5CD", "2CDX", "3GH4E"]
    timeslots_list = [get_timeslot_ids_nctu(client, s) for s in timeslot_codes]
    return {
        "permanent_id": random.choice(pids),
        "credit": random.choice([i for i in range(1, 4)]),
        "semester": random.choice(sems),
        "hours": random.choice([3, 4, 5, 6]),
        "teacher": random.choice(teachers),
        "timeslot_ids": random.choice(timeslots_list),
    }


def test_gen_course(client):
    for i in range(8):
        gen_course_data_nctu(client)


# -- API test:
def test_create_course_success(client):
    course = gen_course_data_nctu(client)

    res = client.post("/course/", json=course)
    assert res.status_code == 200


def test_create_course_return_provided_fields(client):
    course = gen_course_data_nctu(client)

    response = client.post("/course/", json=course)
    assert response.status_code == 200
    res = response.json()
    course_ans = dict(**course)
    del course_ans["timeslot_ids"]
    assert course_ans == filter_dict(course_ans, res)


# @pytest.mark.dev
# def test_update_course(client):
#     course_create = gen_course_data_nctu(client)
#     response = client.post("/course/", json=course_create)
#     assert response.status_code == 200

#     course_id = response.json()["id"]
#     response = client.delete(f"/course/{course_id}")
#     assert response.status_code == 200


def test_delete_courses(client):
    course_create = gen_course_data_nctu(client)

    response = client.post("/course/", json=course_create)
    assert response.status_code == 200

    course_id = response.json()["id"]
    response = client.delete(f"/course/{course_id}")
    assert response.status_code == 200

    course = course_create.copy()
    del course["timeslot_ids"]

    least_info = {**course, "id": course_id}
    assert least_info == filter_dict(least_info, response.json())
