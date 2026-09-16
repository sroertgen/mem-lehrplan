# Prüfbericht — beispiel.ttl

> Erzeugt mit `mem-explorer check references/beispiel.ttl` (Explorer 0.4.0), Exit-Code 0. Die verbleibenden Gruppen sind Reasoner-Artefakte und Warnungen, keine Datenfehler — so sieht eine saubere Datei aus.

Geprüft am 2026-09-16 · Ontologie 1.0.0rc4 · sha256:ee2ba2884696b721e9f365d220ea725a3b666a1c1624d223fa87065929907ece

15 Knoten · 0 geprüft · 0 beanstandet · 15 offen

16 Befunde · 0 davon mehrfach bestätigt · 0 Fehler, 0 Warnungen, 16 Hinweise (16 Reasoner-Artefakte)

## Für die Weiterverarbeitung

Dieser Bericht ist die Grundlage für die Nachbesserung der Datei — von Hand oder mit einem LLM. Dabei gilt:

- **Maßgeblich ist die Dokumentation der Lehrplan-Ontologie** (Version 1.0.0rc4): Muster https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/ · Struktur https://fwu-de.github.io/lehrplan-ontologie/docs/structure/ · Klassenliste https://fwu-de.github.io/lehrplan-ontologie/ · Repo https://github.com/FWU-DE/lehrplan-ontologie. Unter jeder Befundgruppe steht als **Soll** das Muster aus der Doku.
- **Modellierung nicht aus vorhandenen Daten im MEM-Store ableiten.** Die Importe dort weichen von den dokumentierten Mustern ab (Titel mit rdfs:label statt hat Wert).
- **IRIs der Knoten beibehalten.** Der Prüfstand — Haken und Notizen — hängt an ihnen; neue IRIs machen ihn wertlos.
- **Beanstandungen** sind Abweichungen vom PDF (Texttreue, Vollständigkeit); **automatische Befunde** sind Modellierungsfehler gegen die Ontologie. Gruppen mit „Reasoner-Artefakt“ brauchen keine Änderung.
- Das Ergebnis erneut mit dem MEM Explorer prüfen.

## Beanstandungen

Keine.

## Automatische Befunde

### Nur in Gegenrichtung vorhanden (Reasoner-Artefakt) — handelt von  (7)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    fachanforderung-titel
    teil-sek1-titel
    kb-gott-titel
    kb-gott-pk-1-titel
    kb-gott-inhalt-1-titel
    kb-gott-inhalt-2-titel
    kb-gott-beschreibung

### Geforderter Wert fehlt (Reasoner-Artefakt) — von Bundesland  (5)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    teil-sek1
    kb-gott
    kb-gott-pk-1
    kb-gott-inhalt-1
    kb-gott-inhalt-2

### Geforderter Wert fehlt (Reasoner-Artefakt) — hat Funktion  (2)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    kb-gott
    teil-sek1

### Klasse eines Ontologie-Individuums (Reasoner-Artefakt) — von Bundesland  (1)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    fachanforderung  —  https://w3id.org/lehrplan/ontology/LP_3000054

### Nur in Gegenrichtung vorhanden (Reasoner-Artefakt) — ist Teil von  (1)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    kb-gott
