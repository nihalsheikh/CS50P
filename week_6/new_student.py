# Week 6: File I/O
import csv


name = input("What's your name? ")
home = input("Where's your home? ")
house = input("What's your house? ")

with open("new_student.csv", "a") as file:
    writer = csv.DictWriter(file, ["name", "home", "house"])
    writer.writerow({"name": name, "home": home, "house": house}) 
