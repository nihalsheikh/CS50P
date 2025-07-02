# Week 2: Loops

# Print meow 3 times:
# print("meow")
# print("meow")
# print("meow")

# While Loop
# using while loop to execute the same code as above
# print("While Loop")
# i = 3
# while i != 0:
#     print("meow")
#     i -= 1 # earlier we wrote i = i - 1

# # same code as above, just different logic
# i = 0
# while i < 3:
#     print("meow")
#     i += 1 # earlier we wrote i = i + 1

# For loop
# using for loop to perform same tasks as above
# List: a datatype in python, to make a list use square brackets `[]` add items by separation using comma `,`
print("For Loop")
# for i in [0,1,2]: # list is [0,1,2]
#     print("meow")

# same code as above, using range func instead of list
# for i in range(3):
#     print("meow")

# minor improvements in the above code
# as we only initialize i everytime we run for loop, we should use _ symbol, to specify it is never used again
for _ in range(3):
    print("meow")


#  We can also write the above code without ever using loops
print("\nAnother method")
# multiply str by 3

# in this case meow will be printed continuously
# print("meow" * 3)

#  This one below, prints an extra blank line below last meow
# print("meow\n" * 3)

# python lets you decide how to end line
print("meow\n" * 3, end="")
