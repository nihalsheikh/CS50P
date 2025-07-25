# Week 5: Problem 3
# re-make the vanity plate program here
def main():
    plate = input("Enter Plate: ")

    # valid or invalid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    ...


def is_valid(s):
    # condition 1: plate starts with chars and length between 2 and 6 inclusive
    if len(s) < 2 or len(s) > 6:
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # condition 4: no special characters (only alphanumeric allowed)
    if not s.isalnum():
        return False

    # condition 3: nums not in middle and first num != 0
    num_found = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not num_found:
                if char == "0":
                    return False
                num_found = True
            # after first number found, rest of chars must be digits
            if not s[i:].isdigit():
                return False
            break

    return True


if __name__ == "__main__":
    main()
