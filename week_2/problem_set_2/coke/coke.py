# Week 2: Problem 2
# Buy a coke of 50 cent. Enter an amount to pay in cents then give back due/owed amount back to customer.
def main():
    # initail paid amount
    paid_amount = 0
    # inital coke price
    coke_price = 50

    while paid_amount < coke_price:
        # Calculate the due amount
        amount_due = coke_price - paid_amount
        print(f"Amount Due: {amount_due}")

        # User insert some value
        coin_input = (input("Insert Coin: "))
        if coin_input == "" or not coin_input.isdigit():
            continue

        # convert input to integer
        coin = int(coin_input)

        # Check inserted coin is of valid values/coins
        if coin == 25 or coin == 10 or coin == 5:
            paid_amount += coin

    # Calculate change owed
    if paid_amount >= coke_price:
        owed = paid_amount - coke_price
        print(f"Change Owed: {owed}")

main()
