# Week 7: Regular Expressions
import re


email = input("Enter email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
