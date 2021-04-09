import PIL
from PIL import Image
import os

directory = r'C:\python_projects\imges'
c = 1
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png') or not filename.endswith('.py'):
        img = Image.open(filename)
        height = 1200
        width = 1600
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
        img.save(filename)
        c += 1
        print(f'successfully resize image {filename}')
        continue
    else:
        print(f'oops! there is something wrong with {filename} check the format either jpg or png!')
        continue