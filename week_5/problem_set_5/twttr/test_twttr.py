# Week 5: Problem 1
# test cases for twttr problem
import pytest
from twttr import shorten


# def test_default():
#     assert shorten("Twitter") == "Twttr"
#     assert shorten("What's your name?") == "Wht's yr nm?"
#     assert shorten("CS50") == "CS50"

# def test_lowercase_vowel():
#     assert shorten("and that's a goal from ronaldo") == "nd tht's gl frm rnld"


def test_uppercase_vowel():
    assert shorten("WHEN WILL THIS TEST end") == "WHN WLL THS TST nd"
