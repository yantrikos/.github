"""Social preview cards (1280x640) for the yantrikos repos.

GitHub renders these whenever a repo link is shared. Palette sampled from the
product icon: graphite #111315, warm off-white #f2f0ed, site amber #E8A33D.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
BG, FG, MUTED, AMBER = "#111315", "#f2f0ed", "#9aa0a6", "#e8a33d"
PAD = 88
F = "C:/Windows/Fonts/"
bold = lambda s: ImageFont.truetype(F + "segoeuib.ttf", s)
reg = lambda s: ImageFont.truetype(F + "segoeui.ttf", s)
mono = lambda s: ImageFont.truetype(F + "consola.ttf", s)

CARDS = [
    ("yantrikdb", "Memory that notices\nwhen facts change",
     "The engine: Rust core, Python bindings. Local-first and inspectable.",
     "pip install yantrikdb"),
    ("yantrikdb-mcp", "Your agent forgets\neverything. This remembers.",
     "Persistent memory for Claude Code, Cursor, Codex and any MCP client.",
     "uvx yantrikdb-mcp"),
    ("yantrikdb-server", "Shared agent memory,\nhosted by you",
     "Authenticated tenants, replication and failover. Same engine, networked.",
     "docker pull ghcr.io/yantrikos/yantrikdb"),
    ("yantrikdb-hermes-plugin", "Memory for Hermes Agent\nthat maintains itself",
     "Consolidation, contradiction tracking and recall that explains itself.",
     "pip install yantrikdb-hermes-plugin"),
]

logo_full = Image.open(r"C:\Users\sync\codes\yantrikdb-web\public\icon.png").convert("RGBA")
logo = logo_full.resize((64, 64), Image.LANCZOS)

for repo, headline, sub, cmd in CARDS:
    im = Image.new("RGB", (W, H), BG)
    # Oversized, very faint mark on the right: fills the dead space without
    # competing with the headline once the card is scaled down in a feed.
    ghost = logo_full.resize((560, 560), Image.LANCZOS)
    ghost.putalpha(ghost.getchannel("A").point(lambda a: int(a * 0.07)))
    im.paste(ghost, (W - 430, (H - 560) // 2), ghost)
    d = ImageDraw.Draw(im)
    # amber edge: a thin left rule reads at thumbnail size where text does not
    d.rectangle([0, 0, 10, H], fill=AMBER)

    im.paste(logo, (PAD, PAD - 8), logo)
    d.text((PAD + 84, PAD + 2), "YantrikDB", font=bold(38), fill=FG)
    d.text((PAD + 84, PAD + 44), "github.com/yantrikos", font=reg(20), fill=MUTED)

    y = 212
    for line in headline.split("\n"):
        d.text((PAD, y), line, font=bold(62), fill=FG)
        y += 74
    d.rectangle([PAD, y + 24, PAD + 92, y + 28], fill=AMBER)
    d.text((PAD, y + 56), sub, font=reg(27), fill=MUTED)

    # command chip
    f = mono(26)
    tw = d.textlength(cmd, font=f)
    bx, by = PAD, H - PAD - 34
    d.rounded_rectangle([bx - 22, by - 20, bx + tw + 22, by + 44], radius=10,
                        fill="#1b1e21", outline="#2c3034")
    d.text((bx, by), cmd, font=f, fill=AMBER)

    # repo name, right-aligned on the command row
    rf = mono(24)
    d.text((W - PAD - d.textlength(repo, font=rf), by + 2), repo, font=rf, fill=MUTED)

    out = f"{repo}-og.png"
    im.save(out, "PNG", optimize=True)
    print(f"  {out}")
