# Week 6: File I/O
# make a gif from images
import os
from PIL import Image


image_folder_path = "lake_tahoe"
all_images = os.listdir(image_folder_path)

images = []

for img in sorted(all_images):
    if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        img_path = os.path.join(image_folder_path, img)
        image = Image.open(img_path)
        images.append(image)


images[0].save(
    "lake.gif", save_all=True, append_images=images[1:], duration=100, loop=0
)
