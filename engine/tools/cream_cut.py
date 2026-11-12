"""Cut a sticker panel that sits on a cream paper card: drop the pure-white outside + the cream card, keep the sticker (white border + art).
usage: cream_cut.py in.jpg out.png [--cream 222]"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

src, out = sys.argv[1], sys.argv[2]
cream_min = int(sys.argv[sys.argv.index("--cream") + 1]) if "--cream" in sys.argv else 222
im = np.array(Image.open(src).convert("RGB")).astype(int)
mn, mx = im.min(2), im.max(2)
A = (mn >= 250) & (mx - mn <= 5)                  # pure white
B = (mn >= cream_min) & ~A & ((im[..., 0] - im[..., 2]) >= 2)   # cream / warm paper, slightly yellow
h, w = mn.shape
def touching_border(lab):
    ids = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    return ids
la, _ = ndimage.label(A)
outer = np.isin(la, list(touching_border(la)))
lb, nb = ndimage.label(B)
near = ndimage.binary_dilation(outer, iterations=3)
ids = set(np.unique(lb[near])) | touching_border(lb)
ids.discard(0)
creamcut = np.isin(lb, list(ids))
bg = outer | creamcut
# second pass: white bits now enclosed by removed cream (outside the sticker) that touch the removed area
la2, _ = ndimage.label(A & ~bg)
grown = ndimage.binary_dilation(bg, iterations=2)
small = [i for i, s in enumerate(ndimage.sum(np.ones_like(mn), la2, range(1, la2.max() + 1)), 1) if s < 0.002 * h * w]
bg |= np.isin(la2, [i for i in small if grown[la2 == i].any()])
bg = ndimage.binary_opening(bg, iterations=1)
alpha = np.where(bg, 0, 255).astype(np.uint8)
a = Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(1.0))
rgba = Image.fromarray(im.astype(np.uint8)).convert("RGBA"); rgba.putalpha(a)
arr = np.array(rgba); ys, xs = np.where(arr[..., 3] > 20)
lab, n = ndimage.label(arr[..., 3] > 20)
if n > 1:
    sz = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1)); keep = [i + 1 for i, v in enumerate(sz) if v > sz.max() * 0.01]
    arr[~np.isin(lab, keep), 3] = 0; ys, xs = np.where(arr[..., 3] > 20)
arr = arr[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
Image.fromarray(arr).save(out)
print(out, arr.shape[1], arr.shape[0], round(arr.shape[1] / arr.shape[0], 2), f"bg {bg.mean():.0%}")
