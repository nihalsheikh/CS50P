# Week 6: Problem 2
# take a csv file as an input, and output as ASCII art table
import os
import sys
import csv
from tabulate import tabulate


def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")

        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        if len(sys.argv) == 2:
            # if not os.path.isfile(sys.argv[1]):
            #     sys.exit("File not found")

            if sys.argv[1][-4:] != ".csv":
                sys.exit("Not a CSV file")

            table = make_table(sys.argv[1])
            print(table)
    except FileNotFoundError:
        sys.exit("File does not exist")


def make_table(filename_or_filepath):
    with open(filename_or_filepath, "r") as file:
        reader = csv.DictReader(file)
        table = tabulate(reader, headers="keys", tablefmt="grid")
        return table


main()
