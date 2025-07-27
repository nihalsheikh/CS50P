from PIL import Image, ImageFilter

def main():
    with Image.open("in.jpg") as img:
        # print(img.size) # size: (width, height)
        # print(img.format)
        img = img.rotate(360)
        # img = img.filter(ImageFilter.BLUR)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("edges.jpeg")


main()
