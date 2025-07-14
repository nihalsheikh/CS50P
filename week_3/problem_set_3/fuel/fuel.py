# Week 3: Problem 1
def main():
    # get the fraction numbers: numerator/denominator
    X, Y = get_fraction("Enter Fuel in Fraction (x/y): ")
    print(fuel(X, Y))

def get_fraction(f):
    # taking input till we get the right input form
    while True:
        fuel = input(f)

        try:
            X, Y = fuel.split(sep="/")
            # conditions for X and Y to be acceptable
            if X.isdigit() and Y.isdigit() and int(X) <= int(Y) and int(Y) > 0:
                return int(X), int(Y)
        # errors you might encounter during this
        except (ValueError, TypeError, ZeroDivisionError):
            pass

def fuel(x, y):
    # return percentage with those fraction nums
    tank = round((x / y) * 100)

    if tank <= 1:
        return "E"
    elif tank >= 99:
        return "F"
    else:
        return f"{tank}%"

main()
