# Week 7: Problem 4
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b" + re.escape("um") + r"\b"
    um_count = 0

    matches = re.findall(pattern, s, re.IGNORECASE)

    for string in matches:
        um_count += 1

    return um_count


if __name__ == "__main__":
    main()
