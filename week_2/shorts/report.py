# Report statistics of Spaceship
def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft["distance"] = 163

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
    return f"""
    ===== SpaceCraft Details =====

     Name: {spacecraft.get("name", "Unknown")}

     Distance: {spacecraft.get("distance", "Unknown")} AU

    ======== Report Ends =========
    """


main()
