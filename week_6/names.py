# Week 6: File I/O

name = input("What's your name? ")

# "w": for overwriting previous data. "a": to append to existing data
with open("names.md", "a") as file:
    file.write(f"{name}\n")
