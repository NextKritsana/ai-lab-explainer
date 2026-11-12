"""Synthesize the channel's cyber / synthwave background track (no samples, no third-party audio, so no copyright issues).
  python3 tools/make_music.py [OUT.mp3] [--bpm 104] [--bars 16] [--seed 3] [--intro 2]
A minor, Am - F - C - G (2 bars each): detuned saw pad, 16th-note pluck arpeggio with ping-pong delay,
pulsing 8th-note saw bass ducked by the kick (sidechain feel), four-on-the-floor kick, clap on 2 and 4, offbeat hats.
Bars 1-2 are a short intro (pad + arp, --intro N to change); the full beat enters on bar 3; 16ths hats from bar 9. Loops cleanly for tools/mix.py
(it crossfades the loop if the video is longer). Default output: assets/music/cyber-bed.mp3."""
import os, subprocess, sys
import numpy as np

A = [x for x in sys.argv[1:] if not x.startswith("--")]
opt = {k[2:]: v for k, v in zip(sys.argv[1:], sys.argv[2:]) if k.startswith("--")}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = A[0] if A else os.path.join(ROOT, "assets", "music", "cyber-bed.mp3")
SR = 48000; BPM = float(opt.get("bpm", 104)); BARS = int(opt.get("bars", 16))
beat = 60 / BPM; bar = 4 * beat; N = int(BARS * bar * SR); INTRO = int(opt.get("intro", 2))
rng = np.random.default_rng(int(opt.get("seed", 3)))
hz = lambda m: 440 * 2 ** ((m - 69) / 12)

def ff(x, af):  # run a mono float signal through an ffmpeg audio filter
    p = subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "pipe:", "-af", af, "-f", "f32le", "-ac", "1", "pipe:"],
                       input=x.astype(np.float32).tobytes(), capture_output=True, check=True)
    y = np.frombuffer(p.stdout, np.float32).astype(np.float64)
    return np.pad(y, (0, max(0, len(x) - len(y))))[: len(x)]
def add(buf, x, t0, g=1.0):
    i = int(t0 * SR); j = min(len(buf), i + len(x))
    if i < len(buf): buf[i:j] += g * x[: j - i]
def saw(f, d, det=0.0):
    t = np.arange(int(d * SR)) / SR; ph = (f * (1 + det) * t) % 1.0
    return 2 * ph - 1
def env(n, a, r):
    t = np.arange(n) / SR; return np.minimum(t / max(a, 1e-4), 1) * np.exp(-t / r)

# Am - F - C - G, 2 bars each (pad voicings / bass roots / arp tones)
PAD = [[57, 60, 64, 69], [53, 57, 60, 65], [55, 60, 64, 67], [55, 59, 62, 67]]
ROOT_ = [33, 29, 36, 31]
ARP = [[69, 72, 76, 81, 76, 72], [65, 69, 72, 77, 72, 69], [67, 72, 76, 79, 76, 72], [67, 71, 74, 79, 74, 71]]

pad = np.zeros(N); arp = np.zeros(N); bass = np.zeros(N); kick = np.zeros(N); clap = np.zeros(N); hat = np.zeros(N); duck = np.ones(N)
for b in range(BARS):
    c = (b // 2) % 4; t0 = b * bar
    if b % 2 == 0:  # pad: 3 detuned saws per note, slow swell over 2 bars
        d = 2 * bar; n = int(d * SR); e = np.minimum(np.arange(n) / SR / 0.6, 1) * np.minimum((d - np.arange(n) / SR) / 0.4, 1)
        for m in PAD[c]:
            for det in (-0.004, 0, 0.0045): add(pad, saw(hz(m), d, det)[:n] * e, t0, 0.05)
    for s in range(16):  # arp: 16th plucks walking the chord tones
        m = ARP[c][s % len(ARP[c])]; n = int(beat / 4 * SR * 1.8)
        tone = (np.sign(np.sin(2 * np.pi * hz(m) * np.arange(n) / SR)) * 0.6 + saw(hz(m), n / SR)[:n] * 0.4) * env(n, 0.002, 0.09)
        add(arp, tone, t0 + s * beat / 4, 0.09 * (1.0 if s % 4 == 0 else 0.7))
    full = b >= INTRO
    for q in range(8):  # bass: pulsing 8ths on the root (octave up on the last 8th of each bar)
        m = ROOT_[c] + (12 if q == 7 else 0); n = int(beat / 2 * SR)
        add(bass, saw(hz(m), n / SR)[:n] * env(n, 0.004, 0.16), t0 + q * beat / 2, 0.22 if full else 0.12)
    if full:
        for q in range(4):  # kick + sidechain dip
            n = int(0.32 * SR); t = np.arange(n) / SR; f = 45 + 75 * np.exp(-t / 0.04)
            add(kick, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16), t0 + q * beat, 0.9)
            i = int((t0 + q * beat) * SR); k = int(0.22 * SR); duck[i:i + k] = np.minimum(duck[i:i + k], 0.35 + 0.65 * np.linspace(0, 1, len(duck[i:i + k])) ** 1.5)
        for q in (1, 3):  # clap
            n = int(0.2 * SR); add(clap, rng.standard_normal(n) * env(n, 0.001, 0.05), t0 + q * beat, 0.35)
        for e8 in range(8 if b < 8 else 16):  # hats: offbeat 8ths, then 16ths
            step = beat / 2 if b < 8 else beat / 4; n = int(0.05 * SR)
            strong = (e8 % 2 == 1) if b < 8 else (e8 % 4 == 2)
            add(hat, rng.standard_normal(n) * env(n, 0.0005, 0.012), t0 + e8 * step, 0.16 if strong else 0.07)

pad = ff(pad, "lowpass=f=1800,highpass=f=180,aecho=0.7:0.6:180|260:0.25|0.2,chorus=0.6:0.9:50:0.4:0.25:2")
arp = ff(arp, "lowpass=f=4200,aecho=0.8:0.7:" + f"{beat*750:.0f}|{beat*1500:.0f}:0.35|0.2")
bass = ff(bass, "lowpass=f=520") * duck
pad *= duck ** 0.5
clap = ff(clap, "bandpass=f=1600:w=1400,aecho=0.6:0.4:40:0.3")
hat = ff(hat, "highpass=f=7000")
kick = ff(kick, "lowpass=f=4000")
mix = pad + arp + bass + kick + clap + hat
mix = ff(mix, "acompressor=threshold=-18dB:ratio=3:attack=10:release=200,alimiter=limit=0.89")
mix /= max(1e-9, np.abs(mix).max()) / 0.89
# gentle fade at the very end so a loop seam is soft
n = int(0.08 * SR); mix[-n:] *= np.linspace(1, 0, n)
st = np.stack([mix, mix], 1).astype(np.float32)
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "pipe:", "-af", "extrastereo=m=1.6",
                "-b:a", "256k", OUT], input=st.tobytes(), check=True)
print(OUT, f"{BARS} bars @ {BPM:.0f} BPM = {N / SR:.1f}s")
