# Week 5: Unit tests
def main():
    name = input("Enter your name: ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()
