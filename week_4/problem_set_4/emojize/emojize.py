# Week 4: Problem Set 4
# Convert input string to emoji
# Using emoji library
import emoji


def main():
    # get user input fro emoji
    text = input("Input: ").strip()
    print(f"Output: {set_emoji(text)}")


# change text to emoji
def set_emoji(e):
    try:
        return emoji.emojize(e, language="alias", variant="emoji_type")
    except (ValueError, KeyError, AttributeError):
        return "Unknown Emoji"


main()
