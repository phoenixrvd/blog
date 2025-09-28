import re
import subprocess
from bs4 import BeautifulSoup


def insert_zotero_references(markdown, page, config, files, **kwargs):
    """
    Ersetzt Zotero-Zitationskeys im Markdown-Text (z. B. [@Müller2021])
    durch durchnummerierte Referenzlinks im IEEE-Stil (z. B. [[1]](#ref-Müller2021))
    und fügt am Ende der Seite die generierte Bibliographie ein.

    Voraussetzungen:
        - Der Markdown-Text enthält mindestens einen Zitationskey [@...]
        - Im docs_dir liegen die Dateien references.bib und ieee.csl
    """
    RE_CITATION = r"\[@([A-Za-z0-9:_-]+)\]"

    keys = re.findall(RE_CITATION, markdown)
    if not keys:
        return markdown

    docs_dir = config.get("docs_dir", ".")
    bib_path = f"{docs_dir}/references.bib"
    csl_path = f"{docs_dir}/ieee.csl"

    result = subprocess.run(
        [
            "pandoc",
            "--from", "markdown",
            "--to", "html",
            "--citeproc",
            "--csl", csl_path,
            "--bibliography", bib_path,
        ],
        input=markdown,
        text=True,
        capture_output=True,
        check=True,
    )

    refs_node = BeautifulSoup(result.stdout, "html.parser").find(id="refs")
    refs_node['class'].append('footnote')

    unique_keys = list(dict.fromkeys(keys))  # Duplikate entfernen, Reihenfolge behalten

    def replace_key(m):
        key = m.group(1)
        num = unique_keys.index(key) + 1
        return f"[[{num}]](#ref-{key})"

    markdown = re.sub(RE_CITATION, replace_key, markdown)
    return f"{markdown}<hr>{refs_node}"
