# Week 7: Problem 1
# Validate the IP address, and return True or False values
import re
import sys


def main():
    ip_address = input("IPv4 Address: ").strip()
    print(validate(ip_address))


def validate(ip):
    pattern = r"^(?P<g1>\d{1,3})\.(?P<g2>\d{1,3})\.(?P<g3>\d{1,3})\.(?P<g4>\d{1,3}$)"
    matches = re.search(pattern, ip)

    try:
        if all(0 <= int(group) <=255 and (group == "0" or not group.startswith("0")) for group in matches.groups()):
            if matches:
                return True
        else:
            return False
    except AttributeError:
        return False


if __name__ == "__main__":
    main()
