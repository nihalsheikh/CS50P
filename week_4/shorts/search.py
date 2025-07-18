# Week 4: Shorts: Modules and Packages
import requests
import sys

def main():
    artwork = input("Enter art name: ").strip()
    limit = int(input("How many results in nums? "))

    artworks = get_artworks(artwork, limit)
    for artwork in artworks:
        print(f"* {artwork}")


def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        sys.exit("Couldn't complete requests")

    content = response.json()
    return [artwork["title"] for artwork in content["data"]]


main()
