#!/usr/bin/env python3

import os
from PIL import Image


# Paths.
BUILD_PATH = "./build"
OUTPUT_PATH = "../../assets/images/powered-up/status-light/"
os.makedirs(BUILD_PATH, exist_ok=True)

# This placeholder color will be replaced by the frame color.
BASE_COLOR = "#123456"
base_svg_blob = open("light_technichub_base.svg").read()

# Color tags used in the bootloader and Pybricks firmware. Colors may
# adjusted for better visual appearence.
COLORS = {
    "bootloader_red": "#ff0000",
    "bootloader_green": "#09cf00",
    "bootloader_blue": "#0084ff",
    "bootloader_purple": "#ff00ea",
    "pybricks_ui_blue": "#0084ff",
    "pybricks_ui_orange": "#ff6100",
    "off": "#c5c5c5"
}


def render_light_frame(color_name):
    """# Build an svg and render a png for the requested color."""

    try:
        hex_color = COLORS[color_name]
    except KeyError:
        hex_color = color_name
        color_name = color_name[1:]

    # Write the svg file by replacing the base color.
    base_name = os.path.join(BUILD_PATH, "light_technichub_" + color_name)
    with open(base_name + '.svg', "w") as svg_file:
        svg_file.write(base_svg_blob.replace(BASE_COLOR, hex_color))

    # Render the png.
    command = "inkscape --file={0}.svg --export-png={0}.png".format(base_name)
    print(command)
    os.system(command)

    return Image.open(base_name + ".png")


# Assemble all gifs.
for file_name in os.listdir("."):
    base_name, ext = os.path.splitext(file_name)

    # Skip non-text files.
    if ext != ".txt":
        continue

    # Parse file for colors and durations.
    with open(file_name) as text_file:
        images = []
        durations = []
        for line in text_file.readlines():
            color, time = line.strip().split(" ")
            images.append(render_light_frame(color))
            durations.append(int(time))

    # Build the gif.
    first, *rest = images
    gif_path = os.path.join(OUTPUT_PATH, base_name + ".png")
    first.save(fp=gif_path, format="png", append_images=rest, save_all=True, duration=durations, loop=0)
