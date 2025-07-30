# Week 7: Test program for numb3rs.py
from numb3rs import validate


def test_default():
    assert validate("0.0.0.0")
    assert validate("255.255.255.255")


def test_invalid_input():
    assert not validate("ip is 0.0.0.0")
    assert not validate(".0.0.0.0")
    assert not validate("0.0.0.0.")
    assert not validate(" .0.0.0.0.")
    assert not validate("")
    assert not validate("1.1.1.1.1")
    assert not validate("a.b.c.d")
    assert not validate("cat")


def test_valid_range():
    assert validate("0.0.0.0")
    assert validate("1.1.1.1")
    assert validate("1.2.3.4")
    assert validate("255.255.255.255")


def test_invalid_range():
    assert not validate("-1.-2.-3.-4")
    assert not validate("256.256.256.256")


def test_leading_zero_in_ip():
    assert not validate("198.001.1.1")
    assert not validate("001.001.001.001")
