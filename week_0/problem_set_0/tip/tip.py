# Week 0: Problem 5
# define 2 function to print the flost value of amount and tip
# Code structure was given on the page only define the dollar & percent func
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.lstrip('$')
    return float(d)

def percent_to_float(p):
    p = p.rstrip('%')
    return float(p) / 100

main()
