"""Cut the short "hook" clip (about 20 s) from the opening of the rendered full clip, ending on a cliffhanger phrase.
The short clip is the first scenes of the full clip as they are (same voice, music and pictures), cut right after the
phrase you pick, with the last frame held and the sound faded out. No new voice-over is needed.

  python3 tools/hook_cut.py "renders/EP<n> <title>.mp4" <last phrase number> ["renders/EP<n> สตอรี่ hook <title>.mp4"]

- Pick the last phrase so the clip is about 18-22 s and stops on a cliffhanger: after the hook, the promise, the
  explanation and the first proof, before the result stamp and the fix (EP10: phrase 8 "เกือบทุกครั้ง", 21.7 s).
- The picture stops 0.12 s before the next scene's cut (so no transition leaks in) and holds for 0.95 s; the sound stops
  0.1 s after the phrase ends (before the next phrase starts) with a short fade.
- Also writes the "-small" copy at 3 Mbps.
"""
import json, os, subprocess, sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src, last = sys.argv[1], int(sys.argv[2])
out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(src), os.path.basename(src).replace(" ", " สตอรี่ hook ", 1))
ph = json.load(open(os.path.join(R, "transcript.json"), encoding="utf-8"))["phrases"]
cuts = json.load(open(os.path.join(R, "cuts.json")))["cuts"]
end_ph = ph[last - 1]["end"]
nxt_ph = ph[last]["start"] if last < len(ph) else end_ph + 0.3
nxt_cut = min([c for c in cuts if c > end_ph - 0.05] or [end_ph + 0.2])
v_end = min(nxt_cut - 0.12, end_ph + 0.3)
a_end = min(end_ph + 0.1, nxt_ph - 0.04)
hold = 0.95
total = v_end + hold
f = (f"[0:v]trim=0:{v_end:.3f},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={hold}[v];"
     f"[0:a]atrim=0:{a_end:.3f},asetpts=PTS-STARTPTS,afade=t=out:st={a_end - 0.08:.3f}:d=0.08,apad=whole_dur={total:.3f}[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", f, "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", out], check=True)
small = out[:-4] + "-small.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-c:v", "libx264", "-b:v", "3M", "-maxrate", "3.5M", "-bufsize", "6M",
                "-c:a", "aac", "-b:a", "160k", small], check=True)
print(f"{out}  {total:.1f} s (picture to {v_end:.2f}, sound to {a_end:.2f}, ends on phrase {last}: {ph[last - 1]['text']})")
print(small)
if not 17 <= total <= 23: print("warning: aim for about 18-22 s; pick another last phrase")
