# Week 6: File I/O

# Writing into the file
# name = input("What's your name? ")

# # "w": for overwriting previous data. "a": to append to existing data
# with open("names.md", "a") as file:
#     file.write(f"{name}\n")


# Reading the file (or Loading the file)
# with open("names.md", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# Sorting the file only and then printing the names
# with open("names.md") as file:
#     for line in sorted(file):
#         print("hello,",line.rstrip())

# Sorting and then Reading the file
names = [] # we will save the file data here

# reading all the data from the file and saving it the names list
with open("names.md") as file:
    for line in file:
        names.append(line.rstrip())

# sorting the names list and then printing it
for name in sorted(names):
    print(f"hello, {name}")
