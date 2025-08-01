# Week 7: Problem 3
# Take user input in form of a string of 12 hour time format (9:00 AM to 5:00 PM)
# convert the string to 24 hour format and also make test cases for these
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s): # tp: time period, s: start, e: end, hr: hour, min: minutes
    pattern = r"^(?P<s_hr>\d{0,2}):?(?P<s_min>\d{0,2}) (?P<s_tp>AM|PM) to (?P<e_hr>\d{0,2}):?(?P<e_min>\d{0,2}) (?P<e_tp>AM|PM)$"

    try:
        matches = re.search(pattern, s, re.IGNORECASE)

        if matches:
            if matches.group("s_min"):
                s_min = int(matches.group("s_min"))
            else:
                s_min = 0

            if matches.group("e_min"):
                e_min = int(matches.group("e_min"))
            else:
                e_min = 0

            s_hour = int(matches.group("s_hr"))
            start_tp = matches.group("s_tp")

            e_hour = int(matches.group("e_hr"))
            end_tp = matches.group("e_tp")

            if 1 <= s_hour <= 12 and 1 <= e_hour <= 12 and 0 <= s_min < 60 and 0 <= e_min < 60:
                if start_tp == "AM" and s_hour == 12:
                    s_hour = 0
                elif start_tp == "PM" and s_hour != 12:
                    s_hour += 12

                if end_tp == "AM" and e_hour == 12:
                    e_hour = 0
                elif end_tp == "PM" and e_hour != 12:
                    e_hour += 12

                return f"{s_hour:02}:{s_min:02} to {e_hour:02}:{e_min:02}"
            else:
                raise ValueError("'Hour' or 'Minutes' not in correct format")
        else:
            raise ValueError("Incorrect time format")
    except ValueError:
        raise ValueError

if __name__ == "__main__":
    main()
