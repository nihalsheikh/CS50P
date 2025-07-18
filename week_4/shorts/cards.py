# Week 4: Shorts - random module
import random

cards = ["jack", "queen", "king"]

def main():
    # choice: returns a single value from the List passed to it
    # my_card = random.choice(cards)
    # print(my_card)

    # choices: returns multiple value when specified. Uses sampling with replacement
    # my_cards = random.choices(cards, weights=[65,30,5], k=2)
    # print(my_cards)

    # sample: returns multiple value when specified, but without replacement
    # my_cards = random.sample(cards, k=2)
    # print(my_cards)

    # seed: normally set to default change using system time, but we set it to 0 here
    random.seed(1)
    my_cards = random.choices(cards, k=2)
    print(my_cards)

main()
