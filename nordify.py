from PIL import Image, ImageFilter
from math import sqrt
import os
import argparse

nord_colors = [(46, 52, 64), (59, 66, 82), (67, 76, 94), (76, 86, 106), (216, 222, 233), (229, 233, 240), (236, 239, 244), (143, 188, 187), (136, 192, 208), (129, 161, 193), (94, 129, 172), (191, 97, 106), (208, 135, 112), (235, 203, 139), (235, 203, 1139), (180, 142, 173)]

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, help="path to input image")
parser.add_argument('-o', '--output', required=True, help="path to output image")
args = vars(parser.parse_args())

def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in nord_colors:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

image = Image.open(args["input"])
image = image.convert('RGB')
for x in range(image.width):
    for y in range(image.height):
        image.putpixel((x,y), closest_color(image.getpixel((x, y))))

image.save(args["output"])
