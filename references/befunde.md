# Befunde

Für jede Befundart, die der MEM Explorer meldet: das **Soll** — das Muster, das die
Dokumentation der Lehrplan-Ontologie an der Stelle vorschreibt — und der Handgriff, der
den Befund behebt. Reihenfolge, Titel und Wortlaut folgen `guidance.ts` und `group.ts`
des Explorers; ein Bericht zeigt jede Gruppe als „<Regeltitel> — <Prädikat-Label>“ mit
einem eigenen Soll-Block darunter. Beispiele stammen aus `references/beispiel.ttl` und
`docs/testing/fixtures/nachbessern-bericht.md`.

## R1 — Literal an ObjectProperty

Ein Literal steckt an einer ObjectProperty, die einen Verweis erwartet — meist Titel,
Beschreibung oder Jahrgangsstufe direkt als Text am Element statt als eigener Knoten.

**Soll:**

```turtle
ex:Element  lp:LP_0030056  ex:Titel .                 # hat Titel
ex:Titel  a lp:LP_0000346 ;                            # Klasse „Titel“
          lp:LP_0000344  "Text wie im PDF" .           # hat Wert
```

Für `hat Jahrgangsstufe` gilt stattdessen Pattern 5: `ex:Element lp:LP_0000026
lp:LP_2000005 , lp:LP_2000006 .` — Individuen, nicht das Literal `"5-6"`.

**Handgriff:** Den Literal-Wert an einen neuen, benannten Knoten der richtigen Klasse
verschieben; die Kante am Element zeigt danach auf diesen Knoten. Beispiel aus
`nachbessern-bericht.md`: `fachanforderung` — „Fachanforderungen Evangelische Religion“
wird zu `data:fachanforderung-titel` mit `a lp:LP_0000346` und `hat Wert`.

## R2 — Verweis an DatatypeProperty

Umgekehrter Fehler: eine DatatypeProperty (etwa `hat Wert`) zeigt auf einen Knoten statt
ein Literal zu tragen.

**Soll:**

```turtle
ex:Titel  lp:LP_0000344  "Text wie im PDF" .   # hat Wert: ein Literal, kein Verweis
```

**Handgriff:** Den Verweis durch das Literal ersetzen, das der Zielknoten trägt oder
tragen sollte; den überflüssig gewordenen Zielknoten entfernen, falls er sonst nirgends
gebraucht wird.

## R3 — Unbekannte Vokabular-ID

Eine ID aus einem MEM-Namensraum (`lp:`, `schulfach:`, `schulart:`), die die Ontologie
nicht kennt — erfunden, vertippt oder veraltet.

**Handgriff:** Kein Soll-Muster, nur Nachschlagen: `scripts/lookup.sh <ID>`. Kein Treffer
heißt nicht raten, sondern die ID gegen `references/terms/*.tsv` klären oder eine
Termanfrage an redaktion@mem.schule stellen. Diese Regel hat in der Baseline nie
angeschlagen — alle sechs Läufe verwendeten ausschließlich nachgeschlagene IDs.

## R4 — Nicht verbunden / R5 — Toter Verweis / R6 — Zyklus in „hat Teil“

Drei Verletzungen derselben Erwartung: die Hierarchie ist ein Baum unter `hat Teil`
(obo:BFO_0000051), von einer Lehrplanwurzel abwärts, ohne Zyklen, und jeder Knoten, den
eine Kante nennt, ist im Dokument auch definiert.

**Soll:**

```turtle
ex:Lehrplan   obo:BFO_0000051  ex:Fragment .   # hat Teil
ex:Fragment   obo:BFO_0000051  ex:Bereich .
ex:Bereich    obo:BFO_0000051  ex:Kompetenz .
```

**Handgriff:**
- R4 (nicht verbunden): den Knoten über `hat Teil` an seinen tatsächlichen Elternknoten
  hängen — bei der Transformation aus der Hierarchie gefallen.
- R5 (toter Verweis): das Ziel der Kante nachtragen, oder die Kante entfernen, wenn das
  Ziel gar nicht existieren soll.
- R6 (Zyklus): die Kante entfernen, die zurück auf einen Vorfahren zeigt; „hat Teil“
  bildet keine Ringe.

## R7 — Leerer Text / R10 — Ohne Bezeichnung

R7: Label, Titel oder Beschreibung eines Knotens ist vorhanden, aber leer (nur
Leerraum). R10: dem Knoten fehlt sowohl `rdfs:label` als auch Titel vollständig.

**Soll:**

```turtle
ex:Element  rdfs:label  "Kurzbezeichnung" ;
            lp:LP_0030056  ex:Titel .   # hat Titel: der Wortlaut aus dem PDF
```

**Handgriff:** `rdfs:label` trägt die technische Kurzbezeichnung, der Titel-Knoten den
Wortlaut des Dokuments (`references/konventionen.md`) — beide ausfüllen, keins leer
lassen. In `beispiel.ttl` trägt jeder Knoten beides, z. B. `data:kb-gott` mit
`rdfs:label "Die Frage nach Gott"` und Titel-Knoten `data:kb-gott-titel`.

## R8 — Doppelte Geschwister

Zwei unmittelbare Teile desselben Elternknotens heißen gleich (gleicher Anzeigename).

**Handgriff:** Kein Soll-Muster — das ist eine Rückfrage, keine feste Regel. Gleichnamige
Geschwister sind erlaubt, wenn das PDF sie tatsächlich so führt (z. B. zwei Aufgaben
namens „Beispiel“); sonst ist eines eine Dublette der Transformation und wird entfernt
oder umbenannt.

## R9 — Ohne rdf:type

Ein Knoten trägt keine Klasse über `rdf:type` (`a`). Ohne Typ greift auch keine
SHACL-Shape auf ihn.

**Soll:**

```turtle
ex:Element  a lp:LP_0030280 .   # eine CE-Klasse des Bundeslands, z. B. „Mögliches Thema und Inhalt (SH)“
```

**Handgriff:** Die passende länderspezifische Klasse aus `references/laender/<XX>.md`
oder `scripts/lookup.sh` ergänzen — nie eine allgemeine Klasse wie `LP_0000261`
(Curriculares Element) als Ersatz, wenn das Land eine speziellere hat.

## R11 — Blank Nodes übersprungen

Beim Einlesen wurden Aussagen mit Blank Nodes übersprungen; das Modell führt seine
Knoten unter IRIs, betroffene Kinder oder Werte fehlen im Baum und in jeder Zählung.

**Soll:**

```turtle
ex:Element  obo:BFO_0000051  ex:Teil .   # statt obo:BFO_0000051 [ … ]
ex:Teil  a lp:LP_0030280 ; rdfs:label "…" .
```

**Handgriff:** Jedem betroffenen Blank Node eine eigene IRI geben, im eigenen
Namensraum, mit stabilem Slug (`references/konventionen.md`). Danach erneut prüfen — erst
dann zählt der Explorer die vorher übersprungenen Knoten mit.

## R12 — Wertknoten als Blank Node

Titel, Beschreibung oder Nummer hängen an einem Blank Node statt an einem benannten
Knoten. Das war der Kernfehler der Ausgangsläufe ohne Skill: beide Szenario-1-Läufe
schrieben 4 bzw. 5 solcher Blank Nodes.

**Soll:**

```turtle
ex:Element  lp:LP_0030051  ex:Beschreibung .          # hat Beschreibung
ex:Beschreibung  a lp:LP_0030003 ;                     # Klasse „Beschreibung“
                 lp:LP_0000344  "Text wie im PDF" .    # hat Wert
```

**Handgriff:** Den Blank Node durch einen benannten Knoten ersetzen, IRI im eigenen
Namensraum. Beispiel aus `nachbessern-bericht.md`: der Blank Node an `hat Beschreibung`
bei `kb-gott` wird zum benannten Knoten `data:kb-gott-beschreibung`.

## R13 — Text nicht an „hat Wert“

Der Wertknoten existiert und ist benannt, aber sein Text hängt an `rdfs:label` (oder
fehlt ganz) statt an `hat Wert` (LP_0000344).

**Soll:** wie R12 — Text an `lp:LP_0000344`, nicht an `rdfs:label`.

**Handgriff:** Den Text von `rdfs:label` nach `hat Wert` verschieben, `rdfs:label` darf
zusätzlich als technische Kurzbezeichnung stehen bleiben (`references/konventionen.md`),
ersetzt aber nie `hat Wert`. Beispiel: `data:kb-gott-titel` bekommt den fehlenden
`hat Wert`-Wert ergänzt, ohne das vorhandene `rdfs:label` zu entfernen.

## Ziel ohne geforderte Klasse (SHACL, `shacl:Class`)

Ein Verweis zeigt auf einen Knoten, der nicht die von der Shape geforderte Klasse trägt.
Drei Fälle kommen in der Praxis vor:

1. **`hat Beschreibung` zeigt auf die falsche Klasse** — meist CE-Hinweis (LP_0000852)
   statt Beschreibung (LP_0030003). Soll: `ex:Ziel a lp:LP_0030003 .` Beispiel aus
   `nachbessern-bericht.md`: `data:kb-gott-inhalt-1-hinweis` wird von `LP_0000852` auf
   `LP_0030003` umgetypt, IRI und Kante bleiben erhalten.
2. **`hat Teil` zeigt auf eine Klasse, die die Elternklasse nicht als Teil zulässt** —
   welche Klassen erlaubt sind, zeigt `scripts/klasse.sh <ID-der-Elternklasse>`, nicht die
   Muster-Datei.
3. **Eine benannte `rdfs:range`** einer anderen Property ist verletzt — Soll:
   `ex:Ziel a lp:<range-Klasse> .`, die konkrete Klasse liefert `references/terms/lp-terms.tsv`
   (Spalte `range`) oder `scripts/lookup.sh`.

**Handgriff:** Den Zielknoten auf die geforderte Klasse umtypen (`a`-Aussage ersetzen),
IRI und alle anderen Kanten unverändert lassen.

## Pflichtangabe fehlt (SHACL, `shacl:MinCount`)

Eine Shape verlangt eine Kante, die am Knoten fehlt.

**Soll**, wenn die fehlende Kante `ist Teil von` (obo:BFO_0000050) ist — die
Gegenrichtung zu `hat Teil`, meist an CE-Hinweis-Knoten verlangt:

```turtle
ex:Teil  obo:BFO_0000050  ex:Element .   # ist Teil von — die Gegenrichtung zu hat Teil
```

**Handgriff:** Vor dem Ergänzen prüfen, ob die Gegenkante bereits existiert (dann ist es
ein Reasoner-Artefakt, siehe unten) oder wirklich fehlt. Für andere Prädikate: die vom
Bericht genannte Kante mit dem geforderten Ziel ergänzen.

## Reasoner-Artefakte — kein Handlungsbedarf

Drei Befundarten fordern etwas, das ein Reasoner aus der Ontologie ableiten würde; die
Daten sind an dieser Stelle in Ordnung. Sie starten im Bericht eingeklappt und werden
**nicht** behoben:

- **Geforderter Wert fehlt** (`shacl:HasValue`) — meist „von Bundesland“ (jede
  SH-Klasse erbt diese Restriktion) oder „hat Funktion“.
- **Nur in Gegenrichtung vorhanden** (`shacl:MinCount · invers`) — die Shape verlangt
  `ist Teil von` oder „handelt von“, die Daten schreiben nur die Gegenrichtung
  (`hat Teil`), was korrekt ist.
- **Klasse eines Ontologie-Individuums** (`shacl:Class · Individuum`) — das Ziel ist ein
  echtes Individuum der Ontologie (z. B. `lp:LP_3000054`, Schleswig-Holstein), dem nur
  ohne Reasoner keine Klasse zugeordnet werden kann.

**Handgriff:** keiner. Wer hier etwas ergänzt — eine `ist Teil von`-Kante, eine
Klassenangabe am Individuum —, modelliert etwas hinzu, das die Ontologie bereits ableitet;
`beispiel.ttl` zeigt mit Exit 0 und 16 solchen Hinweisen, dass eine saubere Datei diese
Gruppen unverändert lässt.
