#!/usr/bin/env python3

import math
import colorsys

BASE_HUE = 208
DURATION = 40

with open("program-running.txt", "w") as text_file:

    # Intensities from pbsys
    for i in list(range(0, 100, 4)) + list(range(100, 0, -4)):

        # Normalized hue
        h = BASE_HUE / 360

        # Value increments from 0.77 (gray/off) to 1
        v = 0.77 + (i / 100) * 0.23

        # Saturation goes from gray to blue
        s = (i / 100)

        # Print as hex RGB string
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        color = "#{0:02x}{1:02x}{2:02x}".format(*[round(c * 255) for c in (r, g, b)])
        text_file.write("{} 40\n".format(color))

