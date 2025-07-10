# Week 2: Problem 3
# User inputs a string, remove vowels from it to shorten it
def main():
    # User input and remove the whitespaces from left and right
    text = input("Enter Text: ").strip()
    print(shorten(text))

def shorten(user_text):
    # new word without vowels initialized
    # short_word = ""

    # Tuple of vowels
    vowels = ("a", "e", "i", "o" , "u", "A", "E", "I", "O", "U")

    # Method 1: Through loops and Conditions
    # go through every char in user_text and check if exist in vowels
    # for c in user_text:
    #     if c not in vowels:
    #         short_word += c

    # Method 2: Using List Comprehension
    short_word = ''.join([char for char in user_text if char not in vowels])

    return f"Short Word: {short_word}"

main()
