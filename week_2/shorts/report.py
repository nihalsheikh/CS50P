# Report statistics of Spaceship
def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft.update(
        {
            "distance": 163,
            "orbit": "Sun",
            "planet": "Venus"
        }
    )

    print(create_report(spacecraft))

def create_report(spacecraft):
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
