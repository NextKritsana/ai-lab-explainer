# Prompts template for one episode

Give these to the user in chat and save them as `prompts-ep<n>.md`. Replace everything in <angle brackets>.

## 1. Voice-over (ElevenLabs v4, about 720 Thai characters ≈ 48 s after atempo 1.2)
One line per beat. Tags in [brackets] set the delivery. Write English names as words people say ("A2A", "OWASP"), and numbers the way they should be read.
```
[curious] ถ้า <everyday situation> แล้ว <the twist> คุณจะรู้ไหมคะ?
[explaining] <what the thing is, in everyday words, with a comparison>
[explaining] ปัญหาคือ <the weak point>
[ominous] แต่ที่น่ากลัวกว่านั้นคือ <who> ทดลอง/พบว่า <what happened, concrete>
[surprised] <date> <second proof with a number>
[serious] นี่คือ <official name> อันดับ <n> ของ OWASP
[surprised] <the reveal line, one sentence>
[serious] วิธีกันคือ <fix 1> และ <fix 2>
[teasing, curious] <question to the viewer> ตอบมูนในคอมเมนต์เลย
[playful, cheerful] กดติดตามไว้ เรื่อง AI ที่คุณไม่รู้ มูนมีมาเล่าอีกค่ะ
```

## 2. Style line (end every image prompt with it)
```
Hand-drawn science lab notebook look, ink lines with soft watercolour, colours mint #3FD1A6, violet #6A4BB0, pink-red #E8475F, gold #F7D23E, navy #1E2533, small ink test tubes and sparkles. AI robots = cute rounded robots with one big round camera-lens eye and small headphone ears. No text, no letters.
```

## 3. Three single images, 9:16
- **Image 1 (hook):** the whole story in one picture, light page. Keep the LOWER-LEFT quarter empty, because Moon stands there.
- **Image 2 (dark):** a dark lab room with one spotlight, for the cliffhanger or proof.
- **Image 3 (reveal):** the twist in one picture, light page. Keep the LOWER-LEFT quarter empty.

## 4. Six-panel sheet
```
Sticker sheet, 3 columns x 2 rows, pure white background, no card or paper behind, each item separated by white space. <style line>
1 <what-it-is picture>  2 <the weak point>  3 <the attack>
4 <the proof/number>    5 <the fix>         6 <the viewer question>
```
Ask for the 2K or 4K download. Panels smaller than about 500 px look soft once cropped.

## 5. Three Flow videos (8 s, no speech)
The Start frame is the image with the same number: V1 = image 1, V2 = image 2, V3 = image 3. Describe only motion from that frame. Never describe a new scene, or the clip will not match the picture.
```
V1: <slow push-in, the key object moves along, small sparkles>. No text.
V2: <dark spotlight scene: the bad thing happens, a flash at the end>. No text.
V3: <the reveal motion: mask falls, door opens, etc.>. No text.
```

## 6. Captions
Long clip:
```
🧪 ห้องแล็บ AI: <title>
<2-3 short lines with the verified facts>
วิธีกันมีในคลิป 🛡️
<comment question> ตอบมูนในคอมเมนต์ 👇
📚 ที่มา: <source 1 (month year)> · <source 2> · OWASP Top 10 for Agentic Applications (ASIxx)
#AISecurity #ห้องแล็บAI #AIAgent #รู้ทันAI #OWASP
```
Short clip:
```
<one line story with the twist> <emoji>
วิธีกันดูในคลิปเต็ม EP.<n> บนเพจเลย 👉
#ห้องแล็บAI #AISecurity
```
