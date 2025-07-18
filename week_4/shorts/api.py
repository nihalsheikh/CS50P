# Week 4: Shorts
# Using Art Institure of Chicago Public API
# API URL: https://api.artic.edu/api/v1
# using requests library to get access over the internet
import requests
import sys


def main():
    print("Search the ARt Institute of Chicago!")
    artist = input("Enter name of the Artist: ")

    # it is best practice to use Exception Handling when accessing API's
    # API Endpoint: we using "/artworks/search" to access/search artwork
    try:

        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            # API Parameters
            {"q": artist},
        )

        #  we also need to check if the response actually worked as intended
        response.raise_for_status()
    except requests.HTTPError:
        sys.exit("Couldn't Complete request!")

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
