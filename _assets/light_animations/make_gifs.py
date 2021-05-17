#!/usr/bin/env python3

import os
from PIL import Image

OUTPUT_PATH = '../../assets/images/powered-up/status-light/'

# Render all svg files as png.
for file_name in os.listdir('.'):
    base_name, ext = os.path.splitext(file_name)

    if ext == '.svg':
        command = "inkscape --file={0}.svg --export-png={0}.png".format(base_name)
        print(command)
        os.system(command)

# Assemble all gifs.
for file_name in os.listdir('.'):
    base_name, ext = os.path.splitext(file_name)

    # Get images from text file.
    if ext == '.txt':
        with open(file_name) as text_file:
            images = []
            durations = []
            for line in text_file.readlines():
                frame, time = line.strip().split(' ')
                images.append(Image.open(frame + '.png'))
                durations.append(int(time))

        # Build the gif.
        first, *rest = images
        gif_path = os.path.join(OUTPUT_PATH, base_name + '.gif')
        first.save(fp=gif_path, format='GIF', append_images=rest, save_all=True, duration=durations, loop=0)
