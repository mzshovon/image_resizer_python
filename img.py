import PIL
from PIL import Image

height = 1000
width = 1400

img = Image.open('IMG_20191102_145854.jpg')
img = img.resize((width, height), PIL.Image.ANTIALIAS)
img.save('resize.jpg')