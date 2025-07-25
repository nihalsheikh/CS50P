# Week 5: Problem 2
# re-make the solution for the program in problem set 1
def main():
    greet = input("Greetings: ").strip()
    print(f"${value(greet)}")


def value(greeting):
    greet = greeting.lower()
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
