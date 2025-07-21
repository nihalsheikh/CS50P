# Week 4: Problem 2
# convert user input text to ascii art, if font provided, art in that font, if not then random font
from pyfiglet import Figlet # import ascii art package called: pyfiglet
import random
import sys


figlet = Figlet()


def main():
    # get all the fonts for figlet, sort them and store it in a list
    fonts = sorted(figlet.getFonts())
    # print the text art
    if len(sys.argv) == 1:
        # user input of text
        text = input("Input: ").strip()
        # choose one random font, when sys.argv length is 0
        font = random.choice(fonts)
        print(text_art(text, font))
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        # user input of text
        text = input("Input: ").strip()
        print(text_art(text, sys.argv[2]))
    else:
        sys.exit("Something went wrong")


def text_art(text, style):
    # set the desired font
    figlet.setFont(font=style)
    # return the text_art
    return figlet.renderText(text)


main()
