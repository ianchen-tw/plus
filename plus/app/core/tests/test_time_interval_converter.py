from typing import Generator

import pytest

from ..objects import CodedTimeInterval
from ..time_interval_converter import (
    TimeIntervalConverterInterface,
    TimeIntervalConverterNCTU,
    TimeIntervalConvertException,
)
from ..timetable import TimeTableNCTU


@pytest.fixture(scope="module")
def converter_nctu() -> Generator:
    yield TimeIntervalConverterNCTU(TimeTableNCTU())


@pytest.mark.unit
def test_nctu_parser_would_raise_on_invalid_input(
    converter_nctu: TimeIntervalConverterInterface,
):
    with pytest.raises(TimeIntervalConvertException):
        converter_nctu.to_time_intervals("244A")
    with pytest.raises(TimeIntervalConvertException):
        converter_nctu.to_time_intervals("-2A")
    with pytest.raises(TimeIntervalConvertException):
        converter_nctu.to_time_intervals("D2C")
    with pytest.raises(TimeIntervalConvertException):
        converter_nctu.to_time_intervals("2ab")


@pytest.mark.unit
def test_nctu_parser_to_time_slots(converter_nctu: TimeIntervalConverterInterface):
    ts = [
        CodedTimeInterval(code="A", weekday="Mon", timespan="8:00-8:50", kind="nctu"),
        CodedTimeInterval(code="A", weekday="Fri", timespan="8:00-8:50", kind="nctu"),
        CodedTimeInterval(code="B", weekday="Fri", timespan="9:00-9:50", kind="nctu"),
        CodedTimeInterval(code="I", weekday="Fri", timespan="18:30-19:20", kind="nctu"),
    ]
    result = converter_nctu.to_time_intervals("1A5ABI")
    assert ts[0] == result[0]
    assert ts[1] == result[1]
    assert ts[2] == result[2]
    assert ts[3] == result[3]


@pytest.mark.unit
def test_nctu_parser_combine_slots(converter_nctu: TimeIntervalConverterInterface):
    ts = [
        CodedTimeInterval(code="A", weekday="Mon", timespan="8:00-8:50", kind="nctu"),
        CodedTimeInterval(code="A", weekday="Fri", timespan="8:00-8:50", kind="nctu"),
    ]
    result = converter_nctu.to_time_intervals("1A1A5AAA")
    assert len(result) == 2
    assert ts[0] == result[0]
    assert ts[0] == result[0]
    assert ts[1] == result[1]
    assert ts[1] == result[1]
