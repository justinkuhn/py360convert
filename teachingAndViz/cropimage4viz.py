from PIL import Image
import argparse
import os
import math

#argument parser
parser = argparse.ArgumentParser(description='Get Image Information')
parser.add_argument('in_filename', help='Input filename')
args = parser.parse_args()

im = Image.open(str(os.getcwd() + "\\" + args.in_filename))

width, height = im.size 

print('width, height are {}, {}'.format(width, height))

#angle from horizon to top of screen
phi = math.pi/6

#calculate new width and height for 270 degree by 30 degree space
new_w = int(width * 3/4)

#the new height is derived by the the ratio of the new to old height which is
new_h = int(height * math.sin(phi))
margin_h = int((height-new_h)/2)

print('new dimensions are {}, {}'.format(new_w, new_h))

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((0, margin_h, new_w, new_h+margin_h)) 

im1.save("cropped_" + args.in_filename + ".png")
