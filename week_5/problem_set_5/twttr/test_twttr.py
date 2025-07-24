# Week 5: Problem 1
# test cases for twttr problem
import pytest
from twttr import shorten


def test_default():
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"


def test_lowercase_vowel():
    assert shorten("What is your name?") == "Wht s yr nm?"


def test_uppercase_vowel():
    assert shorten("WHAT IS YOUR NAME?") == "WHT S YR NM?"

def some_error():
    with pytest.raises(ValueError):
        shorten("aeiouAEIOU")
