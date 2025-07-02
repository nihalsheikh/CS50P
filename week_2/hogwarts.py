# lists: lists are zero-indexed, meaning their posisiton counting starts from 0
# students = ["Hermione", "Harry", "Ron"]

# printing an list item with its index
#  to access a list item, write list name and its index inside the square bracket
# print(students[0])

# we can print the list items using loops, isntead of printing them manually by assigning index individually
# for student in students:
#     print(student)

#  What if we want the loop to take in numbers as params, then we use following:
# we use len or length to get the count of items in a object
# for i in range(len(students)):
#     print(students[i])

# Dictionaries or dict
# when you want to associate some values with each other, we use dict
# to make dicts use curly braces `{"key" : "value"}` syntax
# lets say we want to associate houses to students
students = {
    "Hermione": "Gryffindor", # `key: value`, key equals value pair
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# to print the names of students, simply iterate over dict
# for student in students:
#     # prints: key: value
#     print(student, students[student], sep=": ")

# Using dict inside lists
# lets say we have more data related to student, how are we gonna associate that data, see below example:
# sometimnes we havce data which is literally empty or has no value, in such places we use None keyword
# None keyword: it literally has no value
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

# itetrating over a dict
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
