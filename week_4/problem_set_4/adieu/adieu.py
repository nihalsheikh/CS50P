# Week 4: Problem 3
# Say adieu to every name user inputs (n), separating them with (n-1) commas, and one (and)
import inflect

def main():
    print(goodbye())

def goodbye():
    # store all input names here
    names = []
    # using the inflect python lib
    p = inflect.engine()

    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            # return f"Adieu, adieu, to {names[n]}, and {names[n-1]}"
            print()j
            return f"Adieu, adieu, to {p.join(names)}"


main()
