import time
import pytest
from src.my_function import increment, division


def test_increment():
    assert increment(5, 3) != 3
    assert increment(2, 6) == 8


def test_division():
    assert division(5, 3) != 3
    assert division(10, 5) == 2


def test_division_by_zero():
    with pytest.raises(ValueError):
        division(5, 0)


def test_add_strings():
    assert increment("i like", "burgers") == "i likeburgers"
    assert increment("i like", " burgers") == "i like burgers"


def main():
    print("Testing!!!!")


"""
    pytest mark provides a way to provide metadata to test. 
    Its a way of providing label and tags to your test

    Some built in markers are 
    skip: this skips the test
    xfail: this mark it has fail

    custom markers, this can be added via the pytest.ini
    slow: this indicates its a slow test. You can this sole by
    pytest -m slow
"""


@pytest.mark.slow
def test_very_slow():
    time.sleep(10)
    assert division(10, 5) == 2


@pytest.mark.skip(reason="Not in use anymore")
def test_skip():
    assert division(10, 5) == 2


@pytest.mark.xfail(reason="No cannot divide by zero")
def test_very_xfail():
    pass
