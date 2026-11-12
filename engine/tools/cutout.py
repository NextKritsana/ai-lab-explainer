"""Cut an illustration on a white background out to a transparent PNG, so it sits straight on the page like the
reference style (no card, no frame). Run with the Python that has scipy (see SETUP.md / Machine notes).
  <python with scipy> tools/cutout.py assets/img/a3.jpg [more.jpg ...] [--thr 228] [--feather 1.2]
Writes assets/img/<name>.png next to each input. Only white that touches the image edge is removed (flood from the
border), so white areas enclosed by ink lines (a robot's body, a page) stay solid. Dark full-bleed scenes (night
office, dark rooms) have no white border: use them as .fullimg pages instead."""
import os, sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

args = sys.argv[1:]; opt = {}
for k in ("--thr", "--feather"):
    if k in args:
        i = args.index(k); opt[k] = float(args[i + 1]); del args[i:i + 2]
THR = opt.get("--thr", 228); FEATHER = opt.get("--feather", 1.2)
for src in args:
    im = Image.open(src).convert("RGB"); a = np.asarray(im).astype(np.int16)
    white = (a.min(axis=2) >= THR) & ((a.max(axis=2) - a.min(axis=2)) < 28)  # near-white, low saturation
    lab, n = ndimage.label(white)
    edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])); edge = edge[edge > 0]
    bg = np.isin(lab, edge)
    bg = ndimage.binary_opening(bg, iterations=1)           # drop specks
    fg = ~bg; fg = ndimage.binary_fill_holes(fg) | fg
    fg = ndimage.binary_erosion(fg, iterations=1)            # eat the light halo round the ink line
    # keep only real pieces (drop stray dots smaller than 0.2% of the picture)
    lab2, n2 = ndimage.label(fg)
    if n2:
        sizes = ndimage.sum(fg, lab2, range(1, n2 + 1)); keep = np.isin(lab2, 1 + np.flatnonzero(sizes > fg.size * 0.002)); fg = keep
    alpha = Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(FEATHER))
    out = im.convert("RGBA"); out.putalpha(alpha)
    bb = alpha.getbbox()
    if bb: out = out.crop((max(0, bb[0] - 8), max(0, bb[1] - 8), min(out.width, bb[2] + 8), min(out.height, bb[3] + 8)))
    dst = os.path.splitext(src)[0] + ".png"; out.save(dst, optimize=True)
    print(f"{dst}  {out.width}x{out.height}  bg removed {bg.mean() * 100:.0f}%")
