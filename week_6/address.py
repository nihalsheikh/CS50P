# Week 6: File I/O
import csv

students = []

with open("address.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"], "house": row["house"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} of house {student['house']} lives in {student['home']}")
