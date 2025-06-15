# Side Effect: any changes occuring because of running a func ither than its return value is side effect
# Global: global keyword is used to modify the Global variale locally in a func
# ex:

emoticon = "V_V" # global variable

def main():
    global emoticon # making global var accessible
    say("is there anyone")

    emoticon = "XD" # modifying the global variable
    say("Oh, Hi!")

def say(phrase):
    print(phrase, emoticon) # side effect of say func

main()
