"""Offline Markdown links, anchors, image and metadata checks."""
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted(p for p in ROOT.rglob("*.md") if not any(x in p.parts for x in [".git", "node_modules", ".venv"]))
errors = []
edges = {}
count = 0


def cleaned(text):
    text = re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def anchors(text):
    seen, result = {}, set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*$", cleaned(text), re.M):
        title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", title).lower()
        slug = "".join(c for c in title if c in "-_ " or unicodedata.category(c)[0] in "LN").replace(" ", "-")
        n = seen.get(slug, 0)
        seen[slug] = n + 1
        result.add(slug + ("-" + str(n) if n else ""))
    return result


texts = {p: p.read_text() for p in FILES}
for p, text in texts.items():
    if not text.strip():
        errors.append(str(p.relative_to(ROOT)) + ": empty document")
    body = cleaned(text)
    targets = re.findall(r'!?\[[^\n]*?\]\(([^\n]+?)\)', body)
    targets += re.findall(r'(?:src|href)=["\']([^"\']+)["\']', body)
    edges[p] = set()
    for raw in targets:
        url = raw.strip().split(' "')[0].strip("<>")
        parts = urlsplit(url)
        if parts.scheme or parts.netloc:
            continue
        target = (p.parent / unquote(parts.path)).resolve() if parts.path else p
        count += 1
        if not target.is_relative_to(ROOT):
            errors.append(f"{p.relative_to(ROOT)}: outside repository: {url}")
        elif not target.exists():
            errors.append(f"{p.relative_to(ROOT)}: missing: {url}")
        elif target.is_file() and target.suffix == ".md":
            edges[p].add(target)
            if parts.fragment and unquote(parts.fragment) not in anchors(texts.get(target, target.read_text())):
                errors.append(f"{p.relative_to(ROOT)}: missing anchor: {url}")
        if target.is_file() and target.suffix.lower() in {".jpg", ".png", ".svg", ".webp"} and target.stat().st_size == 0:
            errors.append(f"{p.relative_to(ROOT)}: empty image: {url}")

required = ["book", "roadmap", "playbook", "toolkit", "cookbook", "cases", "projects", "resources"]
for module in required:
    if not (ROOT / module / "README.md").is_file():
        errors.append("Missing module index: " + module)
chapters = json.loads((ROOT / "book/chapters.json").read_text())
assert [c["number"] for c in chapters] == list(range(1, 13))
for c in chapters:
    if not (ROOT / "book/chapters" / (str(c["number"]).zfill(2) + ".md")).exists():
        errors.append("Missing chapter: " + str(c["number"]))
for file, key in [("cases/catalog.json", "id"), ("resources/catalog.json", "repository")]:
    data = json.loads((ROOT / file).read_text())
    if len({x[key] for x in data}) != len(data):
        errors.append("Duplicate records in " + file)
print(json.dumps({"markdown_files": len(FILES), "internal_links_checked": count,
                  "errors": len(errors)}, ensure_ascii=False))
for error in errors:
    print(error)
sys.exit(bool(errors))
