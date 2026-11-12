        // ---------- Cyber Sketch props: navy ink line (.ink) + watercolour fills, red / cyan marker (.mk), wobble via #rough, wash via #wc ----------
        // Use: <div class="svg" data-svg="name" style="..."></div>. Paths draw on with draw(sel, t). Names: see assets/props/PROPS.md.
        const PI = 'class="ink"', PT = 'class="ink" stroke-width="3"';
        const CH = (w = 12) => `class="mk" stroke-width="${w}" filter="url(#chalkf)"`;            // red marker
        const CY = (w = 12) => `class="mk cy" stroke-width="${w}" filter="url(#chalkf)"`;         // cyan marker
        const G = (s) => `<g filter="url(#wc)"><g filter="url(#rough)">${s}</g></g>`;
        const K = { ink: "#1E2533", soft: "#5B6577", red: "#E0393E", cyan: "#1C9FD6", glow: "#5FD8FF", violet: "#6A4BB0", amber: "#F0A21B",
          gold: "#F3C04A", paper: "#FBFAF6", steel: "#C9D2DB", steel2: "#9AA7B5", green: "#6FB585", green2: "#3E8A5A", term: "#1B222C", term2: "#2A3442", skin: "#E9C6A8" };
        const lockBody = (x, y, w, h, col) => `<rect ${PI} x="${x}" y="${y}" width="${w}" height="${h}" rx="18" fill="${col}"/>
            <circle cx="${x + w / 2}" cy="${y + h * .42}" r="${h * .1}" fill="${K.ink}"/><path ${PI} d="M${x + w / 2} ${y + h * .45} L${x + w / 2} ${y + h * .7}" stroke-width="9"/>
            <path d="M${x + 16} ${y + 18} L${x + 16} ${y + h - 22}" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".55"/>`;
        const SV = {
          // ---- hardware ----
          ram: () => `<svg viewBox="0 0 420 170">${G(`<path ${PI} d="M14 20 L406 20 L406 128 L250 128 L250 140 L226 140 L226 128 L14 128 Z" fill="${K.green}"/>
            ${[40, 128, 260, 348].map((x) => `<rect ${PI} x="${x}" y="40" width="58" height="50" rx="5" fill="${K.term2}"/>`).join("")}
            <path d="M30 32 L390 32" stroke="#fff" stroke-width="4" opacity=".35"/>
            ${Array.from({ length: 30 }, (_, i) => `<path d="M${24 + i * 12.6} 128 L${24 + i * 12.6} 156" stroke="${K.gold}" stroke-width="6"/>`).join("")}
            <path ${PI} d="M14 128 L406 128 L406 160 L14 160 Z" fill="none"/>`)}</svg>`,
          hdd: () => `<svg viewBox="0 0 300 380">${G(`<rect ${PI} x="20" y="16" width="260" height="348" rx="22" fill="${K.steel}"/>
            <circle ${PI} cx="150" cy="150" r="96" fill="#E6ECF1"/><circle ${PT} cx="150" cy="150" r="64" fill="none"/><circle cx="150" cy="150" r="14" fill="${K.ink}"/>
            <path ${PI} d="M232 300 L176 168" stroke-width="12"/><circle ${PI} cx="232" cy="304" r="16" fill="${K.steel2}"/>
            <path ${PT} d="M54 300 L130 300 M54 324 L110 324"/>${[[40, 36], [260, 36], [40, 344], [260, 344]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="6" fill="${K.ink}"/>`).join("")}
            <path d="M92 112 Q112 84 146 80" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".7"/>`)}</svg>`,
          server: () => `<svg viewBox="0 0 280 420">${G(`<rect ${PI} x="30" y="14" width="220" height="392" rx="16" fill="${K.steel}"/>
            ${[40, 130, 220, 310].map((y) => `<rect ${PI} x="52" y="${y}" width="176" height="70" rx="8" fill="#E4EAF0"/><circle cx="82" cy="${y + 35}" r="9" fill="${K.green2}"/><circle cx="110" cy="${y + 35}" r="9" fill="${K.amber}"/>
              <path ${PT} d="M140 ${y + 24} L210 ${y + 24} M140 ${y + 36} L210 ${y + 36} M140 ${y + 48} L210 ${y + 48}"/>`).join("")}`)}</svg>`,
          monitor: (c) => `<svg viewBox="0 0 440 400">${G(`<rect ${PI} x="16" y="16" width="408" height="276" rx="20" fill="${K.steel}"/>
            <rect ${PI} x="40" y="38" width="360" height="230" rx="10" fill="${c === "ok" ? K.term : K.red}"/>
            <path ${PI} d="M190 292 L176 350 L264 350 L250 292" fill="${K.steel2}"/><path ${PI} d="M120 356 L320 356" stroke-width="10"/>
            ${c === "ok" ? `<path d="M80 90 L110 90 M80 120 L200 120 M80 150 L170 150" stroke="${K.green}" stroke-width="10" stroke-linecap="round"/>`
              : `<rect ${PI} x="178" y="98" width="84" height="66" rx="10" fill="${K.gold}"/><path ${PI} d="M196 98 L196 80 Q220 52 244 80 L244 98" fill="none" stroke-width="9"/>
              <text x="220" y="230" text-anchor="middle" font-family="JBMono, monospace" font-weight="800" font-size="46" fill="#FFE9A8" stroke="${K.ink}" stroke-width="2">00:59:59</text>`}`)}</svg>`,
          laptop: () => `<svg viewBox="0 0 440 300">${G(`<rect ${PI} x="70" y="20" width="300" height="200" rx="14" fill="${K.steel}"/><rect ${PI} x="90" y="40" width="260" height="162" rx="6" fill="${K.term}"/>
            <path ${PI} d="M20 232 L420 232 L396 270 L44 270 Z" fill="${K.steel2}"/><path d="M110 70 L140 70 M110 98 L230 98 M110 126 L200 126" stroke="${K.green}" stroke-width="9" stroke-linecap="round"/>`)}</svg>`,
          phone: () => `<svg viewBox="0 0 220 400">${G(`<rect ${PI} x="20" y="14" width="180" height="372" rx="30" fill="${K.term2}"/><rect ${PI} x="36" y="52" width="148" height="290" rx="10" fill="#EAF3F8"/>
            <path ${PI} d="M88 32 L132 32" stroke-width="7"/><rect x="52" y="76" width="116" height="62" rx="10" fill="${K.cyan}" opacity=".85"/><path ${PT} d="M58 168 L160 168 M58 196 L140 196 M58 224 L150 224"/>`)}</svg>`,
          usb: () => `<svg viewBox="0 0 200 380">${G(`<rect ${PI} x="40" y="120" width="120" height="244" rx="22" fill="${K.violet}"/><rect ${PI} x="62" y="20" width="76" height="102" fill="${K.steel}"/>
            <rect x="78" y="44" width="16" height="16" fill="${K.ink}"/><rect x="106" y="44" width="16" height="16" fill="${K.ink}"/><path d="M62 150 L62 330" stroke="#fff" stroke-width="7" opacity=".4" stroke-linecap="round"/>`)}</svg>`,
          plug: () => `<svg viewBox="0 0 300 360">${G(`<path ${PI} d="M150 250 Q150 330 70 352" fill="none" stroke-width="16"/><path d="M150 250 Q150 330 70 352" stroke="${K.term2}" stroke-width="8" fill="none"/>
            <rect ${PI} x="80" y="110" width="140" height="150" rx="26" fill="${K.term2}"/><path ${PI} d="M120 110 L120 30 M180 110 L180 30" stroke-width="18"/>
            <path d="M120 110 L120 34 M180 110 L180 34" stroke="${K.gold}" stroke-width="9" stroke-linecap="round"/><path d="M100 132 L100 236" stroke="#fff" stroke-width="7" opacity=".3" stroke-linecap="round"/>`)}</svg>`,
          cable: () => `<svg viewBox="0 0 420 260">${G(`<path ${PI} d="M10 200 Q140 230 230 150" fill="none" stroke-width="22"/><path d="M10 200 Q140 230 230 150" stroke="${K.amber}" stroke-width="12" fill="none"/>
            <path ${PI} d="M216 104 L300 60 L362 150 L282 196 Z" fill="#E9F2F7" fill-opacity=".9"/><path ${PT} d="M300 80 L338 140 M316 72 L352 130 M286 92 L324 152"/>
            <path d="M380 70 l20 -16 M392 96 l26 -2 M372 46 l6 -24" stroke="${K.cyan}" stroke-width="7" stroke-linecap="round"/>`)}</svg>`,
          wifi: () => `<svg viewBox="0 0 300 240">${G(`<path ${PI} d="M30 96 Q150 -10 270 96" fill="none" stroke-width="18"/><path ${PI} d="M74 140 Q150 72 226 140" fill="none" stroke-width="18"/>
            <path ${PI} d="M118 182 Q150 152 182 182" fill="none" stroke-width="18"/><circle cx="150" cy="214" r="16" fill="${K.ink}"/>`)}</svg>`,
          cloud: () => `<svg viewBox="0 0 360 240">${G(`<path ${PI} d="M80 200 Q20 200 24 150 Q30 104 82 108 Q90 40 160 42 Q226 44 238 102 Q300 92 320 140 Q338 200 270 200 Z" fill="#DDF1FA"/>
            <path d="M70 140 Q76 124 96 122" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".8"/>`)}</svg>`,
          // ---- security ----
          lock: () => `<svg viewBox="0 0 240 300">${G(`<path ${PI} d="M64 130 L64 86 Q64 24 120 24 Q176 24 176 86 L176 130" fill="none" stroke-width="22"/>
            <path d="M64 130 L64 86 Q64 24 120 24 Q176 24 176 86 L176 130" fill="none" stroke="${K.steel}" stroke-width="12"/>${lockBody(30, 126, 180, 156, K.gold)}`)}</svg>`,
          unlock: () => `<svg viewBox="0 0 280 300">${G(`<path ${PI} d="M64 130 L64 86 Q64 24 120 24 Q176 24 180 70" fill="none" stroke-width="22"/>
            <path d="M64 130 L64 86 Q64 24 120 24 Q176 24 180 70" fill="none" stroke="${K.steel}" stroke-width="12"/>${lockBody(30, 126, 180, 156, "#BFE6F5")}`)}</svg>`,
          key: () => `<svg viewBox="0 0 200 380">${G(`<circle ${PI} cx="100" cy="88" r="66" fill="${K.gold}"/><circle ${PI} cx="100" cy="74" r="20" fill="${K.paper}"/>
            <path ${PI} d="M100 154 L100 346" stroke-width="30"/><path d="M100 154 L100 344" stroke="${K.gold}" stroke-width="18"/>
            <path ${PI} d="M100 272 L146 272 M100 318 L136 318" stroke-width="24"/><path d="M100 272 L144 272 M100 318 L134 318" stroke="${K.gold}" stroke-width="12"/>
            <path d="M62 56 Q72 34 96 30" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".7"/>`)}</svg>`,
          bug: () => `<svg viewBox="0 0 320 320">${G(`${[-1, 1].map((s) => [[-40, -50, -90, -110], [-16, -58, -110, -40], [10, -56, -110, 40], [40, -50, -96, 112]].map(([dy, x1, x2, y2]) =>
              `<path ${PI} d="M${160 + s * 40} ${170 + dy} L${160 + s * (-x1)} ${170 + dy - 10} L${160 + s * (-x2 + 30)} ${170 + y2}" fill="none"/>`).join("")).join("")}
            <ellipse ${PI} cx="160" cy="190" rx="62" ry="80" fill="${K.term2}"/><circle ${PI} cx="160" cy="98" r="40" fill="${K.term}"/>
            <path d="M160 116 L160 262" stroke="${K.red}" stroke-width="6"/><circle cx="144" cy="94" r="8" fill="${K.red}"/><circle cx="176" cy="94" r="8" fill="${K.red}"/>
            <path ${PI} d="M140 62 L120 30 M180 62 L200 30" fill="none"/>`)}</svg>`,
          skull: () => `<svg viewBox="0 0 260 300">${G(`<path ${PI} d="M130 20 Q230 20 232 120 Q234 176 190 196 L190 250 L70 250 L70 196 Q26 176 28 120 Q30 20 130 20Z" fill="${K.paper}"/>
            <ellipse cx="90" cy="130" rx="30" ry="34" fill="${K.ink}"/><ellipse cx="170" cy="130" rx="30" ry="34" fill="${K.ink}"/><path ${PI} d="M130 168 L116 200 L144 200 Z" fill="${K.ink}"/>
            <path ${PI} d="M100 250 L100 226 M130 250 L130 226 M160 250 L160 226"/>`)}</svg>`,
          shield: (c) => `<svg viewBox="0 0 260 320">${G(`<path ${PI} d="M130 18 L232 56 Q236 214 130 300 Q24 214 28 56 Z" fill="${c === "red" ? "#F6B8B4" : "#BFE6F5"}"/>
            <path d="M130 44 L130 276" stroke="#fff" stroke-width="10" opacity=".45"/>`)}${c === "red" ? `<path ${CH(16)} d="M86 110 L174 200 M174 110 L86 200"/>` : `<path ${CY(18)} d="M82 160 L118 198 L184 112"/>`}</svg>`,
          folder: (c) => `<svg viewBox="0 0 380 300">${G(`<path ${PI} d="M24 50 L140 50 L166 80 L356 80 L356 270 L24 270 Z" fill="${c === "lock" ? K.steel2 : "#7CCBEA"}"/>
            <path ${PI} d="M24 116 L356 116 L340 270 L40 270 Z" fill="${c === "lock" ? K.steel : "#A8DEF2"}"/><path d="M48 134 L330 134" stroke="#fff" stroke-width="8" opacity=".5"/>
            ${c === "lock" ? `<path ${PI} d="M30 140 L350 250 M350 140 L30 250" stroke-width="14"/><path d="M30 140 L350 250 M350 140 L30 250" stroke="${K.steel2}" stroke-width="7" stroke-dasharray="16 6"/>${lockBody(150, 150, 80, 80, K.red)}` : ""}`)}</svg>`,
          file: (c) => `<svg viewBox="0 0 260 330">${G(`<path ${PI} d="M30 16 L176 16 L232 72 L232 314 L30 314 Z" fill="${K.paper}"/><path ${PI} d="M176 16 L176 72 L232 72" fill="#E3DED2"/>
            <path ${PT} d="M62 120 L200 120 M62 156 L200 156 M62 192 L170 192 M62 228 L190 228"/>
            ${c ? `<rect ${PI} x="70" y="250" width="122" height="44" rx="8" fill="${K.violet}"/><text x="131" y="282" text-anchor="middle" font-family="JBMono, monospace" font-weight="800" font-size="26" fill="#fff">${c}</text>` : ""}`)}</svg>`,
          mail: () => `<svg viewBox="0 0 380 270">${G(`<rect ${PI} x="20" y="30" width="340" height="220" rx="14" fill="${K.paper}"/><path ${PI} d="M24 40 L190 160 L356 40" fill="none"/>
            <path ${PT} d="M24 244 L150 136 M356 244 L230 136"/>`)}</svg>`,
          hook: () => `<svg viewBox="0 0 200 360">${G(`<path ${PI} d="M100 10 L100 40" stroke-width="4" stroke-dasharray="8 8"/><circle ${PI} cx="100" cy="56" r="16" fill="none"/>
            <path ${PI} d="M100 72 L100 250 Q100 320 150 320 Q190 318 186 268 L170 290" fill="none" stroke-width="16"/>
            <path d="M100 72 L100 250 Q100 320 150 320 Q190 318 186 268" fill="none" stroke="${K.steel}" stroke-width="7"/>`)}</svg>`,
          phish: () => `<svg viewBox="0 0 400 420">${G(`<path ${PI} d="M200 10 L200 70" stroke-width="4" stroke-dasharray="8 8"/>
            <path ${PI} d="M200 70 L200 130 Q200 170 236 170" fill="none" stroke-width="14"/><path d="M200 70 L200 130 Q200 170 236 170" fill="none" stroke="${K.steel}" stroke-width="6"/>
            <rect ${PI} x="40" y="170" width="320" height="220" rx="14" fill="${K.paper}"/><path ${PI} d="M44 180 L200 296 L356 180" fill="none"/>
            <rect ${PI} x="248" y="300" width="96" height="66" rx="8" fill="${K.red}"/><text x="296" y="346" text-anchor="middle" font-family="JBMono, monospace" font-weight="800" font-size="40" fill="#fff">!</text>`)}</svg>`,
          finger: () => `<svg viewBox="0 0 260 320"><g filter="url(#rough)">${[0, 1, 2, 3, 4, 5].map((i) => `<path class="ink" stroke-width="7" d="M${130 - 20 - i * 18} ${280 - i * 6} Q${130 - 30 - i * 18} ${120 - i * 14} 130 ${100 - i * 16} Q${130 + 30 + i * 18} ${120 - i * 14} ${130 + 20 + i * 18} ${250 - i * 4}" fill="none" stroke="${i % 2 ? K.cyan : K.ink}"/>`).join("")}
            <path class="ink" stroke-width="7" d="M126 290 L128 140" fill="none"/></g></svg>`,
          eye: () => `<svg viewBox="0 0 360 220">${G(`<path ${PI} d="M20 110 Q180 -20 340 110 Q180 240 20 110Z" fill="${K.paper}"/><circle ${PI} cx="180" cy="110" r="62" fill="${K.cyan}"/><circle cx="180" cy="110" r="28" fill="${K.ink}"/>
            <circle cx="198" cy="90" r="10" fill="#fff"/>`)}</svg>`,
          user: () => `<svg viewBox="0 0 380 260">${G(`<rect ${PI} x="16" y="16" width="348" height="228" rx="18" fill="${K.paper}"/><rect x="16" y="16" width="348" height="40" rx="18" fill="${K.violet}"/>
            <circle ${PI} cx="104" cy="130" r="38" fill="${K.steel}"/><path ${PI} d="M48 218 Q104 152 160 218" fill="${K.steel}"/>
            <path ${PI} d="M196 110 L330 110 M196 150 L300 150 M196 190 L320 190" stroke-width="7"/>`)}</svg>`,
          pass: () => `<svg viewBox="0 0 480 150">${G(`<rect ${PI} x="12" y="22" width="456" height="106" rx="18" fill="${K.paper}"/>
            ${[0, 1, 2, 3, 4, 5, 6].map((i) => `<circle cx="${74 + i * 50}" cy="75" r="15" fill="${K.ink}"/>`).join("")}<path ${PI} d="M426 46 L426 104" stroke="${K.cyan}" stroke-width="7"/>`)}</svg>`,
          term: () => `<svg viewBox="0 0 440 300">${G(`<rect ${PI} x="16" y="16" width="408" height="268" rx="16" fill="${K.term}"/><path d="M16 60 L424 60" stroke="${K.ink}" stroke-width="4"/>
            <circle cx="44" cy="38" r="9" fill="${K.red}"/><circle cx="72" cy="38" r="9" fill="${K.amber}"/><circle cx="100" cy="38" r="9" fill="${K.green}"/>
            <path d="M44 106 L70 126 L44 146" stroke="${K.green}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M88 150 L130 150" stroke="${K.green}" stroke-width="9" stroke-linecap="round"/>
            <path d="M44 196 L250 196 M44 232 L190 232" stroke="${K.glow}" stroke-width="7" stroke-linecap="round" opacity=".7"/>`)}</svg>`,
          warn: () => `<svg viewBox="0 0 300 270">${G(`<path ${PI} d="M150 18 L284 250 L16 250 Z" fill="${K.amber}" stroke-width="7"/><path ${PI} d="M150 92 L150 172" stroke-width="20"/><circle cx="150" cy="210" r="13" fill="${K.ink}"/>`)}</svg>`,
          // ---- generic (from the Athens set, recoloured) ----
          bub: () => `<svg viewBox="0 0 260 200">${G(`<path ${PI} d="M40 30 Q130 8 220 30 Q250 60 236 110 Q220 140 150 142 L110 186 L112 142 Q40 140 26 104 Q16 60 40 30Z" fill="${K.paper}"/>
            <circle cx="90" cy="88" r="9" fill="${K.soft}"/><circle cx="130" cy="88" r="9" fill="${K.soft}"/><circle cx="170" cy="88" r="9" fill="${K.soft}"/>`)}</svg>`,
          bubq: () => `<svg viewBox="0 0 260 200">${G(`<path ${PI} d="M40 30 Q130 8 220 30 Q250 60 236 110 Q220 140 150 142 L110 186 L112 142 Q40 140 26 104 Q16 60 40 30Z" fill="${K.paper}"/>`)}
            <path ${CH(10)} d="M106 62 Q108 40 132 40 Q156 42 154 62 Q152 78 132 84 L132 100"/><circle cx="132" cy="120" r="7" fill="${K.red}"/></svg>`,
          qmark: () => `<svg viewBox="0 0 240 340"><path ${CH(26)} d="M48 96 Q48 22 122 20 Q196 22 196 92 Q196 148 132 172 Q118 180 118 214 L118 236"/><path ${CH(26)} d="M110 296 L126 300"/></svg>`,
          heart: () => `<svg viewBox="0 0 200 180">${G(`<path ${PI} d="M100 164 Q20 110 22 62 Q26 18 66 18 Q92 18 100 48 Q108 18 134 18 Q174 18 178 62 Q180 110 100 164Z" fill="#F6B8B4"/>
            <path d="M44 60 Q46 40 64 34" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round" opacity=".8"/>`)}</svg>`,
          plus: () => `<svg viewBox="0 0 200 200">${G(`<circle cx="100" cy="100" r="80" fill="${K.paper}" stroke="${K.ink}" stroke-width="7"/>`)}<path ${CY(18)} d="M100 56 L100 144 M56 100 L144 100"/></svg>`,
          magni: () => `<svg viewBox="0 0 300 300">${G(`<circle cx="118" cy="118" r="88" fill="rgba(191,230,245,.35)" stroke="${K.ink}" stroke-width="10"/>
            <path d="M70 82 Q86 60 112 56" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".8"/><path ${PI} d="M184 184 L278 278" stroke-width="26"/><path d="M184 184 L278 278" stroke="${K.violet}" stroke-width="14" stroke-linecap="round"/>`)}</svg>`,
          check: () => `<svg viewBox="0 0 200 160"><path ${CY(22)} d="M24 86 L76 136 L178 22"/></svg>`,
          xmark: () => `<svg viewBox="0 0 200 200"><path ${CH(18)} d="M30 30 L170 170 M170 32 L32 170"/></svg>`,
          arrow: (c) => `<svg viewBox="0 0 300 140"><path ${c === "c" ? CY(14) : CH(14)} d="M16 100 Q120 10 270 60"/><path ${c === "c" ? CY(14) : CH(14)} d="M232 26 L272 60 L226 86"/></svg>`,
          strike: () => `<svg viewBox="0 0 400 80" preserveAspectRatio="none"><path ${CH(14)} d="M8 52 Q120 22 220 40 Q300 52 392 24"/></svg>`,
          circ: (c) => `<svg viewBox="0 0 400 160" preserveAspectRatio="none"><path ${c === "c" ? CY(8) : CH(8)} d="M200 10 C80 4 10 40 20 84 C34 140 330 150 384 100 C420 60 330 8 190 14 C170 16 150 22 140 28"/></svg>`,
          under: (c) => `<svg viewBox="0 0 400 40" preserveAspectRatio="none"><path ${c === "c" ? CY(10) : CH(10)} d="M6 24 Q150 10 260 22 Q330 30 394 14"/></svg>`,
          timeline: () => `<svg viewBox="0 0 860 140"><g filter="url(#rough)"><path ${PI} d="M20 70 L840 70 M20 40 L20 100 M840 40 L840 100 M20 70 L56 52 M20 70 L56 88 M840 70 L804 52 M840 70 L804 88"/>
            <path ${PT} d="M184 60 L184 80 M348 60 L348 80 M512 60 L512 80 M676 60 L676 80"/></g></svg>`,
          flow: () => `<svg viewBox="0 0 860 120"><g filter="url(#rough)"><path ${PI} d="M20 60 L830 60" stroke-dasharray="18 14"/><path ${PI} d="M800 36 L836 60 L800 84"/></g></svg>`,
        };
        document.querySelectorAll("[data-svg]").forEach((el) => { el.innerHTML = SV[el.dataset.svg](el.dataset.c); });
        // background HUD marks in the margins: reticles, node links, data brackets, hex readouts (seeded per scene)
        function rnd(s) { return () => { s = (s * 16807) % 2147483647; return s / 2147483647; }; }
        document.querySelectorAll("svg.scrib").forEach((sv) => { const r = rnd(+sv.dataset.seed); let h = ""; const C = "#6A4BB0", M = "#14A57E";  // lab-notebook doodles in the margins
          const pos = () => [r() < .5 ? 60 + r() * 150 : 870 + r() * 150, 140 + r() * 1680];
          for (let i = 0; i < 4; i++) { const [x, y] = pos(), q = 0.7 + r() * 0.5;  // flask
            h += `<g transform="translate(${x.toFixed(0)} ${y.toFixed(0)}) scale(${q.toFixed(2)})" stroke="${i % 2 ? C : M}" stroke-width="2.4" fill="none" opacity="${(0.28 + r() * .2).toFixed(2)}"><path d="M-8 -30 h16 M-5 -30 v18 L-24 22 a6 6 0 0 0 5 9 h38 a6 6 0 0 0 5 -9 L5 -12 v-18"/><path d="M-16 10 h32" stroke-dasharray="4 4"/></g>`; }
          for (let i = 0; i < 4; i++) { const [x, y] = pos(), q = 0.7 + r() * 0.5;  // test tube
            h += `<g transform="translate(${x.toFixed(0)} ${y.toFixed(0)}) rotate(${(r() * 40 - 20).toFixed(0)}) scale(${q.toFixed(2)})" stroke="${i % 2 ? M : C}" stroke-width="2.4" fill="none" opacity="${(0.28 + r() * .2).toFixed(2)}"><path d="M-8 -34 v56 a8 8 0 0 0 16 0 v-56 M-11 -34 h22"/><path d="M-8 4 h16" stroke-dasharray="3 4"/></g>`; }
          for (let i = 0; i < 8; i++) { const [x, y] = pos(), q = 6 + r() * 14;  // bubbles
            h += `<circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="${q.toFixed(0)}" fill="none" stroke="${M}" stroke-width="2" opacity="${(0.25 + r() * .2).toFixed(2)}"/>`; }
          for (let i = 0; i < 10; i++) { const [x, y] = pos(); h += `<text x="${x.toFixed(0)}" y="${y.toFixed(0)}" font-family="JBMono, monospace" font-weight="700" letter-spacing="2" font-size="${(16 + r() * 8).toFixed(0)}" fill="${C}" opacity="${(0.2 + r() * .2).toFixed(2)}">${["EXP.01", "pH 7", "50 ml", "n = 1", "×10", "Δt", "37 °C", "H₂O", "TEST", "#01", "mg/L", "OK?"][Math.floor(r() * 12)]}</text>`; }
          sv.innerHTML = h; });
