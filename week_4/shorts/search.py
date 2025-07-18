# Week 4: Shorts: Modules and Packages
# for searching artworks
# import artworks
# from artworks import get_artworks
# Importing Package: Museum.artworks
from museum.artworks import get_artworks

# for searching artists
# import artists
# from artists import get_artists
# Importing Package: Museum.artists
from museum.artists import get_artists


def main():
    # calling artwork module
    # artwork = input("Enter art name: ").strip()
    # limit = int(input("How many results in nums? "))

    # artworks = get_artworks(artwork, limit)
    # for artwork in artworks:
    #     print(f"* {artwork}")

    # calling artists module
    artist = input("Enter artist name: ").strip()
    limit = int(input("How many results in nums? "))

    artists = get_artists(artist, limit)
    for artist in artists:
        print(f"* {artist}")


main()
