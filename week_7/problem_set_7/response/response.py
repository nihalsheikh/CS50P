# Week 7: Problem 5
# import validators
from validator_collection import validators, checkers


def main():
    is_true = check(input("Enter email: "))

    if is_true:
        print("Valid")
    else:
        print("Invalid")


def check(s):
    try:
        email_address = validators.email(s)
        is_email_address = checkers.is_email(email_address)

        return is_email_address
    except:
        return False


if __name__ == "__main__":
    main()
