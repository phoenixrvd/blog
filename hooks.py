import re
import subprocess
from bs4 import BeautifulSoup


def insert_zotero_references(markdown, page, config, files, **kwargs):
    """
    Replaces Zotero citation keys in Markdown text (e.g., [@Mueller2021])
    with numbered IEEE-style reference links (e.g., [[1]](#ref-Mueller2021))
    and appends the generated bibliography at the end of the page.

    Requirements:
        - The Markdown text contains at least one citation key [@...]
        - The docs_dir contains the files references.bib and ieee.csl
    """
    RE_CITATION = r"\[@([A-Za-z0-9:_-]+)\]"

    keys = re.findall(RE_CITATION, markdown)
    if not keys:
        return markdown

    docs_dir = config.get("docs_dir", ".")
    bib_path = f"{docs_dir}/references.bib"
    csl_path = f"{docs_dir}/ieee.csl"

    try:
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
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error while running Pandoc:")
        print(f"  Command: {' '.join(e.cmd)}")
        print(f"  Return code: {e.returncode}")

        if e.stderr:
            print(f"\n{markdown}\n\n🔍 Pandoc stderr output:\n{e.stderr.strip()}")

        raise SystemExit(1)

    refs_node = BeautifulSoup(result.stdout, "html.parser").find(id="refs")
    refs_node['class'].append('footnote')

    unique_keys = list(dict.fromkeys(keys))  # Remove duplicates, preserve order

    def replace_key(m):
        key = m.group(1)
        num = unique_keys.index(key) + 1
        return f"[[{num}]](#ref-{key})"

    markdown = re.sub(RE_CITATION, replace_key, markdown)
    return f"{markdown}<hr>{refs_node}"
