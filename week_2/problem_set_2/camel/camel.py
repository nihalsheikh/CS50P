# Week 2: Problem 1
# Convert the user input of camelCase to snake_case

def main():
    name = variable_name()
    print(snake_case(name))

def variable_name():
    # Repeating the input prompt till the str length is > 0
    while True:
        name = input("camelCase: ").strip()
        if len(name) >  0:
            return name

def snake_case(var_name):
    # Method 1: Using Loops and Conditions
    # new_word = ""
    # # Check every char in the string through loop
    # for char in var_name:
    #     # when the char in string is Uppercase
    #     if char.isupper():
    #         # check whether the char is at the start of the string
    #         if new_word != "":
    #             new_word = new_word + "_" # add _ only when Uppercase char is not at the start

    #         new_word = new_word + char.lower() # and then add the lowercase version of that char
    #     else:
    #         # all the other the time when char is not uppercase, keep it adding to our new_word
    #         new_word = new_word + char

    # Method 2: Using List Comprehension
    # enumerate(): it is a string method which iterates over a string and gives us the index and individual char in the string
    new_word_list = [
        "_" + char.lower() if char.isupper() and i > 0 else char.lower() for i, char in enumerate(var_name)
    ]

    new_word = ''.join(new_word_list)
    return f"snake_case: {new_word}"

main()
