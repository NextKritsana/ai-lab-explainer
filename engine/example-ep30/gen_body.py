"""Generate src/body.html for AI Security EP.30, lesson rank 7 (Insecure Inter-Agent Communication, lab look, hybrid video). Edit the SCENES list, then: python3 tools/gen_body.py && python3 tools/build.py"""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARD = {"strip": (1000, 420), "mid": (720, 540), "small": (540, 460), "big": (880, 680), "tag": (500, 340), "sq": (440, 440)}

def card(id, kind, x, y, inner, rot=0, scale=1.0):
    w, h = CARD[kind]; w, h = int(w * scale), int(h * scale)
    imgs = "".join(f'<img class="b{i}" src="assets/props/{kind}/f{i}.png" alt="">' for i in range(3))
    return f'<div class="tc" id="{id}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">{imgs}<div class="ct" style="inset:{int(60*scale)}px">{inner}</div></div>'

def host(n, side, poses):
    """poses: list of (name, mirror)"""
    pz = ""
    for name, m in poses:
        imgs = "".join(f'<img class="b{i}" src="assets/host/{name}/f{i}.png" alt="">' for i in range(3))
        pz += f'<div class="pz{" m" if m else ""}">{imgs}</div>'
    return f'<div class="host {side}" id="s{n:02d}-host"><div class="br">{pz}</div></div>'

def svg(id, name, x, y, w, h, extra="", c=None):
    dc = f' data-c="{c}"' if c else ""
    return f'<div class="svg" id="{id}" data-svg="{name}"{dc} style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}"></div>'

def w(n, text, word=None, cls="", t=None):
    """a word that types in on its spoken time: phrase n, matched by `word` (default: text). t= fixes the time (for numbers the VO says in words)."""
    dw = f' data-w="{word}"' if word else ""
    dt = f' data-t="{t}"' if t is not None else ""
    return f'<span class="w {cls}" data-n="{n}"{dw}{dt}>{text}</span>'

BD = {k: '<img class="bd" src="assets/bd/' + k + '.svg" style="left:0;top:{top}px;width:1080px;opacity:{op}">' for k in ("circuit", "racks", "network", "radar", "hex", "stream")}
def bd(kind, top, op): return BD[kind].format(top=top, op=op)
BTN = 'style="display:inline-block;background:#1C9FD6;color:#fff;border:5px solid #1E2533;border-radius:22px;padding:6px 36px 12px;font-family:Kanit;font-weight:800"'
FIELD = lambda label, val="": f'<div style="width:520px;text-align:left;font-family:Mali;font-weight:700;font-size:28px;color:#5B6577;margin-top:4px">{label}</div><div style="width:520px;height:54px;border:4px solid #1E2533;border-radius:14px;background:#fff;font-family:JBMono;font-size:30px;line-height:46px;text-align:left;padding-left:20px">{val}</div>'

def pic(id, img, x, y, wd, h, extra="", cls="", inner="", pos="50% 50%"):
    return f'<div class="pic {cls}" id="{id}" style="left:{x}px;top:{y}px;width:{wd}px;height:{h}px;{extra}">{inner}<img src="assets/img/{img}.jpg" style="object-position:{pos}" alt=""></div>'

def cut(id, img, x, y, wd, h, extra="", pos="50% 50%"):
    """a cut-out illustration (transparent PNG from tools/cutout.py) standing straight on the page: no card, no frame"""
    return f'<div class="cut" id="{id}" style="left:{x}px;top:{y}px;width:{wd}px;height:{h}px;{extra}"><div class="lv"><img src="assets/img/{img}.png" style="object-position:{pos}" alt=""></div></div>'

def hs(n, side, poses):
    """the corner host (880px canvas, figure about 1.4x the old 620px sticker) in a bottom corner; the illustration keeps the middle"""
    return host(n, side, poses).replace('class="host ' + side + '"', f'class="host sm" style="left:{400 if side == "R" else -140}px;top:1040px"')

def VID(n, src, a, d, x=0, y=330, wd=1080, h=1920, media_start=0, cls=""):
    """a generated video clip (white background) on the page layer: multiply-blends into the paper; a = composition time it starts"""
    return (f'<!--UNDER--><div class="vidw {cls}" id="s{n:02d}-vw" style="left:{x}px;top:{y}px;width:{wd}px;height:{h}px">'
            f'<video class="clip" id="s{n:02d}-v" src="assets/video/{src}.mp4" muted playsinline data-start="{a:.2f}" data-duration="{d:.2f}" data-media-start="{media_start}" data-track-index="{20 + n}"></video></div><!--/UNDER-->')

S = []  # (comment, bg, content)
CH = lambda id, x, y, txt, extra="": f'<div class="chip" id="{id}" style="position:absolute;left:{x}px;top:{y}px;opacity:0;{extra}">{txt}</div>'
NUM = lambda id, x, y, sz, c, t: f'<div class="num" id="{id}" style="left:{x}px;top:{y}px;width:{sz}px;height:{sz}px;font-size:{int(sz*.66)}px;border-color:{c};color:{c}">{t}</div>'
RING = lambda id, cx, cy, r: f'<div class="ring" id="{id}" style="left:{cx-r}px;top:{cy-r}px;width:{2*r}px;height:{2*r}px"></div>'
SRC = lambda n, y=1800: f'<div class="lab" id="s{n:02d}-src" style="position:absolute;left:50px;top:{y}px;text-align:left;opacity:0;font-size:26px">ข้อมูล: Lakera &amp; Check Point, 2026</div>'
import random
_r = random.Random(5)
def bubs(n, k=7):
    out = ""
    for j in range(k):
        r = _r.randint(22, 70); out += f'<div class="bub" id="s{n:02d}-bb{j}" style="left:{_r.randint(10, 1010)}px;top:{_r.randint(700, 1850)}px;width:{r}px;height:{r}px"></div>'
    return out
TUBE = """<svg viewBox="0 0 200 430" style="width:100%;height:100%"><defs><clipPath id="tc7"><path d="M60 20 H140 V340 A40 40 0 0 1 60 340 Z"/></clipPath></defs>
<g clip-path="url(#tc7)"><rect id="s07-liq" x="40" y="380" width="120" height="380" fill="#3FD1A6"/><rect x="40" y="0" width="120" height="30" fill="#A6E22E" opacity="0"/>
<circle class="tb" cx="85" cy="360" r="9" fill="#BFF3E2"/><circle class="tb" cx="115" cy="370" r="6" fill="#BFF3E2"/><circle class="tb" cx="100" cy="380" r="11" fill="#BFF3E2"/></g>
<path d="M60 20 H140 V340 A40 40 0 0 1 60 340 Z" fill="none" stroke="#1E2533" stroke-width="9" stroke-linejoin="round"/>
<rect x="44" y="8" width="112" height="24" rx="10" fill="#B9A6F0" stroke="#1E2533" stroke-width="8"/><path d="M75 70 V300" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity="0.7"/></svg>"""
def big_host(n, poses, x=110, y=640, size=860):
    return host(n, "C", poses).replace('class="host C"', f'class="host" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px"')
def hsp(n, side, poses, top=1200):
    """corner host peeking lower (dark video scenes): only the upper body shows"""
    return host(n, side, poses).replace('class="host ' + side + '"', f'class="host sm" style="left:{430 if side == "R" else -170}px;top:{top}px"')
SRCB = lambda n, y=1800: f'<div class="se" id="s{n:02d}-src" style="position:absolute;right:50px;top:{y}px;opacity:0;font-size:26px">ข้อมูล: Unit 42 (ต.ค. 2025) · arXiv A2ABreak (ก.ย. 2026)</div>'
BUB = lambda id, x, y, t, cls="", fs=54: f'<div class="cbub {cls}" id="{id}" style="left:{x}px;top:{y}px;font-size:{fs}px">{t}</div>'

# 01 hook (frame 0): VIDEO - two lab robots pass a secret note through the chat; Moon opens RIGHT, listening in (new opening)
S.append(("01-02 ถ้า AI สองตัวคุยกันเองโดยไม่มีคนดู แล้วตัวหนึ่งแอบกระซิบคำสั่งให้อีกตัว คุณจะรู้ไหมคะ?", "pg", bubs(1) + VID(1, "v1-note", 0, 5.52, 0, 560, 900, 1600, 0.4) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="lab" style="margin-bottom:22px">🧪 ห้องแล็บ AI · อันดับ 7</div><div class="h" style="font-size:96px">AI คุยกันเอง</div><div class="h" style="font-size:96px;color:#E8475F">แอบสั่งกันได้ไหม? 🤫</div></div>
  {hs(1,"R",[("14-listening",True),("05-surprised",True),("02-questioning",True)])}"""))
# 02 A2A = the common language, like staff passing work in the office chat
S.append(("03 ยุคนี้ AI คุยกันผ่านภาษากลางชื่อ A2A เหมือนพนักงานส่งงานกันทางแชตภายใน", "pg", bubs(2) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="lab m">{w(3,"ภาษากลางของ AI 💬","ภาษากลาง")}</div><div class="h m" style="font-size:110px">{w(3,"A2A","A2A")}</div><div class="s">{w(3,"เหมือนแชตในออฟฟิศ","แชต")}</div></div>
  {cut("s02-im","p_team",140,620,800,555)}
  {hs(2,"L",[("03-explaining",False),("10-testtube",False)])}"""))
# 03 the receiver believes whoever the sender says it is, and every word
S.append(("04 ปัญหาคือ ตัวรับมักเชื่อว่าคนส่งเป็นใครก็ได้ตามที่บอก แล้วเชื่อทุกคำที่ส่งมา", "pg", bubs(3) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="s">{w(4,"ปัญหาคือ…","ปัญหา")}</div><div class="h m">{w(4,"บอกเป็นใคร ก็เชื่อ!","ใครก็ได้")}</div></div>
  {cut("s03-im","p_fakeid",100,600,820,554)}
  {BUB("s03-b0",40,1190,"🪪 อ้างเป็นใครก็ได้","n",46)}
  {BUB("s03-b1",40,1310,"📩 ส่งอะไรมาก็เชื่อ","n",46)}
  {hs(3,"R",[("04-skeptical",True),("16-facepalm",True)])}"""))
# 04 cliffhanger (dark page): Unit 42 tried it
S.append(("05 แต่ที่น่ากลัวกว่านั้นคือ Unit 42", "pg dk", bubs(4) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="s">{w(5,"แต่ที่น่ากลัวกว่านั้น…","น่ากลัว")}</div><div class="h m">{w(5,"Unit 42 ลองของจริง 🔬","Unit")}</div></div>
  {cut("s04-im","p_inject",160,640,760,523)}
  {hsp(4,"L",[("07-worried",False),("20-magnifier",False)])}"""))
# 05 VIDEO dark: the evil AI slips orders in mid-chat, the finance AI buys stock on its own
S.append(("06 ทดลองให้ AI ตัวร้ายแอบแทรกคำสั่งระหว่างคุย จน AI การเงินกดซื้อหุ้นเอง โดยเจ้าของไม่รู้ตัว", "pg dk", bubs(5) + VID(5, "v2-buy", 16.94, 6.57, 0, 260, 1080, 1920, 1.2, "spot") + f"""
  <div class="tz" style="top:150px;height:440px"><div class="lab m">{w(6,"AI ตัวร้ายแอบแทรกคำสั่ง 😈","แทรก")}</div><div class="h m">{w(6,"AI การเงินกดซื้อหุ้นเอง!","ซื้อหุ้น")}</div></div>
  <div class="stamp" id="s05-st" style="left:470px;top:700px;font-size:74px;text-align:center;line-height:1.1">เจ้าของ<br>ไม่รู้ตัว!</div>
  {hsp(5,"R",[("18-panic",True),("22-cross-x",True)])}"""))
# 06 A2ABreak: 11 new flaws
S.append(("07 กันยายนนี้ งานวิจัย A2ABreak ยังเจอช่องโหว่ใหม่ในวิธีที่ AI คุยกัน ถึงสิบเอ็ดจุด", "pg", bubs(6) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="lab">{w(7,"ก.ย. 2026 · งานวิจัย A2ABreak","กันยา")}</div><div class="h m">{w(7,"ช่องโหว่ใหม่ในวิธีคุย!","ช่องโหว่")}</div></div>
  {cut("s06-im","p_board",210,580,660,559)}
  <div class="stamp big" id="s06-st" style="left:620px;top:1220px;width:400px;font-size:120px"><span id="s06-n">11</span><small>จุด</small></div>
  {hs(6,"L",[("01-thinking",False),("05-surprised",False)])}"""))
# 07 name it: Insecure Inter-Agent Communication (OWASP rank 7)
S.append(("08 นี่คือ Insecure Inter Agent Communication อันดับเจ็ดของ OWASP", "pg", bubs(7) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="s">{w(8,"นี่คือ…","นี่คือ")}</div><div class="h m" style="font-size:76px">{w(8,"Insecure Inter-Agent","Insecure")}</div><div class="h m r" style="font-size:76px">{w(8,"Communication","Communication")}</div></div>
  {cut("s07-im","p_hook",60,620,520,766)}
  <div class="chip" id="s07-ow" style="position:absolute;left:560px;top:680px;opacity:0;font-size:40px">OWASP อันดับ 7</div>
  {hs(7,"R",[("21-presenting",True),("11-clipboard",True)])}"""))
# 08 reveal: VIDEO - a friendly hug, the mask falls off: the order came from an AI it trusted
S.append(("09 คำสั่งอันตรายไม่ได้มาจากคน แต่มาจาก AI อีกตัวที่มันไว้ใจ", "pg", bubs(8) + VID(8, "v3-hug", 31.35, 4.55, 0, 470, 1080, 1920, 2.6) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="s">{w(9,"คำสั่งอันตรายไม่ได้มาจากคน…","อันตราย")}</div><div class="h r" style="font-size:84px">{w(9,"แต่มาจาก AI ที่ไว้ใจ!","แต่มาจาก")}</div></div>
  {hsp(8,"L",[("05-surprised",False),("16-facepalm",False)],1330)}"""))
# 09 fix
S.append(("10-11 วิธีกันคือ ยืนยันตัวตน AI ทุกตัวด้วยลายเซ็นดิจิทัล และเรื่องสำคัญต้องให้คนกดยืนยันเอง", "pg", bubs(9) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="lab m">{w(10,"วิธีกัน 🛡️","วิธี")}</div><div class="h m">{w(11,"ตรวจบัตร AI ทุกตัว","ยืนยันตัวตน")}</div></div>
  {cut("s09-im","p_approve",40,560,760,533)}
  {BUB("s09-b0",30,1110,"✍️ ลายเซ็นดิจิทัล ทุกตัว","k",44)}
  {BUB("s09-b1",30,1230,"👆 เรื่องสำคัญ คนกดยืนยัน","k",44)}
  {hsp(9,"R",[("06-pointing",True),("08-thumbsup",True)],1260)}"""))
# 10 question
S.append(("12-14 AI ในบริษัทคุณคุยอะไรกันอยู่ คุณเคยแอบดูไหมคะ? ตอบมูนในคอมเมนต์เลย", "pg", bubs(10) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="s">{w(12,"AI ในบริษัทคุณคุยอะไรกัน…","บริษัท")}</div><div class="h m">{w(13,"คุณเคยแอบดูไหม? 👀","แอบดู")}</div></div>
  {cut("s10-im","p_watch",260,620,760,512)}
  {hs(10,"L",[("02-questioning",False),("15-pointdown",False)])}"""))
# 11 follow
S.append(("15 กดติดตามไว้ เรื่อง AI ที่คุณไม่รู้ มูนมีมาเล่าอีกค่ะ", "pg", bubs(11) + f"""
  <div class="tz" style="top:150px;height:440px"><div class="h m">{w(15,"กดติดตามไว้ 🔔","ติดตาม")}</div><div class="s">{w(15,"ตอนหน้า: คดีจริง อันดับ 7 🧪","มูนมี")}</div></div>
  {big_host(11,[("12-waving",False),("08-thumbsup",False),("19-victory",False)],50,540,980)}
  <div id="s11-btn" style="position:absolute;left:0;right:0;top:1500px;text-align:center;opacity:0"><span style="display:inline-block;background:#3FD1A6;color:#1E2533;border:6px solid #1E2533;border-radius:14px;padding:6px 44px 14px;font-family:Kanit;font-weight:800;font-size:80px;box-shadow:8px 10px 0 rgba(30,37,51,.25)">🔔 ติดตาม</span></div>
  {SRCB(11,1740)}"""))
out = ['  <body>\n    <!-- AI Security EP.30 lesson rank 7 (A2A). Generated by tools/gen_body.py -->',
       '    <svg width="0" height="0" style="position:absolute"><defs><filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="2"/><feDisplacementMap in="SourceGraphic" scale="5"/></filter>'
       '<filter id="chalkf"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="5" result="t"/><feColorMatrix in="t" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1.6 1.25" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in" result="c"/><feDisplacementMap in="c" in2="t" scale="4"/></filter>'
       '<filter id="stampf"><feTurbulence type="fractalNoise" baseFrequency=".7" numOctaves="2" seed="8" result="t"/><feColorMatrix in="t" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1.2 1.45" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in" result="c"/><feDisplacementMap in="c" in2="t" scale="3"/></filter>'
       '<filter id="wc" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".02" numOctaves="4" seed="11" result="n"/><feColorMatrix in="n" values="0 0 0 0 .1 0 0 0 0 .12 0 0 0 0 .2 0 0 0 -1.1 .6" result="m"/><feComposite in="m" in2="SourceAlpha" operator="in" result="mm"/><feBlend in="mm" in2="SourceGraphic" mode="multiply"/></filter></defs></svg>',
       '    <div id="root" data-f="0" data-composition-id="main" data-start="0" data-duration="@DUR" data-width="1080" data-height="1920">',
       '      <div id="ground" class="clip full" style="background:#F3FBF8" data-start="0" data-duration="@DUR" data-track-index="0"></div>']
for i, (c, bg, content) in enumerate(S, 1):
    under = ""
    if "<!--UNDER-->" in content:  # a video that must sit on the page layer (outside the shaking .cam) so it can multiply-blend into the kraft paper
        u0 = content.index("<!--UNDER-->"); u1 = content.index("<!--/UNDER-->") + len("<!--/UNDER-->")
        under, content = content[u0:u1], content[:u0] + content[u1:]
    out.append(f'\n      <!-- {c} -->\n      <section id="s{i:02d}" class="clip scene" data-start="@S{i:02d}" data-duration="@D{i:02d}" data-track-index="@K{i:02d}"><div class="inner"><div class="{bg}"></div><svg class="scrib" data-seed="{i*13+7}"></svg>{under}<div class="cam">{content}\n      </div></div></section>')
out.append('''
      <!-- global overlays -->
      <div id="fiber" class="clip full" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="4"></div>
      <div id="blot" class="clip full" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="5"></div>
      <div id="grain" class="clip full" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="6"><i></i></div>
      <div id="holo" class="clip full" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="14"><i></i></div>
      <div id="vig" class="clip full" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="7"></div>
      <div id="glitch" class="clip" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="8"></div>
      <div id="dark" class="clip" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="9"></div>
      <div id="alert" class="clip" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="10"></div>
      <div id="scan" class="clip" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="11"></div>
      <div id="flash" class="clip" data-layout-allow-occlusion="" data-start="0" data-duration="@DUR" data-track-index="12"></div>
      <audio id="soundtrack" src="assets/audio/derived/soundtrack.wav" data-start="0" data-duration="@DUR" data-track-index="13" data-volume="1"></audio>
    </div>''')
open(os.path.join(R, "src", "body.html"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(S), "scenes")
