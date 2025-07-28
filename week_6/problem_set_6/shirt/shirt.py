# Week 6: Problem 4
# User gives two cmd-line args, 1: arg1 is name or path of the img fiel to read as input
# 2: arg2 is name of the img file we want as output
# overaly shirt img on other images, resize and crop the input, and then save the output
import os
import sys
from PIL import Image, ImageOps


def main():
    try:
        # condition 1: Command-line args
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")

        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        if len(sys.argv) == 3:
            n1 = sys.argv[1].lower()
            n2 = sys.argv[2].lower()

            name1, ext1 = os.path.splitext(n1)
            name2, ext2 = os.path.splitext(n2)

            img_ext = (".jpg", ".jpeg", ".png")

            if ext1 not in img_ext:
                sys.exit("Invalid Input")

            if ext2 not in img_ext:
                sys.exit("Invalid Output")

            # input and output have different extensions
            if ext1 != ext2:
                sys.exit("Input and Output have different extensions")

            # if input file does not exist
            if not os.path.isfile(n1):
                raise FileNotFoundError

            new_image = overlay_img(n1, n2)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def overlay_img(input, output):
    # Open shirt img
    shirt_path = "shirt.png"
    shirt = Image.open(shirt_path)

    #  size of the shirt img
    size = shirt.size

    # open the photo to resize
    photo = Image.open(input)
    #  resize the photo
    photo = ImageOps.fit(photo, size)

    # Overlay the shirt and photo
    photo.paste(shirt, shirt)

    # save image
    photo.save(output)


if __name__ == "__main__":
    main()
