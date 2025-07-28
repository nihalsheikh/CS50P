# Week 6: Problem 1
# Take a user input as a cmd-line arg for file name or path
# Find the total line of code in a python file, don't count line starting with "#" or " "
# and exit if file name does not ends with .py or no file found
import sys
import os
import errno


def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")

        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        if len(sys.argv) == 2:
            if not os.path.isfile(sys.argv[1]):
                raise FileNotFoundError

            if sys.argv[1][-3:] != ".py":
                sys.exit("Not a python file")

            total_lines = lines_of_code(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(total_lines)


def lines_of_code(filename_or_file_path):
    try:
        with open(filename_or_file_path, "r") as file:
            reader = file.readlines()
            count = 0
            for row in reader:
                if row.strip().startswith("#"):
                    continue
                if not row.strip(): # if whitespaces still exists after removing them, continue
                    continue
                else:
                    count += 1
            return count
    except:
        pass
    ...


if __name__ == "__main__":
    main()
