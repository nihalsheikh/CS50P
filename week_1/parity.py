# Arithmetic Operators
# + - * / %
def main():
    x = int(input("What's x? "))
    if isEven(x):
        print("Even")
    else:
        print("Odd")

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
