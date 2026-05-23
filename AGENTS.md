# AGENTS

## Repo at a glance
- MkDocs static blog: source is `content/`, generated output is `dist/` (`mkdocs.yml` sets `docs_dir: content`, `site_dir: dist`).
- `dist/` is generated and gitignored; do not treat it as source.
- Posts are German Markdown under `content/blog/posts/`; Material's blog plugin owns URLs/categories/pagination.
- Citation replacement runs through `mkdocs-simple-hooks` in `hooks.py` (`on_page_markdown: hooks:insert_zotero_references`).

## Required local setup
- Python deps: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
- `pandoc` must be installed on the system; citation rendering shells out to `pandoc --citeproc` and exits the build on citation errors.
- Citation files must be at `content/references.bib` and `content/ieee.csl`; trust `hooks.py`/`mkdocs.yml` over README if paths differ.

## Canonical commands
- Local preview: `source .venv/bin/activate && mkdocs serve --livereload`
- CI-equivalent build: `source .venv/bin/activate && mkdocs build --strict`
- Clean local build: `source .venv/bin/activate && rm -rf dist/* && mkdocs build --strict`

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
- No test/lint/typecheck automation is configured (no `pyproject.toml`, `tox.ini`, `Makefile`, or package manifest present); use the MkDocs build as verification.
- GitHub Pages deploy runs on pushes to `main`, installs `pandoc`, then runs `mkdocs build --strict` and uploads `dist`.
- Keep blog frontmatter categories within `mkdocs.yml` `categories_allowed`, or strict builds can fail.
- Use `<!-- more -->` for the blog excerpt separator; citation keys use Pandoc-style `[@Key]` and are replaced with numbered links plus a bibliography.
