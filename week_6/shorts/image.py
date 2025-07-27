from PIL import Image, ImageFilter

def main():
    with Image.open("in.jpg") as img:
        # print(img.size) # size: (width, height)
        # print(img.format)
        img = img.rotate(360)
        img = img.filter(ImageFilter.BLUR)
        img.save("blur.jpeg")


main()
