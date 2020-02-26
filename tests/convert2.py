import py360convert
import math
import numpy as np
from PIL import Image

#input image
x = np.array(Image.open('x.png'))

fov = []
#Field of View, h and w, in degrees


#horizontal viewing angle in radians
u = 0

#vertical viewing angle in degrees
v = 0

#output image in pixels (height, width)
face_w = 1000

#angle from the horizon

for phi in np.arange(0.5, 1.5, 0.2):
    y = py360convert.e2n(x, face_w, phi,sides=3)
    im = Image.fromarray(np.uint8((y)))
    im.save('img' + str(phi) + '.png', 'PNG')