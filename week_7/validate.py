# Week 7: Regular Expressions
import re


email = input("Enter email: ").strip()

if re.search(r"^[a-zA-Z0-9_]+[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
