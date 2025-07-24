# Week 5: Problem 1
# re-make twttr problem from Problem Set 2
def main():
    text = input("say something: ").strip()
    print(shorten(text))


def shorten(word):
    vowels= ("a", "e", "i", "o", "u") # ["a", "e", "i", "o", "u"] ["A", "E", "I", "O", "U"]
    # vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    new_word = "".join([char for char in word if char not in vowels])
    return new_word


if __name__ == "__main__":
    main()
