# Week 5: Problem 4
# re-make the fuel problem from problem set 3
def main():
    # get the fraction numbers: numerator/denominator
    while True:
        try:
            fuel = input("Enter Fuel in Fraction (x/y): ")
            fuel_percentage = convert(fuel)
            print(gauge(fuel_percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    # taking input till we get the right input form
    try:
        X, Y = fraction.split("/")
        # conditions for X and Y to be acceptable
        if not (X.isdigit() and Y.isdigit()):
            raise ValueError

        numerator = int(X)
        denominator = int(Y)

        if denominator == 0:
            raise ZeroDivisionError

        if numerator > denominator:
            raise ValueError

        return round((numerator / denominator) * 100)
        # errors you might encounter during this
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    # return percentage with those fraction nums
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
