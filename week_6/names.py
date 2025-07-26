# Week 6: File I/O

# Writing into the file
# name = input("What's your name? ")

# # "w": for overwriting previous data. "a": to append to existing data
# with open("names.md", "a") as file:
#     file.write(f"{name}\n")


# Reading the file (or Loading the file)
with open("names.md", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
