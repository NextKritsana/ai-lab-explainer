const path=require("path"),{execFileSync}=require("child_process");
let pw;try{pw=require("playwright")}catch(e){pw=require(path.join(execFileSync("npm",["root","-g"]).toString().trim(),"playwright"))}
(async()=>{const b=await pw.chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto("file://"+process.argv[2]);await p.waitForTimeout(1500);
const r=await p.evaluate(()=>Array.from(document.querySelectorAll(".tz > *, .stamp, .cbub")).map(e=>{const s=e.closest("section");const rg=document.createRange();rg.selectNodeContents(e);const w=rg.getBoundingClientRect().width;return [s?s.id:"",e.textContent.trim().slice(0,40),Math.round(w)]}).filter(x=>x[2]>1000));
console.log(JSON.stringify(r));await b.close()})();
