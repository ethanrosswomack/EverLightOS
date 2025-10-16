const owner = 'ethanrosswomack';
const repo  = 'everlightos';
const mount = document.getElementById('project-dashboard');

async function gh(path){
  const r = await fetch(`https://api.github.com/repos/${owner}/${repo}/${path}`);
  if(!r.ok) throw new Error(path);
  return r.json();
}

async function getCommits(){
  return gh('commits?per_page=10');
}

async function getPRs(){
  return gh('pulls?state=open&per_page=10');
}

async function findADRs(){
  // common ADR homes
  const candidates = ['docs/adr','docs/ADRs','ADR','adrs','.adr','docs'];
  for (const dir of candidates){
    try{
      const items = await gh(`contents/${dir}`);
      const mds = items.filter(i => /ADR/i.test(i.name) && /\.md$/i.test(i.name));
      if (mds.length) return mds;
    }catch(_){}
  }
  return [];
}

function h(tag, cls, html){
  const el = document.createElement(tag);
  if (cls) el.className = cls;
  if (html !== undefined) el.innerHTML = html;
  return el;
}

function styles(){
  const css = `
  .dash{background:#0b1220;color:#e6edf3;border:1px solid #182235;border-radius:16px;padding:24px;margin:24px 0}
  .dash h2{color:#d4af37;margin:0 0 12px}
  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}
  .card{background:#0f182a;border:1px solid #1c2840;border-radius:14px;padding:14px}
  .muted{opacity:.8;font-size:12px}
  a{color:#9cc4ff;text-decoration:none}
  a:hover{text-decoration:underline}
  `;
  const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s);
}

async function render(){
  if(!mount) return;
  styles();
  const wrap = h('div','dash');
  wrap.appendChild(h('h2',null,'Federation Project Dashboard'));

  const grid = h('div','grid');
  wrap.appendChild(grid);

  // Commits
  try{
    const commits = await getCommits();
    const c = h('div','card');
    c.appendChild(h('strong',null,'Recent Commits'));
    c.appendChild(h('div','muted',`Branch: ${commits[0]?.commit?.tree?.sha?.slice(0,7) || '—'}`));
    const ul = h('ul');
    commits.slice(0,5).forEach(cm=>{
      const li = h('li',null,
        `<a href="${cm.html_url}" target="_blank">${cm.commit.message.split('\n')[0]}</a><br>
         <span class="muted">${cm.commit.author.name} • ${new Date(cm.commit.author.date).toLocaleString()}</span>`);
      ul.appendChild(li);
    });
    c.appendChild(ul);
    grid.appendChild(c);
  }catch(_){}

  // PRs
  try{
    const prs = await getPRs();
    const c = h('div','card');
    c.appendChild(h('strong',null,'Open PRs'));
    const ul = h('ul');
    prs.forEach(pr=>{
      const labels = pr.labels?.map(l=>l.name).join(', ') || '';
      const li = h('li',null,
        `<a target="_blank" href="${pr.html_url}">#${pr.number}: ${pr.title}</a><br>
         <span class="muted">${labels}</span>`);
      ul.appendChild(li);
    });
    if(!prs.length) ul.appendChild(h('div','muted','No open PRs'));
    c.appendChild(ul);
    grid.appendChild(c);
  }catch(_){}

  // ADRs
  try{
    const adrs = await findADRs();
    const c = h('div','card');
    c.appendChild(h('strong',null,'Decision Records (ADR)'));
    const ul = h('ul');
    if(!adrs.length){
      ul.appendChild(h('div','muted','No ADRs discovered in common locations.'));
    } else {
      adrs.slice(0,6).forEach(a=>{
        ul.appendChild(h('li',null,`<a target="_blank" href="${a.html_url}">${a.name}</a>`));
      });
    }
    c.appendChild(ul);
    grid.appendChild(c);
  }catch(_){}

  mount.innerHTML = '';
  mount.appendChild(wrap);
}

render();
