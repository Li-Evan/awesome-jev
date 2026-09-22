# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "httpx"]
# ///
"""Check every hotlinked image in data/*.yaml.

Usage:
  uv run scripts/check_images.py          # report broken images
  uv run scripts/check_images.py --fix    # drop broken or oversized images so the build falls back
"""

import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx
import yaml

DATA = Path(__file__).resolve().parent.parent / "data"
MAX_BYTES = 6_000_000
HEADERS = {"User-Agent": "Mozilla/5.0 (awesome-jev image check)", "Range": "bytes=0-2047"}


def entries():
    for path in sorted(DATA.glob("*.yaml")):
        if path.name == "sections.yaml":
            continue
        doc = yaml.safe_load(path.read_text())
        for sub in doc.get("subsections") or [doc]:
            for e in sub.get("entries") or []:
                if e.get("image"):
                    yield path, e


def check(url):
    try:
        with httpx.Client(follow_redirects=True, timeout=20, headers=HEADERS) as c:
            r = c.get(url)
        kind = r.headers.get("content-type", "")
        size = r.headers.get("content-range", "").rpartition("/")[2] or r.headers.get("content-length", "0")
        size = int(size) if size.isdigit() else 0
        if r.status_code not in (200, 206):
            return f"HTTP {r.status_code}"
        if not kind.startswith("image/"):
            return f"not an image ({kind or 'no content-type'})"
        if size > MAX_BYTES:
            return f"too large ({size // 1_000_000} MB)"
        return None
    except httpx.HTTPError as err:
        return type(err).__name__


def main():
    items = list(entries())
    urls = sorted({e["image"] for _, e in items})
    with ThreadPoolExecutor(32) as pool:
        results = dict(zip(urls, pool.map(check, urls)))
    bad = {u: why for u, why in results.items() if why}
    print(f"{len(urls)} images checked, {len(bad)} broken")
    for u, why in sorted(bad.items(), key=lambda x: x[1]):
        print(f"  {why}: {u}")
    if "--fix" in sys.argv and bad:
        for path in sorted({p for p, _ in items}):
            doc = yaml.safe_load(path.read_text())
            changed = False
            for sub in doc.get("subsections") or [doc]:
                for e in sub.get("entries") or []:
                    if e.get("image") in bad:
                        del e["image"]
                        changed = True
            if changed:
                path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=1000))
        print("removed broken images; run `uv run scripts/build.py`")
    elif bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
