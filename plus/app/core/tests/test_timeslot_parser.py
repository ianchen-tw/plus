from typing import Generator, List

import pytest

from app.schemas import TimeSlotExp
from ..timeslot_converter import TimeSlotConverterInterface
from ..timeslot_parser import TimeSlotParser
from ..timetable import TimeSlot


def make_ts(code, weekday, timespan, kind):
    return TimeSlot._make([code, weekday, timespan, kind])


dummy_exp = TimeSlotExp(**{"kind": "nctu", "value": "2Z5G"})

dummy_timeslots = [
    make_ts("Z", "Tue", timespan="1:00-2:00", kind="nctu"),
    make_ts("G", "Fri", timespan="1:00-2:00", kind="nctu"),
]


class dummyConverter(TimeSlotConverterInterface):
    """ Dummy Converter object injected into our TimeSlotParser
    """

    def to_time_slots(self, s: str) -> List[TimeSlot]:
        if s == dummy_exp.value:
            return dummy_timeslots
        raise Exception(f"Bad input value from Upstream Parser: {s}")


@pytest.fixture(scope="module")
def parser() -> Generator:
    converters_map = {dummy_exp.kind: dummyConverter()}
    parser = TimeSlotParser(converters_map=converters_map)
    yield parser


@pytest.mark.unit
def test_parser_would_parse(parser):
    timeslots = parser.parse_timeslots(exp=dummy_exp)
    assert timeslots[0] == dummy_timeslots[0]
    assert timeslots[1] == dummy_timeslots[1]


@pytest.mark.unit
def test_parser_would_reject_unregistered_type(parser):
    # TODO: implement this after we have defined mutilple value
    # inside models.course_timeslot.TimeSlotKind
    pass


# ----- intergral test
integral_exp = TimeSlotExp(**{"kind": "nctu", "value": "2AB3I"})

integral_timeslots = [
    make_ts("A", "Tue", timespan="8:00-8:50", kind="nctu"),
    make_ts("B", "Tue", timespan="9:00-9:50", kind="nctu"),
    make_ts("I", "Wed", timespan="18:30-19:20", kind="nctu"),
]

from app.core import timeslot_parser


@pytest.mark.unit
def test_parser_intergral_test():
    """ Test the funtionality of our actual timeslot parser
    """
    timeslots = timeslot_parser.parse_timeslots(exp=integral_exp)
    assert timeslots[0] == integral_timeslots[0]
    assert timeslots[1] == integral_timeslots[1]
    assert timeslots[2] == integral_timeslots[2]
