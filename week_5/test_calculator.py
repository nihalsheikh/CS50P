# Week 5: Unit tests
# testing the calculator file
import pytest
from calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zer():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")
