# Blog

Dieses Projekt enthält den Quellcode für meinen persönlichen [Blog](https://vwolf.eu).
Die Inhalte entstehen als Markdown-Dateien in [Obsidian](https://obsidian.md/) und werden anschließend
mit [MkDocs](https://www.mkdocs.org/) und dem [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)-Theme
zu einer statischen Website gerendert. Die Blog-Funktionalität wird von
[Blog-Plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/) bereitgestellt.

## Installation

Python und Pandoc installieren (Debian/Ubuntu). Pandoc wird für die Verarbeitung
der Quellenangaben mit `--citeproc` benötigt:

```bash
sudo apt update
sudo apt install python3 python3-venv pandoc
```

Anschließend im Projektverzeichnis eine virtuelle Python-Umgebung erstellen und
die Projektabhängigkeiten installieren:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Die direkten Python-Abhängigkeiten sind in `requirements.txt` auf konkrete Versionen
festgelegt; indirekte Abhängigkeiten löst pip auf. Der technische Stand wurde mit
Python 3.14.4 geprüft.

Quellen werden über [Zotero](https://www.zotero.org/) verwaltet. Die Bibliografie liegt
unter `content/references.bib`, der Zitierstil unter `content/ieee.csl`. Beide Dateien
sind bereits im Repository enthalten. Um den IEEE-Zitierstil bei Bedarf zu aktualisieren:

```bash
wget https://www.zotero.org/styles/ieee -O content/ieee.csl
```

## Lokale Vorschau

Starte den Entwicklungsserver, um die Website lokal anzuzeigen:

```bash
source .venv/bin/activate
mkdocs serve --livereload
```

Alternativ kann die Website lokal gebaut werden, um den statischen Output zu prüfen.
Der strikte Build entspricht der Prüfung in GitHub Actions. Die generierten Dateien
landen in `dist/`, werden beim Build standardmäßig bereinigt und nicht committet:

```bash
source .venv/bin/activate
mkdocs build --strict
```

## Python-Abhängigkeiten aktualisieren

In der aktivierten virtuellen Umgebung nach neueren Versionen suchen:

```bash
python -m pip list --outdated
```

Die gewünschten Versionsangaben in `requirements.txt` anpassen, anschließend
installieren und prüfen:

```bash
python -m pip install --upgrade -r requirements.txt
python -m pip check
mkdocs build --strict
```

## License

Code, build scripts, GitHub Actions, configuration files, and other technical parts of this repository are licensed under the MIT License. See [LICENSE](LICENSE).

Blogposts, texts, images, graphics, and other editorial content are licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0). See [CONTENT_LICENSE.md](CONTENT_LICENSE.md).
