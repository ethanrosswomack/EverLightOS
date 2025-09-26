const mount = document.getElementById('federation-council');
if (mount) {
  const css = `
    .council{background:#0b1220;color:#e6edf3;border-radius:16px;padding:24px;margin:24px 0;border:1px solid #182235}
    .council h2{margin:0 0 12px;color:#d4af37}
    .seats{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
    .seat{background:#0f182a;border:1px solid #1c2840;border-radius:14px;padding:14px;display:flex;gap:12px;align-items:center}
    .seat img{width:48px;height:48px;border-radius:10px;object-fit:cover;border:1px solid #243250}
    .seat .meta{display:flex;flex-direction:column}
    .tag{font-size:12px;opacity:.8}
    .status{margin-left:auto;font-size:12px;opacity:.7}
  `;
  const style = document.createElement('style'); style.textContent = css; document.head.appendChild(style);

  fetch('/site/data/council.json')
    .then(r => r.json())
    .then(cfg => {
      mount.innerHTML = `
        <div class="council">
          <h2>Federation Council</h2>
          <div class="seats"></div>
        </div>`;
      const grid = mount.querySelector('.seats');
      cfg.members.forEach(m => {
        const card = document.createElement('div');
        card.className = 'seat';
        card.innerHTML = `
          <img src="${m.avatar || 'https://placehold.co/96x96'}" alt="${m.name}">
          <div class="meta">
            <strong>${m.name}</strong>
            <span class="tag">${m.title} • ${m.role}</span>
            <small>${m.bio}</small>
          </div>
          <span class="status">● ${m.status}</span>
        `;
        grid.appendChild(card);
      });
    })
    .catch(() => { mount.innerHTML = ''; });
}
