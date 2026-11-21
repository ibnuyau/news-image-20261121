#!/usr/bin/env python3
"""Draw the 21 Nov 2026 world-news front page, 1024x1024 PNG.
One image, 17 stories, each with a small hand-drawn pictogram.
All stories verified against news reports first published 21 Nov 2026."""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
NAVY = (26, 47, 74)
RED = (176, 42, 32)
GREY = (90, 90, 86)
RULE = (180, 175, 165)
LEAD_BG = (232, 238, 244)
ICON_BG = (236, 233, 224)
GOLD = (255, 210, 90)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 36

def wrap(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def para(text, font, x, y, max_w, leading, color=INK):
    lines = wrap(text, font, max_w)
    for ln in lines:
        d.text((x, y), ln, font=font, fill=color)
        y += leading
    return y, len(lines)

def hline(y, color=RULE, width=2):
    d.line([(M, y), (W - M, y)], fill=color, width=width)

# ---------- pictograms (each drawn in a 36x36 box at ox, oy) ----------
def icon_bg(ox, oy):
    d.rounded_rectangle([ox, oy, ox + 36, oy + 36], radius=6,
                        fill=ICON_BG)

def ico_missile(ox, oy):
    icon_bg(ox, oy)
    d.polygon([(ox + 18, oy + 4), (ox + 23, oy + 14), (ox + 18, oy + 24),
               (ox + 13, oy + 14)], fill=(120, 120, 120))
    d.polygon([(ox + 13, oy + 16), (ox + 8, oy + 24), (ox + 13, oy + 22)],
              fill=(90, 90, 90))
    d.polygon([(ox + 23, oy + 16), (ox + 28, oy + 24), (ox + 23, oy + 22)],
              fill=(90, 90, 90))
    d.polygon([(ox + 18, oy + 24), (ox + 21, oy + 31), (ox + 15, oy + 31)],
              fill=(230, 120, 30))
    d.line([(ox + 6, oy + 8), (ox + 10, oy + 12)], fill=RED, width=2)
    d.line([(ox + 30, oy + 8), (ox + 26, oy + 12)], fill=RED, width=2)

def ico_quake_sea(ox, oy):
    icon_bg(ox, oy)
    d.polygon([(ox + 4, oy + 5), (ox + 12, oy + 12), (ox + 20, oy + 5),
               (ox + 28, oy + 12), (ox + 32, oy + 9), (ox + 32, oy + 17),
               (ox + 4, oy + 17)], fill=(150, 110, 70))
    d.arc([ox + 4, oy + 19, ox + 18, oy + 29], 200, 340,
          fill=(40, 90, 160), width=3)
    d.arc([ox + 18, oy + 21, ox + 32, oy + 31], 200, 340,
          fill=(40, 90, 160), width=3)
    d.arc([ox + 8, oy + 26, ox + 22, oy + 34], 200, 340,
          fill=(40, 90, 160), width=2)

def ico_quake_mtn(ox, oy):
    icon_bg(ox, oy)
    d.polygon([(ox + 4, oy + 30), (ox + 18, oy + 8), (ox + 32, oy + 30)],
              fill=(110, 85, 60))
    d.polygon([(ox + 18, oy + 8), (ox + 22, oy + 14), (ox + 14, oy + 14)],
              fill=(255, 255, 255))
    d.line([(ox + 18, oy + 12), (ox + 15, oy + 20), (ox + 20, oy + 26)],
           fill=(60, 40, 20), width=2)

def ico_stocks(ox, oy):
    icon_bg(ox, oy)
    d.rectangle([ox + 7, oy + 8, ox + 12, oy + 20], fill=RED)
    d.rectangle([ox + 15, oy + 13, ox + 20, oy + 24], fill=RED)
    d.rectangle([ox + 23, oy + 18, ox + 28, oy + 28], fill=RED)
    d.line([(ox + 5, oy + 6), (ox + 31, oy + 30)], fill=(140, 20, 10),
           width=3)
    d.polygon([(ox + 31, oy + 30), (ox + 24, oy + 28), (ox + 29, oy + 23)],
              fill=(140, 20, 10))

def ico_globe(ox, oy):
    icon_bg(ox, oy)
    d.ellipse([ox + 6, oy + 8, ox + 30, oy + 32], outline=(40, 90, 160),
              width=2)
    d.ellipse([ox + 12, oy + 12, ox + 20, oy + 19], fill=(60, 140, 70))
    d.ellipse([ox + 21, oy + 21, ox + 27, oy + 27], fill=(60, 140, 70))
    d.arc([ox + 13, oy + 8, ox + 23, oy + 32], 270, 90,
          fill=(40, 90, 160), width=1)
    d.line([(ox + 18, oy + 8), (ox + 18, oy + 32)], fill=(40, 90, 160),
           width=1)

def ico_shield(ox, oy):
    icon_bg(ox, oy)
    d.polygon([(ox + 18, oy + 5), (ox + 30, oy + 9), (ox + 30, oy + 19),
               (ox + 18, oy + 31), (ox + 6, oy + 19), (ox + 6, oy + 9)],
              fill=NAVY)
    d.rectangle([ox + 16, oy + 11, ox + 20, oy + 21], fill=GOLD)
    d.ellipse([ox + 16, oy + 23, ox + 20, oy + 27], fill=GOLD)

def ico_stars(ox, oy):
    icon_bg(ox, oy)
    d.ellipse([ox + 5, oy + 5, ox + 31, oy + 31], fill=(30, 60, 140))
    for k in range(8):
        a = k * math.pi / 4
        sx = ox + 18 + int(9 * math.cos(a))
        sy = oy + 18 + int(9 * math.sin(a))
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 210, 60))
    d.line([(ox + 8, oy + 28), (ox + 28, oy + 8)], fill=RED, width=3)

def ico_flags(ox, oy):
    icon_bg(ox, oy)
    d.rectangle([ox + 4, oy + 8, ox + 17, oy + 20], fill=(30, 60, 140))
    d.line([(ox + 10, oy + 8), (ox + 10, oy + 20)], fill=(255, 255, 255),
           width=2)
    d.line([(ox + 4, oy + 14), (ox + 17, oy + 14)], fill=(255, 255, 255),
           width=2)
    d.line([(ox + 10, oy + 8), (ox + 10, oy + 20)], fill=RED, width=1)
    d.line([(ox + 4, oy + 14), (ox + 17, oy + 14)], fill=RED, width=1)
    d.rectangle([ox + 19, oy + 8, ox + 32, oy + 20], fill=(30, 60, 140))
    for k in range(5):
        a = k * 2 * math.pi / 5 - math.pi / 2
        sx = ox + 25 + int(4 * math.cos(a))
        sy = oy + 14 + int(4 * math.sin(a))
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 210, 60))
    d.rectangle([ox + 4, oy + 24, ox + 32, oy + 28], fill=(200, 200, 190))

def ico_storm(ox, oy):
    icon_bg(ox, oy)
    d.ellipse([ox + 5, oy + 8, ox + 17, oy + 18], fill=(120, 120, 120))
    d.ellipse([ox + 13, oy + 5, ox + 25, oy + 16], fill=(140, 140, 140))
    d.ellipse([ox + 21, oy + 9, ox + 31, oy + 19], fill=(120, 120, 120))
    d.rectangle([ox + 5, oy + 16, ox + 31, oy + 20], fill=(130, 130, 130))
    d.polygon([(ox + 17, oy + 20), (ox + 12, oy + 28), (ox + 16, oy + 28),
               (ox + 13, oy + 33), (ox + 21, oy + 24), (ox + 17, oy + 24)],
              fill=(255, 200, 40))
    d.line([(ox + 9, oy + 24), (ox + 9, oy + 30)], fill=(40, 90, 160),
           width=2)
    d.line([(ox + 26, oy + 24), (ox + 26, oy + 30)], fill=(40, 90, 160),
           width=2)

def ico_pill(ox, oy):
    icon_bg(ox, oy)
    d.rounded_rectangle([ox + 5, oy + 12, ox + 31, oy + 24], radius=6,
                        outline=(40, 40, 40), width=2, fill=(255, 255, 255))
    d.rounded_rectangle([ox + 18, oy + 12, ox + 31, oy + 24], radius=6,
                        fill=(30, 130, 70))
    d.rounded_rectangle([ox + 5, oy + 12, ox + 18, oy + 24], radius=6,
                        fill=(255, 255, 255))
    d.text((ox + 18, oy + 28), "$", font=F(SANS_B, 11), fill=(30, 130, 70))

def ico_chip(ox, oy):
    icon_bg(ox, oy)
    d.rectangle([ox + 10, oy + 10, ox + 26, oy + 26], fill=(60, 140, 60))
    d.rectangle([ox + 15, oy + 15, ox + 21, oy + 21], fill=(30, 90, 30))
    for p in (12, 18, 24):
        d.line([(ox + p, oy + 6), (ox + p, oy + 10)], fill=(80, 80, 80),
               width=2)
        d.line([(ox + p, oy + 26), (ox + p, oy + 30)], fill=(80, 80, 80),
               width=2)
    d.ellipse([ox + 20, oy + 20, ox + 33, oy + 33], outline=NAVY, width=2)
    d.line([(ox + 30, oy + 30), (ox + 34, oy + 34)], fill=NAVY, width=2)

def ico_megaphone(ox, oy):
    icon_bg(ox, oy)
    d.polygon([(ox + 6, oy + 15), (ox + 24, oy + 7), (ox + 24, oy + 25),
               (ox + 6, oy + 21)], fill=RED)
    d.rectangle([ox + 4, oy + 14, ox + 8, oy + 22], fill=(140, 20, 10))
    d.rectangle([ox + 12, oy + 22, ox + 17, oy + 29], fill=(140, 20, 10))
    d.arc([ox + 25, oy + 10, ox + 32, oy + 26], 300, 60, fill=NAVY,
          width=2)
    d.arc([ox + 28, oy + 7, ox + 35, oy + 29], 300, 60, fill=NAVY, width=2)

def ico_ballot(ox, oy):
    icon_bg(ox, oy)
    d.rectangle([ox + 8, oy + 16, ox + 28, oy + 31], fill=(40, 90, 160))
    d.rectangle([ox + 8, oy + 27, ox + 28, oy + 31], fill=(200, 40, 40))
    d.rectangle([ox + 14, oy + 6, ox + 22, oy + 18], fill=(255, 255, 255),
                outline=(40, 40, 40))
    d.line([(ox + 16, oy + 9), (ox + 20, oy + 9)], fill=GREY, width=1)
    d.line([(ox + 16, oy + 12), (ox + 20, oy + 12)], fill=GREY, width=1)
    d.line([(ox + 12, oy + 16), (ox + 24, oy + 16)], fill=(20, 20, 20),
           width=2)

# ---------- Masthead ----------
y = 14
d.text((W // 2, y), "THE WORLD IN ONE DAY", font=F(SANS_B, 16),
       fill=GREY, anchor="ma")
y += 24
d.text((W // 2, y), "WORLD NEWS", font=F(SERIF, 76), fill=INK, anchor="ma")
y += 86
d.line([(M, y), (W - M, y)], fill=INK, width=4)
y += 10
d.text((W // 2, y), "SATURDAY  21  NOVEMBER  2026", font=F(SANS_B, 24),
       fill=RED, anchor="ma")
y += 34
d.line([(M, y), (W - M, y)], fill=INK, width=4)

# ---------- Lead story ----------
lead_y = y + 12
d.rectangle([M, lead_y, W - M, lead_y + 134], fill=LEAD_BG, outline=NAVY,
            width=2)
lx, ly = M + 20, lead_y + 10
d.text((lx, ly), "1  •  LEAD STORY — POLAND / GEOPOLITICS",
       font=F(SANS_B, 15), fill=NAVY)
ly += 24
ly, _ = para("Russian missiles land in Poland", F(SERIF, 30), lx, ly,
             700, 34)
ly += 2
para("Two missiles and a suspected drone came down in Poland during a "
     "huge Russian attack on Ukraine. PM Tusk called it a deliberate "
     "provocation; NATO condemned the strike.",
     F(SANS, 16), lx, ly, 700, 21, color=(40, 40, 40))
# lead pictogram: Polish flag + missile + burst
ix = W - M - 132
d.rectangle([ix, lead_y + 16, ix + 58, lead_y + 38], fill=(255, 255, 255),
            outline=(120, 120, 120))
d.rectangle([ix, lead_y + 27, ix + 58, lead_y + 38], fill=(220, 40, 50))
d.polygon([(ix + 78, lead_y + 14), (ix + 88, lead_y + 34),
           (ix + 78, lead_y + 62), (ix + 68, lead_y + 34)],
          fill=(120, 120, 120))
d.polygon([(ix + 68, lead_y + 38), (ix + 58, lead_y + 56),
           (ix + 68, lead_y + 52)], fill=(90, 90, 90))
d.polygon([(ix + 88, lead_y + 38), (ix + 98, lead_y + 56),
           (ix + 88, lead_y + 52)], fill=(90, 90, 90))
d.polygon([(ix + 78, lead_y + 62), (ix + 84, lead_y + 80),
           (ix + 72, lead_y + 80)], fill=(230, 120, 30))
d.line([(ix + 100, lead_y + 16), (ix + 108, lead_y + 24)], fill=RED,
       width=3)
d.line([(ix + 100, lead_y + 40), (ix + 108, lead_y + 32)], fill=RED,
       width=3)
d.line([(ix + 104, lead_y + 28), (ix + 112, lead_y + 28)], fill=RED,
       width=3)
d.text((ix, lead_y + 104), "WARSAW", font=F(SANS_B, 13), fill=GREY)

y = lead_y + 134 + 10
hline(y, color=INK, width=2)
y += 12

# ---------- Grid: 2 columns x 6 rows ----------
cards = [
    ("2", "BANDA SEA — DISASTER", RED, ico_quake_sea,
     "M6.8 quake hits Banda Sea",
     "A magnitude 6.8 earthquake struck north-east of Dili at 09:42 UTC. "
     "No tsunami threat was issued."),
    ("3", "PERU — DISASTER", RED, ico_quake_mtn,
     "M6.7 quake shakes Peru",
     "A magnitude 6.7 earthquake struck the Andes at 00:09 UTC; lawmakers "
     "evacuated the Congress building."),
    ("4", "MARKETS — ECONOMY", NAVY, ico_stocks,
     "AI rout drags S&P into correction",
     "US stocks fell 3.7% as an AI sell-off hit chipmakers; the Nasdaq "
     "erased its 2026 gains."),
    ("5", "ANTALYA — CLIMATE", NAVY, ico_globe,
     "COP31 talks run past deadline",
     "The UN climate summit in Turkey ran into overtime as nearly 200 "
     "nations deadlocked over fossil fuels."),
    ("6", "WASHINGTON — CYBER", NAVY, ico_shield,
     "FBI and USDA hit by hackers",
     "The FBI and the US Agriculture Department were hacked as computer "
     "outages hit strategic US sectors."),
    ("7", "WASHINGTON — POLITICS", NAVY, ico_stars,
     "Trump tells Europe: defund Ukraine",
     "After his summit with Putin, President Trump told European leaders "
     "to withhold funding from Ukraine."),
    ("8", "BRUSSELS — POLITICS", NAVY, ico_flags,
     "UK and EU sign post-Brexit deals",
     "PM Andy Burnham and EU leaders signed three deals on food exports, "
     "carbon markets and youth mobility."),
    ("9", "BRAZIL — DISASTER", RED, ico_storm,
     "Storm kills 3, wrecks 5,000 homes",
     "A severe storm ravaged southern Brazil, killing three people and "
     "destroying about 5,000 homes."),
    ("10", "LEVERKUSEN — ECONOMY", NAVY, ico_pill,
     "Bayer pays $7.25bn over Roundup",
     "A US judge approved Bayer's $7.25 billion deal to settle all "
     "complaints linked to weedkiller Roundup."),
    ("11", "SILICON VALLEY — TECH", NAVY, ico_chip,
     "SEC opens probe into Nvidia",
     "The SEC opened an accounting probe into Nvidia as Trump urged a "
     "second chance for ex-CEO Jensen Huang."),
    ("12", "EUROPE — SOCIETY", NAVY, ico_megaphone,
     "Gen Z protests spread in 25 nations",
     "Youth-led protests spread across 25 European countries, the largest "
     "wave of Gen Z unrest yet."),
    ("13", "MADRID — POLITICS", NAVY, ico_ballot,
     "Spain heads to 29 Nov election",
     "Spain heads to a 29 November election as conservatives gain ground "
     "in the polls."),
]
col_w = (W - 2 * M - 20) // 2
row_h = 94
gap = 6
warn = []
for i, (num, kick, kc, ico, head, summ) in enumerate(cards):
    cx = M + (i % 2) * (col_w + 20)
    cy = y + (i // 2) * (row_h + gap)
    d.rectangle([cx, cy, cx + col_w, cy + row_h], outline=RULE, width=2)
    ico(cx + 12, cy + 12)
    tx = cx + 58
    tw = col_w - 58 - 12
    d.text((tx, cy + 9), f"{num}  •  {kick}", font=F(SANS_B, 11), fill=kc)
    _, hl = para(head, F(SERIF, 19), tx, cy + 27, tw, 22)
    if hl > 1:
        warn.append(f"headline wraps: {head!r}")
    _, sl = para(summ, F(SANS, 13), tx, cy + 27 + hl * 22 + 2, tw, 16,
                 color=(40, 40, 40))
    if sl > 2:
        warn.append(f"summary wraps to {sl}: {summ!r}")

y = y + 6 * row_h + 5 * gap + 8

# ---------- Also-today strip ----------
d.rectangle([M, y, W - M, y + 84], fill=NAVY)
fy = y + 9
d.text((M + 16, fy), "ALSO TODAY", font=F(SANS_B, 13), fill=GOLD)
fy += 19
fy, _ = para("Anthropic mathematician claims an AI proof of the Riemann "
             "hypothesis  •  Indonesia hit by massive forest fires  •  "
             "Basra power plant fire kills at least four  •  Morocco and "
             "Mali win big at the U-17 World Cup",
             F(SANS, 14), M + 16, fy, W - 2 * M - 32, 18,
             color=(255, 255, 255))
fy += 3
d.text((M + 16, fy),
       "Every story above was first reported on Saturday 21 November 2026.",
       font=F(SERIF_R, 13), fill=(200, 210, 225))

out = "/home/hatch/workspace/makefun/news-image-20261121/entry.png"
img.save(out, optimize=True)
import os
print("saved", out, os.path.getsize(out), "bytes")
for w in warn:
    print("WARN:", w)
print("done")
