---
date: 2026-05-23
description: "Warum Code Coverage kein Qualitätsbeweis ist, aber als Indikator für technische Verschwendung und ungenutzten Code hilft."
categories:
    - Software Qualität
    - Legacy
---

# Code Coverage als Indikator für technische Verschwendung

In vielen Softwaresystemen existiert Code, dessen fachliche Relevanz niemand mehr sicher erklären kann. Code Coverage wird meist als Qualitätsmetrik diskutiert. Dabei kann sie in einem ganz anderen Kontext besonders nützlich sein: als Werkzeug, um technische Verschwendung sichtbar zu machen.

<!-- more -->

Features wachsen, Anforderungen ändern sich, Übergangslösungen bleiben bestehen und historische Sonderfälle überleben oft deutlich länger als geplant. So entsteht technische Komplexität, deren fachlicher Nutzen nicht immer klar ist. Als Qualitätsbeweis ist Coverage begrenzt aussagekräftig: Empirische Untersuchungen zeigen, dass Coverage nur begrenzt mit tatsächlicher Testeffektivität korreliert [@inozemtsevaCoverageNotStrongly2014], und auch Martin Fowler warnt davor, sie als Qualitätsbeweis zu interpretieren. [@fowlerTestCoverage] Als Sichtbarkeitswerkzeug kann Coverage dagegen sehr nützlich sein.

## Was Code Coverage eigentlich misst

Je nach Werkzeug betrachtet Coverage beispielsweise Statements, Branches, Funktionen oder allgemein ausgeführten Code während automatisierter Testläufe. [@Coveragepy][@JaCoCo][@webdevCodeCoverage] Die eigentliche Aussage ist dabei vergleichsweise einfach:

> „Welche Teile des Systems wurden tatsächlich ausgeführt?"

Nicht:

> „Ist das System gut getestet?"

Dieser Unterschied wirkt zunächst banal, verändert aber die Interpretation der Metrik grundlegend. Coverage eignet sich deshalb weniger als direkter Qualitätsbeweis, sondern eher als Werkzeug, um Sichtbarkeit über reale Nutzungspfade und ausgeführte Systembereiche zu schaffen. [@inozemtsevaCoverageNotStrongly2014][@fowlerTestCoverage]

## Der eigentliche Denkfehler: falsche Abstraktionsebene

Coverage sollte nicht isoliert betrachtet werden. Entscheidend ist, auf welcher Abstraktionsebene sie entsteht. [@doddsStaticVsUnit2018][@abseilSoftwareEngineering]

Entscheidend ist, Coverage bewusst getrennt zu betrachten:

- Unit-Coverage
- Integrations-Coverage
- E2E-Coverage

Denn diese Ebenen beantworten unterschiedliche Fragen.

Eine gemeinsame Gesamtzahl vermischt dagegen sehr unterschiedliche Aussagen und kann die eigentliche Signalwirkung verwässern. Sinnvoller ist es daher, Coverage gezielt pro Ebene zu interpretieren:

- Unit-Coverage als Signal für technische Pfadabdeckung
- Integrations-Coverage als Signal für Systemzusammenspiel
- E2E-Coverage als Signal für fachliche Nutzungspfade

Gerade Unit Tests greifen häufig tief in Implementierungsdetails ein und erreichen dadurch interne Branches, defensive Sonderlogik, Hilfsklassen oder technische Infrastruktur. Dadurch kann eine hohe Coverage entstehen, ohne viel über reale fachliche Nutzung auszusagen. [@doddsStaticVsUnit2018]

> Nicht jede erreichte Codezeile ist fachlich relevant.

## Warum höhere Testebenen aussagekräftiger werden

Aussagekräftiger wird Coverage auf höheren Ebenen wie Integrationstests, API-Flows oder End-to-End-Tests. Hier lautet die relevante Frage nicht mehr, welche internen Branches gezielt erreicht wurden, sondern welche Teile des Systems durch reale fachliche Abläufe tatsächlich berührt werden. Dadurch koppelt sich Coverage stärker an reale Nutzung und tatsächliche Wertschöpfung.

Dauerhaft unberührter Code auf E2E-Ebene ist ein Untersuchungssignal. Das bedeutet nicht automatisch, dass dieser Code nutzlos ist. Aber es ist ein sinnvoller Anlass, die fachliche Relevanz zu prüfen.

Auf Unit-Test-Ebene besitzt Coverage dagegen vor allem bei hoher algorithmischer oder technischer Komplexität praktischen Wert. In vielen klassischen Business-Anwendungen spielt sie eher eine unterstützende Rolle.

## Praktisches Beispiel

Ein historisch gewachsenes System hatte ursprünglich eine vollständige lokale Pflege von Kundendaten. Später wurde ein CRM angebunden, wodurch große Teile dieser Logik eigentlich überflüssig wurden. Unklar war jedoch, welche Felder und Prozesse tatsächlich noch relevant waren.

Die Grundlage der Analyse war dabei nicht Architekturwissen oder Produktions-Telemetrie, sondern die Coverage realer Integrations- und E2E-Tests. Beim Abgleich der Basisdaten aus dem CRM fiel auf, dass die Schnittstelle weiterhin mehr Daten importierte, als die Anwendung später tatsächlich verarbeitete. Konkret wurden private Adressen wegen historischer Datenbankabhängigkeiten, Null-Constraints und Relationen noch mitgeschrieben, obwohl sie fachlich nicht mehr ausgelesen wurden. Sichtbar wurde das zuerst in der Coverage: Die entsprechenden Setter wurden ausgeführt, passende Getter tauchten in den fachlichen Nutzungspfaden jedoch nicht mehr auf. Das war kein abschließender Beweis, aber ein klares Signal für die weitere Analyse.

Coverage half hier nicht bei der Qualitätsbewertung, sondern als pragmatisches Analysewerkzeug, um fachliche Relevanz, unnötige Kopplung und technisches Aufräumpotenzial sichtbar zu machen.

## Coverage als Signal für technische Verschwendung

Wenn fachliche Nutzungspfade bestimmte Bereiche dauerhaft nicht erreichen, entstehen interessante Fragen:

- Warum existiert dieser Code überhaupt noch?
- Wird die Funktion noch genutzt?
- Handelt es sich um Legacy, Overengineering oder historisch mitgeschleppte Erweiterungen?

Wichtig ist dabei, die Aussage nicht zu überziehen. Nicht erreichter Code ist nicht automatisch nutzlos. Trotzdem kann dauerhaft unberührte Logik ein wirtschaftlich relevantes Signal sein. Im Lean-Verständnis ist nicht wertschöpfende Arbeit Verschwendung; auf Software übertragen betrifft das auch Code und Komplexität, die weiter gepflegt werden müssen, obwohl sie keinen erkennbaren Nutzen mehr stiften. [@poppendieckLeanSoftwareDevelopment2003] Gerade in großen Unternehmensanwendungen entsteht technische Komplexität oft schrittweise über viele Jahre hinweg. Coverage macht solche Bereiche sichtbar und hilft, sie bewusster zu hinterfragen.

## Was man nicht tun sollte

Die Perspektive dieses Artikels bedeutet nicht, dass Coverage pauschal maximiert werden sollte.

Problematisch wird Coverage insbesondere dann, wenn unterschiedliche Abstraktionsebenen vermischt werden, Coverage als Qualitätsbeweis interpretiert wird oder Prozentwerte wichtiger werden als die eigentliche Aussage der Tests.

## Grenzen der Idee

Coverage ist nicht die einzige Möglichkeit, reale Nutzung sichtbar zu machen. Produktions-Telemetrie liefert häufig präzisere Daten. Coverage bleibt jedoch ein pragmatisches Werkzeug, wenn solche Informationen fehlen oder fachlich schwer zuzuordnen sind.

Wichtig ist die richtige Interpretation: Nicht erreichter Code ist nicht automatisch irrelevant. Framework-Mechanismen, Fehlerpfade, defensive Logik, Konfigurationspfade oder seltene Sonderfälle können bewusst außerhalb normaler E2E-Flows liegen. Auch schlechte E2E-Tests können irreführende Signale erzeugen. Coverage bleibt damit eine indirekte Metrik, kann in diesem Kontext aber durchaus nützlich sein.

## Fazit

Code Coverage wurde lange vor allem als Qualitätsmetrik interpretiert, vielleicht oft auf der falschen Ebene. Ihr eigentlicher Wert liegt weniger im Qualitätsbeweis als in der Sichtbarkeit.

Unit-Coverage kann technische Risiken absichern. Coverage auf Integrations- und E2E-Ebene kann sichtbar machen, welche Teile eines Systems unter realen fachlichen Bedingungen tatsächlich noch relevant sind. Gerade in historisch gewachsenen Unternehmensanwendungen entsteht daraus ein praktisches Werkzeug, um technische Verschwendung, unnötige Kopplung und veraltete Strukturen gezielter zu hinterfragen.

Die entscheidende Frage ist nicht, wie viel Code getestet wurde - sondern wie viel davon unter realen fachlichen Bedingungen überhaupt noch relevant ist.

