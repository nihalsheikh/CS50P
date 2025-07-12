# Week 3: Exceptions
# try and except
# Added params
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

# else
# pass
# pass an arg
def get_int(num):
    while True:
        try:
            return int(input(num))
        except ValueError:
            pass # catching the error, but not doing anything about/on it

main()
