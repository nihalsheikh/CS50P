# Functions
# print is a basic function to print something on the terminal
# arguments: anything written in between the parenthesis '()' symbol is an arg
print("Hello, World!")

# Input Function: takes in input from user
# syntax: input()
input("Provide an input: ")

# Variables
# syntax: <varname>
# Assignment operator '=', value from the right of equal to symbol is assigned to left
name = input("Enter your name?")

# separating args with comma
print("hello,", name)

# how to print in a single line, if we use 2 print func
# we can pass additional params such as `end` and `sep`
# end="\n" takes you to next line
# sep=" " adds space between 2 args
print("hello, ", end="")
print(name)

# String Methods
# 1. strip() - this method removes whitespaces from left and right of a string
# ex: .....john.... => john
name = name.string()

# 2. capitalize() - this methods makes the first letter of the word of a string capital
# ex: john doe => John doe
name = name.capitalize()

# 3. title() - this method will capitalize the first letter of every word in a string
# ex: john doe => John Doe
name = name.title()
