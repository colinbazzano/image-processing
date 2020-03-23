from PIL import Image, ImageFilter

img = Image.open("images/pika.jpg")

# a way to edit the photos by running the script. There are many but this one blurs the image a little and saves it into a PNG
# filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')

# filtered_img.save('blur.png', 'png')
filtered_img.save('grey.png', 'png')  # saves the file into a new format
filtered_img.show()

# displays the type of image
# print(img.format)
# # displays the size of the image
# print(img.size)
# # displays the mode, such as RGB
# print(img.mode)

# resize images:

resize = filtered_img.resize((300, 300))  # accepts a tuple
resize.save("grey.png", "png")
