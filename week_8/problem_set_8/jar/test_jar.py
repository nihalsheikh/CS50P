# Week 8: test case for jar program
import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert str(jar) == ""


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    assert jar.size == 1
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    assert jar.size == 11


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert str(jar) == "🍪" * 10
    assert jar.size == 10

    jar.withdraw(1)
    assert str(jar) == "🍪" * 9
    assert jar.size == 9

    jar.withdraw(5)
    assert str(jar) == "🍪" * 4
    assert jar.size == 4

    with pytest.raises(ValueError):
        jar.withdraw(5)


def test_jar_capacity_limit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_negative_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_jar_withdraw_limit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
