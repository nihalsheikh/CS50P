# Week 7: Problem 3
# Take user input in form of a string of 12 hour time format (9:00 AM to 5:00 PM)
# convert the string to 24 hour format and also make test cases for these
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s): # tp: time period, s: start, e: end, hr: hour, min: minutes
    pattern = r"^(?P<s_hr>\d{0,2}):?(?P<s_min>\d{0,2}) (?P<s_tp>AM|PM) to (?P<e_hr>\d{0,2}):?(?P<e_min>\d{0,2}) (?P<e_tp>AM|PM)$"

    matches = re.search(pattern, s, re.IGNORECASE)

    if matches:
        s_hour = matches.group("s_hr")
        s_min = matches.group("s_min")
        start_tp = matches.group("s_tp")
        e_hour = matches.group("e_hr")
        e_min = matches.group("e_min")
        end_tp = matches.group("e_tp")

        if 0 <= int(s_min) < 60 and 0 <= int(e_min) < 60:
            start_hour = 0
            end_hour = 0

            if start_tp == "AM" and int(s_hour) == 12:
                start_hour = 0
            if start_tp == "PM" and int(s_hour) != 12:
                start_hour += 12

            if end_tp == "AM" and int(s_hour) == 12:
                end_hour = 0
            if end_tp == "PM" and int(s_hour) != 12:
                end_hour += 12

        return matches
    else:
        raise ValueError


if __name__ == "__main__":
    main()
