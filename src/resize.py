from PIL import Image, ImageFilter

"""resize

takes an image, creates a thumbnail (keeping aspect ratio) of the image but to a smaller size

"""

img = Image.open("images/zion.jpg")

# initial size of image (2400, 1804)

print(img.size)
img.thumbnail((400, 200))

img.save("thumbnail.jpg")
