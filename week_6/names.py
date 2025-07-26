# Week 6: File I/O

name = input("What's your name? ")

file = open("names.md", "a") # "w": for overwriting previous data. "a": to append to existing data
file.write(f"{name}\n")
file.close()
