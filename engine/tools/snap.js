// Screenshot an HTML file to PNG.  node tools/snap.js IN.html OUT.png [W H] [--transparent] [--hash=pose]
// Uses Playwright (local or global install), or $CHROME.
const path = require("path"), { execFileSync } = require("child_process");
let pw; try { pw = require("playwright"); } catch (e) { pw = require(path.join(execFileSync("npm", ["root", "-g"]).toString().trim(), "playwright")); }
(async () => {
  const a = process.argv.slice(2), flags = a.filter((x) => x.startsWith("--")), pos = a.filter((x) => !x.startsWith("--"));
  const [inp, out, W = 1080, H = 1920] = pos, hash = (flags.find((f) => f.startsWith("--hash=")) || "").slice(7);
  const b = await pw.chromium.launch(process.env.CHROME ? { executablePath: process.env.CHROME } : {});
  const p = await b.newPage({ viewport: { width: +W, height: +H } });
  const errs = []; p.on("pageerror", (e) => errs.push(e.message));
  await p.goto("file://" + path.resolve(inp) + (hash ? "#" + hash : "")); await p.waitForTimeout(500);
  if (errs.length) console.log("ERRORS:", errs);
  await p.screenshot({ path: out, omitBackground: flags.includes("--transparent") });
  await b.close(); console.log(out);
})();
