"""
pix2pix_combine
Combine 2 images from different domains for pix2pix. Make sure images in folderA and folderB have the same name.
Folder Structure:
folderA
    |--> train
    |--> valid (if any)
    |--> test (if any)
folderB
    |--> train
    |--> valid (if any)
    |--> test (if any)
dest_path
    |--> train
    |--> valid (if any)
    |--> test (if any_
Adapted from https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
"""

import os
import numpy as np
from PIL import Image
import cv2

# define paths for translation from domain A (images in folderA) -> domain B (images in folderB)
folderA = '/gpfs/space/home/tarmop/pytorch-CycleGAN-and-pix2pix/tarmo/A_norm'
folderB = '/gpfs/space/home/tarmop/pytorch-CycleGAN-and-pix2pix/tarmo/B_norm'
dest_path = './tarmo'

splits = os.listdir(folderA)

for sp in splits:
    if ".DS_Store" in sp:
        continue
    img_fold_A = os.path.join(folderA, sp)
    img_fold_B = os.path.join(folderB, sp)
    img_list = os.listdir(img_fold_A)
    num_imgs = len(img_list)
    img_fold_AB = os.path.join(dest_path, sp)
    if not os.path.isdir(img_fold_AB):
        os.makedirs(img_fold_AB)
    print('split = %s, number of images = %d' % (sp, num_imgs))
    for n in range(num_imgs):
        name_A = img_list[n]
        path_A = os.path.join(img_fold_A, name_A)
        name_B = name_A
        path_B = os.path.join(img_fold_B, name_B)
        if os.path.isfile(path_A) and os.path.isfile(path_B):
            name_AB = name_A
            path_AB = os.path.join(img_fold_AB, name_AB)
            im_A1 = Image.open(path_A)
            im_A = np.array(im_A1)
            im_B1 = Image.open(path_B)
            im_B = np.array(im_B1)
            im_AB = np.concatenate([im_A, im_B], 1)
            cv2.imwrite(path_AB, im_AB)
