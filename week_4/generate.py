# Week 4: Libraries
# import keyword
# from keyword
import random

# Get a random choice from the list provided
# coin = choice(["heads", "tails"])
# print(coin)

# Get a random integer from (a, b) inclusive range
# number = random.randint(1, 10)
# print(number)

# shuffle the list items
# list of type of cards
cards = ["diamondaaa", "heart", "spade", "club"]
# shuffle function in random module
random.shuffle(cards)
# print card individually
for card in cards:
    print(card)
