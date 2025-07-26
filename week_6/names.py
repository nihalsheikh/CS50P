# Week 6: File I/O

name = input("What's your name? ")

file = open("names.md", "w")
file.write(name)
file.close()
