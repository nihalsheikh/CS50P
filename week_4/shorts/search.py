# Week 4: Shorts: Modules and Packages
# for searching artworks
from artworks import get_artworks

def main():
    # calling artwork module
    artwork = input("Enter art name: ").strip()
    limit = int(input("How many results in nums? "))

    artworks = get_artworks(artwork, limit)
    for artwork in artworks:
        print(f"* {artwork}")


main()
