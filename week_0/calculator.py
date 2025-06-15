# Integers or int in python
# 1. Directly assigning values
# x = 1
# y = 2

# 2. Taking input from user
# x = input("Enter x: ")
# y = input("Enter y: ")

# There is a problem in directly using the values of x & y var in z
# python will treat them as a str values rather than int
# z = x + y

# to get rid of this issue we need to use int func 'int()' as follows
# z = int(x) + int(y)
# print(z)

# Nesting functions: function within a function is called nesting
# ex: we used input func within the int func
# the args taken by input func becomes the param value passed to int func
# x = int(input("Enter x: " ))
# y = int(input("Enter y: " ))

# now we can directly use x & y var & instead of using them in another var
# print(x + y)

# Float point values: decimal values in python
p = float(input("Enter p: "))
q = float(input("Enter q: "))

# Round Function round(): round off value to the nearest int
z = round(p + q)

print(z)

# Better number notations
# we can use f strings to provide comma inside numbers for separation
print(f"{z:,}")
