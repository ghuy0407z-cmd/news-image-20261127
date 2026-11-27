"""Generate entry.png: a one-page poster summing up 27 Nov 2026 world news.

Run locally (Pillow is available on this machine; the entry program
itself, main.py, is standard-library only and just copies the image
this script produces). Deterministic: no timestamps, no random values,
no network — the same input always produces the same PNG bytes.
"""

import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

# (region tag, colour, headline, one-line fact)
STORIES = [
    ("UKRAINE", "#B91C1C",
     "Russia fires 155 drones overnight",
     "110 shot down; strikes hit 27 sites — 6 killed, 25 injured."),
    ("EUROPE", "#1D4ED8",
     "EU summit ends with no deal",
     "24 of 27 back a €45bn Ukraine loan; 2028–34 budget also unsettled."),
    ("NEW ZEALAND", "#047857",
     "Final count leaves a hung parliament",
     "Ruling bloc holds 65 of 130 seats — one short; Opportunity decides."),
    ("UNITED STATES", "#7C3AED",
     "Thanksgiving storm cuts power",
     "900,000+ homes dark; 400+ flights cut; Macy's parade postponed."),
    ("AFRICA", "#B45309",
     "Congo Ebola passes 12,000 cases",
     "12,021 infections, 5,904 deaths; fighting in Ituri disrupts aid."),
    ("DIPLOMACY", "#0E7490",
     "Trump rewrites NATO statement",
     "After meeting Rutte, he adds Ukraine to the warning on widening the war."),
]


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, font_obj, max_width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=font_obj) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_icon(draw, kind, cx, cy, colour):
    """Small geometric icon, centred on (cx, cy), inside a ~64px box."""
    if kind == 0:  # drone: body + four rotors
        draw.ellipse([cx - 12, cy - 8, cx + 12, cy + 8], fill=colour)
        for dx, dy in ((-26, -16), (26, -16), (-26, 16), (26, 16)):
            draw.line([cx, cy, cx + dx, cy + dy], fill=colour, width=3)
            draw.ellipse([cx + dx - 8, cy + dy - 3, cx + dx + 8, cy + dy + 3],
                         fill=colour)
    elif kind == 1:  # EU: ring of stars
        for i in range(12):
            import math
            angle = 2 * math.pi * i / 12 - math.pi / 2
            x = cx + 24 * math.cos(angle)
            y = cy + 24 * math.sin(angle)
            draw.ellipse([x - 4, y - 4, x + 4, y + 4], fill="#FACC15")
    elif kind == 2:  # ballot box with a tick
        draw.rectangle([cx - 24, cy - 12, cx + 24, cy + 22], outline=colour, width=4)
        draw.line([cx - 24, cy - 12, cx + 24, cy - 12], fill=colour, width=4)
        draw.line([cx - 12, cy + 4, cx - 2, cy + 14, cx + 16, cy - 10],
                  fill=colour, width=5)
    elif kind == 3:  # storm cloud + lightning
        draw.rectangle([cx - 28, cy - 4, cx + 28, cy + 12], fill=colour)
        draw.ellipse([cx - 28, cy - 14, cx + 0, cy + 12], fill=colour)
        draw.ellipse([cx - 4, cy - 20, cx + 28, cy + 10], fill=colour)
        draw.polygon([(cx + 2, cy + 8), (cx + 14, cy + 8), (cx + 4, cy + 22),
                      (cx + 12, cy + 22), (cx - 6, cy + 40), (cx - 1, cy + 24),
                      (cx - 10, cy + 24)], fill="#FACC15")
    elif kind == 4:  # virus: spiked circle
        draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=colour)
        for i in range(8):
            import math
            angle = 2 * math.pi * i / 8
            x1 = cx + 14 * math.cos(angle)
            y1 = cy + 14 * math.sin(angle)
            x2 = cx + 26 * math.cos(angle)
            y2 = cy + 26 * math.sin(angle)
            draw.line([x1, y1, x2, y2], fill=colour, width=4)
            draw.ellipse([x2 - 4, y2 - 4, x2 + 4, y2 + 4], fill=colour)
    else:  # compass star
        draw.polygon([(cx, cy - 28), (cx + 8, cy - 8), (cx + 28, cy),
                      (cx + 8, cy + 8), (cx, cy + 28), (cx - 8, cy + 8),
                      (cx - 28, cy), (cx - 8, cy - 8)], fill=colour)


def main():
    image = Image.new("RGB", (WIDTH, HEIGHT), "#F7F5F0")
    draw = ImageDraw.Draw(image)

    # Header band
    draw.rectangle([0, 0, WIDTH, 196], fill="#0F2A4A")
    draw.rectangle([0, 196, WIDTH, 202], fill="#FACC15")
    kicker = font("DejaVuSans-Bold.ttf", 22)
    title = font("DejaVuSans-Bold.ttf", 66)
    subtitle = font("DejaVuSans.ttf", 26)
    draw.text((28, 26), "FRIDAY  •  THE WORLD IN ONE IMAGE", font=kicker,
              fill="#FACC15")
    draw.text((28, 58), "27 NOVEMBER 2026", font=title, fill="white")
    draw.text((28, 140), "Six stories that defined the day", font=subtitle,
              fill="#D7DEE8")

    # Story cards: 2 columns x 3 rows
    tag_font = font("DejaVuSans-Bold.ttf", 19)
    head_font = font("DejaVuSans-Bold.ttf", 30)
    fact_font = font("DejaVuSans.ttf", 21)
    margin, gap = 28, 18
    card_w = (WIDTH - 2 * margin - gap) // 2
    card_h = 232
    top = 222
    for index, (tag, colour, headline, fact) in enumerate(STORIES):
        row, col = divmod(index, 2)
        x0 = margin + col * (card_w + gap)
        y0 = top + row * (card_h + gap)
        x1, y1 = x0 + card_w, y0 + card_h
        draw.rounded_rectangle([x0, y0, x1, y1], radius=14, fill="white",
                               outline="#D9D4CC", width=2)
        draw.rounded_rectangle([x0, y0, x0 + 10, y1], radius=5, fill=colour)
        draw_icon(draw, index, x1 - 46, y1 - 48, colour)
        draw.text((x0 + 26, y0 + 20), tag, font=tag_font, fill=colour)
        lines = wrap(draw, headline, head_font, card_w - 52)
        y = y0 + 52
        for line in lines[:2]:
            draw.text((x0 + 26, y), line, font=head_font, fill="#111827")
            y += 38
        fact_lines = wrap(draw, fact, fact_font, card_w - 52)
        for line in fact_lines[:2]:
            draw.text((x0 + 26, y), line, font=fact_font, fill="#4B5563")
            y += 28

    # Footer: sources
    footer = font("DejaVuSans.ttf", 16)
    draw.text((28, 970),
              "Reported 27 Nov 2026  •  Sources: Reuters, Kyiv Independent, Al Jazeera,",
              font=footer, fill="#6B7280")
    draw.text((28, 992),
              "1News, Ukraine Air Force, Congo health ministry",
              font=footer, fill="#6B7280")

    image.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
