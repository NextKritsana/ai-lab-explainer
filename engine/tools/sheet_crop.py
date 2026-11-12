"""Cut a multi-panel illustration sheet (one Google Flow image holding several scenes) into one image per scene.
  python3 tools/sheet_crop.py assets/img/source/sheet.jpg e1 e2 e3 e4 e5 e6 [--grid 3x2] [--min 1600] [--out assets/img]
Panels are found from the white gutters between them (reading order: left to right, top to bottom). If the gutters
can't be found, or the count doesn't match the names, --grid CxR splits the sheet evenly instead. Each panel is trimmed
of its white margin, upscaled (Lanczos + light sharpen) so its long side is at least --min px, and saved as <name>.jpg.
Free layouts (portrait sheets, panels of different sizes) are found as separate drawings when the gutter search gives the wrong count; that needs the Python with scipy. Use "-" as a name to skip a panel. Writes <out>/sheet-check.jpg (every panel with its name) to look at before building."""
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

args = sys.argv[1:]
opt = {}
for k in ("--grid", "--min", "--out"):
    if k in args:
        i = args.index(k); opt[k] = args[i + 1]; del args[i:i + 2]
if len(args) < 2: sys.exit(__doc__)
SRC, NAMES = args[0], args[1:]
OUT = opt.get("--out", "assets/img"); MIN = int(opt.get("--min", 1600))
im = Image.open(SRC).convert("RGB"); W, H = im.size
a = np.asarray(im).astype(np.int16)
white = (a.min(axis=2) > 232)  # near-white pixels

def runs(frac, minlen, join):  # spans of the profile that are content (not gutter)
    gut = frac > 0.985; spans = []; s = None
    for i, g in enumerate(list(gut) + [True]):
        if not g and s is None: s = i
        if g and s is not None:
            if spans and s - spans[-1][1] < join: spans[-1] = (spans[-1][0], i)  # a thin white gap inside a drawing, not a gutter
            else: spans.append((s, i))
            s = None
    return [sp for sp in spans if sp[1] - sp[0] >= minlen]

def find_panels():
    rows = runs(white.mean(axis=1), H // 12, 3)
    boxes = []
    for y0, y1 in rows:
        cols = runs(white[y0:y1].mean(axis=0), W // 12, max(6, W // 128))
        while len(cols) > 1 and min(b - a for a, b in cols) < W // 8:  # a sliver (one door, one figure) belongs to the panel beside it
            i = min(range(len(cols)), key=lambda k: cols[k][1] - cols[k][0])
            j = i - 1 if i == len(cols) - 1 or (i > 0 and cols[i][0] - cols[i - 1][1] < cols[i + 1][0] - cols[i][1]) else i + 1
            a, b = sorted((i, j)); cols[a:b + 1] = [(cols[a][0], cols[b][1])]
        boxes +=[(x0, y0, x1, y1) for x0, x1 in cols]
    return boxes

def find_blobs(D=22):  # free layouts (portrait sheets, panels of different sizes): each drawing is one blob of ink
    from scipy import ndimage
    lab, _ = ndimage.label(ndimage.binary_dilation(~white, iterations=D))
    bx = [(s[1].start + D, s[0].start + D, s[1].stop - D, s[0].stop - D) for s in ndimage.find_objects(lab)]
    bx = [b for b in bx if (b[2] - b[0]) * (b[3] - b[1]) > W * H // 60]
    return sorted(bx, key=lambda b: ((b[1] + b[3]) // 2 // (H // 8), b[0]))

boxes = [] if "--grid" in opt else find_panels()
if len(boxes) != len(NAMES) and "--grid" not in opt:
    try:
        bl = find_blobs()
        if len(bl) == len(NAMES): boxes = bl; print("free layout: panels found as separate drawings")
    except ImportError: pass
if len(boxes) != len(NAMES):
    c, r = (int(v) for v in opt.get("--grid", "0x0").split("x")) if "--grid" in opt else (0, 0)
    if c * r == 0:
        sys.exit(f"found {len(boxes)} panels for {len(NAMES)} names: pass --grid CxR (e.g. --grid 3x2)")
    boxes = [(W * i // c, H * j // r, W * (i + 1) // c, H * (j + 1) // r) for j in range(r) for i in range(c)]
    print(f"even {c}x{r} grid")
    if len(boxes) != len(NAMES): sys.exit(f"grid has {len(boxes)} panels but {len(NAMES)} names")

def trim(p):  # drop the white margin around the drawing, keep a small breathing pad
    m = np.asarray(p).min(axis=2) < 232
    ys, xs = np.where(m)
    if len(xs) == 0: return p
    pad = int(0.02 * max(p.size))
    return p.crop((max(0, xs.min() - pad), max(0, ys.min() - pad), min(p.width, xs.max() + pad), min(p.height, ys.max() + pad)))

os.makedirs(OUT, exist_ok=True); thumbs = []
for name, b in zip(NAMES, boxes):
    if name == "-": continue
    p = trim(im.crop(b)); s = max(1.0, MIN / max(p.size))
    if s > 1:
        p = p.resize((round(p.width * s), round(p.height * s)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 2))
    p.save(os.path.join(OUT, name + ".jpg"), quality=92)
    print(f"{name}.jpg  {p.width}x{p.height}  (from {b[2]-b[0]}x{b[3]-b[1]}, x{s:.1f})")
    thumbs.append((name, p.copy()))
    if s > 2.2: print(f"  ! {name} was upscaled x{s:.1f} and will look soft: ask for the 2K / 4K download of the sheet")

T = 360; sheet = Image.new("RGB", (T * min(4, len(thumbs)), (T + 50) * -(-len(thumbs) // 4)), "#ddd"); d = ImageDraw.Draw(sheet)
try: f = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 30)
except OSError: f = ImageFont.load_default()
for i, (n, p) in enumerate(thumbs):
    p.thumbnail((T - 10, T - 10)); x, y = (i % 4) * T, (i // 4) * (T + 50)
    sheet.paste(p, (x + 5, y + 5)); d.text((x + 10, y + T + 5), n, fill="#E0393E", font=f)
sheet.save(os.path.join(OUT, "sheet-check.jpg"), quality=85); print(os.path.join(OUT, "sheet-check.jpg"))
