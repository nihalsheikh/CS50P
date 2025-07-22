# Week 4: Problem 5
# make a func, such that user inputs the level as 1,2 or 3 only
# that level is used to make 10 random arithmetic questions (only addition)
# a fucn in this return two randm ints x and y, use them for making questions
# count the times, questions have been answered, if it exceed 3, just return answer
# also prompt the user again and again if nums are negative ints, or not nums
import random


def main():
    level = get_level()
    # count the correct answers given by user
    score = 0

    # asking 10 questions to user
    for i in range(10):
        #  get the integer nums we will add later
        x = generate_integer(level) # int 1
        y = generate_integer(level) # int 2
        correct_ans = x + y

        # counting no. many times user tried to answer,
        # writing here so that we can reset it for every question
        attempts = 0

        # when attempts are less than 3 times
        while attempts < 3:
            # asking question as input itself on screen
            try:
                # ask for input answer from user
                user_ans = int(input(f"{x} + {y} = "))
                if user_ans == correct_ans:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        # when tried answering for 3 times
        if attempts == 3:
            print(f"{x} + {y} = {correct_ans}")

    # After loop ends print score
    print(f"Score: {score}")


def get_level():
    levels = [1,2,3]
    #  taking valid input by the user
    while True:
        try:
            level = int(input("Level: ").strip())
            if level in levels:
                return level
        except ValueError:
            continue


def generate_integer(level):
    # raising the difficulty according to the level input by user
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
