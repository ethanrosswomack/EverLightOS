const bz = document.getElementById('bridgezone-feed');
if (bz){
  const css = `
  .bz{background:#09111c;color:#cde1ff;border-radius:16px;border:1px solid #142035;padding:16px;margin:24px 0;font-family:ui-monospace, SFMono-Regular, Menlo, monospace}
  .bz h2{color:#d4af37;margin:0 0 8px}
  .line{border-bottom:1px solid #1a2740;padding:8px 0}
  `;
  const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s);

  bz.innerHTML = `<div class="bz"><h2>Bridge Zone Live Feed</h2><div id="bz-lines"></div></div>`;
  const lines = document.getElementById('bz-lines');

  async function tick(){
    try{
      const commits = await fetch('https://api.github.com/repos/ethanrosswomack/everlightos/commits?per_page=5').then(r=>r.json());
      lines.innerHTML = '';
      commits.forEach(c=>{
        const msg = c.commit.message.split('\n')[0];
        const t = new Date(c.commit.author.date).toLocaleString();
        const div = document.createElement('div');
        div.className='line';
        div.innerHTML = `[${t}] <a target="_blank" href="${c.html_url}">${msg}</a> — ${c.commit.author.name}`;
        lines.appendChild(div);
      });
    }catch(_){}
  }
  tick(); setInterval(tick, 60000);
}
