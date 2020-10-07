import pytest

from ..fake_nctu import fakeNctu


@pytest.mark.unit
def test_not_none():
    methods = ["classroom", "permanent_id", "course_type", "teacher"]
    for method in methods:
        for _ in range(10):
            res = getattr(fakeNctu, method)()
            assert res != ""


@pytest.mark.unit
def test_timeslot():
    exp = fakeNctu.timeslot_exp()
    assert len(exp) > 0

    # at least longer than '1A'
    assert len(list(exp[:])) >= 2


@pytest.mark.unit
def test_course():
    en, zh = fakeNctu.course()
    assert zh != ""


@pytest.mark.unit
def test_dep():
    en, zh = fakeNctu.course()
    assert zh != ""
