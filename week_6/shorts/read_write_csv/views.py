# Week 6: Shorts - File I/O
import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as views, open("all_data.csv", "w") as data:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(data, reader.fieldnames + ["img_brightness"])
        writer.writeheader()

        for row in reader:
            # Brightness is on scale of (0, 1). 0: max. dark, 1: max. bright
            brightness = calc_brightness(f"mt_fuji/{row['id']}.jpeg")
            # print(row["id"])
            # print(round(brightness, 2))

            writer.writerow({
                "id": row["id"],
                "english_title": row["english_title"],
                "japanese_title": row["japanese_title"],
                "img_brightness": round(brightness, 2)
            })


def calc_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255

    return brightness


main()
