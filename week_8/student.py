# Week 8
import sys


def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    try:
        name = input("Name: ")
        house = input("House: ")
        return [name, house]
    except TypeError:
        sys.exit("Invalid Input: Name or House")


if __name__ == "__main__":
    main()
