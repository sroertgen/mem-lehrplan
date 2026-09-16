# Prüfbericht — nachbessern.ttl

Geprüft am 2026-09-16 · Ontologie 1.0.0rc4 · sha256:a6419a3b61a9aa8d0cf75b6ef8e2ad166a6083037fdc36d9c06c1761871e3807

14 Knoten · 0 geprüft · 0 beanstandet · 14 offen

22 Befunde · 1 davon mehrfach bestätigt · 3 Fehler, 4 Warnungen, 15 Hinweise (15 Reasoner-Artefakte)

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

### Literal an ObjectProperty — hat Titel  (1)  · Regel + SHACL

**Soll** — Ein eigener Knoten mit IRI der Klasse „Titel“ (LP_0000346); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030056  ex:Titel .                 # hat Titel
ex:Titel  a lp:LP_0000346 ;                           # Klasse „Titel“
          lp:LP_0000344  "Text wie im PDF" .          # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    fachanforderung  —  Fachanforderungen Evangelische Religion

### Text nicht an „hat Wert“ — hat Titel  (1)  · Regel

**Soll** — Ein eigener Knoten mit IRI der Klasse „Titel“ (LP_0000346); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030056  ex:Titel .                 # hat Titel
ex:Titel  a lp:LP_0000346 ;                           # Klasse „Titel“
          lp:LP_0000344  "Text wie im PDF" .          # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    kb-gott  —  https://example.org/lehrplan/sh/beispiel/kb-gott-titel

### Wertknoten als Blank Node — hat Beschreibung  (1)  · Regel

**Soll** — Ein eigener Knoten mit IRI der Klasse „Beschreibung“ (LP_0030003); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030051  ex:Beschreibung .          # hat Beschreibung
ex:Beschreibung  a lp:LP_0030003 ;                    # Klasse „Beschreibung“
                 lp:LP_0000344  "Text wie im PDF" .   # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    kb-gott

### Text nicht an „hat Wert“ — hat Beschreibung  (1)  · Regel

**Soll** — Ein eigener Knoten mit IRI der Klasse „Beschreibung“ (LP_0030003); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030051  ex:Beschreibung .          # hat Beschreibung
ex:Beschreibung  a lp:LP_0030003 ;                    # Klasse „Beschreibung“
                 lp:LP_0000344  "Text wie im PDF" .   # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    kb-gott

### Literal an ObjectProperty — hat Jahrgangsstufe  (1)  · Regel

**Soll** — Jahrgangsstufen sind Individuen der Ontologie (LP_2000001 bis LP_2000013), bundeslandunabhängig; eine Spanne wird mehrwertig geschrieben, nicht als Literal „5-6“. Ganze Abschnitte über „hat Schulstufe“ (LP_0000047).

```turtle
ex:Element  lp:LP_0000026  lp:LP_2000005 , lp:LP_2000006 .   # hat Jahrgangsstufe → „Jahrgangsstufe 5“, „Jahrgangsstufe 6“
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-5-jahrgangstufeschulstufe-und-phasen-der-sekundarstufe-ii

    kb-gott-pk-1  —  5-6

### Ziel ohne geforderte Klasse — hat Beschreibung  (1)  · SHACL

**Soll** — Ein eigener Knoten mit IRI der Klasse „Beschreibung“ (LP_0030003); der Text hängt an „hat Wert“ (LP_0000344), nicht an rdfs:label und nicht als Literal direkt am Element. Kein Blank Node („[ … ]“).

```turtle
ex:Element  lp:LP_0030051  ex:Beschreibung .          # hat Beschreibung
ex:Beschreibung  a lp:LP_0030003 ;                    # Klasse „Beschreibung“
                 lp:LP_0000344  "Text wie im PDF" .   # hat Wert
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

    kb-gott-inhalt-1  —  https://example.org/lehrplan/sh/beispiel/kb-gott-inhalt-1-hinweis

### Pflichtangabe fehlt — ist Teil von  (1)  · SHACL

**Soll** — Die Shape verlangt „ist Teil von“ (BFO_0000050) an diesem Knoten.

```turtle
ex:Teil  obo:BFO_0000050  ex:Element .   # ist Teil von — die Gegenrichtung zu hat Teil
```

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    kb-gott-inhalt-1-hinweis

### Geforderter Wert fehlt (Reasoner-Artefakt) — von Bundesland  (5)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    teil-sek1
    kb-gott
    kb-gott-pk-1
    kb-gott-inhalt-1
    kb-gott-inhalt-2

### Nur in Gegenrichtung vorhanden (Reasoner-Artefakt) — handelt von  (5)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    teil-sek1-titel
    kb-gott-titel
    kb-gott-pk-1-titel
    kb-gott-inhalt-1-titel
    kb-gott-inhalt-2-titel

### Geforderter Wert fehlt (Reasoner-Artefakt) — hat Funktion  (3)  · SHACL · Reasoner-Artefakt

**Soll** — Kein Handlungsbedarf. Die Shape fordert etwas, das ein Reasoner aus der Ontologie ableiten würde; die Daten sind an dieser Stelle in Ordnung.

Quelle: https://fwu-de.github.io/lehrplan-ontologie/docs/structure/

    kb-gott-inhalt-1-hinweis
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
