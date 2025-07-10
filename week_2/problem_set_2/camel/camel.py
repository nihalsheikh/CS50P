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
       
    new_word = ""
    # Check every char in the string through loop
    for char in var_name:
        # when the char in string is Uppercase
        if char.isupper():
            # check whether the char is at the start of the string
            if new_word != "":
                new_word = new_word + "_" # add _ only when Uppercase char is not at the start

            new_word = new_word + char.lower() # and then add the lowercase version of that char
        else:
            # all the other the time when char is not uppercase, keep it adding to our new_word
            new_word = new_word + char

    return f"snake_case: {new_word}"

main()
