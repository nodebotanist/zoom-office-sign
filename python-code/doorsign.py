#!/usr/bin/env python3

from inky.inky_uc8159 import Inky
from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold

inky = Inky()

img = Image.new("P", (inky.width, inky.height))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(SourceSerifProSemibold, 12)

draw.multiline_text((0, 0), "Hello World!", fill=inky.WHITE, font=font, align="left")

inky.set_image(img)
inky.show()