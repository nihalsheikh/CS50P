# Main file for project
# main() + additional 3 functions, not nested functions
# those 3 func should have test case, that can be tested with pytest
import csv
import sys
import argparse


class Password:
    # check the password validation, code options to what action to perform
    ...


def main():
    # call whatever action required
    ...


def read_passwords_file():
    # read or import {url, username, password} from a file
    ...


def write_passwords_file():
    # write or make a new passowrd csv file
    ...


def generate_password():
    # generate an alpha-numeric with symbols a strong password with variable length
    ...


def password_hashing():
    # storing the password as it is, is not recommended, so encrypt the password
    ...


def generate_qr_code():
    # return a dictionary of {url: "url", username: "username", password: "password"}
    ...


def modify_passwords():
    # update {url, username, password} in the password file or db
    ...


def table_print_password():
    # print the required password you want on the terminal
    ...


if __name__ == "__main__":
    main()
