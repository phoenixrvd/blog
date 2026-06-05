---
date: 2026-06-05
description: "Wie Zielsysteme als mentale Anker helfen, komplexe CI/CD-Pipelines verständlicher und erweiterbarer zu strukturieren."
categories:
    - CI/CD
    - DevOps
    - Prozesse
---

# CI/CD-Pipelines entlang von Zielsystemen strukturieren

Wenn eine Pipeline unübersichtlich wird, hilft ein Perspektivwechsel: Nicht die Jobs stehen im Mittelpunkt, sondern die Zielsysteme. Wohin soll ein Artefakt gelangen, und welche Anforderungen gelten dort?

<!-- more -->

CI/CD-Pipelines haben sich von einfachen Build- und Deployment-Prozessen zu zentralen Bestandteilen moderner Softwareentwicklung entwickelt. Gleichzeitig steigt ihre Komplexität. Neben klassischen Aktivitäten wie Build, Test und Deployment werden heute zahlreiche weitere Prüfungen integriert. Dazu gehören statische Codeanalysen, Security-Scans, Compliance-Prüfungen, Lizenzanalysen, SBOM-Erzeugung [@cisaSBOM] sowie verschiedenste Qualitätskontrollen.

Agentische Entwicklungswerkzeuge verstärken diesen Trend zusätzlich. Wenn Software schneller verändert wird, steigt auch der Bedarf an automatisierten Prüfungen, die Qualität, Wartbarkeit und Sicherheit absichern. Moderne CI/CD-Systeme bieten dafür viele technische Bausteine. GitLab CI/CD [@gitlabCICD], GitHub Actions [@githubActions], Azure Pipelines [@azurePipelines] und Google Cloud Build [@googleCloudBuild] können Abhängigkeiten, parallele Ausführung, Freigaben und Deployment-Schritte modellieren.

Die Herausforderung besteht daher häufig nicht darin, eine Pipeline technisch umzusetzen. Die eigentliche Herausforderung besteht darin, eine Struktur zu finden, die auch nach Jahren, vielen Erweiterungen und mehreren beteiligten Teams noch verständlich bleibt.

## Problem und Relevanz

Mit jeder zusätzlichen Anforderung wächst die Pipeline. Neue Security-Vorgaben führen zu weiteren Scannern. Compliance-Anforderungen erzeugen zusätzliche Prüfungen. Neue Teststrategien bringen neue Teststufen mit sich. Schon in mittelgroßen Projekten entsteht dadurch schnell eine zweistellige Zahl einzelner Jobs.

Die technische Umsetzung solcher Pipelines ist in modernen Werkzeugen meist problemlos möglich. Die Nachvollziehbarkeit nimmt jedoch kontinuierlich ab. Das ist auch aus kognitiver Sicht plausibel: Menschen können nur eine begrenzte Anzahl unabhängiger Informationseinheiten gleichzeitig aktiv verarbeiten. Für Pipelines ist dabei nicht entscheidend, ob man Millers klassische sieben Einheiten oder Cowans spätere vier Chunks zugrunde legt. Entscheidend ist die Konsequenz: Wenn sehr viele gleichrangige Jobs gleichzeitig verstanden werden müssen, steigt die kognitive Last deutlich. [@millerMagicalNumber1956][@cowanMagicalNumber2001][@swellerCognitiveLoad1988]

Hinzu kommt: Moderne Pipelines sind selten nur eine lange Kette nacheinander ausgeführter Schritte. SAST, SCA, Unit-Tests, Container-Scans oder Policy-Prüfungen laufen häufig parallel, damit die Wartezeit nicht unnötig steigt. Das ist technisch sinnvoll, macht die Pipeline als Prozessbild aber schwerer lesbar.

Besonders deutlich wird dies bei der Kommunikation innerhalb von Teams. Entwickler, Architekten, Plattform-Teams und Fachbereiche sprechen selten über einzelne technische Pipeline-Jobs. Stattdessen sprechen sie über Systeme und Zustände.

Typische Aussagen sind:

- Das Testsystem funktioniert aktuell nicht.
- Die Staging-Umgebung enthält die neue Version.
- Die Produktion erfüllt die aktuellen Compliance-Anforderungen.
- Die Anwendung wurde noch nicht nach Produktion freigegeben.

Die Kommunikation orientiert sich damit meist an Zielsystemen und nicht an einzelnen technischen Schritten.

Daraus ergibt sich eine einfache Beobachtung: Teams denken häufig in Zielsystemen, Pipelines werden jedoch meist über technische Ausführungsschritte beschrieben. Dadurch entsteht eine Lücke zwischen dem mentalen Modell der Beteiligten und der technischen Darstellung der Delivery-Strecke.

> Zielsysteme beschreiben die fachliche Architektur einer Delivery-Strecke, während einzelne Jobs lediglich deren technische Implementierung darstellen.

Dieses Spannungsverhältnis lässt sich an einer aktivitätsorientierten Strukturierung gut zeigen.

## Aktivitätsorientierte Strukturierung

Sie orientiert sich zuerst an technischen Aktivitäten und Stages:

![Aktivitätsorientierte Strukturierung einer CI/CD-Pipeline](ci-cd-pipelines-entlang-von-zielsystemen-strukturieren/model-old.drawio.svg)
/// caption
Aktivitätsorientierte Strukturierung: Die Pipeline wird primär über technische Stages beschrieben.
///

## Schwächen einer aktivitätsorientierten Strukturierung

Aus der Darstellung ist häufig nicht erkennbar, welches Artefakt oder welches Zielsystem tatsächlich geprüft wird. Security-Prüfungen werden häufig über mehrere Stages verteilt, wodurch die Zuordnung zu einem konkreten Zielsystem erschwert wird. Die Zielsysteme selbst treten in den Hintergrund, obwohl sie häufig die eigentlichen fachlichen Zustände der Delivery-Strecke darstellen.

Zudem werden sehr unterschiedliche Prüfungen in solchen Darstellungen oft gleichrangig nebeneinander gestellt. Ein Unit-Test, ein E2E-Test, ein SAST-Scan und ein manueller Approval-Schritt sagen jedoch nicht dasselbe über ein Artefakt aus. In der Abbildung wird das besonders an Production sichtbar: Production erscheint als eigene Stage, obwohl sie fachlich eher ein Zielzustand der Delivery-Strecke ist. Mit zunehmender Komplexität entstehen außerdem häufig zusätzliche Stages mit nur einzelnen Jobs, ohne dass dadurch zusätzliche fachliche Struktur entsteht.

## Zielsysteme als mentale Anker

Menschen beschreiben komplexe Abläufe häufig über Zustände, Orte und Übergänge. Das ist keine Besonderheit von CI/CD, sondern passt zu bekannten Konzepten aus Kognitionswissenschaft und UX: Mentale Modelle helfen dabei, Systeme handhabbar zu machen und abstrakte Zusammenhänge zu strukturieren. [@nielsenNormanMentalModels]

Ein Testsystem beschreibt einen konkreten Zustand eines Artefakts innerhalb des Delivery-Prozesses. Dasselbe gilt für Staging- oder Produktionssysteme. Technische Aktivitäten wie Builds, Security-Scans oder Tests dienen dagegen meist nur dazu, einen bestimmten Zustand zu erreichen oder nachzuweisen.

Während sich konkrete Prüfungen im Laufe der Zeit verändern können, ändern sich Zielsysteme typischerweise deutlich seltener als die innerhalb dieser Systeme ausgeführten Aktivitäten.

> **Die Anzahl technischer Jobs wächst oft schneller als die Anzahl fachlicher Zielsysteme.**

Ein Projekt kann viele neue Scanner, Tests oder Compliance-Prüfungen aufnehmen und trotzdem weiterhin entlang weniger stabiler Zustände wie Test, Staging und Produktion organisiert sein.

Gleichzeitig bündeln Zielsysteme viele technische Aktivitäten zu einer fachlich verständlichen Einheit. Sie eignen sich daher gut als primäre Strukturierungsebene einer Pipeline.

## Zielsystemorientiertes Modell

Das hier vorgestellte Modell versucht, die fachliche Sicht der Teams und die technische Darstellung der Pipeline zusammenzuführen. Es beginnt deshalb nicht mit Build, Test und Deploy, sondern mit den Zielsystemen, die ein Artefakt während seines Lebenszyklus durchläuft. Die horizontale Achse beschreibt diese Zielsysteme. Jedes Zielsystem repräsentiert einen fachlich verständlichen Zustand des Artefakts.

Innerhalb jedes Zielsystems werden anschließend die zugehörigen Pipeline-Jobs angeordnet. Dazu gehören im Beispiel Build- und Deployment-Jobs, Unit- und Integrationstests, SAST, DAST, Performance- und Acceptance-Tests, Tagging, manuelle Freigaben, Smoke Tests, Rollback-Schritte und Benachrichtigungen. Die Spalten beschreiben die Zielsysteme, die einzelnen Jobs zeigen notwendige Nachweise, Prüfungen oder Deployments, und Pfeile beschreiben technische Abhängigkeiten sowie Freigaben zwischen diesen Aktivitäten.

Eine mögliche Darstellung könnte wie folgt aussehen. Das Beispiel ist eine verdichtete Darstellung wesentlicher Pipeline-Schritte aus der Delivery-Strecke eines aktuellen Projekts, das nach Trunk-Based Development [@paul-hammantTrunkBasedDevelopmenta] und dem Prinzip Build Once, Deploy Many [@twelveFactorBuildReleaseRun] arbeitet:

![Verdichtetes Modell einer CI/CD-Delivery-Strecke](ci-cd-pipelines-entlang-von-zielsystemen-strukturieren/model-new.drawio.svg)
/// caption
Zielsystemorientiertes Modell: Pipeline-Jobs werden den fachlichen Zielsystemen der Delivery-Strecke zugeordnet.
///

Das Modell beschreibt dabei nicht einfach eine lineare Ausführungsreihenfolge der Pipeline. Es ordnet konkrete Jobs den Zielsystemen zu und macht sichtbar, welche Jobs zu welchem Abschnitt der Delivery-Strecke gehören.

> Ein Zielsystem beschreibt keinen technischen Ausführungsschritt, sondern einen fachlich verständlichen und grundsätzlich funktionsfähigen Zustand des Artefakts.

Das Artefakt könnte aus technischer Sicht bereits produktiv betrieben werden, erfüllt jedoch noch nicht alle organisatorischen, fachlichen oder regulatorischen Anforderungen für den nächsten Abschnitt der Delivery-Strecke. Die Aktivitäten innerhalb eines Zielsystems dienen daher nicht primär dazu, die Software erstmals betreibbar zu machen. Sie dienen dazu, zusätzliche Nachweise zu erbringen, Risiken zu reduzieren oder Freigaben einzuholen, bevor das Artefakt den nächsten fachlichen Zustand erreicht.

Im dargestellten Beispiel wird das für die weiteren Zielsysteme verwendete Artefakt erst erzeugt, nachdem die grundlegenden Qualitätsnachweise im Testsystem erfolgreich abgeschlossen wurden. Dadurch entsteht erstmals das Artefakt, das anschließend unverändert durch die weiteren Zielsysteme bewegt wird.

In der technischen Pipeline kann die Anzahl einzelner Stages oder Jobs dabei deutlich über dem liegen, was ein Mensch auf einen Blick zuverlässig erfassen kann. Die Aufteilung auf sinnvolle Zielsysteme reduziert diese Komplexität nicht technisch, macht sie aber fachlich handhabbarer.

Gleichzeitig werden kritische Übergangspunkte sichtbar. Übergänge zwischen Zielsystemen markieren häufig auch organisatorische oder technische Vertrauensgrenzen.

## Was dadurch besser wird

Der praktische Effekt liegt nicht darin, technische Jobs zu verstecken. Sie werden weiterhin sichtbar, aber auf einer fachlich aussagekräftigeren Ebene eingeordnet.

Die Frage verschiebt sich von "In welcher Stage liegt dieser Job?" zu "Für welches Zielsystem wird dieser Nachweis benötigt?" Statt nur zu fragen, an welcher Stelle ein Container-Scan, eine Product-Owner-Freigabe oder ein Health Check technisch ausgeführt wird, kann ein Team klären, für welches Zielsystem dieser Nachweis relevant ist. Neue Anforderungen lassen sich dadurch ergänzen, ohne die gesamte Pipeline-Erzählung neu aufzubauen.

## Umsetzung in bestehenden Werkzeugen

Das Modell ersetzt keine bestehenden CI/CD-Werkzeuge. Stattdessen kann es als fachliche Struktur oberhalb der technischen Implementierung dienen.

In GitLab CI/CD können beispielsweise Stages, Jobs und Needs verwendet werden, um Zielsysteme technisch abzubilden. In GitHub Actions wären Workflows, Jobs, Environments und Required Reviewers naheliegende Bausteine. Azure Pipelines arbeitet mit Stages, Jobs, Environments und Approvals. Google Cloud Build kann Build Steps, Substitutions, Trigger und nachgelagerte Deployments kombinieren.

Dadurch unterscheidet sich das Modell bewusst von einer reinen Stage-Betrachtung. Eine Stage beschreibt in erster Linie eine technische Ausführungsreihenfolge. Ein Zielsystem beschreibt dagegen den fachlichen Zustand, den ein Artefakt erreicht hat, und die Anforderungen, die dort erfüllt sein müssen.

Mehrere technische Stages können daher zu demselben Zielsystem gehören. Umgekehrt kann ein Zielsystem zahlreiche Jobs enthalten, ohne dass sich dadurch seine fachliche Bedeutung verändert.

Die konkrete Umsetzung kann sich dabei zwischen den Werkzeugen unterscheiden. Das zugrunde liegende Denkmodell bleibt jedoch identisch.

## Grenzen des Modells

Nicht jede Pipeline lässt sich vollständig durch wenige Zielsysteme beschreiben. Große Organisationen besitzen häufig zusätzliche Systeme, spezielle Freigabeprozesse oder mehrere Produktionsstufen. Die konkreten Zielsysteme unterscheiden sich dabei je nach Delivery-Modell. Neben Test-, Staging- und Produktionssystemen können beispielsweise auch Review-Apps, Security-Umgebungen, kundenspezifische Deployments oder weitere Zwischenstufen Teil der Delivery-Strecke sein.

Auch dieses Modell reduziert Komplexität nicht beliebig. Werden zu viele Zielsysteme, Freigabestufen oder Aktivitäten eingeführt, entsteht erneut eine Struktur, die nur schwer zu überblicken ist.

Zielsysteme beseitigen die Komplexität einer Pipeline daher nicht, sondern organisieren sie entlang stabilerer mentaler Anker. Wird diese Struktur selbst zu groß, gehen die Vorteile wieder verloren.

Das Modell ist deshalb kein Framework und keine feste Vorgabe. Es ersetzt keine Architekturentscheidungen, sondern hilft dabei, vorhandene Komplexität vor der konkreten YAML-Implementierung sichtbarer und verständlicher zu organisieren.

## Fazit

CI/CD-Werkzeuge liefern technische Ausführungsmodelle. Für die fachliche Struktur einer Delivery-Strecke liefern sie jedoch meist keine Antwort. Zielsysteme können diese fehlende Strukturierungsebene bilden. Das hier vorgestellte Modell betrachtet Zielsysteme als fachliche Architektur der Delivery-Strecke. Die einzelnen Jobs stellen lediglich die technische Umsetzung der Anforderungen dar, die innerhalb eines Zielsystems erfüllt werden müssen.

Wer eine bestehende Pipeline vereinfachen möchte, sollte deshalb nicht zuerst die YAML-Datei optimieren. Zielsysteme sind dafür ein pragmatischer Startpunkt: Sie zeigen, welche Zustände ein Artefakt erreichen muss, welche Anforderungen dort gelten und wo Freigaben oder Prüfungen sinnvoll verortet sind.

Sinnvoller ist oft ein Schritt davor: Test, Staging, Produktion und mögliche Zwischenzustände aufzeichnen und je Zielsystem klären, was dort wirklich nachgewiesen werden muss.
