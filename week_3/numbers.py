# Week 3: Exceptions
# try and except

def main():
    x = get_int()
    print(f"x is {x}")

# else
# pass
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass # catching the error, but not doing anything about/on it

main()
