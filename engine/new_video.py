"""Create a fresh AI-Lab video folder from this skill.

Usage: python3 engine/new_video.py PATH/TO/video-N [VOICEOVER.mp3] [--example]

Copies tools/, src/, fonts, gsap, card frames, backdrops, Moon's lab-coat poses and the music bed.
--example also copies the EP30 demo (cut-out pictures, 3 clips, script, timings, scenes, covers) so the
folder builds as-is: the quickest way to test an install or to start from a working episode.
Never overwrites an existing folder.
"""
import os, shutil, sys

SK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EX = "--example" in sys.argv
args = [a for a in sys.argv[1:] if a != "--example"]
if not args:
    raise SystemExit(__doc__)
OUT = os.path.abspath(args[0])
if os.path.exists(OUT):
    raise SystemExit(f"{OUT} already exists: pick the next free video-N number")

cp = lambda a, b: shutil.copytree(os.path.join(SK, a), os.path.join(OUT, b))
cp("engine/tools", "tools")
cp("engine/src", "src")
cp("assets/fonts", "assets/fonts")
cp("engine/lib", "assets/lib")
cp("assets/props", "assets/props")
cp("assets/backdrops", "assets/bd")
cp("assets/host", "assets/host")
for d in ("assets/audio/derived", "assets/img/source", "assets/video", "renders/cover"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)
shutil.copy(os.path.join(SK, "assets/music/bg-music.mp3"), os.path.join(OUT, "assets/audio/bg-music.mp3"))
shutil.copy(os.path.join(SK, "engine/example-ep30/cover-src.html"), os.path.join(OUT, "cover-src.html"))
with open(os.path.join(OUT, "package.json"), "w") as f:
    f.write('{"name": "%s", "private": true}\n' % os.path.basename(OUT))

if EX:
    E = os.path.join(SK, "engine/example-ep30")
    for f in ("script.txt", "cuts.json", "transcript.json"):
        shutil.copy(os.path.join(E, f), OUT)
    shutil.copy(os.path.join(E, "tight-map.json"), os.path.join(OUT, "tools"))
    shutil.copy(os.path.join(E, "gen_body.py"), os.path.join(OUT, "tools"))
    shutil.copy(os.path.join(E, "scenes.js"), os.path.join(OUT, "src"))
    for f in os.listdir(os.path.join(E, "img")):
        shutil.copy(os.path.join(E, "img", f), os.path.join(OUT, "assets/img"))
    for f in os.listdir(os.path.join(E, "video")):
        shutil.copy(os.path.join(E, "video", f), os.path.join(OUT, "assets/video"))

if len(args) > 1:
    shutil.copy(args[1], os.path.join(OUT, "assets/audio/vo-raw" + os.path.splitext(args[1])[1]))
print("created", OUT)
print("next: atempo 1.2 -> tools/tighten.py -> tools/asr_phrases.py -> script.txt -> tools/words.py + words_zip.py"
      " -> cut pictures -> edit tools/gen_body.py + src/scenes.js + cuts.json -> build -> cues -> mix -> render -> short_cut -> cover")
