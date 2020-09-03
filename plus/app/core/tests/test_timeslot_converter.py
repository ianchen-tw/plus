from typing import Generator

import pytest

from ..timeslot_converter import (
    TimeSlotConverterInterface,
    TimeSlotConverterNCTU,
    TimeSlotConvertException,
)
from ..timetable import TimeSlot, TimeTableNCTU


@pytest.fixture(scope="module")
def converter_nctu() -> Generator:
    yield TimeSlotConverterNCTU(TimeTableNCTU())


@pytest.mark.unit
def test_nctu_parser_would_raise_on_invalid_input(
    converter_nctu: TimeSlotConverterInterface,
):
    with pytest.raises(TimeSlotConvertException):
        converter_nctu.to_time_slots("244A")
    with pytest.raises(TimeSlotConvertException):
        converter_nctu.to_time_slots("-2A")
    with pytest.raises(TimeSlotConvertException):
        converter_nctu.to_time_slots("D2C")
    with pytest.raises(TimeSlotConvertException):
        converter_nctu.to_time_slots("2ab")


@pytest.mark.unit
def test_nctu_parser_to_time_slots(converter_nctu: TimeSlotConverterInterface):
    ts = [
        TimeSlot(code="A", weekday="Mon", timespan="8:00-8:50", kind="nctu"),
        TimeSlot(code="A", weekday="Fri", timespan="8:00-8:50", kind="nctu"),
        TimeSlot(code="B", weekday="Fri", timespan="9:00-9:50", kind="nctu"),
        TimeSlot(code="I", weekday="Fri", timespan="18:30-19:20", kind="nctu"),
    ]
    result = converter_nctu.to_time_slots("1A5ABI")
    assert ts[0] == result[0]
    assert ts[1] == result[1]
    assert ts[2] == result[2]
    assert ts[3] == result[3]


@pytest.mark.unit
def test_nctu_parser_combine_slots(converter_nctu: TimeSlotConverterInterface):
    ts = [
        TimeSlot(code="A", weekday="Mon", timespan="8:00-8:50", kind="nctu"),
        TimeSlot(code="A", weekday="Fri", timespan="8:00-8:50", kind="nctu"),
    ]
    result = converter_nctu.to_time_slots("1A1A5AAA")
    assert len(result) == 2
    assert ts[0] == result[0]
    assert ts[0] == result[0]
    assert ts[1] == result[1]
    assert ts[1] == result[1]