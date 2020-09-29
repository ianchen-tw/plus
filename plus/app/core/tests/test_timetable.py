from typing import Generator

import pytest

from ..objects import CodedTimeInterval
from ..timetable import TimeTableNCTU


@pytest.fixture(scope="module")
def table() -> Generator:
    yield TimeTableNCTU()


@pytest.mark.unit
def test_correct_kind(table):
    assert table.get_kind() == "nctu"


@pytest.mark.unit
def test_valid_code(table):
    assert table.is_valid_code("X")
    assert table.is_valid_code("K")
    assert table.is_valid_code("Z") == False
    assert table.is_valid_code("W") == False


@pytest.mark.unit
def test_gen_timespan(table):
    ts = CodedTimeInterval(code="I", weekday="Fri", timespan="18:30-19:20", kind="nctu")
    result = table.gen_time_interval(code="I", weekday_int=5)
    assert ts == result


@pytest.mark.unit
def test_gen_timespan_should_raise_error_on_malformed_input(table):
    with pytest.raises(Exception):
        table.gen_time_interval(code="I", weekday_int=-999)
    with pytest.raises(Exception):
        table.gen_time_interval(code="ZZZZ", weekday_int=3)
