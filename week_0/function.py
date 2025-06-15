# Function in python
# def: this keyword is used to create or define a function
# def hello(): # no args and default values specified here
    # print("hello")

# hello() # fucn with no args and default values

# def greet(toWho="world"):
#     print("hello,", toWho)

# greet() # func with default value only

# name = input("Enter name: ")
# greet(name) # func with an argument

# Scope: context of a vairable's existence in which it is defined
def main():
    name = input("Enter name: ") # name var is defined in main function
    print("hello,", name)

def greet2():
    print(name) # name is defined in main func and we can't access it from another func directly
