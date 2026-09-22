# Contribution Guidelines

**English** · [简体中文](contributing.zh-CN.md)

Thanks for helping make this the most complete collection of what people build with Jev. By contributing you agree to follow the [Code of Conduct](code-of-conduct.md).

## What belongs here

Anything real that uses Jev, TypeSafe's System One model, or helps people use it:

- Projects, apps, demos, and experiments, including posts on X, Reddit, or Hacker News that show something built.
- Integrations, SDKs, and open models that are compatible with Jev.
- Tutorials, benchmarks, case studies, talks, and videos.

Not accepted:

- Other people's lists and directories. Link the original project instead.
- Pure news rewrites, marketing pages, and look-alike sites that pretend to be official.
- Anything that leaks API keys or private data.

## The two rules

1. **Link the original.** The link must point to the project's own repository, app, post, article, or video. Never link another awesome list or directory; the build fails if you do.
2. **Say what it does.** One or two plain sentences: what it is, what it does, and, if you know, how it uses Jev (which primitive or pattern).

## How to add an entry

The READMEs and all gallery pages are generated. Do not edit `README.md`, `README.zh-CN.md`, `scenarios/`, `pages/`, or `zh-CN/` by hand.

1. Pick the scenario file in `data/`, for example `data/finance.yaml` or `data/coding.yaml`. Use `data/other.yaml` if nothing fits.
2. Add an entry:

   ```yaml
   - name: jev-ultrafast
     url: https://github.com/browser-use/jev-ultrafast
     kind: repo            # repo, app, post, reddit, thread, video, article, model, package, docs
     author: browser-use
     description: Browser agent that picks each step's action from the page's element table in one request.
     jev: One Choice per step with speculative targets per operation.   # optional
     image: https://raw.githubusercontent.com/owner/repo/main/screenshot.png   # optional
     metrics: {stars: 14484}   # optional: stars, likes, points, views, or downloads
     date: 2026-09-16          # optional: when it was published
     links: {demo: https://x.com/user/status/123}   # optional secondary links
   ```

3. Run the build and commit the result:

   ```bash
   uv run scripts/build.py
   ```

   `description_zh` (a Chinese description) is optional; the Chinese pages fall back to the English text.

4. Open a pull request. One project per pull request is easiest to review.

The website at <https://li-evan.github.io/awesome-jev/> is built from the same data (`index.html` and `site/data.json`), so it updates by itself once a change lands on `main`.

## Images

- Use an image from the project's own pages: a screenshot in its README, its `og:image`, the media in the original post, or the video thumbnail.
- Link the image where it lives; do not upload copies to this repository.
- Prefer PNG, JPEG, or WebP. Skip animated GIFs larger than about 3 MB.
- Without an image, GitHub repositories and YouTube videos fall back to their automatic preview card.

## Description style

- Start with a capital letter and end with a period.
- Describe the thing, not the hype: "Classifies IRS form pages with two Choices" beats "Revolutionary AI tax tool".
- Keep any number you quote identical to the source.

## Updating or removing

If a link is broken, a project is gone, or a description is wrong, open an issue or a pull request with a short explanation.
