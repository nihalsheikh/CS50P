# Goodbye CS50 Python
import cowsay
import pyttsx3


engine = pyttsx3.init()

this = input("Enter something: ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
