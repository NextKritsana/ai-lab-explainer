import sys,glob
from PIL import Image,ImageDraw
d=sys.argv[1]; fs=sorted(glob.glob(d+'/*.jpg')); ims=[Image.open(f) for f in fs]
w,h=ims[0].size; c=8; r=(len(ims)+c-1)//c
G=Image.new('RGB',(w*c,h*r),'white')
for k,im in enumerate(ims):
    G.paste(im,((k%c)*w,(k//c)*h)); ImageDraw.Draw(G).text(((k%c)*w+5,(k//c)*h+5),f"{k*0.5:.1f}s",fill='red')
G.save(sys.argv[2])
