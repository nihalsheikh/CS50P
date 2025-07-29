# Week 7: Regex
import re

#  user input's some string
name = input("Enter your name: ").strip()

# regex match the inpput string
#  if match is true, format it
# Using Walrus Operator (:=): assign a value from right to left and ask a boolean question at the same time
if matches := re.search("(.+), *(.+)", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
