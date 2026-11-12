"""Crop named boxes out of an irregular sheet: crop_boxes.py SHEET name:x0,y0,x1,y1 ... (upscale to 1500 long side)."""
import sys
from PIL import Image, ImageFilter
im=Image.open(sys.argv[1]).convert("RGB")
for spec in sys.argv[2:]:
    n,b=spec.split(":"); x0,y0,x1,y1=map(int,b.split(","))
    p=im.crop((max(0,x0-14),max(0,y0-14),min(im.width,x1+14),min(im.height,y1+14)))
    s=1500/max(p.size)
    p=p.resize((round(p.width*s),round(p.height*s)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,60,2))
    p.save(f"assets/img/{n}.jpg",quality=92); print(n,p.size,f"x{s:.1f}")
