#!/usr/bin/env python3
"""Omong Studio Journal — static site builder.

No dependencies: Python 3 standard library only.

    python3 build.py            # rebuild docs/ from posts/ + data/
    python3 build.py --check    # build, then fail if a post is outside 900-1300 words

Inputs
    data/site.json        site settings (brand, base URL, nav, footer)
    data/affiliates.json  AI tool links — swap `affiliate_url` in one place later
    data/products.json    Gumroad products shown as cards
    posts/*.md            one markdown file per article, YAML-ish front matter
    templates/*.html      page shells with {{placeholder}} slots
    static/               copied into docs/ as-is

Output
    docs/                 index, posts, categories, sitemap.xml, rss.xml, robots.txt, 404.html
"""

from __future__ import annotations

import html
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
POSTS = ROOT / "posts"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT / "docs"

WORD_MIN, WORD_MAX = 900, 1300


# ---------------------------------------------------------------- utilities


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def slugify(value: str) -> str:
    value = re.sub(r"[^\w\s-]", "", value.lower(), flags=re.UNICODE)
    value = re.sub(r"[\s_]+", "-", value.strip())
    return re.sub(r"-{2,}", "-", value).strip("-")


def read_template(name: str) -> str:
    return (TEMPLATES / name).read_text(encoding="utf-8")


def render(template: str, values: dict) -> str:
    out = template
    for key, value in values.items():
        out = out.replace("{{" + key + "}}", str(value))
    leftovers = re.findall(r"\{\{[a-z_]+\}\}", out)
    if leftovers:
        raise SystemExit(f"template placeholder left unfilled: {sorted(set(leftovers))}")
    return out


# ---------------------------------------------------------------- markdown

TOKEN = "\x00{}\x00"


def escape(text: str) -> str:
    return html.escape(text, quote=False)


def inline(text: str, site: dict, affiliates: dict) -> str:
    """Escape and convert inline markdown. Stashed fragments are restored last."""
    stash: list[str] = []

    def keep(fragment: str) -> str:
        stash.append(fragment)
        return TOKEN.format(len(stash) - 1)

    # code spans first, so nothing inside them is interpreted
    text = re.sub(
        r"`([^`]+)`",
        lambda m: keep("<code>" + html.escape(m.group(1)) + "</code>"),
        text,
    )

    text = escape(text)

    def image(m: re.Match) -> str:
        alt, src = m.group(1), m.group(2)
        return keep(f'<img src="{src}" alt="{alt}" loading="lazy" decoding="async">')

    def link(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        return keep(anchor(href, label, site))

    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", image, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)

    # [[tool:elevenlabs|anchor text]] -> sponsored link from data/affiliates.json
    def tool(m: re.Match) -> str:
        key, label = m.group(1), m.group(2)
        return keep(tool_link(key, label, site, affiliates))

    text = re.sub(r"\[\[tool:([a-z0-9_-]+)\|([^\]]+)\]\]", tool, text)

    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", text)

    for index, fragment in enumerate(stash):
        text = text.replace(TOKEN.format(index), fragment)
    return text


def anchor(href: str, label: str, site: dict) -> str:
    base = site["base_url"].rstrip("/")
    attrs = [f'href="{href}"']
    if href.startswith("http") and not href.startswith(base):
        rel = "noopener"
        if "gumroad.com" in href:
            rel = "noopener sponsored"
        attrs.append(f'rel="{rel}"')
    return f"<a {' '.join(attrs)}>{label}</a>"


def tool_link(key: str, label: str, site: dict, affiliates: dict) -> str:
    tool = affiliates["tools"].get(key)
    if not tool:
        raise SystemExit(f"unknown tool key in post: {key}")
    href = tool.get("affiliate_url") or tool["url"]
    return (
        f'<a href="{href}" rel="nofollow sponsored noopener" '
        f'class="inline-tool">{label}</a>'
    )


def md_to_html(body: str, site: dict, affiliates: dict) -> tuple[str, list[dict]]:
    lines = body.replace("\r\n", "\n").split("\n")
    blocks: list[str] = []
    toc: list[dict] = []
    used_ids: set[str] = set()
    i = 0

    def heading_id(text: str) -> str:
        base = slugify(re.sub(r"[*`\[\]]", "", text)) or "section"
        candidate, n = base, 2
        while candidate in used_ids:
            candidate = f"{base}-{n}"
            n += 1
        used_ids.add(candidate)
        return candidate

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # fenced code
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            i += 1
            code: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            cls = f' class="language-{escape(lang)}"' if lang else ""
            blocks.append(
                f"<pre><code{cls}>" + html.escape("\n".join(code)) + "</code></pre>"
            )
            continue

        # headings
        match = re.match(r"^(#{2,4})\s+(.*)$", stripped)
        if match:
            level = len(match.group(1))
            label = match.group(2).strip()
            hid = heading_id(label)
            inner = inline(label, site, affiliates)
            blocks.append(f'<h{level} id="{hid}">{inner}</h{level}>')
            if level in (2, 3):
                toc.append({"id": hid, "label": re.sub(r"[*`]", "", label), "level": level})
            i += 1
            continue

        # horizontal rule
        if re.match(r"^-{3,}$", stripped):
            blocks.append("<hr>")
            i += 1
            continue

        # table
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(
            r"^\|[\s:|-]+\|$", lines[i + 1].strip()
        ):
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head = "".join(f"<th>{inline(c, site, affiliates)}</th>" for c in header)
            body_rows = ""
            for row in rows:
                cells = "".join(f"<td>{inline(c, site, affiliates)}</td>" for c in row)
                body_rows += f"<tr>{cells}</tr>"
            blocks.append(
                '<div class="table-wrap"><table><thead><tr>'
                + head
                + "</tr></thead><tbody>"
                + body_rows
                + "</tbody></table></div>"
            )
            continue

        # blockquote
        if stripped.startswith(">"):
            quote: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            inner = " ".join(q for q in quote if q)
            blocks.append(f"<blockquote><p>{inline(inner, site, affiliates)}</p></blockquote>")
            continue

        # lists
        if re.match(r"^([-*]|\d+\.)\s+", stripped):
            ordered = bool(re.match(r"^\d+\.\s+", stripped))
            items: list[tuple[str, str]] = []
            while i < len(lines) and re.match(r"^([-*]|\d+\.)\s+", lines[i].strip()):
                raw = re.sub(r"^([-*]|\d+\.)\s+", "", lines[i].strip())
                checkbox = None
                box = re.match(r"^\[( |x|X)\]\s+(.*)$", raw)
                if box:
                    checkbox = "checked" if box.group(1).lower() == "x" else ""
                    raw = box.group(2)
                # continuation line (indented)
                i += 1
                while (
                    i < len(lines)
                    and lines[i].startswith("  ")
                    and lines[i].strip()
                    and not re.match(r"^([-*]|\d+\.)\s+", lines[i].strip())
                ):
                    raw += " " + lines[i].strip()
                    i += 1
                items.append((checkbox, inline(raw, site, affiliates)))
            tag = "ol" if ordered else "ul"
            if not ordered and any(cb is not None for cb, _ in items):
                cls = ' class="checklist"'
            else:
                cls = ""
            rendered = ""
            for checkbox, content in items:
                if ordered:
                    rendered += f"<li>{content}</li>"
                elif checkbox is not None and checkbox != "":
                    rendered += f'<li class="done">{content}</li>'
                elif checkbox is not None:
                    rendered += f'<li class="todo">{content}</li>'
                else:
                    rendered += f"<li>{content}</li>"
            blocks.append(f"<{tag}{cls}>{rendered}</{tag}>")
            continue

        # paragraph
        para: list[str] = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^(#{2,4}\s|```|\||>\s?|[-*]\s|\d+\.\s|-{3,}$)", lines[i].strip()
        ):
            para.append(lines[i].strip())
            i += 1
        merged = " ".join(para)
        cls = ' class="lede"' if not blocks else ""
        blocks.append(f"<p{cls}>{inline(merged, site, affiliates)}</p>")

    return "\n".join(blocks), toc


# ---------------------------------------------------------------- front matter


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("\n")
    meta: dict = {}
    end = None
    for index in range(1, len(parts)):
        line = parts[index].rstrip()
        if line.strip() in ("---", "..."):
            end = index
            break
        if not line.strip() or line.strip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
            meta[key] = items
        elif value:
            meta[key] = value.strip("\"'")
        else:
            meta[key] = ""
    if end is None:
        raise SystemExit("front matter opened with --- but never closed")
    return meta, "\n".join(parts[end + 1 :])


def word_count(text: str) -> int:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"[#*`\[\]()>|-]", " ", text)
    return len([w for w in text.split() if re.search(r"[A-Za-z0-9]", w)])


# ---------------------------------------------------------------- building blocks


def load_posts(site: dict, affiliates: dict) -> list[dict]:
    posts: list[dict] = []
    for path in sorted(POSTS.glob("*.md")):
        if path.name.startswith("_"):
            continue
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        missing = [k for k in ("title", "slug", "date", "category", "description") if not meta.get(k)]
        if missing:
            raise SystemExit(f"{path.name}: missing front matter keys {missing}")
        body_html, toc = md_to_html(body, site, affiliates)
        words = word_count(body)
        reading = max(1, round(words / 220))
        posts.append(
            {
                "path": path,
                "meta": meta,
                "title": meta["title"],
                "slug": meta["slug"],
                "date": meta["date"],
                "category": meta["category"],
                "category_slug": slugify(meta["category"]),
                "description": meta["description"],
                "excerpt": meta.get("excerpt", meta["description"]),
                "tags": meta.get("tags", []),
                "tools": meta.get("tools", []),
                "featured": str(meta.get("featured", "")).lower() in ("true", "yes", "1"),
                "html": body_html,
                "toc": toc,
                "words": words,
                "reading": reading,
            }
        )
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def fmt_date(value: str, style: str = "long") -> str:
    date = datetime.strptime(value, "%Y-%m-%d")
    if style == "short":
        return date.strftime("%b %-d, %Y") if sys.platform != "win32" else date.strftime("%b %d, %Y")
    return date.strftime("%B %-d, %Y") if sys.platform != "win32" else date.strftime("%B %d, %Y")


def rfc822(value: str) -> str:
    date = datetime.strptime(value, "%Y-%m-%d").replace(hour=9, tzinfo=timezone.utc)
    return date.strftime("%a, %d %b %Y %H:%M:%S +0000")


def nav_html(site: dict, current: str) -> str:
    items = []
    for item in site["nav"]:
        active = ' aria-current="page"' if item["key"] == current else ""
        items.append(
            f'<a href="{site["base_path"]}{item["path"]}"{active}>{item["label"]}</a>'
        )
    return "\n".join(items)


def product_cards(products: dict, site: dict, heading: str = "Kits from the studio") -> str:
    cards = []
    for product in products["products"]:
        features = "".join(f"<li>{f}</li>" for f in product.get("features", []))
        cards.append(
            f"""<a class="kit-card" href="{product['url']}" rel="noopener sponsored">
  <span class="kit-badge">{product.get('badge', '')}</span>
  <span class="kit-name">{product['name']}</span>
  <span class="kit-desc">{product['blurb']}</span>
  <span class="kit-foot"><span class="kit-price">{product['price']}</span><span class="kit-go">View kit &rarr;</span></span>
</a>"""
        )
    return f"""<section class="kit-block">
  <h2 class="rule">{heading}</h2>
  <p class="kit-note">{products['note']}</p>
  <div class="kit-grid">
    {''.join(cards)}
  </div>
</section>"""


def hire_strip(site: dict, variant: str = "post") -> str:
    """Commission CTA. variant="post" sits under an article, "home" above the index."""
    base = site["base_path"]
    if variant == "home":
        eyebrow = "Commission the studio"
        title = "Long-form films, 9:16 ad cuts and original brand songs"
        body = (
            "AI storytelling for a 3–12 minute YouTube or brand film, vertical ads for "
            "Reels, TikTok and Shorts, or a custom track with 15 and 30 second cutdowns. "
            "Pilots from $95, delivered in 2–3 business days."
        )
        label = "Scope, price and process"
    else:
        eyebrow = "Work with the studio"
        title = "Want this made for your brand instead of by you?"
        body = (
            "Omong Studio takes commissions for long-form storytelling, 9:16 short-form ads "
            "and original brand songs. Pilots from $95, 2–3 business days, and a fixed quote "
            "in writing before any work starts."
        )
        label = "See what a commission includes"
    return f"""<section class="hire-strip hire-{variant}">
  <div class="hire-copy">
    <p class="hire-eyebrow">{eyebrow}</p>
    <h2>{title}</h2>
    <p>{body}</p>
  </div>
  <a class="hire-cta" href="{base}services/">{label} &rarr;</a>
</section>"""


def sidebar_html(products: dict, site: dict, affiliates: dict, tools: list[str], toc: list[dict]) -> str:
    parts = []
    if toc:
        links = "".join(
            f'<li class="lvl{item["level"]}"><a href="#{item["id"]}">{escape(item["label"])}</a></li>'
            for item in toc
        )
        parts.append(
            f'<nav class="side-box toc-box"><h2>In this article</h2><ul class="toc">{links}</ul></nav>'
        )
    if tools:
        rows = []
        for key in tools:
            tool = affiliates["tools"].get(key)
            if not tool:
                raise SystemExit(f"unknown tool key in front matter: {key}")
            href = tool.get("affiliate_url") or tool["url"]
            rows.append(
                f'<li><a href="{href}" rel="nofollow sponsored noopener">{tool["name"]}</a>'
                f'<span>{tool["blurb"]}</span></li>'
            )
        parts.append(
            '<div class="side-box"><h2>Toolbox</h2><ul class="tools">'
            + "".join(rows)
            + f'</ul><p class="disclosure-mini">{affiliates["disclosure_short"]}</p></div>'
        )
    kc = "".join(
        f'<li><a href="{p["url"]}" rel="noopener sponsored"><strong>{p["name"].split("(")[0].strip()}</strong>'
        f'<em>{p["price"]}</em></a></li>'
        for p in products["products"]
    )
    parts.append(f'<div class="side-box"><h2>Studio kits</h2><ul class="mini-kits">{kc}</ul></div>')
    return "\n".join(parts)


# ---------------------------------------------------------------- pages


def build() -> int:
    site = load_json(DATA / "site.json")
    affiliates = load_json(DATA / "affiliates.json")
    products = load_json(DATA / "products.json")
    posts = load_posts(site, affiliates)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    base_html = read_template("base.html")
    base = site["base_path"]
    brand = site["brand"]
    year = datetime.now().year

    def page(
        *,
        title: str,
        description: str,
        canonical: str,
        content: str,
        current: str = "",
        og_type: str = "website",
        head_extra: str = "",
        body_class: str = "",
    ) -> str:
        return render(
            base_html,
            {
                "lang": site["language"],
                "brand": brand,
                "tagline": site["tagline"],
                "title": html.escape(title, quote=True),
                "description": html.escape(description, quote=True),
                "canonical": canonical,
                "og_type": og_type,
                "base": base,
                "nav": nav_html(site, current),
                "content": content,
                "year": year,
                "footer_note": site["footer_note"],
                "head_extra": head_extra,
                "body_class": body_class,
            },
        )

    def write(rel: str, text: str) -> None:
        target = OUT / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    # ---- posts
    for index, post in enumerate(posts):
        url = f"{site['base_url'].rstrip('/')}/posts/{post['slug']}/"
        post["url"] = url
        related = [p for p in posts if p["slug"] != post["slug"]][:2]
        related_html = ""
        if related:
            links = "".join(
                f'<li><a href="{base}posts/{p["slug"]}/">{escape(p["title"])}</a>'
                f'<span>{escape(p["category"])} · {p["reading"]} min</span></li>'
                for p in related
            )
            related_html = f'<section class="related"><h2 class="rule">Keep reading</h2><ul>{links}</ul></section>'

        toc_html = ""
        if post["toc"]:
            jumps = "".join(
                f'<a href="#{item["id"]}">{escape(item["label"])}</a>' for item in post["toc"]
            )
            toc_html = (
                '<details class="jump" open><summary>In this guide</summary>'
                f'<div class="jump-links">{jumps}</div></details>'
            )

        toolbox = ""
        if post["tools"]:
            rows = []
            for key in post["tools"]:
                tool = affiliates["tools"].get(key)
                if not tool:
                    raise SystemExit(f"unknown tool key: {key}")
                href = tool.get("affiliate_url") or tool["url"]
                rows.append(
                    f'<li><a href="{href}" rel="nofollow sponsored noopener">{tool["name"]}</a>'
                    f'<span>{tool["blurb"]}</span></li>'
                )
            toolbox = (
                '<section class="callout tool-box"><h2>Toolbox for this workflow</h2>'
                f'<ul class="tools">{"".join(rows)}</ul>'
                f'<p class="disclosure-mini">{affiliates["disclosure"]}</p></section>'
            )

        article = f"""
<article class="post">
  <nav class="crumbs"><a href="{base}">Journal</a> / <a href="{base}category/{post['category_slug']}/">{escape(post['category'])}</a></nav>
  <header class="post-head">
    <h1>{escape(post['title'])}</h1>
    <p class="dek">{escape(post['excerpt'])}</p>
    <p class="meta"><time datetime="{post['date']}">{fmt_date(post['date'])}</time> · {post['reading']} min read · {brand}</p>
  </header>
  {toc_html}
  <div class="prose">
    {post['html']}
  </div>
  {toolbox}
  {product_cards(products, site)}
  {hire_strip(site)}
  {related_html}
  <p class="post-foot"><a href="{base}">All posts</a></p>
</article>"""

        jsonld = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": post["title"],
            "description": post["description"],
            "datePublished": post["date"],
            "dateModified": post["date"],
            "inLanguage": "en",
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "author": {"@type": "Organization", "name": brand, "url": site["base_url"].rstrip('/') + "/"},
            "publisher": {"@type": "Organization", "name": brand},
            "articleSection": post["category"],
            "keywords": ", ".join(post["tags"]),
            "wordCount": post["words"],
        }
        head_extra = (
            f'<meta property="article:published_time" content="{post["date"]}">\n'
            f'<meta name="author" content="{brand}">\n'
            f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>'
        )

        aside = sidebar_html(products, site, affiliates, post["tools"], post["toc"])
        content = article + f'\n<aside class="post-aside" aria-label="Sidebar">{aside}</aside>'

        write(
            f"posts/{post['slug']}/index.html",
            page(
                title=f"{post['title']} · {brand}",
                description=post["description"],
                canonical=url,
                content=content,
                current="journal",
                og_type="article",
                head_extra=head_extra,
                body_class="layout-post",
            ),
        )

    # ---- categories
    categories: dict[str, list[dict]] = {}
    for post in posts:
        categories.setdefault(post["category"], []).append(post)

    for name, items in categories.items():
        cslug = slugify(name)
        listing = "".join(
            f"""<li class="entry">
  <a href="{base}posts/{p['slug']}/">
    <span class="entry-cat">{escape(p['category'])}</span>
    <h2>{escape(p['title'])}</h2>
    <p>{escape(p['excerpt'])}</p>
    <span class="entry-meta"><time datetime="{p['date']}">{fmt_date(p['date'])}</time> · {p['reading']} min</span>
  </a>
</li>"""
            for p in items
        )
        url = f"{site['base_url'].rstrip('/')}/category/{cslug}/"
        body = f"""
<header class="page-head">
  <p class="crumbs"><a href="{base}">Journal</a> / Category</p>
  <h1>{escape(name)}</h1>
  <p class="dek">{len(items)} post{'s' if len(items) != 1 else ''} filed under {escape(name)}.</p>
</header>
<ul class="entries">{listing}</ul>
<p class="post-foot"><a href="{base}">All posts</a></p>"""
        write(
            f"category/{cslug}/index.html",
            page(
                title=f"{name} · {brand}",
                description=f"Posts about {name} from {brand}.",
                canonical=url,
                content=body,
                current="journal",
            ),
        )

    # ---- static pages
    for spec in site["pages"]:
        rel = spec["path"].strip("/")
        if not rel:
            continue
        src = ROOT / "pages" / f"{spec['key']}.md"
        meta, body = parse_front_matter(src.read_text(encoding="utf-8"))
        body_html, _ = md_to_html(body, site, affiliates)
        url = f"{site['base_url'].rstrip('/')}/{rel}/"
        content = f"""
<article class="page">
  <header class="page-head">
    <p class="crumbs"><a href="{base}">Journal</a></p>
    <h1>{escape(meta['title'])}</h1>
  </header>
  <div class="prose">{body_html}</div>
</article>"""
        write(
            f"{rel}/index.html",
            page(
                title=f"{meta['title']} · {brand}",
                description=meta.get("description", site["description"]),
                canonical=url,
                content=content,
                current=spec["key"],
            ),
        )

    # ---- index
    featured = next((p for p in posts if p["featured"]), posts[0] if posts else None)
    rest = [p for p in posts if featured and p["slug"] != featured["slug"]]
    hero = ""
    if featured:
        hero = f"""
<section class="hero">
  <p class="eyebrow">Latest field note</p>
  <h1><a href="{base}posts/{featured['slug']}/">{escape(featured['title'])}</a></h1>
  <p class="dek">{escape(featured['excerpt'])}</p>
  <p class="meta"><time datetime="{featured['date']}">{fmt_date(featured['date'])}</time> · {featured['reading']} min read</p>
  <a class="button" href="{base}posts/{featured['slug']}/">Read the note</a>
</section>"""

    listing = "".join(
        f"""<li class="entry">
  <a href="{base}posts/{p['slug']}/">
    <span class="entry-cat">{escape(p['category'])}</span>
    <h2>{escape(p['title'])}</h2>
    <p>{escape(p['excerpt'])}</p>
    <span class="entry-meta"><time datetime="{p['date']}">{fmt_date(p['date'])}</time> · {p['reading']} min</span>
  </a>
</li>"""
        for p in rest
    )
    cat_links = "".join(
        f'<a class="pill" href="{base}category/{slugify(name)}/">{escape(name)} <span>{len(items)}</span></a>'
        for name, items in sorted(categories.items(), key=lambda kv: -len(kv[1]))
    )
    index_content = f"""
{hero}
{hire_strip(site, 'home')}
<section class="intro">
  <h2 class="rule">What this journal is</h2>
  <p>{escape(site['about_blurb'])}</p>
  <div class="pills">{cat_links}</div>
</section>
<section class="latest">
  <h2 class="rule">More notes</h2>
  <ul class="entries">{listing}</ul>
</section>
{product_cards(products, site, "Kits and prompt packs")}
{hire_strip(site)}"""

    blog_ld = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": brand,
        "description": site["description"],
        "url": site["base_url"].rstrip("/") + "/",
        "inLanguage": "en",
        "blogPost": [
            {
                "@type": "BlogPosting",
                "headline": p["title"],
                "datePublished": p["date"],
                "url": p["url"],
            }
            for p in posts
        ],
    }
    write(
        "index.html",
        page(
            title=f"{brand} — {site['tagline']}",
            description=site["description"],
            canonical=site["base_url"].rstrip("/") + "/",
            content=index_content,
            current="journal",
            head_extra=f'<script type="application/ld+json">{json.dumps(blog_ld, ensure_ascii=False)}</script>',
            body_class="layout-home",
        ),
    )

    # ---- feed files
    items = "".join(
        f"""  <item>
    <title>{escape(p['title'])}</title>
    <link>{p['url']}</link>
    <guid isPermaLink="true">{p['url']}</guid>
    <pubDate>{rfc822(p['date'])}</pubDate>
    <category>{escape(p['category'])}</category>
    <description>{escape(p['excerpt'])}</description>
  </item>
"""
        for p in posts
    )
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{escape(brand)}</title>
  <link>{site['base_url'].rstrip('/')}/</link>
  <atom:link href="{site['base_url'].rstrip('/')}/rss.xml" rel="self" type="application/rss+xml"/>
  <description>{escape(site['description'])}</description>
  <language>en</language>
  <lastBuildDate>{rfc822(posts[0]['date']) if posts else rfc822(datetime.now().strftime('%Y-%m-%d'))}</lastBuildDate>
{items}</channel>
</rss>
"""
    write("rss.xml", rss)

    urls = [
        ("", posts[0]["date"] if posts else datetime.now().strftime("%Y-%m-%d")),
        *[(f"posts/{p['slug']}/", p["date"]) for p in posts],
        *[(f"category/{slugify(name)}/", max(i["date"] for i in items_)) for name, items_ in categories.items()],
        *[(f"{spec['path'].strip('/')}/", posts[0]["date"] if posts else datetime.now().strftime("%Y-%m-%d")) for spec in site["pages"] if spec["path"].strip("/")],
    ]
    body = "".join(
        f"  <url><loc>{site['base_url'].rstrip('/')}/{path}</loc><lastmod>{lastmod}</lastmod></url>\n"
        for path, lastmod in urls
    )
    write(
        "sitemap.xml",
        f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}</urlset>
""",
    )

    write(
        "robots.txt",
        f"User-agent: *\nAllow: /\n\nSitemap: {site['base_url'].rstrip('/')}/sitemap.xml\n",
    )

    write(
        "404.html",
        page(
            title=f"Page not found · {brand}",
            description="That page does not exist.",
            canonical=site["base_url"].rstrip("/") + "/404.html",
            content=f'<article class="page"><h1>Lost the thread</h1><p class="dek">That page is not here. The journal index has everything.</p><p><a class="button" href="{base}">Back to the journal</a></p></article>',
        ),
    )

    # ---- static assets
    for path in STATIC.rglob("*"):
        if path.is_file():
            rel = path.relative_to(STATIC)
            target = OUT / "assets" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)

    # ---- report
    print(f"built {len(posts)} posts, {len(categories)} categories -> {OUT}")
    problems = []
    for post in posts:
        flag = ""
        if post["words"] < WORD_MIN or post["words"] > WORD_MAX:
            flag = "  <-- outside 900-1300"
            problems.append(post["slug"])
        print(f"  {post['words']:>5} words  {post['slug']}{flag}")
    if "--check" in sys.argv and problems:
        raise SystemExit(f"word count out of range: {problems}")
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
