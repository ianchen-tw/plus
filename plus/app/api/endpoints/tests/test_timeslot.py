from collections import namedtuple
from typing import Dict, List

import pytest

from app.core import timetable_nctu
from app.testutil import filter_dict

# TODO: initialize database using fixture to prevent creating object in each test.


class TimeSlotCreate(namedtuple("TimeSlotCreate", "code weekday_int")):  # noqa
    def __eq__(self, other):
        return all([getattr(self, f) == getattr(other, f) for f in self._fields])


def gen_timeslots_nctu(slots: List[TimeSlotCreate]) -> List[Dict]:
    """ Use timtable to translate different data object
    """
    result = []
    for t in slots:
        ts = timetable_nctu.gen_timeslot(code=t.code, weekday_int=t.weekday_int)
        result.append(ts._asdict())
    return result


@pytest.mark.unit
def test_gen_timeslot_nctu():
    """ Smok test for our helper function
    """
    slots = [["E", 2], ["B", 4]]
    gen_timeslots_nctu([TimeSlotCreate._make(s) for s in slots])
    # import pprint
    # pprint.pprint(timeslots)


# ====== endpoint test start


def test_create_timeslot_success(client):
    slot = ["K", 2]
    timeslots = gen_timeslots_nctu([TimeSlotCreate._make(slot)])
    response = client.post("/timeslot/", json=timeslots[0])
    assert response.status_code == 200


def test_query_all_timeslot(client):
    slots = [
        ["E", 2],
        ["G", 3],
    ]
    timeslots = gen_timeslots_nctu([TimeSlotCreate._make(s) for s in slots])
    for t in timeslots:
        response = client.post("/timeslot/", json=t)
        assert response.status_code == 200

    # actual test
    response = client.get("/timeslot/")
    assert response.status_code == 200


def test_translate_course(client):

    # Makesure timeslots exist in database
    slots = [
        ["E", 2],
        ["F", 2],
        ["G", 5],
    ]
    timeslots = gen_timeslots_nctu([TimeSlotCreate._make(s) for s in slots])
    for t in timeslots:
        response = client.post("/timeslot/", json=t)
        assert response.status_code == 200

    post_data = {
        "kind": "nctu",
        "value": "2EF5G",
    }
    response = client.post("/timeslot/translate", json=post_data)
    assert response.status_code == 200

    res_data = response.json()
    assert len(res_data) == 3


def test_create_unique_timeslots(client):
    """ Create Method should refer to the same timeslot while there exists
    a timeslot s.t. equals to the one we want to create
    """
    slots = [["K", 1], ["K", 1], ["K", 1]]
    timeslots = gen_timeslots_nctu([TimeSlotCreate._make(s) for s in slots])
    # all three create api call must return the same obejct
    first_id = None
    for t in timeslots:
        response = client.post("/timeslot/", json=t)
        assert response.status_code == 200
        if not first_id:
            first_id = response.json()["id"]
        else:
            assert first_id == response.json()["id"]


def test_delete_timeslot(client):
    # ensure item exists
    slot = ["K", 1]
    ts = TimeSlotCreate._make(slot)
    timeslot = gen_timeslots_nctu([ts])
    response = client.post("/timeslot/", json=timeslot[0])
    assert response.status_code == 200

    tid = response.json()["id"]
    client.delete(f"/timeslot/{tid}")
    assert response.status_code == 200

    least_info = {**ts._asdict(), "id": tid}
    del least_info["weekday_int"]
    assert least_info == filter_dict(least_info, response.json())
