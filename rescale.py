from PIL import Image
import numpy as np
from os import listdir

def rescale(arr):
    arr_new = arr + 1
    arr_new = arr_new / 2
    arr_new = np.array(arr_new * float(arr_max - arr_min), dtype='f')
    arr_new = arr_new + arr_min
    arr_new = np.array(np.round(arr_new, 0), dtype='uint16')
    return arr_new


arr_min = 0  # absolute min
arr_max = 65535  # absolute max

# Test rescaling
path = "./results/syngenta_16bitABSnorm/test_latest/images/"
out = "./results/syngenta_16bitABSnorm/test_latest/rescaled/"

for filename in listdir(path):
    if ".tiff" not in filename:
        continue
    # load image
    image = Image.open(path + filename)
    # convert to numpy array
    image = np.array(image)
    # scale to [-1,1]
    scaled = rescale(image)
    # save image
    im = Image.fromarray(scaled)
    im.save(out + filename)

