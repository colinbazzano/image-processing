"""JPG TO PNG

What we want to have at the end:

using the CLI, you can run the file passing 2 arguments, the current Folder you want to have,
and the new folder you want to create


"""
import sys
import os
from PIL import Image

# grab the first & second argument
prev_folder = sys.argv[1]
new_folder = sys.argv[2]
# check if new folder exists, if not, create it
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop through old folder,
for filename in os.listdir(prev_folder):
    img = Image.open(f'{prev_folder}{filename}')
    # separate the .jpg from the name of the image
    clean_name = os.path.splitext(filename)[0]
    # save the image and tack on a .png to the end
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print('all done')


# convert to PNG
# save to the new folder
