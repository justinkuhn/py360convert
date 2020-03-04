import ffmpeg

print('How long in seconds?')
x = input()

stream = ffmpeg.input('input.mp4')
stream = ffmpeg.trim(stream,duration=x)
stream = ffmpeg.output(stream, 'trim' + x + 'sec.mp4')
ffmpeg.run(stream)
