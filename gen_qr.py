#!/usr/bin/env python3
"""Generate a branded QR code poster for Lean AI Dev Team."""

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os, math

# ── config ────────────────────────────────────────────────────────────────────
URL       = "https://sky791016.github.io/lean-ai-dev-team/"
OUT       = "/Users/super_kai/Programing/lean-ai-dev-team/qrcode-poster.png"
LOGO_PATH = "/Users/super_kai/Programing/lean-ai-dev-team/logo.png"

# Colours (dark theme matching the website)
BG        = (10,  10,  15)      # --bg
CARD      = (22,  22,  31)      # --card
ACCENT    = (108, 99,  255)     # --accent purple
ACCENT3   = (56,  189, 248)     # --accent3 blue
GREEN     = (52,  211, 153)
YELLOW    = (251, 191, 36)
TEXT      = (226, 232, 240)
MUTED     = (148, 163, 184)
QR_FG     = (220, 215, 255)     # light purple dots
QR_BG     = (18,  18,  28)      # slightly lighter than BG

W, H = 900, 1200

# ── helpers ───────────────────────────────────────────────────────────────────
def load_font(size, bold=False):
    """Try system fonts with Chinese support, fall back to default."""
    # Priority: Chinese-capable fonts first
    candidates = [
        "/Library/Fonts/Arial Unicode.ttf",                       # best: full Unicode
        "/System/Library/Fonts/STHeiti Medium.ttc",               # Heiti SC (medium/bold feel)
        "/System/Library/Fonts/STHeiti Light.ttc",                # Heiti SC light
        "/System/Library/Fonts/Supplemental/Songti.ttc",          # Songti SC
        "/System/Library/Fonts/Hiragino Sans GB.ttc",             # Hiragino (CJK)
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def centered_text(draw, y, text, font, color, max_w=W-80):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x, y), text, fill=color, font=font)
    return bbox[3] - bbox[1]   # return line height

def rounded_rect(img, xy, radius, fill, border_color=None, border_width=2):
    draw = ImageDraw.Draw(img)
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill,
                            outline=border_color, width=border_width if border_color else 0)

def gradient_bar(img, x0, y0, x1, y1):
    """Horizontal gradient bar from ACCENT to ACCENT3."""
    draw = ImageDraw.Draw(img)
    for x in range(x0, x1):
        t = (x - x0) / max(x1 - x0 - 1, 1)
        r = int(ACCENT[0] + t * (ACCENT3[0] - ACCENT[0]))
        g = int(ACCENT[1] + t * (ACCENT3[1] - ACCENT[1]))
        b = int(ACCENT[2] + t * (ACCENT3[2] - ACCENT[2]))
        draw.line([(x, y0), (x, y1)], fill=(r, g, b))

# ── build QR code ─────────────────────────────────────────────────────────────
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)
qr.add_data(URL)
qr.make(fit=True)
qr_img = qr.make_image(fill_color=QR_FG, back_color=QR_BG).convert("RGB")
qr_size = 360
qr_img  = qr_img.resize((qr_size, qr_size), Image.LANCZOS)

# ── canvas ────────────────────────────────────────────────────────────────────
poster = Image.new("RGB", (W, H), BG)
draw   = ImageDraw.Draw(poster)

# top gradient bar
gradient_bar(poster, 0, 0, W, 6)

# background glow
for r in range(200, 0, -2):
    alpha = int(30 * (1 - r / 200))
    glow_color = (ACCENT[0], ACCENT[1], ACCENT[2])
    draw.ellipse([W//2 - r, 80 - r, W//2 + r, 80 + r],
                 fill=(*glow_color, alpha) if False else BG)  # skip alpha trick

# ── logo ──────────────────────────────────────────────────────────────────────
logo_y = 32
if os.path.exists(LOGO_PATH):
    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo_h = 90
    ratio  = logo.width / logo.height
    logo_w = int(logo_h * ratio)
    logo   = logo.resize((logo_w, logo_h), Image.LANCZOS)
    lx = (W - logo_w) // 2
    # paste with transparency
    poster.paste(logo, (lx, logo_y), logo)
    top_after_logo = logo_y + logo_h + 20
else:
    top_after_logo = logo_y + 20

# ── badge ─────────────────────────────────────────────────────────────────────
badge_y = top_after_logo
badge_text = "精益AI方法论 · Lean AI Methodology"
font_badge = load_font(16)
bx0, bx1 = W//2 - 180, W//2 + 180
rounded_rect(poster, (bx0, badge_y, bx1, badge_y + 32), 16,
             fill=(108, 99, 255, 30) if False else (28, 26, 50),
             border_color=(108, 99, 255, 80) if False else (80, 70, 180))
draw = ImageDraw.Draw(poster)
centered_text(draw, badge_y + 7, badge_text, font_badge, (167, 139, 250))

# ── headline ──────────────────────────────────────────────────────────────────
font_h1   = load_font(38, bold=True)
font_h1b  = load_font(34, bold=True)
font_sub  = load_font(19)
font_sm   = load_font(15)
font_xs   = load_font(13)

hy = badge_y + 50
centered_text(draw, hy,      "AI Dev Team 精益开发团队", font_h1, TEXT)
centered_text(draw, hy + 50, "8智能体 · 战略优先 · 业务价值驱动", font_sub, MUTED)

# ── divider ───────────────────────────────────────────────────────────────────
div_y = hy + 100
gradient_bar(poster, 60, div_y, W - 60, div_y + 1)

# ── QR card ───────────────────────────────────────────────────────────────────
card_y  = div_y + 24
card_h  = qr_size + 60
cx0, cx1 = (W - qr_size - 48) // 2, (W + qr_size + 48) // 2
rounded_rect(poster, (cx0, card_y, cx1, card_y + card_h), 20,
             fill=CARD, border_color=(80, 70, 180), border_width=1)
# paste QR
qx = (W - qr_size) // 2
poster.paste(qr_img, (qx, card_y + 24))

scan_y = card_y + card_h + 14
centered_text(draw, scan_y, "📱  扫码访问  ·  Scan to Visit", font_sm, MUTED)

# ── URL strip ─────────────────────────────────────────────────────────────────
url_y = scan_y + 36
url_text = URL
font_url = load_font(15)
centered_text(draw, url_y, url_text, font_url, (108, 99, 255))

# ── feature pills ─────────────────────────────────────────────────────────────
pills = ["8 Agents", "6 Phases", "4 Closed Loops", "ROI-First", "Apache 2.0"]
pill_y = url_y + 44
font_pill = load_font(14)
pill_gap   = 12
pill_pad_x = 16
pill_h     = 30

# measure total width
widths = []
for p in pills:
    bb = draw.textbbox((0, 0), p, font=font_pill)
    widths.append(bb[2] - bb[0] + pill_pad_x * 2)

total_w = sum(widths) + pill_gap * (len(pills) - 1)
px = (W - total_w) // 2
colors = [ACCENT, (56, 189, 248), GREEN, YELLOW, (244, 114, 182)]

for i, (p, pw) in enumerate(zip(pills, widths)):
    col = colors[i % len(colors)]
    draw.rounded_rectangle([px, pill_y, px + pw, pill_y + pill_h],
                            radius=15, fill=(col[0]//6, col[1]//6, col[2]//6),
                            outline=col, width=1)
    bb = draw.textbbox((0, 0), p, font=font_pill)
    tw = bb[2] - bb[0]
    draw.text((px + (pw - tw) // 2, pill_y + (pill_h - (bb[3] - bb[1])) // 2),
              p, fill=col, font=font_pill)
    px += pw + pill_gap

# ── author strip ──────────────────────────────────────────────────────────────
auth_y = pill_y + pill_h + 32
author_line1 = "史凯 · Kai Shi"
author_line2 = "Founder of Lean AI Method · sky.kugua@gmail.com"
font_auth1 = load_font(20, bold=True)
font_auth2 = load_font(14)
centered_text(draw, auth_y,      author_line1, font_auth1, TEXT)
centered_text(draw, auth_y + 30, author_line2, font_auth2, MUTED)

# ── bottom gradient bar ───────────────────────────────────────────────────────
gradient_bar(poster, 0, H - 6, W, H)

# ── watermark ─────────────────────────────────────────────────────────────────
wm_text = "Copyright © 2026 Kai Shi · Apache 2.0 · Non-Commercial"
font_wm  = load_font(11)
centered_text(draw, H - 30, wm_text, font_wm, (71, 85, 105))

# ── save ──────────────────────────────────────────────────────────────────────
poster.save(OUT, "PNG", dpi=(300, 300))
print(f"✅ Saved: {OUT}  ({W}×{H}px)")
