# Keys and Values Methods in Dictionary
def main():
    distances = {
        "Voyager 1": 163,
        "Voyager 2": 136,
        "Pioneer 10": 80,
        "Pioneer 11": 44,
        "New Horizon": 58,
    }

    # Key method: For looping over the key name in a dictionary
    # for name in distances.keys():
    #     print(f"{name} is {distances[name]} AU away from earth")

    # Value method: for looping over the values in the dictionary
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")

def convert(au):
    # Converting AU distance in meters
    return au * 149597870700

main()
