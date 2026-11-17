# Omong Studio Journal

Static English blog for **Omong Studio**, published on GitHub Pages.

Live: https://theloz33-bot.github.io/omong-studio-journal/

## How it is built

- `posts/*.md` — one markdown file per article (front matter at the top).
- `data/site.json` — brand, base URL, navigation, page list.
- `data/affiliates.json` — every AI-tool link in one place. When an affiliate link is issued, paste it into `affiliate_url` and rebuild: in-text links, toolboxes and the sidebar all follow.
- `data/products.json` — the Gumroad cards.
- `pages/*.md` — Hire (the commission page at `/services/`), About and Disclosure.
- `templates/base.html` — the page shell.
- `static/` — CSS and favicon, copied to `docs/assets/`.
- `build.py` — no dependencies, Python 3 standard library only. Writes `docs/`.

The commission page (`pages/services.md` → `/services/`) is the studio's hire desk: long-form storytelling, 9:16 short-form ads, custom brand songs, the $95 pilot, delivery specs and the limits. `build.py` injects a CTA strip that links to it on the home page (top and bottom) and at the foot of every post, so new articles carry the offer without any per-post markup. The "Hire" nav item and footer link also point there. Prices on that page are the studio's published terms — change them in `pages/services.md`, and if a package price on Krymong changes, change it in both places.

`docs/` is what GitHub Pages serves (`main` branch, `/ (root)` folder is **not** used — the source is `docs/`). `docs/.nojekyll` stops Jekyll from touching the output.

## Publish a new post

```bash
cp posts/_template.md posts/2026-11-17-my-new-post.md
# write it, then:
python3 build.py --check     # fails if a post is outside 900-1300 words
./deploy.sh "Add post: my new post"
```

`deploy.sh` builds, commits and pushes. GitHub Pages rebuilds within about a minute.

## Front matter

```
---
title: "Post title as it appears in search"
slug: "url-slug"                 # /posts/<slug>/
date: "2026-11-16"
category: "Character Consistency" # its own /category/<slug>/ page
excerpt: "One or two sentences shown on cards and in the feed."
description: "Meta description, 140-160 characters."
tags: ["AI character", "9:16"]
tools: ["elevenlabs", "gamma"]    # keys from data/affiliates.json -> toolbox box
featured: true                    # the newest featured post runs as the home hero
---
```

## Writing rules used on this site

- Only workflows actually run. No invented results, follower counts or revenue.
- Numbers are workflow parameters (shot counts, seconds, dB), not performance claims.
- Failures stay in the article; they are the useful part.
- Affiliate links carry `rel="nofollow sponsored"` and are disclosed in `data/affiliates.json` and on `/disclosure/`.
- No analytics, no cookies, no third-party scripts. Keep it that way.

## Checks before pushing

```bash
python3 build.py --check
python3 tools/audit.py       # internal links, XML validity, HTML tag balance, privacy grep
```

The audit also fails if the output contains a real name, phone number, or personal email — the site is published under the studio brand only.

## Content licence

Text and images © Omong Studio. Code samples in articles may be copied and used freely.
