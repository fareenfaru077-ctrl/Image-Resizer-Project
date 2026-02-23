import os
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        img = Image.open(os.path.join(input_folder, filename))
        img = img.resize((800, 600))
        img.save(os.path.join(output_folder, filename))
        print("Resized:", filename)

print("Done!")


