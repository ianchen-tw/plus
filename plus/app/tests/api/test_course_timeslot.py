import random
from itertools import product

import pytest

from app.tests.utils import filter_dict


def gen_timeslot():
    """
  Generate timeslot which
    code would not conflict
  """

    def gen_timestamp():
        a = random.randint(9, 17)
        interval = random.randint(1, 3)
        return f"{a:02}:00 - {a+interval:02}:00"

    code_set = "ABCDXEFG"
    repeat = 0
    weekdays = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]
    while True:
        repeat += 1
        combi = ["".join(c) for c in product(code_set, repeat=repeat)]
        random.shuffle(combi)
        for code in combi:
            yield {
                "code_name": code,
                "description": gen_timestamp(),
                "weekday": random.choice(weekdays),
            }


@pytest.fixture
def timeslot():
    gen = gen_timeslot()
    return next(gen)


# TODO:read, update

# CREATE
def test_create_timeslot_success(client, timeslot):
    response = client.post("/timeslot/", json=timeslot)
    response.json()
    assert response.status_code == 200


def test_create_timeslot_return_provided_fields(client, timeslot):

    response = client.post("/timeslot/", json=timeslot)
    assert response.status_code == 200
    res = response.json()
    assert timeslot == filter_dict(timeslot, res)


def test_create_timeslot_filter_on_additional_fields(client, timeslot):
    extra = "AAAAAAAA"
    timeslot[extra] = 87
    response = client.post("/timeslot/", json=timeslot)
    assert response.status_code == 200
    assert extra not in response.json().keys()


# TODO: delete realted courses...
def test_delete_timeslot(client, timeslot):

    response = client.post("/timeslot/", json=timeslot)
    assert response.status_code == 200

    tid = response.json()["id"]
    client.delete(f"/timeslot/{tid}")
    assert response.status_code == 200

    least_info = {**timeslot, "id": tid}
    assert least_info == filter_dict(least_info, response.json())
