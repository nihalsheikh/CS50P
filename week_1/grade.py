# and keyword
score = int(input("Enter Score: "))

# if score >= 90 and score <= 100:
#     print("Grade A")
# elif score >= 80 and score < 90:
#     print("Grade B")
# elif score >= 70 and score < 80:
#     print("Grade C")
# elif score >= 80 and score < 70:
#     print("Grade D")
# else:
#     print("Grade F")

# another way to write above example:
# if 90 <= score and score <= 100:
#     print("Grade A")
# elif 80 <= score and score < 90:
#     print("Grade B")
# elif 70 <= score and score < 80:
#     print("Grade C")
# elif 60 <= score and score < 70:
#     print("Grade D")
# else:
#     print("Grade F")

# We can again improve the above code and completely remove the 'and' keyword usage in code
# Python allows the following kind of nesting and chainng of bool exp in conditional statements
if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
else:
    print("Grade F")
