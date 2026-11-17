#!/usr/bin/env python3
"""Pre-publish audit for the built site in docs/.

Checks, in order:
  1. every internal link resolves to a file in docs/
  2. every XML file parses
  3. HTML tags balance in every page
  4. no personal identifiers leaked into the published output
  5. every post has a table or a checklist and the Gumroad cards

Run: python3 tools/audit.py       (exit 1 on any failure)
"""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = ROOT / "data"

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

GENERIC_PERSONAL = [
    r"[a-zA-Z0-9._%+-]+@(?:gmail|naver)\.com",
    r"\b010-?\d{4}-?\d{4}\b",
]

def load_personal_patterns() -> list[str]:
    patterns = list(GENERIC_PERSONAL)
    local_file = ROOT / ".audit_patterns.json"
    if local_file.exists():
        patterns.extend(json.loads(local_file.read_text(encoding="utf-8")))
    return patterns

failures: list[str] = []


class Balance(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"stray </{tag}>")
        elif self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.errors.append(f"unclosed <{self.stack.pop()}>")
            if self.stack:
                self.stack.pop()
        else:
            self.errors.append(f"unmatched </{tag}>")


def resolve(href: str, page: Path, base_path: str) -> Path | None:
    """Map a link in the built site to the file it should reach inside docs/."""
    if href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    parsed = urlparse(href)
    if parsed.scheme in ("http", "https"):
        if not href.startswith("https://theloz33-bot.github.io"):
            return None  # external, checked separately
        path = parsed.path
    else:
        path = parsed.path
        if not path:
            return None
        if not path.startswith("/"):
            target = (page.parent / path).resolve()
            if path.endswith("/") or target.is_dir():
                target = target / "index.html"
            return target

    if not path.startswith(base_path):
        # Another site on the same domain (the studio hub, the Korean journal) lives in
        # its own repository, so those links are external to this one.
        if path in ("", "/") or path.startswith(("/about/", "/privacy/", "/contact/",
                                                "/disclosure/", "/omong-kr-lab/")):
            return None
        return Path("/outside-site-base")  # fails existence check on purpose
    rel = path[len(base_path):]
    target = (DOCS / rel).resolve()
    if rel == "" or rel.endswith("/"):
        target = target / "index.html"
    elif target.is_dir():
        target = target / "index.html"
    return target


def main() -> int:
    if not DOCS.exists():
        sys.exit("docs/ missing — run python3 build.py first")

    site = json.loads((DATA / "site.json").read_text(encoding="utf-8"))
    base_path = site["base_path"]
    pages = sorted(DOCS.rglob("*.html"))
    if not pages:
        failures.append("no HTML output")

    # 1 + 2 + 3
    for page in pages:
        text = page.read_text(encoding="utf-8")

        for href in re.findall(r'(?:href|src)="([^"]+)"', text):
            target = resolve(href, page, base_path)
            if target is None:
                continue
            if not target.exists():
                failures.append(f"{page.relative_to(DOCS)}: broken link {href}")

        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                failures.append(f"{page.relative_to(DOCS)}: invalid JSON-LD ({exc})")

        parser = Balance()
        parser.feed(text)
        if parser.errors or parser.stack:
            failures.append(f"{page.relative_to(DOCS)}: HTML imbalance {parser.errors[:3]} open={parser.stack[:3]}")

    for xml_file in sorted(DOCS.glob("*.xml")):
        try:
            ET.parse(xml_file)
        except ET.ParseError as exc:
            failures.append(f"{xml_file.name}: XML parse error ({exc})")

    # 4
    personal_patterns = load_personal_patterns()
    for path in sorted(DOCS.rglob("*")):
        if not path.is_file() or path.suffix not in {".html", ".xml", ".css", ".txt", ".svg", ""}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        stripped = text.replace("theloz33-bot.github.io", "").replace("theloz33-bot", "")
        for pattern in personal_patterns:
            for match in re.finditer(pattern, stripped):
                line = stripped[max(0, match.start() - 40): match.end() + 40].replace("\n", " ")
                failures.append(f"{path.relative_to(DOCS)}: personal identifier '{match.group(0)}' near …{line}…")

    # 5
    for post in sorted((DOCS / "posts").glob("*/index.html")):
        text = post.read_text(encoding="utf-8")
        if "<table" not in text and "checklist" not in text:
            failures.append(f"{post.parent.name}: no table or checklist")
        if text.count("kit-card") < 3:
            failures.append(f"{post.parent.name}: Gumroad cards missing")
        if "sponsored" not in text:
            failures.append(f"{post.parent.name}: no sponsored/affiliate markup")

    # Advertising makes any "no cookies" claim false; the privacy policy is the only place
    # that describes what actually happens.
    for pattern in (r"\bno cookies\b(?! of its own)", r"\bno cookie\b(?! of its own)",
                    r"does not use cookies", r"never sets? (?:a )?cookies?"):
        for page in pages:
            if re.search(pattern, page.read_text(encoding="utf-8"), re.I):
                failures.append(f"{page.relative_to(DOCS)}: cookie claim contradicts advertising")

    for required in ("privacy/index.html", "contact/index.html"):
        if not (DOCS / required).exists():
            failures.append(f"missing required page: {required}")

    if failures:
        print("AUDIT FAILED")
        for item in failures:
            print("  -", item)
        return 1

    print(f"AUDIT OK — {len(pages)} pages, {len(list(DOCS.glob('*.xml')))} XML files, no personal identifiers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
