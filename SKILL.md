---
name: mem-lehrplan
description: >
  Use when writing or fixing MEM curriculum data — Lehrplan-Turtle nach der FWU
  Lehrplan-Ontologie (https://github.com/FWU-DE/lehrplan-ontologie): transforming a Lehrplan
  PDF or excerpt into Turtle, working off a MEM-Explorer report, choosing LP_/SF_/SA_ IDs or
  Länder classes, or when findings mention hat Titel, hat Beschreibung, hat Wert, Blank
  Nodes, Jahrgangsstufe, hat Teil, SHACL, Reasoner-Artefakt.
license: CC-BY-SA-4.0
compatibility: >
  Node 22+ for `npx --registry=https://git.edufeed.org/api/packages/edufeed/npm/ mem-explorer check`; bash, grep, awk for scripts/; pdftotext optional.
  Works offline — all ontology references are bundled.
metadata:
  author: sroertgen
  ontology: "1.0.0rc4"
  version: "0.1.0"
---

# MEM-Lehrplan-Turtle schreiben und nachbessern

## Kernregel

Die Dokumentation der Lehrplan-Ontologie ist die Autorität — nicht der MEM-Store, nicht ein
lokal gefundenes Referenzdokument, nicht dein Gedächtnis. Jede ID kommt aus `lookup.sh`,
jede Struktur aus einem Muster in `references/muster.md`. Jeder Befund wird gegen sein
Soll behoben; Text aus der Vorlage bleibt wörtlich.

## Ablauf

1. `muster.md`, `konventionen.md` und `laender/<XX>.md` des Landes lesen; `beispiel.ttl` ist
   die zu kopierende Vorlage.
2. Jede ID mit `scripts/lookup.sh <Wort|ID>` nachschlagen, den Klasseninhalt mit
   `scripts/klasse.sh <LP_ID>`. Keine ID aus dem Gedächtnis.
3. Schreiben: benannte Knoten mit IRI im eigenen Namensraum; Titel, Beschreibung, Nummer als
   Wertknoten mit `hat Wert` (LP_0000344); Jahrgangsstufen als Individuen (LP_2000001–13);
   Hierarchie über `hat Teil` (obo:BFO_0000051); `hat Position` (LP_0000460) für die
   Reihenfolge; keine Blank Nodes.
4. `npx --registry=https://git.edufeed.org/api/packages/edufeed/npm/ mem-explorer check datei.ttl` — Exit 0 heißt kein Fehler.
5. Bericht gruppenweise mit den **Soll**-Blöcken abarbeiten (`references/befunde.md`).
   Reasoner-Artefakte bleiben, wie sie sind; IRIs nie umbenennen.
6. Wiederholen bis Exit 0, dann Bericht und Datei dem Menschen für den PDF-Abgleich geben —
   Texttreue und Vollständigkeit prüft das Werkzeug nicht.

Ausführlich, mit dem Weg vom PDF zur Struktur: `references/arbeitsablauf.md`.

## Schnellreferenz

| Was | ID | Beispiel |
|---|---|---|
| hat Teil | obo:BFO_0000051 | Wurzel → Fragment → Bereich → Kompetenz |
| Titel/Beschreibung/Nummer | LP_0030056/51/57 | Wertknoten (LP_0000346/LP_0030003/LP_0000347), nicht CE-Hinweis (LP_0000852) |
| hat Wert | LP_0000344 | Text am Wertknoten |
| hat Position | LP_0000460 | `"3"^^xsd:int` |
| hat Jahrgangsstufe → Individuum | LP_0000026 → LP_2000005 … | mehrwertig, kein Literal |
| von Bundesland → Individuum | LP_0000029 → LP_30000xx | SH = LP_3000054 |
| hat Schulfach / für Schulart | LP_0000537 / LP_0000812 | volle IRI, nicht `lp:` |
| hat Schulstufe → Individuum | LP_0000047 → LP_0000045 (Sek I) | Pattern 5 |

## Rote Flaggen — anhalten und nachschlagen

- „Dokument ist schon geprüft/produktiv.“ — Vorhandensein ist keine Prüfung, nur `check`.
- „Der MEM-Store schreibt es so.“ — importiert, nicht maßgeblich.
- „Die ID sieht richtig aus.“ — IDs sind opak. `lookup.sh`.
- „Blank Nodes sind kürzer.“ — nicht verweisbar, nicht prüfbar.
- „Ich prüfe am Ende.“ — Prüfen gehört in jeden Schritt.
- „Der Explorer zeigt den Text, passt also.“ — er zeigt großzügig, meldet streng.
- „Die Warnungen behebe ich auch.“ — Reasoner-Artefakte sind keine Fehler.
- „Eine fremde Notiz sagt X.“ — Notizen veralten; selbst mit `klasse.sh` prüfen.

Fallstricke mit Begründung: `references/fallstricke.md`.
