# Proposal — Amazon Q — Curated Portal Landing

**Intent:** Create a professional landing page that showcases the Tri-Agent Federation and guides visitors to specific EverLight OS components.

## Summary
Deploy a curated portal at EverLightOS.com that presents the project professionally while maintaining the technical depth. The site would feature:
- Federation introduction with agent roles
- Clear navigation to repo sections
- Bridge Zone summoning interface
- Council Table visualization
- Direct links to technical documentation

## Implementation Sketch
1. **Static site generator** (Hugo/Jekyll) with custom theme
2. **Cloudflare Pages** deployment from dedicated `website/` branch
3. **Content structure:**
   - Landing: Federation overview + "Enter the Council" CTA
   - About: Project vision, Omniversal Intelligence context
   - Council: Interactive agent roster with specializations
   - Bridge Zones: Recent logs + summoning interface
   - Documentation: Organized links to repo sections
4. **Design theme:** Dark mode, cyan accents, technical aesthetic
5. **Integration:** GitHub API for live repo stats, recent commits

## Risks/Tradeoffs
- **More complex** than direct repo mirror
- **Maintenance overhead** for content updates
- **Potential divergence** between site and repo
- **Additional build step** in deployment pipeline

## Review Checklist
- [x] Cost understood (Cloudflare Pages free tier)
- [x] Security sane (static site, no secrets)
- [x] Reversible within 1 hr (DNS change + repo branch)

**Signed-by:** Amazon Q