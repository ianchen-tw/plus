from typing import Generator, List

import pytest

from app.schemas import TimeSlotExp
from ..objects import CodedTimeInterval
from ..time_interval_converter import TimeIntervalConverterInterface
from ..time_interval_parser import TimeIntervalParser


def make_interval(code, weekday, timespan, kind):
    return CodedTimeInterval(code=code, weekday=weekday, timespan=timespan, kind=kind)


dummy_exp = TimeSlotExp(**{"kind": "nctu", "value": "2Z5G"})

dummy_timeslots = [
    make_interval("Z", "Tue", timespan="1:00-2:00", kind="nctu"),
    make_interval("G", "Fri", timespan="1:00-2:00", kind="nctu"),
]


class dummyConverter(TimeIntervalConverterInterface):
    """ Dummy Converter object injected into our TimeIntervalParser
    """

    def to_time_intervals(self, s: str) -> List[CodedTimeInterval]:
        if s == dummy_exp.value:
            return dummy_timeslots
        raise Exception(f"Bad input value from Upstream Parser: {s}")


@pytest.fixture(scope="module")
def parser() -> Generator:
    converters_map = {dummy_exp.kind: dummyConverter()}
    parser = TimeIntervalParser(converters_map=converters_map)
    yield parser


@pytest.mark.unit
def test_parser_would_parse(parser):
    timeslots = parser.parse_time_intervals(exp=dummy_exp)
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
    make_interval("A", "Tue", timespan="8:00-8:50", kind="nctu"),
    make_interval("B", "Tue", timespan="9:00-9:50", kind="nctu"),
    make_interval("I", "Wed", timespan="18:30-19:20", kind="nctu"),
]

from app.core import time_interval_parser


@pytest.mark.unit
def test_parser_intergral_test():
    """ Test the funtionality of our actual timeslot parser
    """
    timeslots = time_interval_parser.parse_time_intervals(exp=integral_exp)
    assert timeslots[0] == integral_timeslots[0]
    assert timeslots[1] == integral_timeslots[1]
    assert timeslots[2] == integral_timeslots[2]
