# Week 2: Problem 4
# Verify the conditions for Vanity plate to be valid or invalid
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Conditions for Vanity to be VALID
    # 1: plate start with 2 CHAR
    # 2: max 6 CHAR allowed and a min of 2 CHAR
    # 3: NUMS not in middle of CHAR, first num should not be 0, ex:  AAA222 <- Valid, AAA22A <- Invalid
    # 4: Periods, Spaces or Punctuation NOT ALLOWED (".", " ", "!")

    # Check if all required conditions are met
    if two_char(s) and char_length(s) and is_digit(s) and invalid_char(s):
        return True
    else:
        return False

def two_char(s):
    # C1: plate start with 2 CHAR
    # If length greater than 2 and first 2 chars are not nums
    # isalpha: check if all letters in plate are chars
    if len(s) >= 2:
        if s[0].isalpha() and s[1].isalpha(): # checking if numbers
            return True
    return False

def char_length(s):
    # C2: allowed plate string length: MIN - 2, MAX - 6
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False

def is_digit(s):
    # C3: NUMS not in middle of plate and first num should not be 0
    # ex:  AAA222 <- Valid, AAA22A <- Invalid, AAA02 <- Invalid

    # if num found in the middle of plate chars
    found_num = False

    for i, char in enumerate(s):
        # isdigit: string method to check if char is a digit
        # if we found a number in our plate
        if char.isdigit():
            # check if it is the first num we found in plate
            if not found_num:
                # check if that num is '0'
                if char == '0':
                    return False
                # if the found num is not zero, turn found_num to True
                found_num = True

            # When we found a num in char, we need to make sure it is not in the middle of chars
            # and the remaining chars in plates are all nums, followed by the first num we find
            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return False
            # if all the chars we find after the first num, are also nums, then break out of the loop
            break

    return True

def invalid_char(s):
    # C4: Periods, Spaces or Punctuation NOT ALLOWED (".", " ", "!")
    # isalnum: checks if string contains only alphanumeric values
    # returns True if all chars are alphanumeric, and False in every other case
    if s.isalnum():
        return True
    else:
        return False

main()
