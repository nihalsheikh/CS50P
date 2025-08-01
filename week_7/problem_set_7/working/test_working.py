# Week 7: Test case for Problem 3
import pytest
from working import convert


def test_default():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_invalid_input():
    with pytest.raises(ValueError):
        assert convert("9:00 AM - 5:00 PM")
        assert convert("9 AM - 5 PM")
        assert convert("9:00 PM - 17:00 AM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM")
        assert convert("10:-1 AM to 5:-1 PM")
        assert convert("9:71 AM to 5:93 PM")


def test_invalid_hour():
    with pytest.raises(ValueError):
        assert convert("17:40 AM to 5:20 PM")
        assert convert("9:40 AM to 15:33 PM")


def test_invalid_time_min_output():
    with pytest.raises(AssertionError):
        assert convert("9:53 AM to 10:11 PM") == "09 to 10"


def test_invalid_time_hour_output():
    with pytest.raises(AssertionError):
        assert convert("10:53 AM to 7:11 PM") == "00:53 to 00:11"
