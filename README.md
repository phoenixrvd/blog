# Blog

Dieses Projekt enthält den Quellcode für meinen persönlichen [Blog](https://vwolf.eu).
Die Inhalte entstehen als Markdown-Dateien in [Obsidian](https://obsidian.md/) und werden anschließend
mit [MkDocs](https://www.mkdocs.org/) und dem [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)-Theme
zu einer statischen Website gerendert. Die Blog-Funktionalität wird von
[Blog-Plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/) bereitgestellt.

## Installation

Alle Projektabhängigkeiten in einer Python-Virtual-Environment installieren:

```bash
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Den Zitierstil importieren, um Quellen über [Zotero](https://www.zotero.org/) zu verwalten:

```bash
wget https://www.zotero.org/styles/ieee -O content/blog/ieee.csl
```

## Lokale Vorschau

Starte den Entwicklungsserver, um die Website lokal anzuzeigen:

```bash
source .venv/bin/activate
mkdocs serve --livereload
```

Alternativ kann die Website lokal gebaut werden, um den statischen Output zu prüfen.
Die generierten Dateien landen in `dist` und werden nicht committet:

```bash
source .venv/bin/activate
rm -rf dist/*
mkdocs build
```

## License

Code, build scripts, GitHub Actions, configuration files, and other technical parts of this repository are licensed under the MIT License. See [LICENSE](LICENSE).

Blogposts, texts, images, graphics, and other editorial content are licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0). See [CONTENT_LICENSE.md](CONTENT_LICENSE.md).
