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
LANGS = ("en", "zh")
KINDS_ZH = {"repo": "GitHub", "app": "应用", "post": "X", "reddit": "Reddit", "thread": "Hacker News", "video": "视频",
            "article": "文章", "model": "Hugging Face", "package": "软件包", "docs": "文档"}
T = {
    "en": {
        "switch": "**English** · [简体中文]({other})",
        "contents": "Contents", "browse": "Browse by Scenario", "contributing": "Contributing", "footnotes": "Footnotes",
        "browse_intro": "Highlights are ranked by community traction (stars, likes, points, and views). Open a scenario for its full gallery.",
        "browse_all": "Browse all {n} in {title} →", "see_all": "See all {n} {title} →", "also": "Also", "how": "How it uses Jev",
        "more": "{n} more", "back": "← Back to Awesome Jev", "ranked": " {n} entries, ranked by community traction.", "count": " {n} entries.",
        "missing": "Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).",
        "repo": " repo",
    },
    "zh": {
        "switch": "[English]({other}) · **简体中文**",
        "contents": "目录", "browse": "按场景浏览", "contributing": "参与贡献", "footnotes": "附注",
        "browse_intro": "精选按社区热度排序（star、点赞、得分和播放量）。点开场景查看完整画廊。",
        "browse_all": "查看{title}全部 {n} 条 →", "see_all": "查看全部 {n} 条{title} →", "also": "相关", "how": "Jev 用法",
        "more": "还有 {n} 条", "back": "← 返回 Awesome Jev", "ranked": "共 {n} 条，按社区热度排序。", "count": "共 {n} 条。",
        "missing": "还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。",
        "repo": " 仓库",
    },
}


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


def tr(obj, field, lang):
    return (obj.get(f"{field}_zh") if lang == "zh" else None) or obj.get(field) or ""


def link(e, lang):
    return (e.get("url_zh") if lang == "zh" else None) or e["url"]


def sec_title(sec, lang, emoji=False):
    t = tr(sec, "title", lang)
    return f"{sec['emoji']} {t}" if emoji else t


def meta_line(e, lang):
    bits = []
    if e.get("author"):
        bits.append(html.escape(e["author"]))
    bits.append((KINDS_ZH if lang == "zh" else KINDS)[e["kind"]])
    m = e.get("metrics") or {}
    for key, icon in METRICS:
        if m.get(key):
            bits.append(f"{icon} {compact(m[key])}" + (T[lang]["repo"] if key == "repo_stars" else ""))
            break
    if e.get("date"):
        bits.append(str(e["date"]))
    return " · ".join(bits)


def extra_links(e, lang):
    links = e.get("links") or {}
    if not links:
        return ""
    parts = [f'<a href="{html.escape(u)}">{html.escape(k)}</a>' for k, u in links.items()]
    return f"<br><sub>{T[lang]['also']}: " + " · ".join(parts) + "</sub>"


def card(e, lang):
    url, img, name = html.escape(link(e, lang)), image_of(e), tr(e, "name", lang)
    pic = f'<a href="{url}"><img src="{html.escape(img)}" alt="{html.escape(name)}" width="100%"></a><br>' if img else ""
    return (
        f'<td width="{100 // COLUMNS}%" valign="top">{pic}'
        f'<b><a href="{url}">{inline(name)}</a></b><br>'
        f"<sub>{meta_line(e, lang)}</sub><br>{inline(tr(e, 'description', lang))}</td>"
    )


def card_grid(entries, lang):
    rows = []
    for i in range(0, len(entries), COLUMNS):
        cells = [card(e, lang) for e in entries[i : i + COLUMNS]]
        cells += ['<td width="33%"></td>'] * (COLUMNS - len(cells))
        rows.append("<tr>\n" + "\n".join(cells) + "\n</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def gallery_row(e, lang):
    url, img, name = html.escape(link(e, lang)), image_of(e), tr(e, "name", lang)
    pic = f'<a href="{url}"><img src="{html.escape(img)}" alt="{html.escape(name)}" width="240"></a>' if img else ""
    jev = tr(e, "jev", lang)
    jev = f"<br><sub><b>{T[lang]['how']}:</b> {inline(jev)}</sub>" if jev else ""
    note = tr(e, "note", lang)
    note = f" <sub>({html.escape(note)})</sub>" if note else ""
    return (
        f'<tr>\n<td width="260" valign="top">{pic}</td>\n'
        f'<td valign="top"><b><a href="{url}">{inline(name)}</a></b>{note}<br>'
        f"<sub>{meta_line(e, lang)}</sub><br>{inline(tr(e, 'description', lang))}{jev}{extra_links(e, lang)}</td>\n</tr>"
    )


def readme_name(lang):
    return "README.md" if lang == "en" else "README.zh-CN.md"


def page_name(sec, sub=None, lang="en"):
    folder = "scenarios" if sec["group"] == "scenarios" else "pages"
    prefix = "" if lang == "en" else "zh-CN/"
    return f"{prefix}{folder}/{sec['slug']}" + (f"-{sub['slug']}" if sub else "") + ".md"


def page_url(sec, sub=None, lang="en"):
    return f"{REPO_URL}/blob/main/{page_name(sec, sub, lang)}"


def slugify(t):
    return re.sub(r"[^\w\- ]", "", t.lower()).replace(" ", "-")


def list_item(e, lang):
    desc = tr(e, "description", lang).strip()
    note = tr(e, "note", lang)
    if note:
        desc = desc[:-1] + (f"（{note}）" if lang == "zh" else f" ({note})") + desc[-1]
    return f"- [{tr(e, 'name', lang)}]({link(e, lang)}) - {desc}"


def render_list_section(sec, lang):
    out = [f"## {sec_title(sec, lang)}", ""]
    if tr(sec, "description", lang):
        out += [tr(sec, "description", lang), ""]
    subs = sec.get("subsections") or [{"title": None, "entries": sec.get("entries") or []}]
    for sub in subs:
        es = ranked(sub.get("entries") or [])
        if not es:
            continue
        if sub["title"]:
            out += [f"### {tr(sub, 'title', lang)}", ""]
        limit = len(es) if sec["group"] == "reference_top" else LIST_TEASER
        out += [list_item(e, lang) for e in es[:limit]] + [""]
        if len(es) > limit:
            label = tr(sub, "title", lang) if sub["title"] else sec_title(sec, lang)
            out += [f"**[{T[lang]['see_all'].format(n=len(es), title=label)}]({page_url(sec, sub if sub['title'] else None, lang)})**", ""]
    return out


def render_gallery_teaser(sec, lang, level=3):
    es = ranked(entries_of(sec))
    out = [f"{'#' * level} {sec_title(sec, lang, emoji=level == 3)}", "", tr(sec, "description", lang), ""]
    featured = pick_featured(es)
    if featured:
        out += [card_grid(featured, lang), ""]
    out += [f"**[{T[lang]['browse_all'].format(n=len(es), title=sec_title(sec, lang))}]({page_url(sec, lang=lang)})**", ""]
    return out


INTRO = {
    "en": [
        "> [Jev](https://typesafe.ai) is TypeSafe's System One model. It answers typed questions about text with calibrated probabilities instead of generating prose, so code can branch, sort, and route on its judgments.",
        "",
        "The most complete collection of what people build with Jev: **{total} projects, demos, posts, and write-ups**, gathered from GitHub, X, Reddit, Hacker News, YouTube, and the web, and organized by scenario. "
        "Every entry links to its original source and says what it does. "
        "Jev has three primitives: **Choice** picks one option, **Score** places something on an ordered scale, and **Noul** gives the probability that a statement is true.",
        "",
        "This list is community-maintained and not affiliated with TypeSafe. The official sites are `typesafe.ai` and `docs.typesafe.ai`, and the official GitHub organization is `typesafe-ai`. Be careful with look-alike domains that claim to be official.",
    ],
    "zh": [
        "> [Jev](https://typesafe.ai) 是 TypeSafe 的 System One 模型。它不生成文字，而是对文本回答带类型的问题，并给出校准过的概率，让代码可以直接根据它的判断分支、排序和路由。",
        "",
        "这里是最全的 Jev 用例合集：**{total} 个项目、演示、帖子和实测文章**，从 GitHub、X、Reddit、Hacker News、YouTube 和各类网站收集而来，按应用场景整理。"
        "每一条都链接到原始出处，并说明它具体做了什么。"
        "Jev 有三种原语：**Choice** 从选项中选一个，**Score** 在有序等级上打分，**Noul** 给出某个陈述为真的概率。",
        "",
        "本列表由社区维护，与 TypeSafe 官方无关。官方网站是 `typesafe.ai` 和 `docs.typesafe.ai`，官方 GitHub 组织是 `typesafe-ai`。请警惕自称官方的仿冒域名。",
    ],
}
OUTRO = {
    "en": [
        "Contributions welcome! Add an entry to the matching file in `data/`, run `uv run scripts/build.py`, and open a pull request. "
        "Read the [contribution guidelines](contributing.md) first, or [suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose) through an issue.",
        "Images are loaded from each project's own pages and belong to their owners. The list text is released under CC0.",
    ],
    "zh": [
        "欢迎贡献！不会写代码也没关系，[填一个表单](https://github.com/Li-Evan/awesome-jev/issues/new/choose)就能提交，X 上的一条演示也算。"
        "想直接改数据的话，在 `data/` 里对应场景的文件中加一条，运行 `uv run scripts/build.py`，然后提 PR。详见[贡献指南](contributing.zh-CN.md)。",
        "图片直接引用各项目自己的页面，版权归原作者所有。列表文字以 CC0 发布。",
    ],
}


def render_readme(order, sections, lang):
    t = T[lang]
    scen = [sections[s] for s in order["scenarios"] if entries_of(sections[s])]
    top = [sections[s] for s in order["reference_top"]]
    bottom = [sections[s] for s in order["reference_bottom"] if entries_of(sections[s])]
    total = sum(len(entries_of(s)) for s in sections.values())

    contents = [f"## {t['contents']}", ""]
    for s in top:
        contents.append(f"- [{sec_title(s, lang)}](#{slugify(sec_title(s, lang))})")
    contents.append(f"- [{t['browse']}](#{slugify(t['browse'])})")
    for s in scen:
        title = sec_title(s, lang, emoji=True)
        contents.append(f"  - [{title}](#{slugify(title)})")
    for s in bottom:
        contents.append(f"- [{sec_title(s, lang)}](#{slugify(sec_title(s, lang))})")
        for sub in s.get("subsections") or []:
            if sub.get("entries"):
                contents.append(f"  - [{tr(sub, 'title', lang)}](#{slugify(tr(sub, 'title', lang))})")

    cells = [f'<td><a href="{page_url(s, lang=lang)}">{s["emoji"]} {html.escape(sec_title(s, lang))}</a> <sub>{len(entries_of(s))}</sub></td>' for s in scen]
    overview = ["<table>"] + ["<tr>" + "".join(cells[i:i + 4]) + "</tr>" for i in range(0, len(cells), 4)] + ["</table>"]

    other = readme_name("zh" if lang == "en" else "en")
    out = [
        "# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        *[line.replace("{total}", f"{total:,}") for line in INTRO[lang][:1]],
        "",
        t["switch"].format(other=other),
        "",
        *[line.replace("{total}", f"{total:,}") for line in INTRO[lang][2:]],
        "",
        *contents,
        "",
    ]
    for s in top:
        out += render_list_section(s, lang)
    out += [f"## {t['browse']}", "", t["browse_intro"], "", "\n".join(overview), ""]
    for s in scen:
        out += render_gallery_teaser(s, lang)
    for s in bottom:
        out += render_gallery_teaser(s, lang, level=2) if s["layout"] == "gallery" else render_list_section(s, lang)
    out += [f"## {t['contributing']}", "", OUTRO[lang][0], "", f"## {t['footnotes']}", "", OUTRO[lang][1], ""]
    return "\n".join(out)


def compact_item(e, lang):
    note = tr(e, "note", lang)
    note = f" ({html.escape(note)})" if note else ""
    return f"- **[{tr(e, 'name', lang)}]({link(e, lang)})**{note} · <sub>{meta_line(e, lang)}</sub><br>{inline(tr(e, 'description', lang))}"


def gallery_block(entries, lang, image_rows=PAGE_IMAGE_ROWS):
    es = ranked(entries)
    out = ["<table>", *[gallery_row(e, lang) for e in es[:image_rows]], "</table>", ""]
    if len(es) > image_rows:
        out += [f"<details><summary>{T[lang]['more'].format(n=len(es) - image_rows)}</summary>", "", *[compact_item(e, lang) for e in es[image_rows:]], "", "</details>", ""]
    return out


def render_page(sec, lang, sub=None):
    t = T[lang]
    es = sub["entries"] if sub else entries_of(sec)
    readme = f"{REPO_URL}/blob/main/{readme_name(lang)}" if lang == "zh" else REPO_URL
    anchor = slugify(t["browse"]) if sec["group"] == "scenarios" else slugify(tr(sub, "title", lang) if sub else sec_title(sec, lang))
    title = sec_title(sec, lang, emoji=True) + (f": {tr(sub, 'title', lang)}" if sub else "")
    count = (t["count"] if any(e.get("pinned") for e in es) else t["ranked"]).format(n=len(es))
    other = page_url(sec, sub, "zh" if lang == "en" else "en")
    out = [
        f"# {title}",
        "",
        t["switch"].format(other=other),
        "",
        tr(sec, "description", lang) + count,
        "",
        f"[{t['back']}]({readme}#{anchor})",
        "",
    ]
    if sec.get("subsections"):
        subs = [x for x in sec["subsections"] if x.get("entries")]
        out += [" · ".join(f"**{tr(x, 'title', lang)}**" if x is sub else f"[{tr(x, 'title', lang)}]({page_url(sec, x, lang)}) ({len(x['entries'])})" for x in subs), ""]
    out += gallery_block(es, lang)
    out += [t["missing"], ""]
    return "\n".join(out)


def outputs():
    order, sections = load()
    count = validate(sections)
    files = {}
    for lang in LANGS:
        files[ROOT / readme_name(lang)] = render_readme(order, sections, lang)
        for s in order["scenarios"] + order["reference_bottom"]:
            sec = sections[s]
            if sec.get("subsections"):
                for sub in sec["subsections"]:
                    if sub.get("entries"):
                        files[ROOT / page_name(sec, sub, lang)] = render_page(sec, lang, sub)
            elif entries_of(sec):
                files[ROOT / page_name(sec, lang=lang)] = render_page(sec, lang)
    zh = sum(bool(e.get("description_zh")) for s in sections.values() for e in entries_of(s))
    return files, count, zh


def main():
    files, count, zh = outputs()
    stale = [p for p, text in files.items() if not p.exists() or p.read_text() != text]
    expected = set(files)
    dirs = ("scenarios", "pages", "zh-CN/scenarios", "zh-CN/pages")
    orphans = [p for d in dirs for p in (ROOT / d).glob("*.md") if p not in expected]
    coverage = f"{zh}/{count} entries have Chinese descriptions"
    if "--check" in sys.argv:
        if stale or orphans:
            fail("generated files are stale, run `uv run scripts/build.py`: " + ", ".join(str(p.relative_to(ROOT)) for p in stale + orphans))
        print(f"ok: {count} entries, generated files up to date ({coverage})")
        return
    for p in stale:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(files[p])
    for p in orphans:
        p.unlink()
    print(f"built {len(files)} files from {count} entries ({len(stale)} changed, {len(orphans)} removed; {coverage})")


if __name__ == "__main__":
    main()
