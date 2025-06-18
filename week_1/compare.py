# Compare values
x = int(input("Enter x: "))
y = int(input("Enter y: "))

# if keyword
# syntax: if > Boolean expression > : ><nextLine> some code/func
# if x < y :
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")

# elif
# when you have multiple questions istead of using only 'if' keyword we use 'elif' to be more inclusive
# if x < y :
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")


# else
# used at last, when we know the all the other values of bool exp will return false
# if x < y :
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else: # no need to write bool exp for 'else'
#     print("x is equal to y") # executed only when other (above) conditions for bool exp return false

# or
# used to reduce the no. of questions asked
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
