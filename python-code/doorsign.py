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

font = ImageFont.truetype(SourceSerifProSemibold, 36)

bg_color = inky.GREEN
status_text = "Kassian is Available."

if args.status == "dnd":
    bg_color = inky.RED
    status_text = "Kassian is Busy."
elif args.status == "streaming":
    bg_color = inky.BLUE
    status_text = "Kassian is Streaming."

draw.rectangle([0,0,inky.width,inky.height], fill=bg_color)
draw.rectangle([50,50,inky.width-50,inky.height-50], fill=inky.WHITE)

textLength, textHeight = font.getsize(status_text)
print(textLength)

draw.multiline_text((75, inky.height/2), status_text, fill=inky.BLACK, font=font, align="center")

inky.set_image(img)
inky.show()