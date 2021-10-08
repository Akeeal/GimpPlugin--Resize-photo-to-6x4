#portrait 6x4

from gimpfu import *

def portrait64(image, drawable):
    # Image
    # Scale Image

    new_height = 1800
    new_width = (new_height*image.width)/image.height
    
    pdb.gimp_image_scale(image, new_width, new_height)
    
    pdb.gimp_image_set_resolution(image, 1000.0, 1000.0)
    
    
register(
    "python-fu-portrait64",
    "scales image 6x4",
    "Scales images to 1800 high, preserve form factor and save as jpg, png and webp files.",
    "Akeeal", "Akeeal", "2020",
    "Scale to Portrait 6x4",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    portrait64, menu="<Image>/READY PICTURE/STEP 1 = Scaling to 6x4 or 4x6 photo")  # second item is menu location

main()
