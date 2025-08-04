# Week 8: Problem 1
# User inputs their: DOB in YYYY-MM-DD format
# print how old the user is in minutes. rounded to the nearest int
# using english words instead of numerals, without any `and` between words
# assume the user was born midnight time 00:00:00 on the DOB provided
# also assume the current time is midnight on the same date
import sys
import inflect
from datetime import date, datetime


class AgeInMinutes:
    def __init__(self, dob_str=None):
        self.dob = self.valid_date_format(dob_str)
        self.p = inflect.engine()

    def valid_date_format(self, dob_str):
        if dob_str is None:
            dob_input = input("Date of Birth: ")
        else:
            dob_input = dob_str

        try:
            dob_time = datetime.strptime(dob_input, "%Y-%m-%d")
            dob = dob_time.date()
            today = date.today()

            if dob > today:
                sys.exit("Invalid Date of birth")

            return dob
        except ValueError:
            sys.exit("Invalid date")

    @property
    def time_in_min(self):
        date_diff = date.today() - self.dob
        return date_diff.days * 24 * 60

    @property
    def min_in_words(self):
        words = self.p.number_to_words(self.time_in_min, andword="")
        return f"{words.capitalize()} minutes"


def main():
    print(get_time_in_min())


def get_time_in_min(dob_str=None):
    return AgeInMinutes(dob_str).min_in_words


if __name__ == "__main__":
    main()
