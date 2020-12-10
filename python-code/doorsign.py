#!/usr/bin/env python3

from inky.inky_uc8159 import Inky
from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold

inky = Inky()

for y in range(inky.height - 1):
    color = y // (inky.height // 7)
    for x in range(inky.width - 1):
        inky.set_pixel(x, y, color)

# Create a new canvas to draw on

img = Image.new("P", (inky.width, inky.height))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(SourceSerifProSemibold, font_size)

draw.multiline_text((0, 0), "Hello World!", fill=inky_display.WHITE, font=font, align="left")

inky.show()
