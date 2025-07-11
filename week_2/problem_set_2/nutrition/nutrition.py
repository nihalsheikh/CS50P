# Week 2: Problem 5
# From a FDA approved list of fruits, user will provide a fruit name, give back the calories for that fruit
def main():
    item = input("Item: ").strip().lower()
    print(calc_calorie(item))

def calc_calorie(item):
    # Method 1: List inside Dictionary
    # fruits = [
    #     {"fruit" : "Apple", "calories": 130},
    #     {"fruit" : "Avocado", "calories": 50},
    #     {"fruit" : "Banana", "calories": 110},
    #     {"fruit" : "Cantaloupe", "calories": 50},
    #     {"fruit" : "Grapefruit", "calories": 60},
    #     {"fruit" : "Grape", "calories": 90},
    #     {"fruit" : "Honeydew Melon", "calories": 50},
    #     {"fruit" : "Kiwifruit", "calories": 90},
    #     {"fruit" : "Lemon", "calories": 15},
    #     {"fruit" : "Lime", "calories": 20},
    #     {"fruit" : "Nectarine", "calories": 60},
    #     {"fruit" : "Orange", "calories": 80},
    #     {"fruit" : "Peach", "calories": 60},
    #     {"fruit" : "Pear", "calories": 100},
    #     {"fruit" : "Pineapple", "calories": 50},
    #     {"fruit" : "Plums", "calories": 70},
    #     {"fruit" : "Strawberries", "calories": 50},
    #     {"fruit" : "Sweet Cherries", "calories": 100},
    #     {"fruit" : "Tangerine", "calories": 50},
    #     {"fruit" : "Watermelon", "calories": 80}
    # ]

    # for fru in fruits:
    #     if item == fru["fruit"].lower():
    #         return f"Calories: {fru["calories"]}"

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

    # fruit = item.lower()

    if item in fruits:
        return f"Calories: {fruits[item]}"
    else:
        return f""

main()
