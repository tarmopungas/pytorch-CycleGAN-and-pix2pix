"""
scale_images.py
Function to scale any image to the pixel values of [-1, 1] for GAN input.
Author: liuhh02 https://machinelearningtutorials.weebly.com/
"""
from PIL import Image
import numpy as np
from os import listdir

def normalize(arr, amin, amax):
    """ Function to scale an input array to [-1, 1] """
    # Check the original min and max values
    # print('Min: %.3f, Max: %.3f' % (arr_min, arr_max))
    new = np.where(arr > amax, amax, arr)  # replace values larger than max with max
    new = np.where(new < amin, amin, new)  # replace values smaller than min with min
    arr_range = amax - amin
    scaled = np.array((new - amin) / float(arr_range), dtype='f')
    arr_new = -1 + (scaled * 2)
    # Make sure min value is -1 and max value is 1
    # print('Min: %.3f, Max: %.3f' % (arr_new.min(), arr_new.max()))
    return arr_new


classes = ["A", "B"]
fold = ["train", "test", "val"]

for c in classes:
    if c == "A":
        amin = 1550
        amax = 3100
    else:
        amin = 150
        amax = 1400
    for f in fold:
        # path to folder containing images
        path = './tarmo/{}/{}/'.format(c, f)
        out = './tarmo/{}_norm/{}/'.format(c, f)
        # loop through all files in the directory
        for filename in listdir(path):
            if ".tiff" not in filename:
                continue
            # load image
            image = Image.open(path + filename)
            image = image.resize((256, 256)) # resize image first
            # convert to numpy array
            image = np.array(image)
            # scale to [-1,1]
            norm_image = normalize(image, amin, amax)
            # save image
            im = Image.fromarray(norm_image)
            im.save(out + filename)
        print("Completed " + c + "_" + f)

