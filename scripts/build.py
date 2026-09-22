# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Render README.md and scenarios/*.md from data/*.yaml.

Usage:
  uv run scripts/build.py          # write files
  uv run scripts/build.py --check  # fail if generated files are stale or data is invalid
"""

import html
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPO_URL = "https://github.com/Li-Evan/awesome-jev"
FEATURED = 6
COLUMNS = 3
LIST_TEASER = 10
PAGE_IMAGE_ROWS = 150

KINDS = {
    "repo": "GitHub",
    "app": "App",
    "post": "X",
    "reddit": "Reddit",
    "thread": "Hacker News",
    "video": "YouTube",
    "article": "Article",
    "model": "Hugging Face",
    "package": "Package",
    "docs": "Docs",
}
METRICS = [("stars", "⭐"), ("likes", "♥"), ("points", "▲"), ("views", "▶"), ("downloads", "⬇"), ("repo_stars", "⭐")]

# Other people's lists and directories: discovery sources only, never link targets.
AGGREGATORS = {
    "github.com/yibie/awesome-jev", "github.com/logicrw/awesome-jev-projects", "github.com/hellogumbo/awesome-jev",
    "github.com/abdelstark/awesome-typesafe-jev", "github.com/cobanov/awesome-jev", "github.com/v-modal/awesome-jev-tools",
    "github.com/fatwang2/awesome-jev", "github.com/anotiawang/awesome-jev", "github.com/valentynkit/awesome-jev-typesafe",
    "github.com/yzfly/awesome-jev-zh", "github.com/keltokhy/awesome-jev-typesafe", "github.com/omnijev/awesome-jev-gallery",
    "github.com/anil-matcha/awesome-jev-by-typesafe", "madewithjev.com", "jevable.com", "jev.directory",
    "academy.dair.ai/resources/jev-field-notes",
}
REQUIRED = ("name", "url", "kind", "description")


def fail(msg):
    sys.exit(f"build error: {msg}")


def load():
    order = yaml.safe_load((DATA / "sections.yaml").read_text())
    sections = {}
    for group in ("reference_top", "scenarios", "reference_bottom"):
        for slug in order[group]:
            path = DATA / f"{slug}.yaml"
            if not path.exists():
                fail(f"missing {path.name}")
            sec = yaml.safe_load(path.read_text())
            sec["slug"], sec["group"] = slug, group
            sections[slug] = sec
    return order, sections


def entries_of(sec):
    if "subsections" in sec:
        return [e for sub in sec["subsections"] for e in sub.get("entries") or []]
    return sec.get("entries") or []


def is_aggregator(url):
    p = urlparse(url.lower())
    host = p.netloc.removeprefix("www.")
    path = host + p.path.rstrip("/")
    return any(path == a or path.startswith(a + "/") for a in AGGREGATORS)


def validate(sections):
    seen = {}
    for sec in sections.values():
        for e in entries_of(sec):
            where = f"{sec['slug']}: {e.get('name', '?')}"
            for field in REQUIRED:
                if not e.get(field):
                    fail(f"{where} is missing '{field}'")
            if e["kind"] not in KINDS:
                fail(f"{where} has unknown kind '{e['kind']}'")
            if not e["url"].startswith("https://"):
                fail(f"{where} url must start with https://")
            if is_aggregator(e["url"]):
                fail(f"{where} links to an aggregator list; link the original source instead")
            key = e["url"].rstrip("/").lower()
            if key in seen:
                fail(f"duplicate url {e['url']} in {where} and {seen[key]}")
            seen[key] = where
            d = e["description"].strip()
            first = next((c for c in d if c.isalnum()), "")
            if not (first.isupper() or first.isdigit()):
                fail(f"{where} description must start with a capital letter")
            if not d.endswith((".", "!", "?")):
                fail(f"{where} description must end with a period")
    return len(seen)


def heat(e):
    m = e.get("metrics") or {}
    return max(
        m.get("stars", 0), m.get("likes", 0), 3 * m.get("points", 0),
        m.get("views", 0) / 50, m.get("downloads", 0) / 100, m.get("repo_stars", 0) / 20,
    )


def ranked(entries):
    pinned = [e for e in entries if e.get("pinned")]
    rest = sorted((e for e in entries if not e.get("pinned")), key=lambda e: (not e.get("featured", False), -heat(e), e["name"].lower()))
    return pinned + rest


def real_image(e):
    return bool(e.get("image")) or e["kind"] == "video"


def pick_featured(entries):
    pool = [e for e in entries[:15] if image_of(e)]
    return sorted(pool, key=lambda e: (not real_image(e), -heat(e)))[:FEATURED]


def image_of(e):
    if e.get("image"):
        return e["image"]
    p = urlparse(e["url"])
    parts = [x for x in p.path.split("/") if x]
    if p.netloc == "github.com" and len(parts) >= 2:
        return f"https://opengraph.githubassets.com/1/{parts[0]}/{parts[1]}"
    m = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", e["url"])
    if m:
        return f"https://i.ytimg.com/vi/{m[1]}/hqdefault.jpg"
    return None


def compact(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M".replace(".0M", "M")
    if n >= 1_000:
        return f"{n / 1_000:.1f}k".replace(".0k", "k")
    return str(int(n))


def inline(text):
    out = html.escape(text.strip(), quote=False)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", out)


def meta_line(e):
    bits = []
    if e.get("author"):
        bits.append(html.escape(e["author"]))
    bits.append(KINDS[e["kind"]])
    m = e.get("metrics") or {}
    for key, icon in METRICS:
        if m.get(key):
            bits.append(f"{icon} {compact(m[key])}" + (" repo" if key == "repo_stars" else ""))
            break
    if e.get("date"):
        bits.append(str(e["date"]))
    return " · ".join(bits)


def extra_links(e):
    links = e.get("links") or {}
    if not links:
        return ""
    parts = [f'<a href="{html.escape(u)}">{html.escape(k)}</a>' for k, u in links.items()]
    return "<br><sub>Also: " + " · ".join(parts) + "</sub>"


def card(e):
    url, img = html.escape(e["url"]), image_of(e)
    pic = f'<a href="{url}"><img src="{html.escape(img)}" alt="{html.escape(e["name"])}" width="100%"></a><br>' if img else ""
    return (
        f'<td width="{100 // COLUMNS}%" valign="top">{pic}'
        f'<b><a href="{url}">{inline(e["name"])}</a></b><br>'
        f"<sub>{meta_line(e)}</sub><br>{inline(e['description'])}</td>"
    )


def card_grid(entries):
    rows = []
    for i in range(0, len(entries), COLUMNS):
        cells = [card(e) for e in entries[i : i + COLUMNS]]
        cells += ['<td width="33%"></td>'] * (COLUMNS - len(cells))
        rows.append("<tr>\n" + "\n".join(cells) + "\n</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def gallery_row(e):
    url, img = html.escape(e["url"]), image_of(e)
    pic = f'<a href="{url}"><img src="{html.escape(img)}" alt="{html.escape(e["name"])}" width="240"></a>' if img else ""
    jev = f"<br><sub><b>How it uses Jev:</b> {inline(e['jev'])}</sub>" if e.get("jev") else ""
    note = f" <sub>({html.escape(e['note'])})</sub>" if e.get("note") else ""
    return (
        f'<tr>\n<td width="260" valign="top">{pic}</td>\n'
        f'<td valign="top"><b><a href="{url}">{inline(e["name"])}</a></b>{note}<br>'
        f"<sub>{meta_line(e)}</sub><br>{inline(e['description'])}{jev}{extra_links(e)}</td>\n</tr>"
    )


def page_name(sec, sub=None):
    folder = "scenarios" if sec["group"] == "scenarios" else "pages"
    return f"{folder}/{sec['slug']}" + (f"-{sub['slug']}" if sub else "") + ".md"


def page_url(sec, sub=None):
    return f"{REPO_URL}/blob/main/{page_name(sec, sub)}"


def slugify(t):
    return re.sub(r"[^\w\- ]", "", t.lower()).replace(" ", "-")


def list_item(e):
    note = f" ({e['note']})" if e.get("note") else ""
    desc = e["description"].strip()
    if note:
        desc = desc[:-1] + note + desc[-1]
    return f"- [{e['name']}]({e['url']}) - {desc}"


def render_list_section(sec):
    out = [f"## {sec['title']}", ""]
    if sec.get("description"):
        out += [sec["description"], ""]
    subs = sec.get("subsections") or [{"title": None, "entries": sec.get("entries") or []}]
    for sub in subs:
        es = ranked(sub.get("entries") or [])
        if not es:
            continue
        if sub["title"]:
            out += [f"### {sub['title']}", ""]
        limit = len(es) if sec["group"] == "reference_top" else LIST_TEASER
        out += [list_item(e) for e in es[:limit]] + [""]
        if len(es) > limit:
            out += [f"**[See all {len(es)} {sub['title'] or sec['title']} →]({page_url(sec, sub if sub['title'] else None)})**", ""]
    return out


def render_gallery_teaser(sec, level=3):
    es = ranked(entries_of(sec))
    title = f"{sec['emoji']} {sec['title']}" if level == 3 else sec["title"]
    out = [f"{'#' * level} {title}", "", sec["description"], ""]
    featured = pick_featured(es)
    if featured:
        out += [card_grid(featured), ""]
    out += [f"**[Browse all {len(es)} in {sec['title']} →]({page_url(sec)})**", ""]
    return out


def render_readme(order, sections):
    scen = [sections[s] for s in order["scenarios"] if entries_of(sections[s])]
    top = [sections[s] for s in order["reference_top"]]
    bottom = [sections[s] for s in order["reference_bottom"] if entries_of(sections[s])]
    total = sum(len(entries_of(s)) for s in sections.values())

    contents = ["## Contents", ""]
    for s in top:
        contents.append(f"- [{s['title']}](#{slugify(s['title'])})")
    contents.append("- [Browse by Scenario](#browse-by-scenario)")
    for s in scen:
        t = f"{s['emoji']} {s['title']}"
        contents.append(f"  - [{t}](#{slugify(t)})")
    for s in bottom:
        contents.append(f"- [{s['title']}](#{slugify(s['title'])})")
        for sub in s.get("subsections") or []:
            if sub.get("entries"):
                contents.append(f"  - [{sub['title']}](#{slugify(sub['title'])})")

    cells = [f'<td><a href="{page_url(s)}">{s["emoji"]} {html.escape(s["title"])}</a> <sub>{len(entries_of(s))}</sub></td>' for s in scen]
    overview = ["<table>"] + ["<tr>" + "".join(cells[i:i + 4]) + "</tr>" for i in range(0, len(cells), 4)] + ["</table>"]

    out = [
        "# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> [Jev](https://typesafe.ai) is TypeSafe's System One model. It answers typed questions about text with calibrated probabilities instead of generating prose, so code can branch, sort, and route on its judgments.",
        "",
        f"The most complete collection of what people build with Jev: **{total:,} projects, demos, posts, and write-ups**, gathered from GitHub, X, Reddit, Hacker News, YouTube, and the web, and organized by scenario. "
        "Every entry links to its original source and says what it does. "
        "Jev has three primitives: **Choice** picks one option, **Score** places something on an ordered scale, and **Noul** gives the probability that a statement is true.",
        "",
        "This list is community-maintained and not affiliated with TypeSafe. The official sites are `typesafe.ai` and `docs.typesafe.ai`, and the official GitHub organization is `typesafe-ai`. Be careful with look-alike domains that claim to be official.",
        "",
        *contents,
        "",
    ]
    for s in top:
        out += render_list_section(s)
    out += ["## Browse by Scenario", "", "Highlights are ranked by community traction (stars, likes, points, and views). Open a scenario for its full gallery.", "", "\n".join(overview), ""]
    for s in scen:
        out += render_gallery_teaser(s)
    for s in bottom:
        out += render_gallery_teaser(s, level=2) if s["layout"] == "gallery" else render_list_section(s)
    out += [
        "## Contributing",
        "",
        "Contributions welcome! Add an entry to the matching file in `data/`, run `uv run scripts/build.py`, and open a pull request. "
        "Read the [contribution guidelines](contributing.md) first, or [suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose) through an issue.",
        "",
        "## Footnotes",
        "",
        "Images are loaded from each project's own pages and belong to their owners. The list text is released under CC0.",
        "",
    ]
    return "\n".join(out)


def compact_item(e):
    note = f" ({html.escape(e['note'])})" if e.get("note") else ""
    return f"- **[{e['name']}]({e['url']})**{note} · <sub>{meta_line(e)}</sub><br>{inline(e['description'])}"


def gallery_block(entries, image_rows=PAGE_IMAGE_ROWS):
    es = ranked(entries)
    out = ["<table>", *[gallery_row(e) for e in es[:image_rows]], "</table>", ""]
    if len(es) > image_rows:
        out += [f"<details><summary>{len(es) - image_rows} more</summary>", "", *[compact_item(e) for e in es[image_rows:]], "", "</details>", ""]
    return out


def render_page(sec, sub=None):
    es = sub["entries"] if sub else entries_of(sec)
    back = "#browse-by-scenario" if sec["group"] == "scenarios" else f"#{slugify(sub['title'] if sub else sec['title'])}"
    title = f"{sec['emoji']} {sec['title']}" + (f": {sub['title']}" if sub else "")
    out = [
        f"# {title}",
        "",
        f"{sec['description']} {len(es)} entries" + (", ranked by community traction." if not any(e.get("pinned") for e in es) else "."),
        "",
        f"[← Back to Awesome Jev]({REPO_URL}{back})",
        "",
    ]
    if sec.get("subsections"):
        subs = [x for x in sec["subsections"] if x.get("entries")]
        out += [" · ".join(f"**{x['title']}**" if x is sub else f"[{x['title']}]({page_url(sec, x)}) ({len(x['entries'])})" for x in subs), ""]
    out += gallery_block(es)
    out += ["Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).", ""]
    return "\n".join(out)


def outputs():
    order, sections = load()
    count = validate(sections)
    files = {ROOT / "README.md": render_readme(order, sections)}
    for s in order["scenarios"] + order["reference_bottom"]:
        sec = sections[s]
        if sec.get("subsections"):
            for sub in sec["subsections"]:
                if sub.get("entries"):
                    files[ROOT / page_name(sec, sub)] = render_page(sec, sub)
        elif entries_of(sec):
            files[ROOT / page_name(sec)] = render_page(sec)
    return files, count


def main():
    files, count = outputs()
    stale = [p for p, text in files.items() if not p.exists() or p.read_text() != text]
    expected = set(files)
    orphans = [p for d in ("scenarios", "pages") for p in (ROOT / d).glob("*.md") if p not in expected]
    if "--check" in sys.argv:
        if stale or orphans:
            fail("generated files are stale, run `uv run scripts/build.py`: " + ", ".join(str(p.relative_to(ROOT)) for p in stale + orphans))
        print(f"ok: {count} entries, generated files up to date")
        return
    for p in stale:
        p.parent.mkdir(exist_ok=True)
        p.write_text(files[p])
    for p in orphans:
        p.unlink()
    print(f"built {len(files)} files from {count} entries ({len(stale)} changed, {len(orphans)} removed)")


if __name__ == "__main__":
    main()
