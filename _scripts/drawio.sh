#!/bin/bash

# Converts all .drawio files in the workspace to .svg using drawio CLI

find . -type f -name "*.drawio" | while read -r file; do
    svg_file="${file%.drawio}.svg"
    drawio --export --format svg --output "$svg_file" "$file" --scale 1.2
    echo "Converted $file to $svg_file"
done
