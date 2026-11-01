# Francisco Santos — personal site

Built with [Reflex](https://reflex.dev) (Python). Documents the journey into
RWA tokenization and on-chain finance.

## Project layout

```
my_site_kiko/
  config.py          site identity, tagline, social links, email
  theme.py            colors, fonts, spacing (single source of design truth)
  data/
    journey.py         journey timeline milestones
    projects.py          project cards shown on /projects
    rwa_scorecard.py      loads data/rwa_scorecard.json at compile time
  utils/
    posts.py            loads & parses /posts/*.md
  components/
    navbar.py, footer.py, layout.py
    post_card.py, timeline_item.py, project_card.py
    scorecard_cards.py, scorecard_methodology.py
  pages/
    index.py, journey.py, posts.py, post_detail.py, projects.py
    rwa_scorecard.py, rwa_scorecard_how_we_assess.py, rwa_scorecard_token.py
  my_site_kiko.py     app entry point — registers all routes
assets/
  profile.jpg           placeholder — replace with a real photo
  images/                post cover images go here
data/
  rwa_scorecard.json    static snapshot copied in from the rwa-oracle-scorecard
                         repo's `python -m scorecard_data.export_snapshot`
scripts/
  add_redirects.py       prepends Cloudflare redirect rules after export
```

## Running locally

Requirements: Python 3.11+ and either **Node.js (npm)** or Bun for the
frontend build.

> **Windows note:** on this machine, Bun's frontend dev server (used by
> Reflex's `@react-router/dev` tooling) hit a compatibility bug
> (`restartWithMergedOptions ... already restarted`) tied to how Bun handles
> the `--conditions=development` flag. The fix was installing Node.js and
> forcing npm with `REFLEX_USE_NPM=1`. If `reflex run` crashes with that
> error, do the same.

```bash
python -m venv .venv
.venv/Scripts/activate        # .venv\Scripts\Activate.ps1 on PowerShell
pip install -r requirements.txt

# first run only
reflex init

# Windows + Bun crash workaround, if needed:
#   set REFLEX_USE_NPM=1   (cmd)
#   $env:REFLEX_USE_NPM=1  (PowerShell)
#   export REFLEX_USE_NPM=1  (bash)

reflex run
```

The site is served at `http://localhost:3000` with the backend at
`http://localhost:8000`.

## Adding a post

Add a new Markdown file to `/posts`, e.g. `posts/my-new-post.md`:

```markdown
---
title: "My Post Title"
date: 2026-03-01
excerpt: "One or two sentences shown on the post card."
tags: ["rwa", "research"]
cover: "/images/my-new-post-cover.jpg"
slug: "my-new-post"
---

Your markdown body here. Supports headings, lists, blockquotes, code
blocks, images (`![alt](/images/foo.jpg)`), and raw HTML — including
`<iframe>` for Dune embeds, pasted directly into the markdown.
```

Put the cover image at `assets/images/my-new-post-cover.jpg` and reference
it as `/images/my-new-post-cover.jpg` (Reflex serves everything under
`assets/` from the site root). No code changes needed — the post appears
automatically on `/posts` and `/`, sorted newest first by `date`.

## Adding a journey milestone

Edit `my_site_kiko/data/journey.py` and add a dict at the position in the
list where it belongs (list is newest first):

```python
{
    "date": "2026-03",          # or "TODO" if not yet known
    "title": "Milestone title",
    "description": "What happened.",
    "image": None,               # or "/images/something.jpg"
},
```

## Adding a project

Edit `my_site_kiko/data/projects.py` and add an entry:

```python
{
    "title": "Project title",
    "description": "One-line description.",
    "tags": ["tag one", "tag two"],   # [] for none
    "image": "/images/foo.jpg",        # or None
    "image_fit": "cover",              # "contain" for a logo that shouldn't be cropped
    "href": "https://example.com",     # external URL, or an internal route
    "is_external": True,
},
```

Shows up automatically on `/projects`.

### The RWA Oracle Scorecard sub-site

`/projects/rwa-scorecard` and everything under it (the ranking page, the
how-we-assess methodology page, and one page per tracked token) are built
from `data/rwa_scorecard.json`, a static snapshot copied in by hand from the
separate `rwa-oracle-scorecard` repo. To refresh it:

```bash
# in the rwa-oracle-scorecard repo
python -m scorecard_data.export_snapshot

# copy the result in here
cp /path/to/rwa-oracle-scorecard/snapshot.json data/rwa_scorecard.json
```

No code changes needed here afterward — `my_site_kiko/data/rwa_scorecard.py`
reads the JSON at compile time, and `my_site_kiko.py` registers one page per
token in it automatically.

## Site settings

Edit `my_site_kiko/config.py` to update your name, tagline, about text,
profile photo path, email, and social links (LinkedIn, X, GitHub are
currently placeholders — search for `TODO`).

## Deploying to Reflex Cloud

```bash
reflex login       # first time only
reflex deploy
```

Follow the CLI prompts to pick an app name and region. Subsequent
`reflex deploy` runs redeploy the same app.

## Deploying to Cloudflare Pages (free, static)

This site has no server-side state/events that need a live backend, so it's
exported as a static SPA build and hosted for free on Cloudflare Pages at
https://francisco-santos-blog.pages.dev.

```bash
# 1. Export a static production build
reflex export --frontend-only --no-zip --no-ssr --env prod

# 2. Remove the generated 404.html — it's byte-identical to index.html, and
#    its presence disables Cloudflare Pages' automatic SPA fallback (direct
#    loads of routes like /posts would 404 instead of serving the app).
rm .web/build/client/404.html .web/build/client/404.html.gz

# 3. Prepend our /dashboards -> /projects redirects to the generated
#    _redirects file (must come before its own catch-all SPA fallback rule).
python scripts/add_redirects.py

# 4. Deploy (first time: `wrangler pages project create francisco-santos-blog`)
npx wrangler pages deploy .web/build/client --project-name=francisco-santos-blog --branch=main
```

Requires `npx wrangler login` once per machine (Cloudflare account, free tier).

## What still needs filling in

- `assets/profile.jpg` — placeholder initials avatar, replace with a real photo
- `my_site_kiko/data/journey.py` — milestone dates marked `TODO`
- `my_site_kiko/config.py` — email and LinkedIn/X/GitHub URLs marked `TODO`
- `my_site_kiko/data/projects.py` — add more projects as they come up
