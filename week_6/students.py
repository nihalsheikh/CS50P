# Week 6: File I/O
# reading .csv file
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in house {house}")
