#!/usr/bin/env python3

import argparse
from inky.inky_uc8159 import Inky
from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold

parser = argparse.ArgumentParser()
parser.add_argument("status", help="Status of the user ['available', 'dnd', 'streaming'")
args = parser.parse_args()
print(args.status)

inky = Inky()

img = Image.new("P", (inky.width, inky.height))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(SourceSerifProSemibold, 12)

draw.rectangle([0,0,inky.width,inky.height], fill=inky.RED)

draw.multiline_text((0, 0), "Hello World!", fill=inky.WHITE, font=font, align="left")

inky.set_image(img)
inky.show()