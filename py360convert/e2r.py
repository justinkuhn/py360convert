import numpy as np
import math
from . import utils


def e2r(e_img, face_w=256, theta=math.pi/4, mode='bilinear'):
    '''
    e_img:  ndarray in shape of [H, W, *]
    face_w: int, the length of each face of the cubemap
    '''
    
    new_z = 0.5 * math.sqrt(2) * math.cos(theta)
    face_h = int(math.tan(theta) * face_w)
    
    assert len(e_img.shape) == 3
    h, w = e_img.shape[:2]
    if mode == 'bilinear':
        order = 1
    elif mode == 'nearest':
        order = 0
    else:
        raise NotImplementedError('unknown mode')

    xyz = utils.xyz_rectsides(face_w, face_h, new_z)
    uv = utils.xyz2uv(xyz)
    coor_xy = utils.uv2coor(uv, h, w)

    cubemap = np.stack([
        utils.sample_equirec(e_img[..., i], coor_xy, order=order)
        for i in range(e_img.shape[2])
    ], axis=-1)

    cubemap = utils.cube_h2NCSU(cubemap)

    return cubemap

