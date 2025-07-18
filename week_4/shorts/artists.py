# Week 4: Shorts: Modules and Packages
# Making a artists module/package
import requests
import sys

def get_artists(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search",
            {"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        sys.exit("Couldn't complete requests")

    content = response.json()
    return [artist["title"] for artist in content["data"]]
