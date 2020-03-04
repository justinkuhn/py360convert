import ffmpeg
import math
import argparse
import sys


#argument parser
parser = argparse.ArgumentParser(description='Get Video Information')
parser.add_argument('in_filename', help='Input filename')
args = parser.parse_args()

#print('Rotate by how many degrees?')
#x = input()

#angle above horizon
phi = math.pi/6

#Get Video Info
try:
    probe = ffmpeg.probe(args.in_filename)
except ffmpeg.Error as e:
    print(e.stderr, file=sys.stderr)
    sys.exit(1)

#get stream
#stream = ffmpeg.input('trim3sec.mp4')
stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)

width = int(stream['width'])
height = int(stream['height'])

print('width, height are {}, {}'.format(width, height))

#calculate new width and height for 270 degree by 30 degree space
new_w = int(width * 3/4)

#the new height is derived by the the ratio of the new to old height which is
new_h = int(height * math.sin(phi))
margin_h = int((height-new_h)/2)

print('new dimensions are {}, {}'.format(new_w, new_h))

#crop top, bottom, and part of width
#ffmpeg.crop(stream, x, y, width, height, **kwargs)
stream = ffmpeg.input(str(args.in_filename))
stream = ffmpeg.crop(stream, 0, margin_h, new_w, new_h)
stream = ffmpeg.output(stream, 'cropped_' args.in_filename + '.mp4')
ffmpeg.run(stream)
