# Week 7: Regex
import re

#  user input's some string
name = input("Enter your name: ").strip()

# regex match the inpput string
matches = re.search("(.+), *(.+)", name)

#  if match is true, format it
if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
