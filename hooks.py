import re
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup

RE_CITATION = re.compile(r"\[@([A-Za-z0-9:_-]+)]")


def _refs_from_markdown(text, csl_path, bib_path, *, strict=False):
    try:
        html = subprocess.run(
        [
            "pandoc",
            "--from",
            "markdown",
            "--to",
            "html",
            "--citeproc",
            "--csl",
            str(csl_path),
            "--bibliography",
            str(bib_path),
        ],
        input=text,
        text=True,
        capture_output=True,
        check=True,
    ).stdout
    except subprocess.CalledProcessError:
        if strict:
            raise
        return None

    return BeautifulSoup(html, "html.parser").find(id="refs")


def insert_zotero_references(markdown, page, config, files, **kwargs):
    """Replace Zotero keys with numbered refs and append bibliography HTML."""
    keys = RE_CITATION.findall(markdown)
    if not keys:
        return markdown

    unique_keys = list(dict.fromkeys(keys))
    key_to_number = {key: i for i, key in enumerate(unique_keys, 1)}

    docs_dir = Path(config.get("docs_dir", "."))
    bib_path = docs_dir / "references.bib"
    csl_path = docs_dir / "ieee.csl"

    try:
        refs_node = _refs_from_markdown(markdown, csl_path, bib_path, strict=True)
    except subprocess.CalledProcessError as e:
        print(f"Pandoc failed ({e.returncode}): {e.stderr.strip()}")
        raise SystemExit(1)

    # Pandoc ignores citations inside code spans/fences; generate refs from synthetic citations.
    if refs_node is None:
        refs_node = _refs_from_markdown(
            "\n".join(f"[@{key}]" for key in unique_keys),
            csl_path,
            bib_path,
        )

    if refs_node is None:
        # If refs cannot be generated at all, keep markdown untouched.
        return markdown

    classes = refs_node.get("class") or []
    if isinstance(classes, str):
        classes = classes.split()
    if "footnote" not in classes:
        classes.append("footnote")
    refs_node["class"] = " ".join(classes)

    def replace_key(m):
        key = m.group(1)
        return f"[[{key_to_number[key]}]](#ref-{key})"

    return f"{RE_CITATION.sub(replace_key, markdown)}<hr>{refs_node}"
