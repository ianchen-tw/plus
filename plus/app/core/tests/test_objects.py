from typing import Generator

import pytest
from attr.exceptions import FrozenInstanceError

from ..objects import CodedTimeInterval


@pytest.fixture(scope="module")
def interval_arg() -> Generator:
    yield {"code": "A", "weekday": "Fri", "timespan": "8:00-9:00", "kind": "nctu"}


@pytest.mark.unit
def test_interval_dict(interval_arg):
    interval = CodedTimeInterval(**interval_arg)
    assert interval.as_dict() == interval_arg


@pytest.mark.unit
def test_interval_is_immutable(interval_arg):
    interval = CodedTimeInterval(**interval_arg)
    with pytest.raises(FrozenInstanceError):
        interval.code = "Nah"


@pytest.mark.unit
def test_interval_comparison():
    i1 = CodedTimeInterval(code="A", weekday="Fri", timespan="8:00-9:00", kind="nctu")
    i2 = CodedTimeInterval(code="A", weekday="Fri", timespan="8:00-9:00", kind="nctu")
    assert i1 == i2

    i3 = CodedTimeInterval(code="A", weekday="Fri", timespan="8:00-9:00", kind="nctu")
    i4 = CodedTimeInterval(code="B", weekday="Mon", timespan="8:00-9:00", kind="nctu")
    assert i3 != i4
