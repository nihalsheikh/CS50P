# Report statistics of Spaceship
def main():
    # print(create_report(spacecraft)) # used for Method 1 & 2
    spacecraft = {
        "Voyager 1": 163,
        "Voyager 2": 136,
        "Pioneer 10": 80,
        "Pioneer 10": 44,
        "New Horizon": 58,
    }

    for name in spacecraft.keys():
        print(f"{name} is {spacecraft[name]} AU away from earth")


def create_report(spacecraft): # used for Method 1 & 2 only
    # Method 1: Normal access to dictionaries
    # return f"""
    # ===== SpaceCraft Details =====
    #  Name: {spacecraft["name"]}
    #  Distance: {spacecraft["distance"]} AU
    # ======== Report Ends =========
    # """

    # Method 2: Using get() method to avoid error
    # return f"""
    # ===== SpaceCraft Details =====
    #  Name: {spacecraft.get("name", "Unknown")}
    #  Distance: {spacecraft.get("distance", "Unknown")} AU from Earth
    #  Orbit: in {spacecraft.get("orbit", "Unknown")} Orbit
    #  Planet: going towrads {spacecraft.get("planet", "Unknown")}
    # ======== Report Ends =========
    # """

    # Method 3: Looping on dictionary using key method to get key name
    return f"""
    ===== SpaceCraft Details =====

     Name: {spacecraft.get("name", "Unknown")}

     Distance: {spacecraft.get("distance", "Unknown")} AU from Earth

     Orbit: in {spacecraft.get("orbit", "Unknown")} Orbit

     Planet: going towrads {spacecraft.get("planet", "Unknown")}

    ======== Report Ends =========
    """


main()
