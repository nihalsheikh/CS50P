# greet hello
def main():
    greet = input("Greetings: ") # take input from user
    greet = greet.lower().strip() # make sure input is in lower case and no white spaces
    greetMe(greet) # calling greetMe func with user input

def greetMe(g):
    # 'startswith' method: use this method, when searching for a specific string in the start
    if g.startswith("hello"):
        print("$0")
    elif g.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
