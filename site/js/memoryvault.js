const mvMount = document.getElementById('memoryvault-explorer');
if (mvMount){
  const css = `
  .mv{background:#0b1220;color:#e6edf3;border:1px solid #182235;border-radius:16px;padding:24px;margin:24px 0}
  .mv h2{color:#d4af37;margin:0 0 12px}
  .mv .list a{display:block;padding:8px 10px;border:1px solid #1c2840;border-radius:10px;margin-bottom:8px;background:#0f182a;color:#9cc4ff;text-decoration:none}
  .mv .preview{white-space:pre-wrap;background:#0f182a;border:1px solid #1c2840;border-radius:14px;padding:14px;margin-top:12px;max-height:420px;overflow:auto}
  `;
  const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s);

  mvMount.innerHTML = `<div class="mv">
    <h2>MemoryVault Explorer</h2>
    <div class="list"></div>
    <div class="preview" id="mv-preview">Select a document to preview…</div>
  </div>`;

  const list = mvMount.querySelector('.list');
  const preview = mvMount.querySelector('#mv-preview');

  async function gh(path){ const r = await fetch(`https://api.github.com/repos/ethanrosswomack/everlightos/contents/${path}`); if(!r.ok) throw 0; return r.json(); }

  async function load(){
    try{
      const files = await gh('codex');
      const mds = files.filter(f => /\.md$/i.test(f.name)).sort((a,b)=>a.name.localeCompare(b.name));
      mds.forEach(f=>{
        const a = document.createElement('a');
        a.href = '#'; a.textContent = f.name;
        a.onclick = async (e)=>{ e.preventDefault();
          const raw = `https://raw.githubusercontent.com/ethanrosswomack/everlightos/HEAD/codex/${encodeURIComponent(f.name)}`;
          const txt = await fetch(raw).then(r=>r.text());
          preview.textContent = txt.slice(0, 50000); // simple text preview (safe)
        };
        list.appendChild(a);
      });
      if (!mds.length) list.innerHTML = `<div class="muted">No Markdown files in /codex yet.</div>`;
    }catch(_){
      list.innerHTML = `<div class="muted">Couldn't read /codex via GitHub API.</div>`;
    }
  }
  load();
}
