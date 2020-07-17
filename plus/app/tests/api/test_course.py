import random

from app.tests.utils import fakeChinese, filter_dict


def gen_course():
    pids = ["DCP1138", "ZW987", "AC123", "SJ618"]
    sems = [f"{i}{j}" for i in range(106, 109) for j in "ABX"]
    teachers = [fakeChinese.name() for i in range(4)]
    return {
        "permanent_id": random.choice(pids),
        "credit": random.choice([i for i in range(1, 4)]),
        "semester": random.choice(sems),
        "hours": random.choice([3, 4, 5, 6]),
        "teacher": random.choice(teachers),
    }


def test_gen_course(client):
    for i in range(8):
        c = gen_course()
        print(c)


# TODO:read, update

# CREATE
def test_create_course_success(client):
    course = gen_course()
    response = client.post("/course/", json=course)
    assert response.status_code == 200


def test_create_course_return_provided_fields(client):
    course = gen_course()

    response = client.post("/course/", json=course)
    assert response.status_code == 200
    res = response.json()
    assert course == filter_dict(course, res)


def test_create_course_filter_on_additional_fields(client):
    course = gen_course()
    extra = "AAAAAAAA"
    course[extra] = 87
    response = client.post("/course/", json=course)
    assert response.status_code == 200
    assert extra not in response.json().keys()


def test_delete_courses(client):
    course = gen_course()

    response = client.post("/course/", json=course)
    assert response.status_code == 200

    course_id = response.json()["id"]
    client.delete(f"/course/{course_id}")
    assert response.status_code == 200

    least_info = {**course, "id": course_id}
    assert least_info == filter_dict(least_info, response.json())
