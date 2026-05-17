# AGENTS

## Repo at a glance
- This is a MkDocs static blog project (German content) with source in `content/` and output in `dist/` (`mkdocs.yml` sets `docs_dir: content`, `site_dir: dist`).
- Citation replacement is implemented via `mkdocs-simple-hooks` in `hooks.py` (`on_page_markdown: hooks:insert_zotero_references`).

## Required local setup
- Python deps: `pip install -r requirements.txt`.
- `pandoc` must be installed on the system; citation rendering in `hooks.py` shells out to `pandoc --citeproc` and build fails (`SystemExit(1)`) if that call errors.
- Citation files expected by the hook: `content/references.bib` and `content/ieee.csl`.

## Canonical commands
- Local preview: `source .venv/bin/activate && mkdocs serve --livereload`
- Static build: `source .venv/bin/activate && rm -rf dist/* && mkdocs build`

## Verified conventions and gotchas
- No test/lint/typecheck automation is configured in this repo (no `pyproject.toml`, `tox.ini`, or `Makefile` present).
- Prefer treating config as source of truth over README prose when they differ (e.g., `dist` is gitignored in `.gitignore`).
