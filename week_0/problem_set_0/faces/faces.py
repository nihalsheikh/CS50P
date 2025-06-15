# Week 0: Problem 3
# covert emoticons to emoji 🙂 🙁
def main():
    emoji = str(input("Enter an emoticon: "))
    print(convert(emoji))

def convert(emote):
    emote= emote.replace(":(", '🙁').replace(":)", '🙂')
    return emote

main()
