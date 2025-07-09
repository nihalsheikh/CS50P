# Week 2: Problem 1
# Convert the user input of camelCase to snake_case

def main():
    name = variable_name()
    print(snake_case(name))

def variable_name():
    # Repeating the input prompt till the str length is > 0
    while True:
        name = input("Enter camelCase: ").strip()
        if len(name) >  0:
            return name

def snake_case(var_name):
    if len(var_name) > 0:
        return 2

main()
