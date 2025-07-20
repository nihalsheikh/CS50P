# Week 4: Problem Set 4
# Convert input string to emoji
# Using emoji library
import emoji


def main():
    # get user input fro emoji
    text = input("").strip()
    print(set_emoji(text), end="")


# change text to emoji
def set_emoji(e):
    try:
        return f"{emoji.emojize(e, language="alias")}"
    except (ValueError, KeyError, AttributeError):
        return "Unknown Emoji"


main()
