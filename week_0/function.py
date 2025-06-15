# Function in python
# def: this keyword is used to create or define a function
def hello(): # no args and default values specified here
    print("hello")

# hello() # fucn with no args and default values

def greet(toWho="world"):
    print("hello,", toWho)

greet() # func with default value only

name = input("Enter name: ")
greet(name) # func with an argument
