# Week 4: Problem 4
# Guess the number: user inputs a `num`, make that the `range` from `1 to num` both inclusive
# Randomly chooses a num, if guessed num is small, say `Too small`, if guessed num is big, say `Too big`
# if guessed num is correct, say `Just right`
import random


def main():
    # print outcome
    print(guessed_num())


def guessed_num():
    # take user input for level and range
    while True:
        level = int(input("Level: ").strip())
        if level > 0:
            break
    # set an random answer between 1 and user input
    ans = random.randint(1, level)

    # guess answer
    while True:
        try:
            guess = int(input("Guess: ").strip())
            if guess > 0:
                # compare
                if guess < ans:
                    print("Too small!")
                elif guess > ans:
                    print("Too large!")
                elif guess == ans:
                    return "Just right!"
        except ValueError:
            guess = int(input("Guess: ").strip())


main()
