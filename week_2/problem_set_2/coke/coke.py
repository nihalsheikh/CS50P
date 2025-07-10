# Week 2: Problem 2
# Buy a coke of 50 cent. Enter an amount to pay in cents then give back due/owed amount back to customer.
def main():
    # Taking user input of valid amount
    paid = [0]
    coke = 50

    while coke > 0:
        print(f"Amount Due: {coke}")
        coin = insert_coin()
        paid.append(coin)
        coke -= coin
        total_amount_paid = sum(paid)

        if coke <= 0:
            owed = abs(50 - total_amount_paid)
            print(f"Change Owed: {owed}")

def insert_coin():
    while True:
        coin = int(input("Insert Coin: "))
        if coin > 0 and coin == 25 or coin == 10 or coin == 5:
            return coin

main()
