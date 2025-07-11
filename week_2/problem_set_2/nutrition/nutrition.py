# Week 2: Problem 5
# From a FDA approved list of fruits, user will provide a fruit name, give back the calories for that fruit
def main():
    item = input("Item: ").strip().lower()
    print(calc_calorie(item))

def calc_calorie(item):
    # Method 2: Dictionary with .get method
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grape": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    if item in fruits:
        return f"Calories: {fruits[item]}"
    else:
        return f""

main()
