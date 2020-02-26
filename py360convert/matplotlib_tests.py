import matplotlib.pyplot as plt
import numpy as np
import math

n = 4
phi = math.pi/4
theta = math.pi / n
w = 256
h = int(math.tan(phi) * w)
z = 1

def rotate_points(points, theta):
    rot = 1 * theta
    rot_mat = np.array([[math.cos(rot),-math.sin(rot)],[math.sin(rot),math.cos(rot)]])
    
    for num,x in enumerate(points):
        points[num] = rot_mat.dot(x)
    
    return points

# Prepare the data
p = 2*z*math.tan(theta)
q = 2*z*math.tan(phi)
rect_w = np.linspace(-p/2,p/2,num=w, dtype=np.float32)
rect_h = np.linspace(-q/2,q/2,num=h, dtype=np.float32)
out = np.zeros((h, w*n, 3), np.float32)

for a in range(n):
    angle = theta * a
    
    # take each rect and rotate it (just the p's) around the z axis by increments of theta
    # top view x,y
    coord = np.array([np.ones(w)*z,rect_w]).T 
    
    #calculate rect_w  and z for a given side
    new_coord = rotate_points(coord,angle)
    
    #pull the x value of each coord
    depth = new_coord[:,0]

    #calculate full_rect for that side
    full_rect = np.stack(np.meshgrid(new_coord[:,1], -rect_h),axis=-1)
    
    #plot 3d coordinates for a side (y,z,x)
    # dimensions are [h,w,coords]
    out[:, a*w:(a+1)*w, [0, 1]] = full_rect
    out[:, a*w:(a+1)*w, 2] = depth

print(out.shape)