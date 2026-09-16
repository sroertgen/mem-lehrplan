# Konventionen dieses Projekts, keine FWU-Vorgabe

Die Lehrplan-Ontologie schreibt Klassen, Properties und die sechs Muster in
`references/muster.md` vor. Wie ein Namensraum aussieht, wie ein Knoten heißt, wie eine
Datei geschnitten wird — dazu schweigt die Doku. Das hier ist die Antwort dieses Projekts
darauf, nicht die der Ontologie. Wer eine andere, ebenso gültige Antwort vorfindet (ein
Store-Export, ein fremdes Transformationsprojekt), übernimmt trotzdem diese hier — sonst
bricht der Abgleich zwischen Läufen.

## Namensraum

Ein eigener `data:`-Namensraum je Land und Projekt, zum Beispiel
`https://lp-sh.org/resource/` in der relidesk-Transformation für Schleswig-Holstein.
Kein geteilter Namensraum mit einem anderen Projekt, auch wenn der Lehrplan derselbe ist.

## Slugs statt UUIDs

Lesbare, stabile Slugs (`kb-gott`, `kb-gott-inhalt-1`), keine UUIDs. Genau eine IRI je
Knoten. **IRIs werden zwischen Iterationen nie umbenannt** — der Prüfstand (der
MEM-Explorer-Bericht, seine Notizen und Haken) hängt an ihnen; eine neue IRI macht den
alten Bericht für diesen Knoten wertlos.

## Label und Titel sind zwei verschiedene Dinge

`rdfs:label` ist die technische Kurzbezeichnung, unter der ein Knoten im Baum des Explorers
erscheint — frei formuliert, kurz. Der Titel-Knoten (Pattern 2, `hat Wert`) trägt den
Wortlaut des Dokuments. Beide stehen nebeneinander, keiner ersetzt den anderen.

## Text

Literale ohne Sprachtag, wie in den Pattern-Dateien — kein `"…"@de`. Text steht wörtlich
wie im PDF, nie paraphrasiert, nie gekürzt, auch wenn er lang oder umständlich ist. Jeder
Knoten, der von einer Textstelle stammt, trägt einen Kommentar mit der Seite, zum
Beispiel `# S. 12` — für den späteren Abgleich mit dem Original.

## Eine Datei je Lehrplan

Schnitt nach Schulstufe: `Bundesland/schulstufe.ttl`, zum Beispiel `SH/sekundarstufe-1.ttl`.
Kein gemeinsames Dokument für mehrere Schulstufen oder mehrere Fächer.

## Präfixblock zum Kopieren

Aus `references/beispiel.ttl`, unverändert bis auf den eigenen `data:`-Namensraum:

```turtle
@prefix lp:   <https://w3id.org/lehrplan/ontology/> .
@prefix obo:  <http://purl.obolibrary.org/obo/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix data: <https://example.org/lehrplan/sh/beispiel/> .
```
