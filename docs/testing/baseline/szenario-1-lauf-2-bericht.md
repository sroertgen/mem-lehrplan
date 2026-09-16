# Prüfbericht — szenario-1-lauf-2.ttl

Geprüft am 2026-09-16 · Ontologie 1.0.0rc4 · sha256:2463011105793fab04fedc3bd0da54ad0c233aa6de3a8426ebb44d0165383464

7 Knoten · 0 geprüft · 0 beanstandet · 7 offen

20 Befunde · 0 davon mehrfach bestätigt · 1 Fehler, 10 Warnungen, 9 Hinweise (9 Reasoner-Artefakte)

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

### Wertknoten als Blank Node — hat Titel  (4)  · Regel

**Soll** — Ein eigener Knoten mit IRI der Klasse „Titel“ (LP_0000346); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030056  ex:Titel .                 # hat Titel
ex:Titel  a lp:LP_0000346 ;                           # Klasse „Titel“
          lp:LP_0000344  "Text wie im PDF" .          # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    fachanforderung-ev-religion-sh-gym
    kb1-frage-nach-gott
    kb1-pk-56
    kb1-themen-56

### Text nicht an „hat Wert“ — hat Titel  (4)  · Regel

**Soll** — Ein eigener Knoten mit IRI der Klasse „Titel“ (LP_0000346); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030056  ex:Titel .                 # hat Titel
ex:Titel  a lp:LP_0000346 ;                           # Klasse „Titel“
          lp:LP_0000344  "Text wie im PDF" .          # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    fachanforderung-ev-religion-sh-gym
    kb1-frage-nach-gott
    kb1-pk-56
    kb1-themen-56

### Wertknoten als Blank Node — hat Beschreibung  (1)  · Regel

**Soll** — Ein eigener Knoten mit IRI der Klasse „Beschreibung“ (LP_0030003); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030051  ex:Beschreibung .          # hat Beschreibung
ex:Beschreibung  a lp:LP_0030003 ;                    # Klasse „Beschreibung“
                 lp:LP_0000344  "Text wie im PDF" .   # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    kb1-frage-nach-gott

### Text nicht an „hat Wert“ — hat Beschreibung  (1)  · Regel

**Soll** — Ein eigener Knoten mit IRI der Klasse „Beschreibung“ (LP_0030003); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030051  ex:Beschreibung .          # hat Beschreibung
ex:Beschreibung  a lp:LP_0030003 ;                    # Klasse „Beschreibung“
                 lp:LP_0000344  "Text wie im PDF" .   # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    kb1-frage-nach-gott

### Ziel ohne geforderte Klasse — hat Beschreibung  (1)  · SHACL

**Soll** — Ein eigener Knoten mit IRI der Klasse „Beschreibung“ (LP_0030003); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030051  ex:Beschreibung .          # hat Beschreibung
ex:Beschreibung  a lp:LP_0030003 ;                    # Klasse „Beschreibung“
                 lp:LP_0000344  "Text wie im PDF" .   # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    kb1-frage-nach-gott  —  n3-2

### Geforderter Wert fehlt (Reasoner-Artefakt) — von Bundesland  (6)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    kb1-frage-nach-gott
    kb1-pk-56
    kb1-themen-56
    kb1-themen-56-1
    kb1-themen-56-2
    kb1-themen-56-3

### Geforderter Wert fehlt (Reasoner-Artefakt) — hat Funktion  (1)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    kb1-frage-nach-gott

### Klasse eines Ontologie-Individuums (Reasoner-Artefakt) — von Bundesland  (1)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    fachanforderung-ev-religion-sh-gym  —  https://w3id.org/lehrplan/ontology/LP_3000054

### Nur in Gegenrichtung vorhanden (Reasoner-Artefakt) — ist Teil von  (1)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    kb1-frage-nach-gott
