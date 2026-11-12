# AI Lab look: style spec

## Frame
- 1080x1920, 30 fps.
- **Safe zones.** Keep the top 140 px, the bottom 220 px and the right 120 px free of key text, because the Reels UI covers them.
- **Headline zone.** `.tz`, top 150 px, height 440 px. Use 1-3 lines:
  - `.lab` pill: violet; `.lab.m` mint; `.lab.p` red.
  - `.s`: small lead-in line.
  - `.h`: big line; `.h.m` mint underline; `.h.r` pink-red.
- **Picture zone.** y 560-1200.
- **Host zone.** Bottom corners, from y about 1040. `hsp(..., top)` sits lower so only Moon's upper body shows.

## Page and colour
| token | hex | use |
|---|---|---|
| mint | #3FD1A6 | good, highlight, buttons |
| violet | #6A4BB0 | labels, ink doodles |
| pink-red | #E8475F | danger, the twist |
| gold | #F7D23E | sparkles, numbers |
| navy | #1E2533 | ink, outlines, text |
| ground | #F3FBF8 | page base |

- `.pg` is the mint grid notebook page. `.pg.dk` is the lavender "something is wrong" page.
- Margin doodles (flasks, test tubes, bubbles, "pH 7", "EXP.01") come from `props.js`, and are seeded per scene.

## Motion
- **Pace.** A scene change every 3-6 s, and a visual beat at least every 1-1.5 s: a pose change, a pop, a stamp or a kick.
- **Pictures.** They land with a squash, then float (±16 px, ±1.5°) and kick (scale 1.1 + wobble + sound) on every new sentence.
- **Host.** Moon pops in with a back-ease, then breathes (scale 1.015). Change her pose with `hPose` on a spoken word.
- **Camera.** The camera slowly tilts ±0.6° per scene. Add `shake(cam(n))` on stamps and reveals.
- **Transitions.** Use a different one every cut: tZoom, tSlide, tBlackout (into a dark page), tGlitch, tScan, tDoors, tAlert, tErase, tSmudge, tIris.

## Type
- Kanit ExtraBold for headlines (76-110 px) and stamps.
- Mali for bubbles and small lines.
- JetBrains Mono for chips, numbers and sources.
- Thai lines of 14 characters or fewer read best on a phone.

## Sound
- **Music.** `bg-music.mp3` is ducked about 7 dB under the voice.
- **VO.** +7 dB.
- **SFX.** All synthesized: pop, whoosh, thud, stamp, stampsoft, ping, ding, tick, key, paper, flick, lock, clink, static, crt, wrong, thunder, shh, slap, snap, rise, flash.
- **Master.** About -13 LUFS / -1.5 dBTP.

## Covers
- Light mint page and ONE big subject: a cute robot plus one everyday object.
- A 2-line title ending in "…ได้ไหม?", with no jargon.
- Moon big in a corner, plus at most one stamp or bubble.
- v2 may use the lavender page.
- Change the layout and poses every episode.
