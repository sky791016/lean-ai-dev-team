#!/usr/bin/env python3
"""Generate 8 role-perspective QR cards × 2 languages for Lean AI Dev Team.

Output: role-cards/{lang}/{id}.png   (lang = zh | en)
"""

import os
from PIL import Image, ImageDraw, ImageFont
import qrcode

URL     = "https://sky791016.github.io/lean-ai-dev-team/"
OUT_DIR = "/Users/super_kai/Programing/lean-ai-dev-team/role-cards"
LOGO    = "/Users/super_kai/Programing/lean-ai-dev-team/logo.png"

W, H = 900, 1200

BG    = (10,  10,  15)
CARD  = (20,  20,  30)
TEXT  = (226, 232, 240)
MUTED = (148, 163, 184)
DIM   = (71,  85, 105)

# ─── role data ────────────────────────────────────────────────────────────────
ROLES = [
    dict(
        id="1-solo-dev",
        accent=(108, 99, 255),
        zh=dict(
            badge="独立开发者  Solo Developer",
            pain_label="你是不是也这样？",
            pain="一个人扛整个项目\n又要想需求，又要做架构\n又要写前端后端，根本顾不过来",
            value_label="有了它，相当于你多了一整支团队",
            value="业务规划师  帮你想清楚做什么\n产品经理  帮你算值不值得做\n架构师  帮你设计技术方案\n前端、后端、数据集成  并行开发\n\n一个人说需求，8个AI陪你完成",
        ),
        en=dict(
            badge="Solo Developer",
            pain_label="Does this sound familiar?",
            pain="You're the only one on the project.\nHandle requirements, architecture,\nfrontend AND backend — all alone.",
            value_label="With Lean AI Dev Team, you get a full crew.",
            value="Business Planner  — clarifies what to build\nProduct Manager  — validates ROI before coding\nArchitect         — designs the tech stack\nFE + BE + Data    — build in parallel\n\nYou talk, 8 AI agents execute.",
        ),
    ),
    dict(
        id="2-ceo",
        accent=(255, 107, 0),
        zh=dict(
            badge="创业者 / CEO  Founder / CEO",
            pain_label="你是不是踩过这个坑？",
            pain="花了3个月，让AI帮做了个产品\n上线才发现用户根本不需要这个功能\n时间白费了，钱也烧没了",
            value_label="有了它，先算清楚值不值得做",
            value="每个功能开发前，先跑 ROI 测算\n投多少钱、能省多少人力、几个月回本\n有数据才开始写代码\n\n从「做了再说」到「算清楚再做」",
        ),
        en=dict(
            badge="Founder / CEO",
            pain_label="Burned by this before?",
            pain="3 months building an AI product.\nLaunched — nobody needed that feature.\nTime wasted. Budget burned.",
            value_label="With Lean AI Dev Team, prove ROI before you code.",
            value="Every feature starts with a business case:\nhow much to invest, how much to save,\nmonths to break even.\nData first. Code second.\n\nFrom 'ship and pray' to 'prove then build'.",
        ),
    ),
    dict(
        id="3-pm",
        accent=(56, 189, 248),
        zh=dict(
            badge="产品经理  Product Manager",
            pain_label="是不是经常遇到这种情况？",
            pain="需求文档写了十页\n开发出来的还是和你想的\n完全不是一回事",
            value_label="有了它，需求不会再跑偏",
            value="业务分析师  把需求拆成用户故事\n每条都有验收标准：Given / When / Then\n前后端按同一份 API 契约开发\n\n需求从写下来那刻起就被锁死",
        ),
        en=dict(
            badge="Product Manager",
            pain_label="Does this keep happening?",
            pain="You wrote a 10-page spec.\nDevelopers built something completely\ndifferent from what you envisioned.",
            value_label="With Lean AI Dev Team, requirements stay locked.",
            value="Business Analyst breaks requirements into user stories.\nEvery story has acceptance criteria: Given/When/Then.\nFrontend and backend share one API contract.\n\nWhat you write is what gets built.",
        ),
    ),
    dict(
        id="4-cto",
        accent=(52, 211, 153),
        zh=dict(
            badge="CTO / 技术总监  Tech Lead",
            pain_label="AI 时代团队的新难题",
            pain="人人都在用 AI 写代码\n每个人写的风格不一样\n合到一起全是 bug，比以前更乱",
            value_label="有了它，团队统一标准并行开发",
            value="架构师先出 ADR 和 API 契约\n前端、后端、数据集成  严格按契约实现\n合规PM最后检查接口是否一致\n\n架构标准从一开始就对齐",
        ),
        en=dict(
            badge="CTO / Tech Lead",
            pain_label="The new AI team headache",
            pain="Everyone's using AI to write code.\nEvery dev's output looks different.\nMerging it all creates more bugs than before.",
            value_label="With Lean AI Dev Team, one standard, parallel execution.",
            value="Architect publishes ADRs and API contracts first.\nFE, BE, and Data all implement against the same spec.\nCompliance PM audits interface consistency at the end.\n\nAlignment from day one.",
        ),
    ),
    dict(
        id="5-outsource",
        accent=(244, 114, 182),
        zh=dict(
            badge="外包 / 接包开发者  Freelancer",
            pain_label="接包最怕的事情",
            pain="客户说「就改一个小功能」\n改到第 8 次需求还在变\n每次都要推倒重来，做一单亏一单",
            value_label="有了它，需求从第一步就锁死",
            value="开工前先跑业务分析师 + 业务规划师\n把验收标准、边界、不做什么全写清楚\n客户签字确认后才开始写代码\n\n改需求？有合同有依据",
        ),
        en=dict(
            badge="Freelancer / Contractor",
            pain_label="Every freelancer's nightmare",
            pain="Client says 'just one small change.'\nThat's change number 8.\nScope creep kills every project.",
            value_label="With Lean AI Dev Team, scope is locked before coding starts.",
            value="Business Analyst + Business Planner run first.\nAcceptance criteria, boundaries, and out-of-scope — all written.\nClient signs off before a single line of code.\n\nChange requests? You have documentation.",
        ),
    ),
    dict(
        id="6-enterprise",
        accent=(251, 191, 36),
        zh=dict(
            badge="企业数字化负责人  Digital Lead",
            pain_label="向上汇报最难的问题",
            pain="花了半年上了 AI 系统\n领导问：省了多少钱？提升了多少效率？\n完全算不清楚，说不出口",
            value_label="有了它，每个功能都有可量化的 ROI",
            value="产品经理智能体自动输出：\n节省工时 × 人力单价 = 人效收益\n流程周期缩短比例、准确率提升\n\n上 AI 之前先算账，上线之后有数据",
        ),
        en=dict(
            badge="Digital Transformation Lead",
            pain_label="The hardest question from leadership",
            pain="Six months. A new AI system deployed.\nLeadership asks: how much did we save?\nHow much more efficient are we? No answer.",
            value_label="With Lean AI Dev Team, every feature ships with measurable ROI.",
            value="Product Manager agent auto-generates:\nhours saved x labor cost = productivity gain\nprocess cycle reduction, accuracy improvement.\n\nBuild the business case first. Report with data after.",
        ),
    ),
    dict(
        id="7-engineer",
        accent=(167, 139, 250),
        zh=dict(
            badge="开发工程师  Software Engineer",
            pain_label="有没有这种经历？",
            pain="需求没想清楚就开始写\n写到一半说方向不对\n推倒重来，效率还不如不用 AI",
            value_label="有了它，代码只写一遍，方向从一开始就是对的",
            value="架构师先出系统设计和 API 契约\n代码写之前你已经知道：\n  调哪些接口  写哪些模块\n  数据库怎么设计\n\n不再靠猜，直接开干",
        ),
        en=dict(
            badge="Software Engineer",
            pain_label="Sound familiar?",
            pain="Started coding before requirements were clear.\nHalfway through: wrong direction.\nStarted over. AI made it slower, not faster.",
            value_label="With Lean AI Dev Team, write code once — get the direction right first.",
            value="Architect produces system design and API contracts.\nBefore you write a line, you already know:\n  which APIs to call  which modules to build\n  how the database is structured\n\nNo guessing. Just execute.",
        ),
    ),
    dict(
        id="8-proj-mgr",
        accent=(34, 197, 94),
        zh=dict(
            badge="项目经理 / BA  Project Manager",
            pain_label="上线后最头疼的扯皮",
            pain="项目上线了，运营说数据不对\n开发说按需求做的\n需求说没这个问题\n谁也不知道问题出在哪",
            value_label="有了它，上线前把所有坑提前堵死",
            value="合规PM自动做四闭环检查：\n  价值闭环：业务目标有没有覆盖到？\n  数据闭环：数据有没有回流机制？\n  技术闭环：接口是否一致？\n  运营闭环：上线后监控是否就位？\n\n出问题之前就解决问题",
        ),
        en=dict(
            badge="Project Manager / BA",
            pain_label="The blame game after launch",
            pain="Project launched. Ops says data is wrong.\nDev says they built the spec.\nBA says the spec was fine.\nNobody knows where the gap is.",
            value_label="With Lean AI Dev Team, every gap is caught before launch.",
            value="Compliance PM runs four closed-loop checks:\n  Value loop:   does it cover the business goal?\n  Data loop:    is there a data feedback mechanism?\n  Tech loop:    are all interfaces consistent?\n  Ops loop:     is post-launch monitoring in place?\n\nSolve problems before they happen.",
        ),
    ),
]

# ─── utilities ────────────────────────────────────────────────────────────────
def font(size):
    for p in [
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def hgrad(img, x0, y0, x1, y1, c0, c1):
    d = ImageDraw.Draw(img)
    w = max(x1 - x0 - 1, 1)
    for x in range(x0, x1):
        t = (x - x0) / w
        col = tuple(int(c0[i] + t * (c1[i] - c0[i])) for i in range(3))
        d.line([(x, y0), (x, y1)], fill=col)


def vgrad_rect(img, xy, r, c0, c1):
    x0, y0, x1, y1 = xy
    tmp = Image.new("RGB", (x1 - x0, y1 - y0), BG)
    td = ImageDraw.Draw(tmp)
    h = max(y1 - y0 - 1, 1)
    for row in range(y1 - y0):
        t = row / h
        col = tuple(int(c0[i] + t * (c1[i] - c0[i])) for i in range(3))
        td.line([(0, row), (x1 - x0, row)], fill=col)
    mask = Image.new("L", (x1 - x0, y1 - y0), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, x1 - x0, y1 - y0], radius=r, fill=255)
    img.paste(tmp, (x0, y0), mask)


def rr(img, xy, r, fill=None, outline=None, lw=2):
    ImageDraw.Draw(img).rounded_rectangle(
        [xy[0], xy[1], xy[2], xy[3]], radius=r,
        fill=fill, outline=outline, width=lw if outline else 0,
    )


def cx(draw, y, text, f, color):
    bb = draw.textbbox((0, 0), text, font=f)
    draw.text(((W - (bb[2] - bb[0])) // 2, y), text, fill=color, font=f)
    return bb[3] - bb[1]


def cx_block(draw, y, lines, f, color, line_gap=8):
    """Draw centered multiline; return total height used."""
    total = 0
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=f)
        lh = bb[3] - bb[1]
        draw.text(((W - (bb[2] - bb[0])) // 2, y + total), line, fill=color, font=f)
        total += lh + line_gap
    return total


# ─── QR (generate once) ───────────────────────────────────────────────────────
def make_qr(size=200):
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=8, border=2)
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color=(220, 215, 255), back_color=(18, 18, 28)).convert("RGB")
    return img.resize((size, size), Image.LANCZOS)


QR = make_qr(200)

logo_base = None
if os.path.exists(LOGO):
    logo_base = Image.open(LOGO).convert("RGBA")


# ─── card builder ─────────────────────────────────────────────────────────────
def make_card(role, lang):
    ac  = role["accent"]
    ac2 = tuple(min(255, int(c * 0.55)) for c in ac)
    data = role[lang]

    img = Image.new("RGB", (W, H), BG)
    hgrad(img, 0, 0, W, 5, ac, (56, 189, 248))

    draw = ImageDraw.Draw(img)
    y = 28

    # logo
    if logo_base:
        lh = 64
        lw = int(lh * logo_base.width / logo_base.height)
        logo = logo_base.resize((lw, lh), Image.LANCZOS)
        img.paste(logo, ((W - lw) // 2, y), logo)
        y += lh + 14

    # role badge pill
    f_badge = font(18)
    bb = draw.textbbox((0, 0), data["badge"], font=f_badge)
    bw, bh = bb[2] - bb[0], bb[3] - bb[1]
    pad = 14
    bx0 = (W - bw - pad * 2) // 2
    bx1 = bx0 + bw + pad * 2
    by0, by1 = y, y + bh + pad
    vgrad_rect(img, (bx0, by0, bx1, by1), 20,
               tuple(int(c * 0.22) for c in ac),
               tuple(int(c * 0.10) for c in ac))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=20,
                           fill=None, outline=ac, width=2)
    draw.text((bx0 + pad, by0 + pad // 2), data["badge"], fill=ac, font=f_badge)
    y = by1 + 20

    # pain label
    f_label = font(15)
    cx(draw, y, data["pain_label"], f_label, MUTED)
    y += 26

    # pain box
    f_pain  = font(22)
    p_lines = data["pain"].split("\n")
    lh_pain = 36
    box_h   = len(p_lines) * lh_pain + 32
    px0, px1 = 44, W - 44
    rr(img, (px0, y, px1, y + box_h), 16, fill=(50, 18, 18), outline=(180, 40, 40), lw=1)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([px0, y, px0 + 4, y + box_h], radius=2, fill=(220, 60, 60))
    ty = y + 16
    for line in p_lines:
        bb = draw.textbbox((0, 0), line, font=f_pain)
        draw.text(((W - (bb[2] - bb[0])) // 2, ty), line, fill=(248, 190, 190), font=f_pain)
        ty += lh_pain
    y = y + box_h + 18

    # value label
    f_vlabel = font(16)
    cx(draw, y, data["value_label"], f_vlabel, ac)
    y += 28

    # value box
    f_val   = font(19)
    v_lines = data["value"].split("\n")
    lh_val  = 32
    vbox_h  = len(v_lines) * lh_val + 32
    vgrad_rect(img, (px0, y, px1, y + vbox_h), 16,
               tuple(int(c * 0.18) for c in ac),
               tuple(int(c * 0.08) for c in ac))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([px0, y, px1, y + vbox_h], radius=16, fill=None, outline=ac, width=2)
    draw.rounded_rectangle([px0, y, px0 + 4, y + vbox_h], radius=2, fill=ac)
    vy = y + 16
    for line in v_lines:
        bb = draw.textbbox((0, 0), line, font=f_val)
        draw.text(((W - (bb[2] - bb[0])) // 2, vy), line, fill=TEXT, font=f_val)
        vy += lh_val
    y = y + vbox_h + 22

    # divider
    hgrad(img, 80, y, W - 80, y + 1, ac, (56, 189, 248))
    y += 16

    # QR + label
    qr_sz = 200
    qpad  = 12
    qcw   = qr_sz + qpad * 2
    qch   = qr_sz + qpad * 2
    qcx   = (W - qcw) // 2
    rr(img, (qcx, y, qcx + qcw, y + qch), 14, fill=CARD, outline=ac, lw=2)
    img.paste(QR.resize((qr_sz, qr_sz), Image.LANCZOS), (qcx + qpad, y + qpad))
    draw = ImageDraw.Draw(img)

    f_scan = font(15)
    f_url  = font(13)
    scan_x = qcx + qcw + 16
    if scan_x + 180 < W:
        sy = y + qch // 2 - 30
        draw.text((scan_x, sy),      "Scan to Visit" if lang == "en" else "扫码访问",
                  fill=MUTED, font=f_scan)
        draw.text((scan_x, sy + 26), URL.replace("https://", ""),
                  fill=ac, font=f_url)
    else:
        cy_scan = y + qch + 10
        cx(draw, cy_scan,      "Scan to Visit" if lang == "en" else "扫码访问", f_scan, MUTED)
        cx(draw, cy_scan + 24, URL, f_url, ac)
        qch += 48
    y += qch + 14

    # footer brand
    f_brand = font(13)
    brand = ("Lean AI Dev Team Skills  ·  Precision AI Development"
             if lang == "en"
             else "Lean AI Dev Team Skills  ·  精益AI开发团队技能")
    cx(draw, y, brand, f_brand, DIM)
    y += 20
    cx(draw, y, "by Kai Shi  sky.kugua@gmail.com  Apache 2.0", font(12), DIM)
    y += 20

    # bottom bar
    hgrad(img, 0, H - 5, W, H, ac, (56, 189, 248))

    # crop to content + margin
    crop_y = min(y + 30, H)
    img = img.crop((0, 0, W, crop_y))

    return img


# ─── generate all ─────────────────────────────────────────────────────────────
for lang in ("zh", "en"):
    os.makedirs(os.path.join(OUT_DIR, lang), exist_ok=True)

for role in ROLES:
    for lang in ("zh", "en"):
        card = make_card(role, lang)
        path = os.path.join(OUT_DIR, lang, f"{role['id']}.png")
        card.save(path, "PNG", dpi=(200, 200))
        print(f"  {path}")

print("\nDone — 16 cards generated.")
