# Week 6: Problem 3
# Take tow cmd-line args, 1: a csv file as input with name and house as the headers/columns
# 2: name of the new csv file with first, last and house columns
import os
import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line argument")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line argument")

    if len(sys.argv) == 3:
        if not os.path.isfile(sys.argv[1]):
            sys.exit(f"Could not read {sys.argv[1]}")

        make_file = new_file(sys.argv[1], sys.argv[2])


def new_file(input, output):
    with open(input, "r") as inp, open(output, "w") as out:
        # reading the input file as dictionaries
        reader = csv.DictReader(inp)

        # write new header or fieldnames for new file
        writer = csv.DictWriter(out, fieldnames=["first", "last", "house"])
        writer.writeheader()

        # split the names
        for row in reader:
            # print(row)
            last, first = row["name"].split(",")
            writer.writerow({
                "first": first.strip(),
                "last": last.strip(),
                "house": row["house"]
            })

main()
