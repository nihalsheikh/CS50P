# Week 5: Problem 4
# test cases for fuel gauge program
import pytest
from fuel import convert, gauge


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percent_value():
    assert gauge(2) == "2%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_non_integer():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_not_fraction():
    with pytest.raises(ValueError):
        convert("1.5")


def test_convert_negative_numerator():
    with pytest.raises(ValueError):
        convert("-1/4")


def test_convert_negative_denominator():
    with pytest.raises(ValueError):
        convert("1/-4")


def test_convert_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        convert("5/4")


def test_convert_not_fraction():
    with pytest.raises(ValueError):
        convert("34")


def test_convert_multiple_slashes():
    with pytest.raises(ValueError):
        convert("1/2/3")


def test_convert_valid_fractions():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    assert convert("4/4") == 100
    assert convert("1/3") == 33
    assert convert("2/3") == 67
