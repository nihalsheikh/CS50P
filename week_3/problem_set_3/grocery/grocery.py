# Week 3: Problem 3
# Make a grocery list, user inputs the items (case-insensitive), when user exits,
# output list alphabetically in uppercase prefixed with number
def main():
    # add user input item in this dictionary
    item_list = {}

    while True:
        try:
            # Taking input from user of grocery items
            item = input().strip().lower()

            # adding items to dictionary, when item is not empty string and a string
            if len(item) > 0 and not item.isdigit():
                # when item exist in dict, increase its count value
                if item in item_list:
                    item_list[item] += 1
                # else set its value to 1
                else:
                    item_list[item] = 1

        except EOFError:
            # empty line before printing the Grocery List
            print()

            # sorting alphabetically arranged items in this dictionary (only keys stored)
            sorted_list = sorted(item_list.keys())
            for item in sorted_list:
                count = item_list[item]
                print(f"{count} {item.upper()}")
            break
        except (KeyError, ValueError, TypeError, KeyboardInterrupt):
            break
main()
