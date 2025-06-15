# Integers or int in python
# 1. Directly assigning values
# x = 1
# y = 2

# 2. Taking input from user
x = input("Enter x: ")
y = input("Enter y: ")

# There is a problem in directly using the values of x & y var in z
# python will treat them as a str values rather than int
# z = x + y

# to get rid of this issue we need to use int func 'int()' as follows
z = int(x) + int(y)
print(z)
