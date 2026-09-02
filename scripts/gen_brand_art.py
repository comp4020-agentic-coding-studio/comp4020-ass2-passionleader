"""One-off generator for the course's flat two-ink artwork. Not part of the
build; run manually to (re)produce src/assets/images/card.png and hero-home.png."""

import math
from PIL import Image, ImageDraw, ImageFont

CREAM = (242, 232, 213)
GOLD = (185, 125, 28)
INK = (26, 26, 26)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def prohibited(draw, cx, cy, r, width, color):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=width)
    ang = math.radians(45)
    dx, dy = r * math.cos(ang), r * math.sin(ang)
    draw.line([cx - dx, cy + dy, cx + dx, cy - dy], fill=color, width=width)


def sneeze_burst(draw, cx, cy, color, scale=1.0):
    # a flat "head" (circle) with a burst of droplet arcs, no facial detail
    head_r = 46 * scale
    draw.ellipse([cx - head_r, cy - head_r, cx + head_r, cy + head_r], fill=color)
    for i, ang in enumerate(range(-40, 45, 20)):
        rad = math.radians(ang)
        length = (70 + (i % 3) * 22) * scale
        x0 = cx + head_r * 0.9 * math.cos(rad)
        y0 = cy + head_r * 0.9 * math.sin(rad)
        x1 = cx + length * math.cos(rad)
        y1 = cy + length * math.sin(rad)
        draw.line([x0, y0, x1, y1], fill=color, width=int(9 * scale))
        draw.ellipse(
            [x1 - 7 * scale, y1 - 7 * scale, x1 + 7 * scale, y1 + 7 * scale], fill=color
        )


def make_card():
    w, h = 1200, 630
    im = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(im)

    d.rectangle([0, 0, w - 1, h - 1], outline=INK, width=10)

    sneeze_burst(d, 250, 300, INK, scale=1.5)
    prohibited(d, 250, 300, 165, 16, GOLD)

    title_font = ImageFont.truetype(SERIF_BOLD, 74)
    sub_font = ImageFont.truetype(SANS, 32)
    code_font = ImageFont.truetype(SANS, 30)

    d.text((470, 190), "Weaponised", font=title_font, fill=INK)
    d.text((470, 270), "Etiquette", font=title_font, fill=INK)
    d.text((470, 360), "a field course in public nuisance", font=sub_font, fill=GOLD)
    d.text((470, 410), "SLOP2950 · Slop University", font=code_font, fill=INK)

    im.save("src/assets/images/card.png")


def make_hero():
    w, h = 1600, 900
    im = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(im)

    # lecture-theatre seating, raked toward a vanishing point above the frame,
    # each row wider and lower than the one behind it
    rows = 9
    vx, vy = w / 2, -260
    offender_row, offender_col = 6, 6
    ox = oy = None
    for row in range(rows):
        t = row / (rows - 1)
        y = vy + (h - 40 - vy) * (t**1.15)
        seats = 6 + row
        span = 160 + 1500 * (t**1.05)
        x0 = w / 2 - span / 2
        r = 10 + 24 * t
        for i in range(seats):
            x = x0 + span * (i + 0.5) / seats
            if row == offender_row and i == offender_col:
                ox, oy = x, y
                continue
            d.ellipse([x - r, y - r, x + r, y + r], fill=GOLD)

    # the offending attendee, mid-sneeze, breaking the pattern in ink
    sneeze_burst(d, ox, oy, INK, scale=0.95)

    # a prohibited ring drawn tight around that one seat
    prohibited(d, ox, oy, 105, 14, INK)

    im.save("src/assets/images/hero-home.png")


if __name__ == "__main__":
    make_card()
    make_hero()
    print("wrote card.png and hero-home.png")
