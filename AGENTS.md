# AGENTS.md

Astro-powered static site (Greg's Workbench). Node 20+. No test suite.

## Setup

- `npm install` to install dependencies.
- Node >= 20 required (CI pins Node 20; `package.json` requires `>=22.12.0` locally).

## Commands

| Action | Command |
| --- | --- |
| Dev server (live reload) | `npm run dev` |
| Production build → `dist/` | `npm run build` |
| Preview the built site | `npm run preview` |
| Clean rebuild | `rm -rf dist .astro && npm run build` |

## Deploy

- **Automated**: pushing to `main` triggers `.github/workflows/pelican.yml`, which
  runs `npm ci && npx astro build` and publishes `dist/` to GitHub Pages via the
  official `actions/deploy-pages` action. This is the normal path — no manual deploy step.
- GitHub Pages must be set to deploy from **GitHub Actions** (Settings → Pages → Source).
- `astro.config.mjs` sets `site: 'https://gregoryhayes.us'` (used for sitemap, RSS, canonical URLs).

## Content layout

- Articles: `src/content/articles/**/*.{md,mdx}` (collection `articles`).
- Pages: `src/content/pages/**/*.{md,mdx}` (collection `pages`, rendered at `/<slug>/`).
- Schemas defined in `src/content.config.ts` (Zod). Frontmatter is type-checked at build.
- Site-wide data (title, author, social, patents/projects list) lives in `src/consts.ts`.
- Static files (favicon, robots.txt) go in `public/` → served at root.
- Images in `src/assets/` are optimized by Astro; images in `public/` are copied verbatim.
- Build output (`dist/`) and `.astro/` are gitignored.

## Markdown / rendering

- Configured in `astro.config.mjs` via remark/rehype plugins — preserve these when editing:
  - `remark-toc` — generates a table of contents where a `## Table of Contents` heading appears.
  - `remark-smartypants` — typographic quotes (replaces Pelican's `smarty`).
  - `rehype-slug` — `id` anchors on headings (replaces Pelican's `toc` permalinks).
  - Shiki (built into Astro) — syntax highlighting (replaces Pelican's `codehilite`).
  - `remark-gfm` (tables/fences/footnotes) is on by default in Astro.
- MDX is supported (via `@astrojs/mdx`) — use `.mdx` extension for component-in-Markdown.

## Page routing

- `src/pages/index.astro` — landing page.
- `src/pages/about.astro` — about page.
- `src/pages/articles/index.astro` — article list (sorted by `pubDate` desc).
- `src/pages/articles/[...slug].astro` — single article render.
- `src/pages/[...slug].astro` — renders entries from the `pages` collection (e.g. `/patents/`).
- `src/pages/rss.xml.js` — Atom feed at `/rss.xml`.

## Legacy note

Migrated from Pelican. The `pelican-plugins/` submodule, `pelicanconf.py`, `publishconf.py`,
`Makefile`, `tasks.py`, and `requirements.txt` were removed. Old `content/` moved into
`src/content/`.
