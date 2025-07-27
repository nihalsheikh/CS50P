# Week 6: Shorts - File I/O
import csv


def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

main()
