        // AI Security EP.30 timeline, lesson rank 7 (A2A). C[n] = cut where scene n+1 starts; P(n) = [start, end] of phrase n; W/T(n, "word") = spoken time.
        const C = [@CUTS];
        const DUR = @DUR;
        const NS = @NSCENES;
        const P = (n) => PH[n - 1];
        const fw = (n, w, fb) => T(n, w) ?? fb;
        for (let n = 1; n <= NS; n++) pushIn(n, Math.max(0, C[n - 1] - 0.4), Math.min(DUR, C[n] + 0.4), 1.05);
        tl.set(inner(1), { opacity: 1 }, 0);

        // paper boil: every sticker/card swaps edge frames at 8 fps
        for (let k = 0; k < DUR * 8; k++) tl.set("#root", { attr: { "data-f": k % 3 } }, k / 8);

        // ---------- host (.pz pose layers) ----------
        function hIn(n, t, end) {
          const h = S(n).querySelector(".host"), pz = h.querySelectorAll(".pz"), br = h.querySelector(".br");
          tl.set(pz[0], { opacity: 1 }, t);
          tl.fromTo(h, { y: 90, scale: 0.94, rotation: -2 }, { y: 0, scale: 1, rotation: 0, duration: 0.34, ease: "back.out(1.7)", immediateRender: false }, t);
          const reps = Math.max(1, Math.floor((end - t - 0.35) / 1.1));
          tl.fromTo(br, { scale: 1, rotation: 0 }, { scale: 1.015, rotation: 0.6, duration: 1.1, ease: "sine.inOut", yoyo: true, repeat: reps - 1, immediateRender: false }, t + 0.35);
          cue(t, "paper", 0.7);
        }
        function hPose(n, idx, t, sound = "flick") {
          const h = S(n).querySelector(".host");
          h.querySelectorAll(".pz").forEach((p, i) => tl.set(p, { opacity: i === idx ? 1 : 0 }, t));
          tl.fromTo(h, { y: 40, scale: 0.95 }, { y: 0, scale: 1, duration: 0.24, ease: "back.out(2.2)", immediateRender: false }, t);
          if (sound) cue(t, sound, 0.8);
        }
        function swap(a, b, t) { blurOut(a, t - 0.12, 0.16); tl.set(b, { opacity: 1 }, t); }
        function card(sel, t, sound = "paper", g = 0.9) { show(sel, t, 0.3, { y: 70, scale: 0.85 }, sound, g); }
        function sv(sel, t, d = 0.35, sound = "pencil") { tl.set(sel, { opacity: 1 }, t); draw(sel, t, d, sound); }
        function pop(sel, t, sound = "pop", g = 0.6) { show(sel, t, 0.26, { y: 30, scale: 0.6 }, sound, g); }
        function rstamp(sel, t, rot = -8, shakeCam = null) {  // rubber stamp thud (replaces the wax seal)
          tl.set(sel, { opacity: 0 }, 0);
          tl.fromTo(sel, { opacity: 0, scale: 2.2, rotation: rot - 10 }, { opacity: 0.92, scale: 1, rotation: rot, duration: 0.15, ease: "power4.in", immediateRender: false }, t);
          cue(t + 0.13, "stamp", 1); if (shakeCam) shake(shakeCam, t + 0.15, 7);
        }
        function count(sel, t, d, to, fmt = (v) => v.toLocaleString("en-US")) {
          const N = 14; for (let i = 0; i <= N; i++) tl.set(sel, { textContent: fmt(Math.round(to * Math.pow(i / N, 0.6))) }, t + d * i / N);
          cue(t, "tick", 0.7); cue(t + d, "stampsoft", 0.8);
        }
        function countdown(sel, t, end, from = 24 * 3600, step = 0.12) {  // hh:mm:ss ticking down fast (urgency)
          const f = (s) => [Math.floor(s / 3600), Math.floor(s / 60) % 60, s % 60].map((v) => String(v).padStart(2, "0")).join(":");
          for (let i = 0, s = from; t + i * step < end; i++, s--) { tl.set(sel, { textContent: f(s) }, t + i * step); if (i % 2 === 0) cue(t + i * step, "tick", 0.5); }
        }
        function lines(sel, t, gap = 0.18, sound = "key") { $$(sel).forEach((el, i) => { tl.set(el, { opacity: 0 }, 0); tl.set(el, { opacity: 1 }, t + i * gap); cue(t + i * gap, sound, 0.8); }); }

        // ---------- cyber transitions (0.2-0.4s) ----------
        const tSmudge = (n, cut) => { tBlur(n, cut); cue(cut - 0.16, "shh", 0.5); };
        const tPage = (n, cut) => tSlide(n, cut);
        function tErase(n, cut) {  // wipe left to right
          tl.set(inner(n), { opacity: 1 }, cut - 0.18);
          tl.fromTo(inner(n), { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 0.36, ease: "power2.inOut", immediateRender: false }, cut - 0.18);
          tl.set(inner(n), { clipPath: "none" }, cut + 0.19); tl.set(inner(n - 1), { opacity: 0 }, cut + 0.19);
          cue(cut - 0.18, "scratch", 0.8);
        }
        function tGlitch(n, cut) {  // RGB-split jitter, scanline bands, hard switch on the cut
          const a = inner(n - 1), b = inner(n), J = [[-28, 0], [22, 0], [-12, 0], [34, 0], [0, 0]];
          J.forEach(([x], i) => { tl.set(a, { x, filter: `drop-shadow(${-x / 2}px 0 0 rgba(224,57,62,.7)) drop-shadow(${x / 2}px 0 0 rgba(28,159,214,.7))` }, cut - 0.2 + i * 0.04); });
          tl.set(a, { x: 0, filter: "none", opacity: 0 }, cut); tl.set(b, { opacity: 1 }, cut);
          [[-20], [14], [0]].forEach(([x], i) => tl.set(b, { x, filter: x ? `drop-shadow(${x / 2}px 0 0 rgba(224,57,62,.7)) drop-shadow(${-x / 2}px 0 0 rgba(28,159,214,.7))` : "none" }, cut + i * 0.04));
          [[.9, -.2], [0, -.12], [.7, -.06], [0, .04], [.5, .08], [0, .14]].forEach(([o, dt]) => tl.set("#glitch", { opacity: o }, cut + dt));
          cue(cut - 0.2, "static", 0.8);
        }
        function tScan(n, cut) {  // a cyan scan line sweeps down and reveals the new page behind it
          tl.set(inner(n), { opacity: 1 }, cut - 0.2);
          tl.fromTo(inner(n), { clipPath: "inset(0 0 100% 0)" }, { clipPath: "inset(0 0 0% 0)", duration: 0.38, ease: "power1.inOut", immediateRender: false }, cut - 0.2);
          tl.fromTo("#scan", { opacity: 1, y: -30 }, { y: 1920, duration: 0.38, ease: "power1.inOut", immediateRender: false }, cut - 0.2);
          tl.set("#scan", { opacity: 0 }, cut + 0.19); tl.set(inner(n), { clipPath: "none" }, cut + 0.19); tl.set(inner(n - 1), { opacity: 0 }, cut + 0.19);
          cue(cut - 0.2, "whoosh", 0.4); cue(cut - 0.18, "beep", 0.35);
        }
        function tBlackout(n, cut) {  // screen goes dark like a power cut, then the new page boots up
          tl.fromTo("#dark", { opacity: 0 }, { opacity: 1, duration: 0.14, ease: "power2.in", immediateRender: false }, cut - 0.16);
          tl.set(inner(n), { opacity: 1 }, cut); tl.set(inner(n - 1), { opacity: 0 }, cut);
          tl.to("#dark", { opacity: 0, duration: 0.34, ease: "power2.out" }, cut + 0.02);
          tl.fromTo(inner(n), { filter: "brightness(1.6) contrast(1.3)" }, { filter: "brightness(1) contrast(1)", duration: 0.4, ease: "power2.out", immediateRender: false }, cut + 0.02);
          cue(cut - 0.16, "click", 0.8); cue(cut, "crt", 0.5);
        }
        function tAlert(n, cut) {  // red alert pulse + white flash on the cut
          tl.fromTo("#alert", { opacity: 0 }, { opacity: 1, duration: 0.12, ease: "power2.in", immediateRender: false }, cut - 0.12);
          tl.to("#alert", { opacity: 0, duration: 0.4, ease: "power2.out" }, cut + 0.02);
          flash(cut - 0.02, 0.6); tl.set(inner(n), { opacity: 1 }, cut); tl.set(inner(n - 1), { opacity: 0 }, cut);
          cue(cut - 0.12, "wrong", 0.5);
        }
        function tIris(n, cut) {  // a circle opens from the centre onto the new page
          tl.set(inner(n), { opacity: 1 }, cut - 0.2);
          tl.fromTo(inner(n), { clipPath: "circle(0% at 50% 50%)" }, { clipPath: "circle(80% at 50% 50%)", duration: 0.38, ease: "power2.in", immediateRender: false }, cut - 0.2);
          tl.set(inner(n), { clipPath: "none" }, cut + 0.19); tl.set(inner(n - 1), { opacity: 0 }, cut + 0.19);
          cue(cut - 0.2, "whoosh", 0.6); cue(cut + 0.1, "crt", 0.4);
        }
        function tZoom(n, cut) {  // fly through the old page into the new one
          tl.to(inner(n - 1), { scale: 2.6, opacity: 0, filter: "blur(10px)", duration: 0.3, ease: "power2.in" }, cut - 0.22);
          tl.set(inner(n - 1), { scale: 1, filter: "none" }, cut + 0.1);
          tl.fromTo(inner(n), { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.32, ease: "power3.out", immediateRender: false }, cut - 0.06);
          cue(cut - 0.22, "whoosh", 0.8);
        }
        function tDoors(n, cut) {  // the new page opens from the centre like two gate doors
          tl.set(inner(n), { opacity: 1 }, cut - 0.2);
          tl.fromTo(inner(n), { clipPath: "inset(0 50% 0 50%)" }, { clipPath: "inset(0 0% 0 0%)", duration: 0.36, ease: "power3.inOut", immediateRender: false }, cut - 0.2);
          tl.set(inner(n), { clipPath: "none" }, cut + 0.17); tl.set(inner(n - 1), { opacity: 0 }, cut + 0.17);
          cue(cut - 0.2, "whoosh", 0.6); cue(cut + 0.12, "lock", 0.5);
        }
        function tFile(n, cut) {  // case files: the next page slides up like a folder pulled from the drawer
          tl.set(inner(n), { opacity: 1 }, cut - 0.22);
          tl.fromTo(inner(n), { y: 1920, rotation: 4 }, { y: 0, rotation: 0, duration: 0.4, ease: "power3.out", immediateRender: false }, cut - 0.22);
          tl.set(inner(n - 1), { opacity: 0 }, cut + 0.2); cue(cut - 0.22, "paper", 0.9); cue(cut + 0.1, "slide", 0.5);
        }
        function tPhoto(n, cut) {  // case files: camera flash + shutter, hard switch under the white
          flash(cut - 0.05, 0.3); tl.set(inner(n), { opacity: 1 }, cut); tl.set(inner(n - 1), { opacity: 0 }, cut); cue(cut - 0.07, "shutter", 1);
        }
        function ring(sel, t, to = 2.6, d = 0.7) { tl.fromTo(sel, { opacity: 0.95, scale: 0.4 }, { opacity: 0, scale: to, duration: d, ease: "power2.out", immediateRender: false }, t); }
        // never the same one twice in a row
        const TR = { 2: tZoom, 3: tSlide, 4: tBlackout, 5: tGlitch, 6: tScan, 7: tDoors, 8: tAlert, 9: tErase, 10: tSmudge, 11: tIris };
        for (let n = 2; n <= NS; n++) TR[n](n, C[n - 1]);
        const TY = (n) => typeIn("#" + sid(n), "tick");
        // lab bubbles drift up in every scene
        for (let n = 1; n <= NS; n++) S(n).querySelectorAll(".bub").forEach((b, j) => tl.fromTo(b, { y: 0, x: 0 }, { y: -420 - (j % 4) * 140, x: j % 2 ? 30 : -30, duration: C[n] - C[n - 1] + 0.9, ease: "none", immediateRender: false }, Math.max(0, C[n - 1] - 0.45)));

        // 01 hook VIDEO (source 0.4): the note slides along the chat; Moon opens RIGHT, listening in (new opening)
        hIn(1, 0.0, C[1]); cue(0.05, "stamp", 0.6);
        $$("#s01 .tz > *").forEach((el, i) => tl.fromTo(el, { scale: 1.14 }, { scale: 1, duration: 0.5, ease: "elastic.out(1, 0.5)", immediateRender: false }, 0.05 + i * 0.1));
        cue(0.8, "pop", 0.5); cue(1.8, "shh", 0.5); cue(3.2, "pop", 0.4);
        hPose(1, 1, fw(1, "กระซิบ", 2.6));
        const t1 = fw(2, "รู้ไหม", 4.6); hPose(1, 2, t1 - 0.2); cue(t1, "ding", 0.5);

        // 02 A2A
        TY(2); hIn(2, C[1] + 0.2, C[2]); inPic("#s02-im", C[1] + 0.05, { y: 700, rotation: -5 }, "thud", 0.7);
        const t2 = fw(3, "A2A", 6.9); cue(t2, "ping", 0.7); hPose(2, 1, fw(3, "แชต", 8.9) - 0.2);

        // 03 believes anyone
        TY(3); hIn(3, C[2] + 0.2, C[3]); inPic("#s03-im", C[2] + 0.05, { x: -1100 }, "whoosh", 0.8);
        pop("#s03-b0", fw(4, "ใครก็ได้", 11.9) - 0.1, "pop", 0.6);
        const t3 = fw(4, "ทุกคำ", 13.6); pop("#s03-b1", t3 - 0.2, "pop", 0.6); hPose(3, 1, t3);

        // 04 cliffhanger (dark page): Unit 42
        TY(4); hIn(4, C[3] + 0.25, C[4]); inPic("#s04-im", C[3] + 0.05, { scale: 1.2 }, "thunder", 0.4);
        hPose(4, 1, fw(5, "Unit", 16.2)); cue(fw(5, "Unit", 16.2), "ping", 0.5);

        // 05 VIDEO dark (source 1.2 at 16.94): coins pour out, flash near the end
        TY(5); hIn(5, C[4] + 0.15, C[5]);
        cue(fw(6, "แทรก", 18.9), "static", 0.5); cue(19.6, "clink", 0.6); cue(20.6, "clink", 0.5);
        const t5 = fw(6, "ซื้อหุ้น", 21.0); cue(t5, "ding", 0.6); hPose(5, 1, t5);
        rstamp("#s05-st", fw(6, "ไม่รู้ตัว", 22.4) - 0.2, -6, cam(5));

        // 06 A2ABreak 11 flaws
        TY(6); hIn(6, C[5] + 0.15, C[6]); inPic("#s06-im", C[5] + 0.03, { scale: 0.6, rotation: 6 }, "pop", 0.7);
        const t6 = fw(7, "สิบเอ็ด", 27.2) - 0.1; rstamp("#s06-st", t6, -7, cam(6)); count("#s06-n", t6, 0.4, 11); hPose(6, 1, t6);

        // 07 name it
        TY(7); hIn(7, C[6] + 0.2, C[7]); inPic("#s07-im", C[6] + 0.05, { y: 700 }, "thud", 0.7);
        const t7 = fw(8, "Insecure", 28.9); cue(t7, "ping", 0.8);
        const t7b = fw(8, "อันดับ", 30.6); pop("#s07-ow", t7b - 0.1, "tick", 0.7); hPose(7, 1, t7b);

        // 08 reveal VIDEO (source 2.6 at 31.35): the mask falls off, then the push
        TY(8); hIn(8, C[7] + 0.15, C[8]);
        const t8 = fw(9, "แต่มาจาก", 33.4); shake(cam(8), t8, 7); cue(t8, "wrong", 0.6); hPose(8, 1, t8 + 0.2, null);
        cue(fw(9, "ไว้ใจ", 34.8), "thud", 0.6);

        // 09 fix
        TY(9); hIn(9, C[8] + 0.2, C[9]); inPic("#s09-im", C[8] + 0.05, { x: -1100 }, "whoosh", 0.7);
        pop("#s09-b0", fw(11, "ลายเซ็น", 38.2) - 0.2, "stampsoft", 0.7);
        const t9 = fw(11, "กดยืนยัน", 40.1); pop("#s09-b1", t9 - 0.2, "lock", 0.7); hPose(9, 1, t9);

        // 10 question
        TY(10); hIn(10, C[9] + 0.2, C[10]); inPic("#s10-im", C[9] + 0.05, { scale: 0.4, rotation: 10 }, "pop", 0.7);
        const t10 = fw(14, "คอมเมนต์", 44.4) - 0.3; hPose(10, 1, t10); cue(t10, "ding", 0.6);

        // 11 follow
        TY(11); hIn(11, C[10] + 0.1, C[11]);
        const t11 = fw(15, "ติดตาม", 45.4) + 0.1; hPose(11, 1, t11); pop("#s11-btn", t11, "ding", 0.8);
        tl.to("#s11-btn", { scale: 1.12, duration: 0.18, yoyo: true, repeat: 5, ease: "sine.inOut" }, t11 + 0.4);
        hPose(11, 2, fw(15, "มูนมี", 47.3) - 0.4); show("#s11-src", DUR - 1.7, 0.3, { y: 10 }, null, 0);
        tl.to(inner(11), { opacity: 0, duration: 0.35, ease: "power1.in" }, DUR - 0.35);

        // ---------- keep every illustration alive (on the inner .lv layer, so the scene moves above still work) ----------
        // land squash after the entrance, a slow float + tilt the whole scene, and a punch (zoom-kick + wobble + sound) on every new sentence
        const QUIET = ["tick", "blip", "key", "paper", "flick", "pencil"];
        const BUSY = cues.filter((c) => !QUIET.includes(c[1])).map((c) => c[0]);
        const KICK = ["pop", "whoosh", "thud", "snap", "slap"];
        let kick = 0;
        for (let n = 1; n <= NS; n++) {
          const lvs = Array.from(S(n).querySelectorAll(".cut .lv"));
          const a = n === 1 ? 0 : C[n - 1] + 0.5, b = C[n] - 0.25;
          tl.fromTo(cam(n), { rotation: n % 2 ? -0.6 : 0.6 }, { rotation: n % 2 ? 0.6 : -0.6, duration: C[n] - C[n - 1] + 0.4, ease: "sine.inOut", immediateRender: false }, Math.max(0, C[n - 1] - 0.2));
          if (!lvs.length) continue;
          lvs.forEach((lv, i) => {
            if (n > 1) tl.fromTo(lv, { scaleX: 1.1, scaleY: 0.88 }, { scaleX: 1, scaleY: 1, duration: 0.45, ease: "elastic.out(1, 0.4)", immediateRender: false }, a - 0.05);
            const per = 1.25, reps = Math.max(1, Math.floor((b - a) / per));
            tl.fromTo(lv, { y: 0, rotation: i % 2 ? 1.5 : -1.5 }, { y: -16, rotation: i % 2 ? -1.5 : 1.5, duration: per, ease: "sine.inOut", yoyo: true, repeat: reps - 1, immediateRender: false }, a);
          });
          const ts = PH.map((p) => p[0]).filter((t) => t > a + 0.45 && t < b - 0.2);
          const pts = [a, ...ts, b], beats = [...ts];
          for (let k = 0; k < pts.length - 1; k++) { const g = pts[k + 1] - pts[k]; if (g > 2.2) { const m = Math.floor(g / 1.6); for (let j = 1; j <= m; j++) beats.push(pts[k] + (g * j) / (m + 1)); } }
          beats.sort((x, y) => x - y).forEach((t) => {
            if (BUSY.some((u) => Math.abs(u - t) < 0.3)) return;
            lvs.forEach((lv) => {
              tl.fromTo(lv, { scale: 1 }, { scale: 1.1, duration: 0.07, ease: "power2.out", immediateRender: false }, t);
              tl.to(lv, { scale: 1, duration: 0.4, ease: "elastic.out(1, 0.4)" }, t + 0.07);
              [12, -9, 6, -3, 0].forEach((x, i) => tl.to(lv, { x, duration: 0.035, ease: "none" }, t + i * 0.035));
            });
            cue(t, KICK[kick++ % KICK.length], 0.45);
          });
        }
