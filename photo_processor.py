# Importing in the Pillow and Misc Operating System Interfaces (OS) libraries. 
# Pillow overfiew and additional features can be found here: https://pillow.readthedocs.io/en/stable/
from importlib.resources import path
from PIL import Image, ImageEnhance, ImageFilter
import os

# Establishing variables for folder pathways for both unedited and edited images
path_unedited = './images'
path_edited = '/edited_images'

# Creating a foorloop for each unedited image in the folder
for filename in os.listdir(path_unedited):
    # importing in the image from the folder
    img = Image.open(f'{path_unedited}/{filename}')

    # Edits made to the recently opened image
    # changing the image to greyscale
    img_edit = img.filter(ImageFilter.SHARPEN).convert('L')
    
    # Adjusting contrast. change the contrast factor below as needed
    contrast_factor = 1.5
    contrast_edit = ImageEnhance.Contrast(img_edit).enhance(contrast_factor)

    # Creating the new edited picture file name
    root_edit_name = os.path.splitext(filename)[0]
    img_edit.save(f'.{path_edited}/{root_edit_name}_edited.jpg')