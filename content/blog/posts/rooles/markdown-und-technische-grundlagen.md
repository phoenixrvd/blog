---
date: 1975-10-30
draft: true
description: "Markdown-Formatierung, technische Hinweise und Beispiele"
categories:
    - Blogging
---

# Markdown und technische Grundlagen

Dieses Blog wird im Markdown-Format geführt, enthält jedoch einige kleine Abweichungen vom Standardstil. Diese Abweichungen sind auf dieser Seite zusammengefasst.

<!-- more -->

## Worum es hier geht

- Frontmatter und Metadaten
- `<!-- more -->` als Trennlinie für die Vorschau
- Überschriften, Hervorhebungen und Listen
- Bilder, Captions und Ausrichtung
- Downloads und externe Links

## Grundregeln

- Die Länge liegt meist bei 1.500 bis 3.000 Wörtern, maximal bei 5.000 Wörtern
- Der Abstract steht vor `more` und hat keine eigene Überschrift
- Im Header stehen `description` und `categories`
- `h1` ist der Titel des Beitrags
- Literaturdaten werden mit Zotero gepflegt; die Datei `references.bib` wird immer nach `content/references.bib` exportiert und mit Zotero synchron gehalten

## Zitation und Literaturverwaltung

Für dieses Blog werden Zitationen über die zentrale BibTeX-Datei verwaltet. Als Stil wird je nach Beitrag ein passender Zitierstil verwendet (z. B. IEEE oder APA).

Beispiel für eine In-Text-Zitation [@LoremIpsumGenerator]:

`Wie bereits gezeigt [@LoremIpsumGenerator], verbessert ein konsistenter Stil die Lesbarkeit.`

Wichtig:
- Zotero ist die führende Quelle für Literaturdaten
- `content/references.bib` ist die einzige Datei, aus der zitiert wird
- Nach Änderungen in Zotero muss `references.bib` erneut nach `content/` exportiert werden

## Beispiele

![Wiki Logo](https://de.wikipedia.org/static/images/icons/wikipedia.png){:width=250px}
/// caption
Image caption [@LoremIpsumGenerator]
///


![Wiki Logo](https://de.wikipedia.org/static/images/icons/wikipedia.png){:width=250px align=left}

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,

sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,

![Wiki Logo](https://de.wikipedia.org/static/images/icons/wikipedia.png){:width=250px align=right}

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd

## Downloads

Hier wird eine Möglichkeit bereitgestellt, etwas als Download anzubieten.

[XY herunterladen](post_struktur/download.txt){:target="_blank" rel="noopener"}
