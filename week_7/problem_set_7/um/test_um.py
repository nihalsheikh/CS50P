# Week 7: test case for program 4
from um import count
import pytest


def test_default():
    assert count("yummy") == 0
    assert count("hello, um, world") == 1


def test_invalid_input():
    with pytest.raises(TypeError):
        assert count(1)

def test_not_whole_string():
      assert count("yummy") == 0

def test_whitespace_with_um():
      assert count("hello  um  thereum") == 1

def test_um_case_insensitive():
     assert count("um") == 1
     assert count("UM") == 1
     assert count("uM") == 1
     assert count("Um") == 1
