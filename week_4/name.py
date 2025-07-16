# Week 4: Libraries
# sys module
import sys

# sys.exit function
# exiting program prematurely if error exist
# if len(sys.argv) < 2:
#     sys.exit("Too few arguements")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguements")

# print("Hello, my name is", sys.argv[1])

# Slicing
# Multiple Cmd line arguements
if len(sys.argv) < 2:
    sys.exit("Too few arguements")

for arg in sys.argv[1:]:
    print("Hi, my name is", arg)
