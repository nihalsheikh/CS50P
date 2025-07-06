# Report statistics of Spaceship
def main():
    spacecraft = {"name": "Voyager 1", "distance": "163"}

    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""

    ===== SpaceCraft Details =====

     Name: {spacecraft["name"]}

     Distance: {spacecraft["distance"]} AU

    ======== Report Ends =========

    """

main()
