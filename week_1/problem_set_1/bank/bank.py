# greet hello
def main():
    greet = input("Greetings: ")
    greet = greet.lower().strip()
    g, n = greet.split()
    greetMe(g)

def greetMe(g):
    if(g == "hello"):
        print("$0")
    elif(g != "hello"):
        g = g.lstrip()
        if g == "h":
            print("$20")
    else:
        print("$100")
