# Week 5: Unit tests
# testing the calculator file
from calculator import square


def main():
    test_square()


def test_square():
    # using assert keyword, we may also encounter error aliongside, so use Exception Handling
    try:
        assert square(2) == 4
    except AssertionError:
        print("Error: 2 squared was not 4")

    try:
        assert square(- 2) == 4
    except AssertionError:
        print("Error: -2 squared was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("Error: 3 squared was not 9")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("Error: -3 squared was not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("Error: 0 squared was not 0")


if __name__ == "__main__":
    main()
