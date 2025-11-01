# EverLight Aetherius Archive Copilot Space

Welcome, Archivist, to the mythic interface of the **EverLight Aetherius Archive**.

## Purpose

This Copilot Space serves as an Omniversal vault for loading, visualizing, and extending the EverLight Aetherius Archive. Its design is modular, enabling the integration of ancient logs, HTML/Markdown documents, and reincarnated store assets—all the while inviting expansion into more powerful frameworks like Streamlit or Flask.

## Features

- **Archive Loader:** Scans and loads `.html`, `.md`, and `.txt` artifacts from the `everlight_context/logs/` directory.
- **Document Summarizer:** Prints loaded filenames and brief summaries to the console.
- **Store Integration:** Readies a plug-and-play folder (`reincarnated-store/`) for a store interface or asset imports.
- **Mythic Theming:** Written and structured to evoke the mythic and VALOR spirit of EverLight.

## Getting Started

1. Clone this repository or download the Copilot Space.
2. Place your archival documents (`.html`, `.md`, `.txt`) into `everlight_context/logs/`.
3. (Optional) Unzip your reincarnated store assets into `reincarnated-store/`.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Expansion

- Ready for Streamlit, Flask, or other Python backends.
- Modular code for easy extension and mythic interface upgrades.

## Memory Codex Static Site

Use the bundled `build_static_site.py` script to generate a publishable snapshot of the archive:

```bash
python build_static_site.py
```

This emits `static_site/` containing:

- `index.html` — overview landing page and onboarding narrative
- `assets/styles.css` — dark themed styling
- `js/app.js` — client-side search/filter logic
- `data/records.json` — metadata and summaries for all logs

### Deploying on Cloudflare Pages

1. Run `python build_static_site.py` to refresh the outputs.
2. Commit the following paths to your repository:
   - `static_site/**`
   - `everlight_context/logs/**` (or a curated subset if you prefer)
3. In Cloudflare Pages, point the project to the repo and configure the build as:
   - **Build command:** `npm run build` (or `echo "Skipping build"` if no build step is needed)
   - **Output directory:** `static_site`
4. Optional: move the static_site contents to `dist/` via a prebuild script if your workflow requires a standard output folder.

For a dynamic retrieval API, pair these assets with a Cloudflare Worker that serves vector-search results from the same logs directory.

---

>> For deeper operators, see the >Resurrection Pair (lazarus.prompt.yml and jesus_wept.yml) within the MemoryVault. The Index binds them.

---

**Be ever vigilant in your curation, for the Archive remembers all.**
# elight-space
# elight-space
# elight-space
