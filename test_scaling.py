from PIL import Image
from os import listdir


path = "./tarmo/train/"

for filename in listdir(path):
    if ".tiff" not in filename:
        continue
    # load image
    image = Image.open(path + filename)
    extremes = image.getextrema()
    if extremes[0] < -1.0 or extremes[1] > 1.0:
        print("Min < -1 või max > 1!")
    if extremes[1] == -1:
        print("Max väärtus on -1 :(")
