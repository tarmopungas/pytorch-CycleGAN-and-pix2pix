"""
scale_images.py
Function to scale any image to the pixel values of [-1, 1] for GAN input.
Author: liuhh02 https://machinelearningtutorials.weebly.com/
"""
from PIL import Image
import numpy as np
from os import listdir

def normalize(arr):
    ''' Function to scale an input array to [-1, 1] '''
    # Check the original min and max values
    # print('Min: %.3f, Max: %.3f' % (arr_min, arr_max))
    arr_range = arr_max - arr_min
    scaled = np.array((arr - arr_min) / float(arr_range), dtype='f')
    arr_new = -1 + (scaled * 2)
    # Make sure min value is -1 and max value is 1
    # print('Min: %.3f, Max: %.3f' % (arr_new.min(), arr_new.max()))
    return arr_new

arr_min = 0  # absolute min
arr_max = 65535  # absolute max

classes = ["A", "B"]
fold = ["train", "test", "val"]

for c in classes:
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
            # convert to numpy array
            image = np.array(image)
            # scale to [-1,1]
            norm_image = normalize(image)
            # save image
            im = Image.fromarray(norm_image)
            im.save(out + filename)
        print("Completed " + c + "_" + f)

