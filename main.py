#!/usr/bin/env python3
"""Global Edition — world news poster for Tuesday 24 November 2026.
Fresh generator written 24 Nov 2026 for the news-image-20261124 edition.
Deterministic: fixed data, fixed fonts, no timestamps, no randomness.
Renders entry.png at exactly 1024x1024.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 32, 46)
NAVY = (14, 42, 71)
NAVY2 = (23, 64, 105)
GOLD = (201, 162, 39)
GOLD_LT = (232, 203, 110)
RED = (178, 44, 36)
TEAL = (15, 118, 110)
MUTED = (96, 104, 112)
CARD = (255, 255, 255)
LINE = (203, 196, 180)

FDIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(FDIR, name), size)

F_TITLE = font("DejaVuSerif-Bold.ttf", 30)
F_SUB = font("DejaVuSans-Bold.ttf", 12)
F_DATE = font("DejaVuSans-Bold.ttf", 13)
F_SEC = font("DejaVuSans-Bold.ttf", 11)
F_STORY = font("DejaVuSans.ttf", 10)
F_SRC = font("DejaVuSans-Bold.ttf", 8)
F_SMALL = font("DejaVuSans.ttf", 8)
F_TINY = font("DejaVuSans.ttf", 8)
F_NUM = font("DejaVuSans-Bold.ttf", 15)
F_BIG = font("DejaVuSans-Bold.ttf", 22)
F_PANEL = font("DejaVuSans-Bold.ttf", 8)
F_PC = font("DejaVuSans.ttf", 8)

# (number, region, headline, source, pin?)
REGIONS = [
    ("NORTH AMERICA", (178, 44, 36)),
    ("LATIN AMERICA & CARIBBEAN", (186, 104, 12)),
    ("EUROPE", (23, 64, 105)),
    ("MIDDLE EAST & N. AFRICA", (122, 63, 23)),
    ("SUB-SAHARAN AFRICA", (15, 118, 110)),
    ("ASIA-PACIFIC", (90, 48, 130)),
    ("GLOBAL: MARKETS, CULTURE & SPORT", (70, 70, 70)),
]

STORIES = [
    (1, 0, "Nvidia reinstates Jensen Huang as CEO after 11 days out", "REUTERS", True),
    (2, 0, "Trump and Vance personally pressed Nvidia board on Huang", "REUTERS", False),
    (3, 0, "Wall St soars: Nasdaq +6%, S&P +5%, Nvidia +31% in a day", "REUTERS", False),
    (4, 0, "Democrats clinch House: 258 seats, biggest majority since 1992", "AP", True),
    (5, 0, "Trump: Army must not detonate Iowa chemicals sans court OK", "AP", False),
    (6, 0, "States sue Musk firms over sexualised images from Grok AI", "AP", False),
    (7, 0, "Princeton neuroscientist from China held by ICE at airport", "AP", False),
    (8, 0, "Delta glitch delays flights as Thanksgiving travel peaks", "AP", False),
    (9, 0, "Democrats plan 12 debates for 2028 primary, first in June", "AP", False),
    (10, 1, "Cartel boss 'Chapo Isidro' captured; 11 die in Sinaloa clash", "AP", False),
    (11, 1, "Ecuador gang chief expelled by Spain, held in pretrial jail", "RIO TIMES", False),
    (12, 1, "Brazil economists lift 2027 Selic rate forecast to 13.00%", "RIO TIMES", False),
    (13, 1, "Ex-president Bolsonaro hospitalised with severe stomach pain", "RADIO GEN", False),
    (14, 1, "Uruguay unions lose pension board seat in 454,917-372,936 vote", "RIO TIMES", False),
    (15, 1, "Peru quake damages 170 homes in preliminary count", "APPISTOS", False),
    (16, 1, "Guatemala arrests wanted Mexican; US seeks extradition", "APPISTOS", False),
    (17, 2, "COP31 collapses: EU and allies reject Antalya Pact draft", "REUTERS", True),
    (18, 2, "UN chief 'disappointed' as COP31 ends with no climate pact", "PANA", False),
    (19, 2, "Burnham: 'pragmatic' UK-EU reset deal struck after Brexit", "BBC", False),
    (20, 2, "UK to host 2035 Women's World Cup, FIFA confirms", "BBC", False),
    (21, 2, "NHS launches world's largest AI breast-cancer screening trial", "BBC", False),
    (22, 2, "Andrew 'received £750,000 from Turkish millionaire', court told", "BBC", False),
    (23, 2, "Capita shares plunge 70% as boss quits in pensions failure", "BBC", False),
    (24, 2, "Finland probes suspected Russian helicopter airspace breach", "APPISTOS", False),
    (25, 2, "Troops from 11 European states drill in Poland for Ukraine", "AP", False),
    (26, 3, "Ukraine drones hit Russian warship at Benghazi naval base", "AP", True),
    (27, 3, "US weighs training Syrian soldiers in demining, first since 2024", "REUTERS", False),
    (28, 3, "Oxfam: Israeli attacks turned Gaza into 'toxic wasteland'", "BBC", False),
    (29, 3, "Israeli opposition chief calls settler arson 'terrorism'", "AP", False),
    (30, 3, "Iran strikes 3 tankers and unveils underground missile base", "AP", False),
    (31, 3, "UN Libya mission condemns attacks on ships off Benghazi", "PANA", False),
    (32, 3, "Pugh swims Strait of Hormuz for wildlife hit by Iran war", "AP", False),
    (33, 3, "West Bank settler violence threatens Israel coalition talks", "REUTERS", False),
    (34, 4, "DR Congo halts cobalt exports again from 30 November", "REUTERS", True),
    (35, 4, "Fighting in Ituri traps Ebola responders, WHO warns", "PANA", False),
    (36, 4, "Kenya and DR Congo restore full diplomatic relations", "RADIO GEN", False),
    (37, 4, "At least 24 killed in South Sudan's Warrap State clashes", "RADIO GEN", False),
    (38, 4, "Boat capsizes in Nigeria's Bayelsa; 24 bodies recovered", "APPISTOS", False),
    (39, 4, "Gambia intercepts 491 would-be irregular migrants", "PANA", False),
    (40, 4, "UN: drones killed 1,600+ people in Sudan this year", "PANA", False),
    (41, 4, "Johannesburg mayor vote pushed to Friday amid coalition talks", "RIO TIMES", False),
    (42, 5, "Indonesia factory blaze kills 24; dozens still missing", "REUTERS", True),
    (43, 5, "AustralianSuper backs Brookfield's $2.53bn Reliance deal", "REUTERS", True),
    (44, 5, "India weighs rice export duties as domestic prices climb", "REUTERS", False),
    (45, 5, "China sets 2030 targets as ageing strains care services", "RADIO GEN", False),
    (46, 5, "Taiwan warns Canada's Carney over deeper China ties", "AP", False),
    (47, 5, "Okinawa celebrates Shuri Castle hall restored after 2019 fire", "AP", False),
    (48, 5, "All 146 aboard Air Niugini jet safe after emergency landing", "AP", False),
    (49, 5, "UK sanctions Myanmar generals after ICJ genocide ruling", "BBC", False),
    (50, 5, "South Korea accepts education minister's resignation", "APPISTOS", False),
    (51, 6, "CrowdStrike to buy Zscaler in $44bn all-stock cyber deal", "REUTERS", False),
    (52, 6, "Anthropic IPO values AI lab at record $1.5 trillion", "AP", False),
    (53, 6, "Miley Cyrus weds drummer Maxx Morando in California", "REUTERS", False),
    (54, 6, "Don Toliver postpones London show after Manchester evacuation", "AP", False),
    (55, 6, "Boxer Tyson Fury reveals schizophrenia diagnosis", "BBC", False),
    (56, 6, "Houston leaps to No. 1 in AP Top 25 men's basketball poll", "AP", False),
]

# (lon, lat, story no, label) for the 7 map pins
PINS = [
    (-122.0, 37.4, 1, "Nvidia HQ"),
    (-77.0, 38.9, 4, "Washington"),
    (30.7, 36.9, 17, "Antalya COP31"),
    (20.1, 32.1, 26, "Benghazi"),
    (27.5, -11.7, 34, "Lubumbashi"),
    (106.8, -6.2, 42, "Jakarta"),
    (151.2, -33.9, 43, "Sydney"),
]

# Dot-matrix land mask: row -> list of (col_start, col_end) inclusive, 64 cols x 28 rows
LAND = {
    0: [(6, 12), (40, 58)],
    1: [(4, 14), (17, 19), (38, 58)],
    2: [(4, 14), (29, 33), (36, 60)],
    3: [(4, 14), (29, 33), (36, 60)],
    4: [(5, 16), (29, 33), (36, 60)],
    5: [(5, 16), (30, 35), (36, 60)],
    6: [(5, 16), (30, 35), (38, 59)],
    7: [(7, 16), (30, 35), (38, 59)],
    8: [(7, 16), (31, 34), (38, 59)],
    9: [(7, 16), (30, 37), (40, 57)],
    10: [(9, 14), (30, 37), (40, 57)],
    11: [(9, 14), (30, 37), (42, 54)],
    12: [(12, 14), (14, 18), (31, 38), (42, 54)],
    13: [(14, 18), (31, 38), (44, 50)],
    14: [(14, 19), (31, 38), (48, 53)],
    15: [(14, 19), (31, 38)],
    16: [(14, 19), (32, 37)],
    17: [(14, 19), (32, 37)],
    18: [(15, 18), (32, 37)],
    19: [(15, 18), (33, 35), (52, 58)],
    20: [(15, 18), (33, 35), (52, 58)],
    21: [(16, 17), (52, 58)],
    22: [(16, 17), (53, 56)],
    23: [(60, 61)],
}

NUMBERS = [
    ("NVDA", "+31%", "Nvidia in one day"),
    ("NASDAQ", "+6%", "Monday's rally"),
    ("DEAL", "$44BN", "CrowdStrike buys Zscaler"),
    ("HOUSE", "258", "seats: Democrats"),
    ("BLAZE", "24", "killed in Indonesia"),
    ("SUDAN", "1,600+", "drone deaths in 2026"),
]

WEATHER = [
    ("New York", "13°C", "Mainly clear"),
    ("London", "3°C", "Clear"),
    ("Kyiv", "0°C", "Overcast"),
    ("Jakarta", "26°C", "Overcast"),
    ("Tokyo", "13°C", "Partly cloudy"),
    ("Sydney", "22°C", "Drizzle"),
    ("Mexico City", "19°C", "Partly cloudy"),
    ("São Paulo", "23°C", "Overcast"),
]

TIMELINE = [
    ("01:00", "Jakarta: 24 dead"),
    ("06:30", "COP31 fails"),
    ("10:15", "Huang returns"),
    ("13:30", "Nasdaq +6%"),
    ("16:00", "Benghazi strike"),
    ("19:45", "House: 258"),
    ("22:15", "$44bn deal"),
]

PANELS = [
    ("chip", "1  NVIDIA", "Huang back as CEO"),
    ("ballot", "4  HOUSE 258", "Democrats' biggest win"),
    ("flame", "42  FACTORY FIRE", "24 dead in Indonesia"),
    ("ship", "26  WARSHIP HIT", "Drones strike Benghazi"),
    ("globe", "17  COP31 FAILS", "No pact in Antalya"),
    ("scale", "49  ICJ AFTERMATH", "Myanmar generals hit"),
    ("coin", "51  $44BN DEAL", "CrowdStrike + Zscaler"),
    ("factory", "34  COBALT HALT", "Congo stops exports"),
    ("plane", "48  SAFE LANDING", "146 safe in Manila"),
    ("trophy", "56  HOUSTON NO.1", "AP Top 25 leaders"),
    ("music", "53  WEDDING BELLS", "Miley Cyrus weds"),
    ("bolt", "30  TANKERS HIT", "Iran shows missiles"),
    ("leaf", "18  CLIMATE VOID", "UN chief disappointed"),
    ("mask", "55  FURY OPENS UP", "Schizophrenia diagnosis"),
    ("castle", "47  SHURI REBORN", "Castle hall restored"),
    ("chart", "3  MARKETS ROAR", "Nasdaq +6% in a day"),
]


def draw_icon(d, kind, cx, cy, s, col):
    """Tiny pictograms drawn from primitives. cx,cy = centre, s = half-size."""
    if kind == "chip":
        d.rectangle([cx - s, cy - s, cx + s, cy + s], outline=col, width=2)
        d.rectangle([cx - s // 2, cy - s // 2, cx + s // 2, cy + s // 2], fill=col)
        for dx in (-1, 0, 1):
            d.line([cx + dx * s // 2, cy - s - 4, cx + dx * s // 2, cy - s], fill=col, width=2)
            d.line([cx + dx * s // 2, cy + s, cx + dx * s // 2, cy + s + 4], fill=col, width=2)
    elif kind == "ballot":
        d.rectangle([cx - s, cy - s // 2, cx + s, cy + s], outline=col, width=2)
        d.line([cx - s, cy - s // 2, cx + s, cy - s // 2], fill=col, width=2)
        d.line([cx - 4, cy + 2, cx - 1, cy + 6, cx + 6, cy - 5], fill=col, width=2)
    elif kind == "flame":
        d.polygon([(cx, cy - s - 3), (cx + s, cy + 2), (cx + s // 2, cy + s),
                   (cx - s // 2, cy + s), (cx - s, cy + 2)], fill=col)
    elif kind == "ship":
        d.polygon([(cx - s, cy + 2), (cx + s, cy + 2), (cx + s // 2, cy + s),
                   (cx - s // 2, cy + s)], fill=col)
        d.rectangle([cx - 2, cy - s - 2, cx + 2, cy + 2], fill=col)
        d.polygon([(cx + 2, cy - s - 2), (cx + s, cy - 2), (cx + 2, cy - 2)], fill=col)
    elif kind == "globe":
        d.ellipse([cx - s, cy - s, cx + s, cy + s], outline=col, width=2)
        d.ellipse([cx - s // 2, cy - s, cx + s // 2, cy + s], outline=col, width=1)
        d.line([cx - s, cy, cx + s, cy], fill=col, width=1)
    elif kind == "scale":
        d.line([cx, cy - s, cx, cy + s], fill=col, width=2)
        d.line([cx - s, cy - s + 4, cx + s, cy - s + 4], fill=col, width=2)
        d.polygon([(cx - s, cy - s + 4), (cx - s + 6, cy + 2), (cx - s - 6, cy + 2)], fill=col)
        d.polygon([(cx + s, cy - s + 4), (cx + s + 6, cy + 2), (cx + s - 6, cy + 2)], fill=col)
        d.line([cx - s, cy + s, cx + s, cy + s], fill=col, width=2)
    elif kind == "coin":
        d.ellipse([cx - s, cy - s, cx + s, cy + s], outline=col, width=2)
        d.text((cx - 3, cy - 7), "$", font=F_NUM, fill=col)
    elif kind == "factory":
        d.rectangle([cx - s, cy - 2, cx + s, cy + s], outline=col, width=2)
        d.polygon([(cx - s, cy - 2), (cx - s // 2, cy - s), (cx, cy - 2)], fill=col)
        d.rectangle([cx + 2, cy - s - 3, cx + 6, cy - 2], fill=col)
    elif kind == "plane":
        d.polygon([(cx - s, cy), (cx + s, cy - 3), (cx + s, cy + 3)], fill=col)
        d.polygon([(cx, cy - s), (cx + 4, cy), (cx - 2, cy)], fill=col)
    elif kind == "trophy":
        d.rectangle([cx - 5, cy - s, cx + 5, cy + 2], outline=col, width=2)
        d.arc([cx - s, cy - s, cx - 2, cy - 2], 90, 270, fill=col, width=2)
        d.arc([cx + 2, cy - s, cx + s, cy - 2], 270, 90, fill=col, width=2)
        d.line([cx, cy + 2, cx, cy + s - 3], fill=col, width=2)
        d.line([cx - 5, cy + s, cx + 5, cy + s], fill=col, width=2)
    elif kind == "music":
        d.ellipse([cx - 7, cy + 2, cx - 1, cy + 8], fill=col)
        d.line([cx - 2, cy + 4, cx - 2, cy - s], fill=col, width=2)
        d.line([cx - 2, cy - s, cx + 6, cy - s + 3], fill=col, width=2)
    elif kind == "bolt":
        d.polygon([(cx + 3, cy - s - 2), (cx - 5, cy + 1), (cx, cy + 1),
                   (cx - 3, cy + s + 2), (cx + 5, cy - 1), (cx, cy - 1)], fill=col)
    elif kind == "leaf":
        d.ellipse([cx - s, cy - s // 2, cx + s, cy + s // 2], outline=col, width=2)
        d.line([cx - s, cy, cx + s, cy], fill=col, width=1)
    elif kind == "mask":
        d.ellipse([cx - s, cy - s + 2, cx - 1, cy + s - 2], outline=col, width=2)
        d.ellipse([cx + 1, cy - s + 2, cx + s, cy + s - 2], outline=col, width=2)
    elif kind == "castle":
        d.rectangle([cx - s, cy - 2, cx + s, cy + s], outline=col, width=2)
        for bx in (-s + 2, -2, s - 6):
            d.rectangle([cx + bx, cy - s, cx + bx + 4, cy - 2], fill=col)
    elif kind == "chart":
        pts = [(cx - s, cy + 5), (cx - s // 2, cy - 2), (cx, cy + 2),
               (cx + s // 2, cy - 6), (cx + s, cy - s)]
        d.line(pts, fill=col, width=2, joint="curve")
        d.polygon([(cx + s - 5, cy - s), (cx + s, cy - s), (cx + s, cy - s + 5)], fill=col)


def trunc(d, text, fnt, max_w):
    if d.textlength(text, font=fnt) <= max_w:
        return text
    while text and d.textlength(text + "…", font=fnt) > max_w:
        text = text[:-1]
    return text + "…"


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- header ----
    d.rectangle([0, 0, W, 72], fill=NAVY)
    d.rectangle([0, 72, W, 76], fill=GOLD)
    d.text((16, 10), "THE WORLD IN ONE DAY", font=F_TITLE, fill=(255, 255, 255))
    d.text((16, 48), "GLOBAL EDITION  •  56 STORIES  •  7 REGIONS  •  16 PANELS",
           font=F_SUB, fill=GOLD_LT)
    d.text((W - 16, 12), "TUESDAY", font=F_DATE, fill=(255, 255, 255), anchor="ra")
    d.text((W - 16, 32), "24 NOVEMBER 2026", font=F_DATE, fill=GOLD_LT, anchor="ra")
    d.text((W - 16, 52), "ALL STORIES CHECKED 24 NOV", font=F_TINY, fill=(200, 210, 220), anchor="ra")

    # ---- info strip ----
    d.text((16, 82), "Every story real, dated 24 Nov 2026 in Asia (23 Nov UTC) — outlet cited on each line.  Full list + links: SOURCES.md",
           font=F_SMALL, fill=MUTED)

    # ---- top band: map (left) + numbers/weather (right) ----
    # map panel
    mx0, my0, mx1, my1 = 16, 100, 500, 268
    d.rectangle([mx0, my0, mx1, my1], fill=CARD, outline=LINE, width=1)
    d.text((mx0 + 8, my0 + 5), "WHERE IT HAPPENED — 7 PINS, NUMBERED TO THE STORIES",
           font=F_SEC, fill=NAVY)
    map_x, map_y, map_w, map_h = mx0 + 6, my0 + 24, mx1 - mx0 - 12, 118
    cols, rows = 64, 28
    cw, ch = map_w / cols, map_h / rows
    for r, spans in LAND.items():
        for a, b in spans:
            for c in range(a, b + 1):
                cx = map_x + (c + 0.5) * cw
                cy = map_y + (r + 0.5) * ch
                d.ellipse([cx - 1.8, cy - 1.8, cx + 1.8, cy + 1.8], fill=NAVY2)
    for lon, lat, num, label in PINS:
        px = map_x + (lon + 180.0) / 360.0 * map_w
        py = map_y + (75.0 - lat) / 130.0 * map_h
        if num == 26:  # Benghazi sits almost on top of Antalya (17): nudge for legibility
            px += 13
            py += 11
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=GOLD, outline=(255, 255, 255), width=1)
        d.text((px, py - 6), str(num), font=font("DejaVuSans-Bold.ttf", 9),
               fill=(255, 255, 255), anchor="ma")
    legend = "  ".join(f"{n} {lab}" for _, _, n, lab in PINS)
    d.text((mx0 + 8, my1 - 16), trunc(d, legend, F_TINY, mx1 - mx0 - 16), font=F_TINY, fill=MUTED)

    # right rail: by the numbers
    rx0, rx1 = 516, 1008
    d.rectangle([rx0, 100, rx1, 196], fill=CARD, outline=LINE, width=1)
    d.text((rx0 + 8, 105), "BY THE NUMBERS", font=F_SEC, fill=NAVY)
    cell_w = (rx1 - rx0 - 16) / 3
    for i, (lab, val, cap) in enumerate(NUMBERS):
        cx = rx0 + 8 + (i % 3) * cell_w
        cy = 126 + (i // 3) * 34
        d.text((cx, cy), val, font=F_BIG, fill=RED if i in (0, 1) else NAVY)
        d.text((cx, cy + 22), lab + " — " + cap, font=F_TINY, fill=MUTED)

    # weather strip
    d.rectangle([rx0, 204, rx1, 268], fill=CARD, outline=LINE, width=1)
    d.text((rx0 + 8, 209), "WEATHER — NOW (OPEN-METEO, 23:15 UTC 23 NOV)",
           font=F_SEC, fill=NAVY)
    wcell = (rx1 - rx0 - 16) / 4
    for i, (city, temp, cond) in enumerate(WEATHER):
        cx = rx0 + 8 + (i % 4) * wcell
        cy = 226 + (i // 4) * 20
        d.text((cx, cy), f"{city} {temp}", font=F_SRC, fill=INK)
        d.text((cx, cy + 9), cond, font=F_TINY, fill=MUTED)

    # ---- UTC timeline strip ----
    ty0, ty1 = 276, 300
    d.rectangle([16, ty0, 1008, ty1], fill=NAVY, outline=NAVY)
    d.text((24, ty0 + 5), "UTC", font=F_SRC, fill=GOLD_LT)
    tl_x0, tl_x1 = 70, 990
    d.line([tl_x0, ty0 + 16, tl_x1, ty0 + 16], fill=(120, 140, 160), width=1)
    for hh in range(0, 24, 3):
        x = tl_x0 + hh / 24.0 * (tl_x1 - tl_x0)
        d.text((x, ty0 + 18), f"{hh:02d}", font=F_TINY, fill=(180, 190, 200), anchor="ma")
    for ts, label in TIMELINE:
        hh, mm = int(ts[:2]), int(ts[3:])
        x = tl_x0 + (hh + mm / 60.0) / 24.0 * (tl_x1 - tl_x0)
        d.ellipse([x - 3, ty0 + 13, x + 3, ty0 + 19], fill=GOLD)
        d.text((x, ty0 + 1), label, font=F_TINY, fill=(255, 255, 255), anchor="ma")

    # ---- stories, two columns ----
    col_x = [16, 516]
    col_w = 484
    # split: col 0 = regions 0,1,2 (25 stories); col 1 = regions 3,4,5,6 (31 stories)
    col_regions = [[0, 1, 2], [3, 4, 5, 6]]
    y_start = 310
    row_h = 13
    for ci, regs in enumerate(col_regions):
        x = col_x[ci]
        y = y_start
        for ri in regs:
            name, col = REGIONS[ri]
            d.rectangle([x, y, x + col_w, y + 15], fill=col)
            d.text((x + 5, y + 2), name, font=F_SRC, fill=(255, 255, 255))
            cnt = sum(1 for s in STORIES if s[1] == ri)
            d.text((x + col_w - 5, y + 2), f"{cnt} STORIES", font=F_SRC,
                   fill=(255, 255, 255), anchor="ra")
            y += 18
            for num, r, head, src, _pin in STORIES:
                if r != ri:
                    continue
                d.rectangle([x, y + 1, x + 13, y + 12], fill=col)
                d.text((x + 6.5, y + 1), str(num), font=font("DejaVuSans-Bold.ttf", 8),
                       fill=(255, 255, 255), anchor="ma")
                max_head = col_w - 13 - 8 - d.textlength(" · " + src, font=F_SRC) - 6
                h = trunc(d, head, F_STORY, max_head)
                d.text((x + 18, y + 1), h, font=F_STORY, fill=INK)
                d.text((x + col_w - 4, y + 1), "· " + src, font=F_SRC, fill=MUTED, anchor="ra")
                y += row_h
            y += 3
    stories_end = y

    # ---- left out & why ----
    ly0 = 800
    d.rectangle([16, ly0, 1008, ly0 + 30], fill=(255, 244, 214), outline=GOLD, width=1)
    d.text((24, ly0 + 3), "LEFT OUT & WHY:", font=F_SRC, fill=RED)
    leftout = ("Just Security Early Edition 24 Nov not out at build time (06:30 WIB) — wires used.  "
               "Cut: Skubal $450m Mets deal.  Too old: Trump card-rate vow.  "
               "Unconfirmed: FBI hack probe.  23 Nov UTC = 24 Nov Asia.")
    d.text((24, ly0 + 15), trunc(d, leftout, F_TINY, 1008 - 48), font=F_TINY, fill=INK)

    # ---- 16 illustrated panels ----
    py0 = 838
    pw = (1008 - 16 - 7 * 4) / 8
    ph = 76
    pastel = [(253, 230, 216), (220, 235, 245), (226, 240, 226), (245, 226, 240),
              (255, 243, 205), (232, 222, 244), (220, 240, 240), (245, 228, 228)]
    for i, (kind, title, cap) in enumerate(PANELS):
        px = 16 + (i % 8) * (pw + 4)
        py = py0 + (i // 8) * (ph + 4)
        bg = pastel[i % len(pastel)]
        d.rectangle([px, py, px + pw, py + ph], fill=bg, outline=LINE, width=1)
        draw_icon(d, kind, px + pw / 2, py + 20, 11, NAVY)
        d.text((px + pw / 2, py + 38), trunc(d, title, F_PANEL, pw - 6),
               font=F_PANEL, fill=INK, anchor="ma")
        d.text((px + pw / 2, py + 52), trunc(d, cap, F_PC, pw - 6),
               font=F_PC, fill=MUTED, anchor="ma")

    # ---- footer ----
    d.text((16, 1006),
           "Sources: Reuters · AP · BBC · PANA · Radio Generation Kenya · Rio Times · AppiSToS — full list + links in SOURCES.md  •  Deterministic build — rerun is byte-identical",
           font=F_TINY, fill=MUTED)

    img.save(OUT, format="PNG")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
