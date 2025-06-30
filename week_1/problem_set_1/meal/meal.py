# Week 1: Problem 5
# Tell user id it time for a meal?
def main():
    whatTime = input("What time is it? ").strip()
    t = convert(whatTime)

    # Chekcing is it a meal time
    if 7.00 <= t <= 8.00:
        print("breakfast time")
    elif 12.00 <= t <= 13.00:
        print("lunch time")
    elif 18.00 <= t <= 19.00:
        print("dinner time")

def convert(time):
    if ":" not in time:
        return "Invalid Time"
    hrs, min = time.split(":")
    hrs = float(hrs)
    min = float(min)

    isMealTime = hrs + (min / 60) # converting time. ex: 7:30 -> 7.5
    return isMealTime

if __name__ == "__main__":
    main()
