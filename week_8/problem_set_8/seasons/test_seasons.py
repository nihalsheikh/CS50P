# Week 8: Test case for Seasons program
import pytest
from datetime import date, datetime
from seasons import AgeInMinutes

def test_default():
    assert AgeInMinutes("1999-01-01").min_in_words == "Thirteen million, nine hundred eighty-five thousand, two hundred eighty minutes"

    assert AgeInMinutes("2024-08-04").min_in_words == "Five hundred twenty-five thousand, six hundred minutes"


# def test_invalid_date_format():
#     with pytest.raises(ValueError):
#         assert AgeInMinutes("January 1, 1999")
