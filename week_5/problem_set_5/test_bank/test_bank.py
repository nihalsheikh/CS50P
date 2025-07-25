# Week 5: Problem 2
#  test cases for bank problem
import pytest
from bank import value


def test_greet_hello():
    assert value("hello") == 0
    assert value("hello, how is your day?") == 0
    assert value("Hello") == 0
    assert value("Hello, how you doing?") == 0


def test_greet_h():
    assert value("hi, nice to meet you!") == 20
    assert value("how is your day?") == 20
    assert value("hey") == 20
    assert value("Hola amigo") == 20


def test_not_h():
    assert value("What's happening?") == 100
    assert value("What's up") == 100


def test_case_insensitivty():
    assert value("HELLo there, how you doin?") == 0
    assert value("HEy ya'll") == 20
    assert value("what's up amigo?") == 100

# def test_no_return():
#     with pytest.raises(AttributeError):
#         value(3)
