"""Build cover.html from src/head.html (all CSS) + src/props.js + cover-src.html (two variants), then screenshot both at 1080x1920.
cover-src.html holds <div class="v v1 full">...</div><div class="v v2 full">...</div>; everything in it is shown (no animation).
Usage (from the video folder): python3 tools/cover.py   -> cover.html, renders/cover/cover-v1.jpg, cover-v2.jpg
"""
import os, subprocess

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda f: open(os.path.join(R, f), encoding="utf-8").read()
head = rd("src/head.html").replace("  </head>", """    <style>
      .v { display: none; } body.v1 .v1, body.v2 .v2 { display: block; }
      .w, .svg, .tc, .term, .box, .tape { opacity: 1 !important; } .stamp { opacity: .92 !important; }
      .host .pz:first-child { opacity: 1; } .b1, .b2 { visibility: hidden !important; }
    </style>
  </head>""")
defs = '<svg width="0" height="0" style="position:absolute"><defs>' \
    '<filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="2"/><feDisplacementMap in="SourceGraphic" scale="5"/></filter>' \
    '<filter id="chalkf"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="5" result="t"/><feColorMatrix in="t" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1.6 1.25" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter>' \
    '<filter id="stampf"><feTurbulence type="fractalNoise" baseFrequency=".7" numOctaves="2" seed="8" result="t"/><feColorMatrix in="t" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1.2 1.45" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter>' \
    '<filter id="wc" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".02" numOctaves="4" seed="11" result="n"/><feColorMatrix in="n" values="0 0 0 0 .1 0 0 0 0 .12 0 0 0 0 .2 0 0 0 -1.1 .6" result="m"/><feComposite in="m" in2="SourceAlpha" operator="in" result="mm"/><feBlend in="mm" in2="SourceGraphic" mode="multiply"/></filter>' \
    '</defs></svg>'
overlays = '<div id="fiber" class="full"></div><div id="blot" class="full"></div><div id="vig" class="full"></div>'
html = head + '  <body class="v1">' + defs + '<div id="root" data-f="0">' + rd("cover-src.html") + overlays + '</div>\n<script>\n' + rd("src/props.js") + \
    '\nif (location.hash) document.body.className = location.hash.slice(1);\n</script></body></html>\n'
open(os.path.join(R, "cover.html"), "w", encoding="utf-8").write(html)
os.makedirs(os.path.join(R, "renders/cover"), exist_ok=True)
for v in ("v1", "v2"):
    png = os.path.join(R, f"renders/cover/cover-{v}.png")
    subprocess.run(["node", os.path.join(R, "tools/snap.js"), os.path.join(R, "cover.html"), png, "1080", "1920", f"--hash={v}"], check=True, capture_output=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", png, "-q:v", "2", png[:-4] + ".jpg"], check=True); os.remove(png)
    print(f"renders/cover/cover-{v}.jpg")
