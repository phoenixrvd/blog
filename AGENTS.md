# AGENTS

## Repo at a glance
- MkDocs static blog: source is `content/`, generated output is `dist/` (`mkdocs.yml` sets `docs_dir: content`, `site_dir: dist`).
- `dist/` is generated and gitignored; do not treat it as source.
- Posts are German Markdown under `content/blog/posts/`; Material's blog plugin owns URLs/categories/pagination.
- Citation replacement runs through `mkdocs-simple-hooks` in `hooks.py` (`on_page_markdown: hooks:insert_zotero_references`).
- Theme overrides live in `overrides/`; `mkdocs.yml` watches only `overrides`, `content`, and itself.

## Required local setup
- Python deps: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
- `pandoc` must be installed on the system; citation rendering shells out to `pandoc --citeproc` and exits the build on citation errors.
- Citation files must be at `content/references.bib` and `content/ieee.csl`; the README's old `content/blog/ieee.csl` path is stale.

## Canonical commands
- Local preview: `source .venv/bin/activate && mkdocs serve --livereload`
- CI-equivalent build: `source .venv/bin/activate && mkdocs build --strict`
- Clean local build: `source .venv/bin/activate && rm -rf dist/* && mkdocs build --strict`
- No test/lint/typecheck automation is configured (no `pyproject.toml`, `tox.ini`, `Makefile`, package manifest, or pre-commit config); use `mkdocs build --strict` as verification.
- Never run a build after editing blog articles under `content/blog/posts/`, unless the user explicitly requests it.

## Branch and merge policy
- When asked to merge a branch into `main`, always use a squash merge; do not create a regular merge commit.
- Never push to any remote unless the user explicitly asks for it.
- Before squashing, inspect the branch commits and synthesize a short commit message that summarizes the branch as a whole.
- Prefer a concise subject line based on the commit subjects, then optionally add a brief body if it adds value.
- Typical flow for an instruction like "merge branch `x` into `main`":
    1. Review the branch commit subjects with `git log --oneline main..x`.
    2. Switch to `main`.
    3. Run `git merge --squash x`.
    4. Create the squash commit with the short summary message.
    5. Stop there unless the user explicitly requests a push.

## Verified conventions and gotchas
- GitHub Pages deploy runs on pushes to `main`, installs `pandoc`, then runs `mkdocs build --strict` and uploads `dist`.
- Keep blog frontmatter categories within `mkdocs.yml` `categories_allowed`, or strict builds can fail.
- Future-dated posts become drafts (`draft_if_future_date: true`); explicit drafts use `draft: true` in frontmatter.
- Use `<!-- more -->` for the blog excerpt separator; the abstract/intro before it should have no heading.
- Citation keys use Pandoc-style `[@Key]` and are replaced with numbered links plus a bibliography.
- Mermaid fences are configured in `mkdocs.yml`; PlantUML diagrams render through `http://www.plantuml.com/plantuml`, so local builds need network access for those diagrams.
- Editorial draft rules live under `content/blog/posts/rooles/`: German, clear/professional tone, usually 1,500-3,000 words, max about 5,000.
