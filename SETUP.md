# Setup (for the AI to run)

The user opened this folder in Claude Code and typed something like "อ่าน SETUP.md แล้วติดตั้งให้หน่อย". Do the whole setup for them, one step at a time, in their language, without jargon. Before each step, check whether it already works and skip it if so.

1. **Package manager.** Homebrew on Mac; winget on Windows.
2. **Tools.** Run `brew install node git ffmpeg python` (Windows: winget Node.js, Git, FFmpeg, Python). `tools/contact.py` needs an ffmpeg that has `drawtext`. On Mac, `brew install ffmpeg-full` and run contact.py with `PATH=/opt/homebrew/opt/ffmpeg-full/bin:$PATH`.
3. **HyperFrames.** Run:
   - `claude plugin marketplace add https://github.com/heygen-com/hyperframes.git`
   - `claude plugin install hyperframes@hyperframes`
   - `npx hyperframes doctor`
   - `npx hyperframes browser ensure`
4. **Python environment.** Run `python3 -m venv ~/.venvs/ai-lab && ~/.venvs/ai-lab/bin/pip install numpy pillow scipy sherpa-onnx`. From now on, `PY=~/.venvs/ai-lab/bin/python`.
5. **Thai word timing.** Download `sherpa-onnx-zipformer-thai-2024-06-20.tar.bz2` from https://github.com/k2-fsa/sherpa-onnx/releases (tag `asr-models`) and unpack it into `~/asr/`.
6. **Previews and covers.** Run `npm i -g playwright && npx playwright install chromium`.
7. **Install the skill** so every new Claude Code session knows this look:
   - Mac: `mkdir -p ~/.claude/skills && cp -R <this folder> ~/.claude/skills/ai-lab-explainer`
   - Windows: copy the folder to `%USERPROFILE%\.claude\skills\ai-lab-explainer`.
8. **Self-test** (below). Then tell the user in 4 short lines how clips in this look are made, where the test clip is, and what to type next time: "ทำคลิปธีมห้องแล็บจากเสียงนี้", with a voice-over attached.

## Self-test
This rebuilds the bundled EP30 demo. Its voice-over is not included, so the test uses a silent track: the result has music and sound effects only.
```
python3 <skill>/engine/new_video.py ~/Desktop/edit-video/lab-test --example
cd ~/Desktop/edit-video/lab-test
ffmpeg -y -f lavfi -i anullsrc=r=48000:cl=mono -t 48.5 assets/audio/derived/vo-tight.wav
$PY tools/gen_body.py && $PY tools/build.py && node tools/wide.js "$PWD/index.html"
$PY tools/cues.py && $PY tools/mix.py && $PY tools/build.py
npx hyperframes render . -q draft -o renders/test.mp4
$PY tools/cover.py
```
The result should be about 49 s long and look like `example-output/ep30-frames.jpg`, with covers like `example-output/ep30-cover-v1.jpg`. Open it for the user.
