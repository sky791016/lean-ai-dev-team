#!/usr/bin/env python3
"""Generate 8 role-perspective QR cards for Lean AI Dev Team."""

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os, textwrap

URL       = "https://sky791016.github.io/lean-ai-dev-team/"
OUT_DIR   = "/Users/super_kai/Programing/lean-ai-dev-team/role-cards"
LOGO_PATH = "/Users/super_kai/Programing/lean-ai-dev-team/logo.png"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 900, 1280

# ── shared palette ────────────────────────────────────────────────────────────
BG    = (10, 10, 15)
CARD  = (20, 20, 30)
TEXT  = (226, 232, 240)
MUTED = (148, 163, 184)
DIM   = (71,  85, 105)

# ── 8 roles ───────────────────────────────────────────────────────────────────
ROLES = [
    dict(
        id="1-solo-dev",
        emoji="🧑‍💻",
        role="独立开发者",
        role_en="Solo Developer",
        accent=(108, 99, 255),          # purple
        pain_label="你是不是也这样？",
        pain="一个人扛整个项目\n又要想需求，又要做架构\n又要写前端后端，根本顾不过来",
        value_label="有了它，相当于你多了一整支团队",
        value="业务规划师 帮你想清楚做什么\n产品经理 帮你算值不值得做\n架构师 帮你设计技术方案\n前端、后端、数据集成 并行开发\n\n一个人说需求，8个AI陪你完成",
    ),
    dict(
        id="2-ceo",
        emoji="🚀",
        role="创业者 / CEO",
        role_en="Founder / CEO",
        accent=(255, 107, 0),           # orange
        pain_label="你是不是踩过这个坑？",
        pain="花了3个月，让AI帮做了个产品\n上线才发现用户根本不需要这个功能\n时间白费了，钱也烧没了",
        value_label="有了它，先算清楚值不值得做",
        value="每个功能开发前，先跑 ROI 测算\n投多少钱、能省多少人力、几个月回本\n有数据才开始写代码\n\n从「做了再说」到「算清楚再做」",
    ),
    dict(
        id="3-pm",
        emoji="📋",
        role="产品经理",
        role_en="Product Manager",
        accent=(56, 189, 248),          # blue
        pain_label="是不是经常遇到这种情况？",
        pain="需求文档写了十页\n开发出来的还是和你想的\n完全不是一回事",
        value_label="有了它，需求不会再跑偏",
        value="业务分析师 把需求拆成用户故事\n每条都有验收标准：Given / When / Then\n前端后端都按同一份 API 契约开发\n\n需求从写下来那刻起就被锁死",
    ),
    dict(
        id="4-cto",
        emoji="👨‍💼",
        role="CTO / 技术总监",
        role_en="CTO / Tech Lead",
        accent=(52, 211, 153),          # green
        pain_label="AI 时代团队的新难题",
        pain="人人都在用 AI 写代码\n每个人写的风格不一样\n合到一起全是 bug，比以前更乱",
        value_label="有了它，团队统一标准并行开发",
        value="架构师先出 ADR 和 API 契约\n前端、后端、数据集成 严格按契约实现\n合规PM最后检查接口是否一致\n\n架构标准从一开始就对齐",
    ),
    dict(
        id="5-outsource",
        emoji="🔧",
        role="外包 / 接包开发者",
        role_en="Freelancer / Contractor",
        accent=(244, 114, 182),         # pink
        pain_label="接包最怕的事情",
        pain="客户说「就改一个小功能」\n改到第 8 次需求还在变\n每次都要推倒重来，做一单亏一单",
        value_label="有了它，需求从第一步就锁死",
        value="开工前先跑业务分析师 + 业务规划师\n把验收标准、边界、不做什么全写清楚\n客户签字确认后才开始写代码\n\n改需求？有合同有依据",
    ),
    dict(
        id="6-enterprise",
        emoji="🏢",
        role="企业数字化负责人",
        role_en="Digital Transformation Lead",
        accent=(251, 191, 36),          # yellow
        pain_label="向上汇报最难的问题",
        pain="花了半年上了 AI 系统\n领导问：省了多少钱？提升了多少效率？\n完全算不清楚，说不出口",
        value_label="有了它，每个功能都有可量化的 ROI",
        value="产品经理智能体自动输出：\n节省工时 × 人力单价 = 人效收益\n流程周期缩短比例、准确率提升\n\n上 AI 之前先算账，上线之后有数据",
    ),
    dict(
        id="7-engineer",
        emoji="💻",
        role="开发工程师",
        role_en="Software Engineer",
        accent=(167, 139, 250),         # light purple
        pain_label="有没有这种经历？",
        pain="需求没想清楚就开始写\n写到一半说方向不对\n推倒重来，效率还不如不用 AI",
        value_label="有了它，代码只写一遍，方向从一开始就是对的",
        value="架构师先出系统设计和 API 契约\n代码写之前已经知道：\n  ✓ 调哪些接口  ✓ 写哪些模块\n  ✓ 数据库怎么设计\n\n不再靠猜，直接开干",
    ),
    dict(
        id="8-proj-mgr",
        emoji="📊",
        role="项目经理 / 业务分析师",
        role_en="Project Manager / BA",
        accent=(34, 197, 94),           # green2
        pain_label="上线后最头疼的扯皮",
        pain="项目上线了，运营说数据不对\n开发说按需求做的\n需求说没这个问题\n谁也不知道问题出在哪",
        value_label="有了它，上线前把所有坑提前堵死",
        value="合规 PM 自动做四闭环检查：\n  ✅ 价值闭环：业务目标有没有覆盖到？\n  ✅ 数据闭环：数据有没有回流机制？\n  ✅ 技术闭环：接口是否一致？\n  ✅ 运营闭环：上线后监控是否就位？\n\n出问题之前就解决问题",
    ),
]

# ── shared QR (generate once) ─────────────────────────────────────────────────
def make_qr(size=260):
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=8, border=2)
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color=(220, 215, 255), back_color=(18, 18, 28)).convert("RGB")
    return img.resize((size, size), Image.LANCZOS)

qr_img = make_qr(260)

# ── font loader ───────────────────────────────────────────────────────────────
def font(size, bold=False):
    candidates = [
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for p in candidates:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: pass
    return ImageFont.load_default()

def cx(draw, y, text, f, color, width=W-60):
    bb = draw.textbbox((0, 0), text, font=f)
    tw = bb[2] - bb[0]
    draw.text(((W - tw) // 2, y), text, fill=color, font=f)
    return bb[3] - bb[1]

def draw_multiline(draw, x, y, text, f, color, line_gap=10):
    lines = text.split('\n')
    total = 0
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=f)
        lh = bb[3] - bb[1]
        draw.text((x, y + total), line, fill=color, font=f)
        total += lh + line_gap
    return total

def cx_multiline(draw, y, text, f, color, line_gap=10):
    lines = text.split('\n')
    total = 0
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=f)
        tw = bb[2] - bb[0]
        lh = bb[3] - bb[1]
        draw.text(((W - tw) // 2, y + total), line, fill=color, font=f)
        total += lh + line_gap
    return total

def rr(img, xy, r, fill, outline=None, lw=2):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(xy, radius=r, fill=fill,
                        outline=outline, width=lw if outline else 0)

def hgrad(img, x0, y0, x1, y1, c0, c1):
    d = ImageDraw.Draw(img)
    for x in range(x0, x1):
        t = (x - x0) / max(x1 - x0 - 1, 1)
        r = int(c0[0] + t * (c1[0] - c0[0]))
        g = int(c0[1] + t * (c1[1] - c0[1]))
        b = int(c0[2] + t * (c1[2] - c0[2]))
        d.line([(x, y0), (x, y1)], fill=(r, g, b))

def vgrad_rect(img, xy, r, c_top, c_bot):
    """Vertical gradient inside a rounded rect via pixel-row approach."""
    x0, y0, x1, y1 = xy
    tmp = Image.new("RGB", (x1-x0, y1-y0), BG)
    td  = ImageDraw.Draw(tmp)
    for row in range(y1 - y0):
        t = row / max(y1 - y0 - 1, 1)
        col = tuple(int(c_top[i] + t*(c_bot[i]-c_top[i])) for i in range(3))
        td.line([(0, row), (x1-x0, row)], fill=col)
    # mask into rounded rect
    mask = Image.new("L", (x1-x0, y1-y0), 0)
    md   = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, x1-x0, y1-y0], radius=r, fill=255)
    img.paste(tmp, (x0, y0), mask)

# ── logo ──────────────────────────────────────────────────────────────────────
logo_base = None
if os.path.exists(LOGO_PATH):
    logo_base = Image.open(LOGO_PATH).convert("RGBA")

# ── generate each card ────────────────────────────────────────────────────────
for role in ROLES:
    ac  = role["accent"]
    ac2 = tuple(min(255, int(c * 0.55)) for c in ac)   # darker shade

    poster = Image.new("RGB", (W, H), BG)

    # top gradient bar
    hgrad(poster, 0, 0, W, 5, ac, (56, 189, 248))

    # subtle top glow blob
    glow = Image.new("RGB", (W, 300), BG)
    gd   = ImageDraw.Draw(glow)
    for radius in range(220, 0, -4):
        alpha_val = int(18 * (1 - radius / 220))
        col = tuple(min(255, c + alpha_val) for c in BG)
        cx_offset = W // 2
        gd.ellipse([cx_offset - radius, -radius, cx_offset + radius, radius],
                   fill=tuple(min(255, BG[i] + int((ac[i]-BG[i]) * alpha_val / 255)) for i in range(3)))
    poster.paste(glow, (0, 0))

    draw = ImageDraw.Draw(poster)

    y = 28

    # ── logo ──────────────────────────────────────────────────────────────────
    if logo_base:
        lh = 72
        lw = int(lh * logo_base.width / logo_base.height)
        logo = logo_base.resize((lw, lh), Image.LANCZOS)
        poster.paste(logo, ((W - lw) // 2, y), logo)
        y += lh + 16

    # ── role badge ────────────────────────────────────────────────────────────
    badge_txt = f"{role['emoji']}  {role['role']}  ·  {role['role_en']}"
    f_badge   = font(17)
    bb = draw.textbbox((0,0), badge_txt, font=f_badge)
    bw, bh = bb[2]-bb[0], bb[3]-bb[1]
    pad = 14
    bx0 = (W - bw - pad*2) // 2
    bx1 = bx0 + bw + pad*2
    by0 = y; by1 = y + bh + pad
    # gradient pill
    vgrad_rect(poster, (bx0, by0, bx1, by1), 20,
               tuple(int(c*0.22) for c in ac),
               tuple(int(c*0.10) for c in ac))
    draw = ImageDraw.Draw(poster)
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=20, fill=None,
                           outline=ac, width=2)
    draw.text((bx0 + pad, by0 + pad//2), badge_txt, fill=ac, font=f_badge)
    y = by1 + 22

    # ── pain label ────────────────────────────────────────────────────────────
    f_label = font(15)
    cx(draw, y, role["pain_label"], f_label, MUTED)
    y += 24

    # ── pain box (big quote style) ────────────────────────────────────────────
    f_pain = font(23)
    lines  = role["pain"].split('\n')
    line_h = 38
    box_h  = len(lines) * line_h + 36
    px0, px1 = 44, W - 44
    # dark red-tinted bg
    rr(poster, (px0, y, px1, y + box_h), 16,
       fill=(50, 18, 18), outline=(180, 40, 40), lw=1)
    draw = ImageDraw.Draw(poster)
    # left red bar
    draw.rounded_rectangle([px0, y, px0+4, y+box_h], radius=2, fill=(220, 60, 60))
    ty = y + 18
    for line in lines:
        bb = draw.textbbox((0,0), line, font=f_pain)
        tw = bb[2]-bb[0]
        draw.text(((W-tw)//2, ty), line, fill=(248, 190, 190), font=f_pain)
        ty += line_h
    y = y + box_h + 18

    # ── value label ───────────────────────────────────────────────────────────
    f_vlabel = font(16)
    cx(draw, y, role["value_label"], f_vlabel, ac)
    y += 28

    # ── value box ─────────────────────────────────────────────────────────────
    f_val  = font(20)
    vlines = role["value"].split('\n')
    vline_h = 34
    vbox_h  = len(vlines) * vline_h + 36
    # accent-tinted bg
    vgrad_rect(poster, (px0, y, px1, y + vbox_h), 16,
               tuple(int(c*0.18) for c in ac),
               tuple(int(c*0.08) for c in ac))
    draw = ImageDraw.Draw(poster)
    draw.rounded_rectangle([px0, y, px1, y+vbox_h], radius=16, fill=None,
                           outline=ac, width=2)
    draw.rounded_rectangle([px0, y, px0+4, y+vbox_h], radius=2, fill=ac)
    vy = y + 18
    for line in vlines:
        bb = draw.textbbox((0,0), line, font=f_val)
        tw = bb[2]-bb[0]
        draw.text(((W-tw)//2, vy), line, fill=TEXT, font=f_val)
        vy += vline_h
    y = y + vbox_h + 24

    # ── divider ───────────────────────────────────────────────────────────────
    hgrad(poster, 80, y, W-80, y+1, ac, (56, 189, 248))
    y += 18

    # ── QR + url row ──────────────────────────────────────────────────────────
    qr_sz  = 200
    qr_tmp = qr_img.resize((qr_sz, qr_sz), Image.LANCZOS)

    # QR card
    qcard_pad = 14
    qcard_w = qr_sz + qcard_pad*2
    qcard_h = qr_sz + qcard_pad*2
    qcx = (W - qcard_w) // 2
    rr(poster, (qcx, y, qcx+qcard_w, y+qcard_h), 14,
       fill=CARD, outline=ac, lw=2)
    poster.paste(qr_tmp, (qcx + qcard_pad, y + qcard_pad))
    draw = ImageDraw.Draw(poster)

    # scan text + url beside or below
    f_scan = font(15)
    f_url  = font(13)
    scan_x = qcx + qcard_w + 18
    scan_y = y + qcard_h//2 - 36
    if scan_x + 200 < W:
        draw.text((scan_x, scan_y), "📱 扫码访问", fill=MUTED, font=f_scan)
        draw.text((scan_x, scan_y+28), "Scan to Visit", fill=DIM, font=f_scan)
        draw.text((scan_x, scan_y+60), URL.replace("https://",""), fill=ac, font=f_url)
    else:
        # center below
        cy_scan = y + qcard_h + 10
        cx(draw, cy_scan,    "📱 扫码访问 · Scan to Visit", f_scan, MUTED)
        cx(draw, cy_scan+24, URL, f_url, ac)
        qcard_h += 52

    y += qcard_h + 12

    # ── bottom skill name ──────────────────────────────────────────────────────
    f_brand = font(14)
    cx(draw, y, "Lean AI Dev Team Skills  ·  精益AI开发团队技能", f_brand, DIM)
    y += 22
    cx(draw, y, "by 史凯 Kai Shi · sky.kugua@gmail.com · Apache 2.0", font(12), DIM)

    # bottom bar
    hgrad(poster, 0, H-5, W, H, ac, (56, 189, 248))

    # ── crop to actual content + margin ───────────────────────────────────────
    # just save full H
    out_path = os.path.join(OUT_DIR, f"{role['id']}.png")
    poster.save(out_path, "PNG", dpi=(200, 200))
    print(f"✅ {out_path}")

print("\n🎉 All 8 role cards generated!")
