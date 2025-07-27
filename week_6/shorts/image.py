from PIL import Image


def main():
    with Image.open("in.jpg") as img:
        print(img.size) # size: (width, height)
        print(img.format)


main()
