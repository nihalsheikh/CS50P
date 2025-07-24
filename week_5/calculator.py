# Week 5: Unit Tests
# calculate square
def main():
    x = input("What's x? ")
    print("x squared is", square(x))


def square(n):
    return n * n


# calling main only when this file will be executed
if __name__ == "__main__":
    main()
