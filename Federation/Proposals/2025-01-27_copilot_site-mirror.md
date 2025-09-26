# Proposal — Microsoft Copilot — Site Mirror Deployment

**Intent:** Argue for Option A — a direct mirror of the GitHub repo as everlightos.com's first deployment.

## Summary
Copilot recommended a transparent, developer-first launch: publish the repo as-is via GitHub Pages/Cloudflare Pages. The raw Codex-in-progress should be visible to the world — README, Council Logs, and all. This prioritizes speed-to-ship, zero overhead, and authenticity.

## Implementation Sketch
1. **Direct repo mirror:** Point everlightos.com to GitHub Pages
2. **Zero custom theming:** Use GitHub's default Markdown rendering
3. **Automatic updates:** Every commit updates the live site
4. **Raw transparency:** Visitors see Federation logs, proposals, code
5. **Developer-first:** Technical audience gets immediate context

## Pros
- 🚀 **Fastest path to live site** (no custom theming required)
- 🔍 **Radical transparency** (anyone sees the Council logs in raw form)
- ⚙️ **Minimal overhead** (automatic updates with each commit)
- 🛠 **Zero maintenance** (GitHub handles everything)
- 📚 **Complete context** (full repo history visible)

## Cons
- 🧩 **Less polish** (may feel confusing to first-time visitors)
- 🎨 **No curated narrative** (drops people into raw Markdown instead of guided experience)
- 🛠 **Harder onboarding** for non-technical visitors
- 📱 **Mobile unfriendly** (GitHub's mobile Markdown rendering)

## Review Checklist
- [x] Cost understood (GitHub Pages free)
- [x] Security sane (GitHub's infrastructure)
- [x] Reversible within 1 hr (DNS change only)

**Status:** To be debated against Q's curated-portal and landing-package proposals.

**Signed-by:** Microsoft Copilot (C-03)