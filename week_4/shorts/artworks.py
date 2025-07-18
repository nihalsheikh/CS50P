# Week 4: Shorts: Modules and Packages
# Making a artworks module/package
import requests
import sys

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
