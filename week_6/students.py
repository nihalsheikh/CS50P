# Week 6: File I/O

# Reading .csv file
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in house {house}")


# Sorting the names and then printing the csv file
# creating a list of dictionary to save "name: house" data
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# def get_name(student):
#     return student["name"]

# students: list iterable, get_name: gives name from dictionary, reverse: sorting order (True: desc, False: asc)
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in house: {student['house']}")
