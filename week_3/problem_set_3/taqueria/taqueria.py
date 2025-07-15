# Week 3: Problem 2
# Order from the Felipe Taqueria restaurant
def main():
    # Dictionary of menu items and prices
    # writing `key` in lowercase, because we are making program case-insensitive
    menu = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }

    # Initializing total price
    total = 0.00

    # To ask user for infinite inputs
    while True:
        try:
            # Input is case-insenitive and remove whitespaces
            item = input("Item: ").strip().lower()
            if item in menu:
                # Adding the value of each item input to the total price
                total += menu[item]
                print(f"Total: ${total:.2f}")
        # Catching all the errors and doing something about it.
        except (KeyError, ValueError, TypeError):
            pass
        except EOFError:
            print() # going to next line
            break

main()
