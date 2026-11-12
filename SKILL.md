---
name: ai-lab-explainer
description: Make vertical (1080x1920) AI-security explainer Reels in the "AI Lab" look ("…ได้ไหม?" series): light mint lab-notebook grid page, mint + violet palette, Moon (cat-eared host in a lab coat) as a big sticker that changes pose every 2-3 s, cut-out illustrations that always move, generated video clips blended into the page, stamps, count-ups, lab bubbles, a synthesized music bed and SFX. From one voice-over it delivers a long clip, a ≤30 s short clip that tells the whole story, 2 covers and captions, and it writes the voice, image, sheet and Flow-video prompts for the next episode. Use for คลิปห้องแล็บ AI, คลิป AI Security ธีมแล็บ, ทำคลิปจากเสียงพากย์ธีมห้องแล็บ, หลอก AI ได้ไหม, or any explainer in this look.
---

# AI Lab explainer (long clip + short clip + covers + captions)

Reply in the user's language (Thai). Users are not technical: run everything yourself, name files exactly, and send the finished mp4s and covers.

Example of the finished look: `example-output/` (EP30 "AI คุยกันเอง แอบสั่งกันได้ไหม?": covers and a frame grid). The full EP30 project is in `engine/example-ep30/` and builds with `engine/new_video.py <dir> --example`.

## The look (details in `references/style-spec.md`)
- **Page.** Light mint grid page `.pg` (lavender `.pg.dk` for the scary beat), doodles of flasks, test tubes and bubbles in the margins, lab bubbles drifting up in every scene.
- **Palette.** Mint #3FD1A6, violet #6A4BB0, pink-red #E8475F, gold #F7D23E, navy ink #1E2533. The ground colour is #F3FBF8.
- **Host.** Moon, cat ears, lab coat (`assets/host/NN-pose/f0..f2.png`, 24 poses, listed below). She is in almost every scene, BIG (the `hs()` corner sticker, 880 px canvas), and changes pose every 2-3 s on a spoken word.
- **Pictures.** One illustration per scene, cut out onto the page (`cut()`): no frames or cards. Every picture always moves: it lands with a squash, floats, and kicks with a sound on every new sentence (the "keep every illustration alive" block in `scenes.js`).
- **Video.** Generated clips go on the page layer with `VID()`. White clips multiply-blend into the page; dark clips use `cls="spot"` (a soft oval spotlight).
- **Text.** Keyword pop-ups (1-2 lines, Kanit 76-110 px) typed in on their spoken word; never running subtitles. The top 150-590 px is the headline zone (`.tz`). No line may be wider than 1000 px (check with `tools/wide.js`).
- **Sound.** The music bed is `assets/music/bg-music.mp3`, an original synthesized track (`tools/make_music.py`), so it is copyright-free. All SFX are synthesized in `tools/mix.py`. Master about -13 LUFS.

## Story rules (what got views)
- **Hook.** Frame 0 shows the label pill ("🧪 ห้องแล็บ AI · อันดับ N") and a 2-line question ending in **"…ได้ไหม?"** in plain words. There is no filler in the first 4 s. Only about 1 viewer in 4 passes 3 s.
- **Order.**
  1. hook question
  2. what the thing is, in everyday words
  3. the problem
  4. cliffhanger ("แต่ที่น่ากลัวกว่านั้นคือ…", on a dark page)
  5. the proof: real research or news with a number
  6. the name (OWASP etc.)
  7. the reveal line
  8. the fix
  9. the comment question
  10. follow
- **Keep the answer and the fix for the end.** No "การทดลองที่ N", "ผลการทดลอง" or "สำเร็จ" stamps: it is a story, not a lab report.
- **Facts.** Only verified facts from primary sources (research paper, vendor report, reputable news), each with its month and year. Drop any number you cannot verify. Credit the sources in the last scene (`SRCB`) and in the caption.
- **Jargon.** None on covers. Inside the clip it is fine as the "name it" beat.
- **Story format with an actor (optional).** Open spooky or with a character in trouble, then reveal it was a hacker, then the real case and the fix. A recurring actor (for example a gullible AI owner with a crush on Moon) can carry the story; Moon stays the narrator.

## Clip lengths
- **Voice speed.** Speed the voice up with `atempo=1.2`. After that, about 15 Thai characters ≈ 1 s.
- **Long clip.** Normally at most 50 s (about 720 characters of script). A story-format episode may run longer if the user wants.
- **Short clip.** At most 30 s, cut from the long one with `tools/short_cut.py`. It must be a complete story ending on the reveal, never on a cliffhanger. Usually scenes 1-5 plus the reveal scene.

## Workflow
`PY` = a Python that has numpy, pillow, scipy and sherpa-onnx (see SETUP.md). `<skill>` = this folder.

1. **New folder.** Run `python3 <skill>/engine/new_video.py <workdir>/video-N voiceover.mp3`. Check which numbers exist first, and never overwrite an old folder. To start from the working EP30 episode, add `--example`, then replace its pictures, script and scenes.
2. **Voice.**
   - Speed it up: `ffmpeg -i assets/audio/vo-raw.mp3 -af atempo=1.2 assets/audio/vo-src.mp3`.
   - Tighten it: `$PY tools/tighten.py assets/audio/vo-src.mp3 assets/audio/derived/vo-tight.wav --gap 0.12 --long 0.24`.
   - Run `$PY tools/asr_phrases.py`, which prints the phrases.
3. **`script.txt`.** Write one line per printed phrase, using the real script text (English words as written, numbers as spoken). Then run `$PY tools/words.py && $PY tools/words_zip.py` for exact per-word times.
4. **Pictures.**
   - Sheets: `$PY tools/sheet_crop.py <sheet.jpg> name1 … name6 --grid 3x2` writes `assets/img/<name>.jpg`. Rename each to `p_<name>.jpg`.
   - Cut-outs: `$PY tools/cutout.py assets/img/p_<name>.jpg --thr 242` turns each into a transparent PNG. For a sheet with a cream card behind it, use `tools/cream_cut.py`.
   - Clean thin slivers left by the cut-out if any remain.
5. **Videos.**
   - Look at each clip first with `$PY tools/contact.py clip.mp4 out.jpg`.
   - Prepare white clips with `ffmpeg -an -vf "colorlevels=rimax=0.95:gimax=0.95:bimax=0.95,fps=30"` so the background disappears in multiply. Dark clips get `fps=30` only.
   - `VID(n, src, a, d, x, y, w, h, media_start, cls)`:
     - `a` = scene start − 0.45
     - `d` = scene end + 0.45 − a
     - `media_start` + `d` must fit inside the clip.
6. **Scenes.**
   - In `tools/gen_body.py`, edit the `S.append(...)` list (one per scene) and the helpers:
     - `hs(n, side, poses)`: corner host.
     - `hsp(n, side, poses, top)`: Moon peeking lower, for video or dark scenes.
     - `big_host`, `cut`, `BUB` (speech bubble `k` mint / `n` neutral), `RING`, `.stamp` / `.stamp.big`, `.chip`.
     - `w(n, text, word)`: types a word in on phrase n's spoken `word`.
   - In `src/scenes.js`, between `// 01 hook` and `// ---------- keep every illustration alive`, time the beats with `fw(n, "word", fallback)`. Use `hIn`, `hPose`, `inPic`, `pop`, `rstamp`, `count`, `cue` and `shake(cam(n))`.
   - Set the transitions in `const TR = {…}`, never the same one twice in a row: tZoom, tSlide, tBlackout, tGlitch, tScan, tDoors, tAlert, tErase, tSmudge, tIris.
   - Set `cuts.json` to `{"cuts": [0, …scene starts…, DURATION]}`, where DURATION = VO length + about 0.4 s.
   - Change Moon's side every scene, and change her pose on a spoken word inside each scene.
7. **Build.**
   - Run `$PY tools/gen_body.py && $PY tools/build.py`.
   - Then `node tools/wide.js "$PWD/index.html"`, which must print `[]`.
   - Then `node tools/frames.js preview.jpg t1 t2 …` (one time per scene) and look at it: text over Moon, stamps off-page, headlines arriving too late.
8. **Sound.** Run `$PY tools/cues.py && $PY tools/mix.py`, then `$PY tools/build.py` again. Do not make a no-music version unless asked.
9. **Render.** Run `npx hyperframes render . -o "renders/EP<n> <title>.mp4"` in the background. Then pull about 16 frames with ffmpeg and look at them (`tools/grid.py <frames dir> grid.jpg`).
10. **Short clip.** Run `$PY tools/short_cut.py "renders/EP<n> <title>.mp4" 1-5,8 "renders/EP<n> สตอรี่ hook <title>.mp4"`. Choose the scene list so it ends on the reveal and runs at most 30 s.
11. **Covers.**
    - Edit `cover-src.html` (`.v1` and `.v2`) and run `$PY tools/cover.py`, which writes `renders/cover/cover-v1.jpg` and `cover-v2.jpg`.
    - Light mint page, ONE big robot or subject, a 2-line "…ได้ไหม?" title, and Moon big.
    - Every episode uses a different layout and different Moon poses from the last one. Note them in the comment at the top of `cover-src.html`.
    - Remind the user to set cover v1 as the Reel's custom thumbnail.
12. **Caption.** Write the long-clip caption:
    - 🧪 title line
    - 2-3 short story lines with the verified numbers
    - "วิธีกันมีในคลิป 🛡️"
    - the comment question
    - 📚 sources with month and year
    - hashtags

    Write the short-clip caption: 1-2 lines plus "ดูคลิปเต็ม EP.<n> บนเพจ".
13. **Deliver.** Name files `EP<n> <title>.mp4` and `EP<n> สตอรี่ hook <title>.mp4`, never `video-N`. Move them, never delete. Put the covers and the caption txt into the user's episode folder.

## Moon's poses (`assets/host`)
01-thinking, 02-questioning, 03-explaining, 04-skeptical, 05-surprised, 06-pointing, 07-worried, 08-thumbsup, 09-smug, 10-testtube, 10b-testtube, 11-clipboard, 12-waving, 13-shush, 14-listening, 15-pointdown, 16-facepalm, 17-laughing, 18-panic, 19-victory, 20-magnifier, 21-presenting, 22-cross-x, 23-pouring.
Pass `(name, True)` to mirror a pose so Moon faces the middle when she is on the right.

## Prompts for the next episode
Write them with `references/prompts-template.md`: the ElevenLabs v4 voice script, 3 single 9:16 images, a 6-panel sheet, and 3 Flow videos, each using the image with the same number as its Start frame. Save them as `prompts-ep<n>.md` and also paste them into the chat.
