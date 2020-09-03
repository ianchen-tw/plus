import pytest
from pydantic import ValidationError

from ..timeslot_exp import TimeSlotExp


@pytest.mark.unit
def test_good_coursetime_validator():
    must_pass = ["2B5CDX", "2EF5G", "3IJK", "1AB2GH3IHJ"]

    for s in must_pass:
        TimeSlotExp(value=s, kind="nctu")


@pytest.mark.unit
def test_coursetime_valid_format():
    """Also valid format"""
    # must parse all these string without raising exception
    TimeSlotExp(value="3iJK", kind="nctu")
    TimeSlotExp(value="0A", kind="nctu")


@pytest.mark.unit
def test_coursetime_accept_lowercase():
    """Also valid format"""
    TimeSlotExp(value="2z", kind="nctu")
    TimeSlotExp(value="2ef5g", kind="nctu")


@pytest.mark.unit
def test_bad_coursetime_validator():
    with pytest.raises(ValidationError):
        TimeSlotExp(value="1A5C", kind="ncku")
    with pytest.raises(ValidationError):
        TimeSlotExp(value="1A", kind="uccu")
    with pytest.raises(ValidationError):
        TimeSlotExp(value="27A", kind="nctu")
    with pytest.raises(ValidationError):
        TimeSlotExp(value="A2", kind="nctu")
    with pytest.raises(ValidationError):
        TimeSlotExp(value="X2C", kind="nctu")
    with pytest.raises(ValidationError):
        TimeSlotExp(value="2", kind="nctu")
    with pytest.raises(ValidationError):
        TimeSlotExp(value="B", kind="nctu")
    with pytest.raises(ValidationError):
        TimeSlotExp(value="-1E", kind="nctu")
