# Baseline — Ausgangsläufe ohne Skill (RED)

Sechs Läufe, je zwei pro Szenario aus `docs/testing/szenarien.md`, jeweils ein frischer
`general-purpose`-Subagent ohne Erwähnung der Skill. Geprüft mit mem-explorer 0.4.0
(`node ~/coding/comenius/mem-explorer/bin/mem-explorer.mjs check`). Zahlen und Rohdaten aus
`.superpowers/sdd/2026-09-14-mem-lehrplan-skill/task-5-baseline-scores.md` und
`task-5-agent-returns.md` (Controller-Messung); Rohausgaben liegen unter
`docs/testing/baseline/`.

## Szenario 1 — Transformieren

### Lauf 1 (`szenario-1-lauf-1.ttl`)

- Exit: 1
- Kopfzeile: 18 Befunde · 0 mehrfach bestätigt · 1 Fehler, 8 Warnungen, 9 Hinweise (9 Reasoner-Artefakte)
- Befundgruppen (ohne Reasoner-Artefakte):
  - Wertknoten als Blank Node — hat Titel (3) · Regel
  - Text nicht an „hat Wert“ — hat Titel (3) · Regel
  - Wertknoten als Blank Node — hat Beschreibung (1) · Regel
  - Text nicht an „hat Wert“ — hat Beschreibung (1) · Regel
  - Ziel ohne geforderte Klasse — hat Beschreibung (1) · SHACL
- Erfundene IDs: 0 von 19 verwendeten Ontologie-IDs
- Blank Nodes: ja (4 `[`)
- Jahrgangsstufe als Literal: nein
- Textträger am Titelknoten: `rdfs:label`, nicht `hat Wert` (0 Zeilen `hat Wert` gesamt, 11 `rdfs:label`-Zeilen)
- CE-Hinweis (LP_0000852) statt Beschreibung verwendet: 1×
- Datennamensraum: `data: <https://lp-sh.org/resource/>` (aus der SH-Datei übernommen, nicht selbst gewählt)

Begründung (wörtlich):

> Meine Entscheidungen zu Klassen, IDs und Schreibweise stützen sich erstens auf die kuratierte MEM-Wissensbasis (`~/coding/mem-knowledge-base/MEM.md` und `reference/lp-terms.tsv`), aus der ich jede ID nachgeschlagen und nicht geraten habe — etwa `LP_0000824` (Fachanforderung SH), `LP_0030070` (Kompetenzbereich SH), `LP_0030278` (Prozessbezogene Kompetenz SH) und `LP_0030280` (Mögliches Thema und Inhalt SH), sowie die Individuen `LP_3000054` (Schleswig-Holstein), `SH_0000008` (Schulfach Ev. Religion), `SH_0000003` (Schulart Gymnasium) und `LP_2000005`/`LP_2000006` (Jahrgangsstufe 5/6). Zweitens habe ich mich eng an das reale, bereits geprüfte Referenzbeispiel `~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl` gehalten, das exakt denselben Lehrplan (inklusive desselben Kompetenzbereichs „Die Frage nach Gott“) bereits modelliert — daher dieselben Muster: Titel/Beschreibung als Blank Nodes vom Typ `lp:LP_0000346`/`lp:LP_0000852` statt Literale, `obo:BFO_0000051` für die Teil-Hierarchie, `lp:LP_0000026` mit realen Jahrgangsstufen-Individuen statt Textspannen, und den Datennamensraum `data: <https://lp-sh.org/resource/>`. Drittens habe ich die Datei mit dem projekteigenen `n3`-Parser syntaktisch verifiziert, bevor ich sie als Ergebnis ausgegeben habe.

### Lauf 2 (`szenario-1-lauf-2.ttl`)

- Exit: 1
- Kopfzeile: 20 Befunde · 0 mehrfach bestätigt · 1 Fehler, 10 Warnungen, 9 Hinweise (9 Reasoner-Artefakte)
- Befundgruppen (ohne Reasoner-Artefakte):
  - Wertknoten als Blank Node — hat Titel (4) · Regel
  - Text nicht an „hat Wert“ — hat Titel (4) · Regel
  - Wertknoten als Blank Node — hat Beschreibung (1) · Regel
  - Text nicht an „hat Wert“ — hat Beschreibung (1) · Regel
  - Ziel ohne geforderte Klasse — hat Beschreibung (1) · SHACL
- Erfundene IDs: 0 von 19 verwendeten Ontologie-IDs
- Blank Nodes: ja (5 `[`)
- Jahrgangsstufe als Literal: nein
- Textträger am Titelknoten: `rdfs:label`, nicht `hat Wert` (0 Zeilen `hat Wert` gesamt, 12 `rdfs:label`-Zeilen)
- CE-Hinweis (LP_0000852) statt Beschreibung verwendet: 1×
- Datennamensraum: `data: <https://lp-sh.org/resource/>` (aus der SH-Datei übernommen)

Begründung (wörtlich):

> Meine Entscheidungen zu Klassen, IDs und Schreibweise stützen sich auf drei Quellen: Erstens auf `~/coding/mem-knowledge-base/reference/lp-terms.tsv`, wo ich jede verwendete ID einzeln nachgeschlagen habe (`LP_0000824` Fachanforderung SH, `LP_0030070` Kompetenzbereich SH, `LP_0030278` Prozessbezogene Kompetenz SH, `LP_0030280` Mögliches Thema und Inhalt SH, sowie die Objektproperties `LP_0030056`/`LP_0030051`/`LP_0000026`/`LP_0000029`/`LP_0000537`/`LP_0000812`/`LP_0000047`) statt IDs zu raten. Zweitens auf das reale, bereits produktiv erstellte Referenzdokument `~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl` — exakt dieselbe Fachanforderung (SH, Ev. Religion) —, dessen Muster ich übernommen habe: Titel/Beschreibung als eigene Blank Nodes vom Typ `lp:LP_0000346`/`lp:LP_0000852` statt als reine Literale, Jahrgangsstufenbezug über die Individuen `lp:LP_2000005`/`LP_2000006` statt als String, und den Datennamensraum `data: <https://lp-sh.org/resource/>`. Drittens auf die Schulfach-/Schulart-Tabellen (`sf-terms.tsv`, `sa-terms.tsv`) für die IRIs `https://w3id.org/schulfach/SH_0000008` (Evangelische Religion) und `https://w3id.org/schulart/SH_0000003` (Gymnasium) — nur Gymnasium getaggt, da die Aufgabe ausdrücklich nur diese Schulart nennt, anders als im Referenzdokument, das zusätzlich Gemeinschaftsschule enthält.

## Szenario 2 — Nachbessern

### Lauf 1 (`szenario-2-lauf-1.ttl`)

- Exit: 0
- Kopfzeile: 17 Befunde · 0 mehrfach bestätigt · 0 Fehler, 0 Warnungen, 17 Hinweise (17 Reasoner-Artefakte)
- Befundgruppen (ohne Reasoner-Artefakte): keine
- IRI-Diff gegen die Fixture: 0 fehlende Fixture-Subjekte; 2 neue Subjekte ergänzt (`data:fachanforderung-titel`, `data:kb-gott-beschreibung` — von der Korrektur der Fehler 1 und 2 verlangt); kein Reasoner-Artefakt „repariert“ (0 hinzugefügte `ist Teil von`/`hat Funktion`-Kanten)
- Blank Nodes: nein (0 `[`)
- Jahrgangsstufe als Literal: nein — durch die Individuen ersetzt
- Textträger am Titelknoten: `hat Wert` vorhanden (10 Zeilen), zusätzlich `rdfs:label` als Konvention (19 Zeilen gesamt)
- CE-Hinweis (LP_0000852) im Ergebnis: 1× — aber korrigiert auf die geforderte Klasse (siehe Begründung)

Begründung (wörtlich):

> Alle fünf Fehlerklassen behoben:
> 1. `hat Titel` an `fachanforderung`: Literal ersetzt durch benannten Knoten `data:fachanforderung-titel` (Klasse Titel, hat Wert).
> 2. `hat Beschreibung` an `kb-gott`: Blank Node ersetzt durch benannten Knoten `data:kb-gott-beschreibung` (Klasse Beschreibung, hat Wert).
> 3. `data:kb-gott-titel`: fehlendes `hat Wert` ergänzt.
> 4. `hat Jahrgangsstufe` an `kb-gott-pk-1`: Literal `"5-6"` ersetzt durch die Individuen `lp:LP_2000005` und `lp:LP_2000006`.
> 5. `data:kb-gott-inhalt-1-hinweis`: Klasse von CE-Hinweis (LP_0000852) auf Beschreibung (LP_0030003) korrigiert — behebt sowohl die SHACL-Meldung „Ziel ohne geforderte Klasse“ als auch die daran hängende „Pflichtangabe fehlt — ist Teil von“ (die nur für CE-Hinweis-Knoten gilt).
>
> Keine IRI wurde verändert; die 15 als Reasoner-Artefakt markierten Hinweise wurden unangetastet gelassen, wie im Bericht verlangt.
>
> Gestützt habe ich die Korrekturen auf drei Dinge: die im Bericht angegebenen Soll-Muster (Pattern 2 für Titel/Beschreibung, Pattern 5 für Jahrgangsstufen) samt der Ontologie-Doku-Links; die Referenzdatei `references/beispiel.ttl`, aus der `nachbessern.ttl` laut Kopfkommentar absichtlich kaputt abgeleitet wurde und die für die betroffenen Knoten (Titel- und Beschreibungstexte, Jahrgangsstufen-Individuen) die exakten Originalwerte lieferte; und die explizite Vorgabe, nur Werte/Typen zu ändern bzw. den in Fehler 5 beschriebenen Zusatzknoten typmäßig zu korrigieren, ohne irgendeine IRI anzufassen.

### Lauf 2 (`szenario-2-lauf-2.ttl`)

- Exit: 0
- Kopfzeile: 17 Befunde · 0 mehrfach bestätigt · 0 Fehler, 0 Warnungen, 17 Hinweise (17 Reasoner-Artefakte)
- Befundgruppen (ohne Reasoner-Artefakte): keine
- IRI-Diff gegen die Fixture: 0 fehlende Fixture-Subjekte; 2 neue Subjekte ergänzt (`data:fachanforderung-titel`, `data:kb-gott-beschreibung`); kein Reasoner-Artefakt „repariert“ (0 hinzugefügte `ist Teil von`/`hat Funktion`-Kanten)
- Blank Nodes: nein (0 `[`)
- Jahrgangsstufe als Literal: nein — durch die Individuen ersetzt
- Textträger am Titelknoten: `hat Wert` vorhanden (10 Zeilen), zusätzlich `rdfs:label` als Konvention (19 Zeilen gesamt)

Begründung (wörtlich):

> Die korrigierte Datei liegt unter `.../szenario-2-lauf-2.ttl`.
>
> Alle fünf Fehlerklassen behoben:
> 1. `hat Titel` an `fachanforderung`: Literal ersetzt durch benannten Knoten `data:fachanforderung-titel` (Klasse Titel, hat Wert).
> 2. `hat Beschreibung` an `kb-gott`: Blank Node ersetzt durch benannten Knoten `data:kb-gott-beschreibung` (Klasse Beschreibung, hat Wert).
> 3. `data:kb-gott-titel`: fehlendes `hat Wert` ergänzt.
> 4. `hat Jahrgangsstufe` an `kb-gott-pk-1`: Literal `"5-6"` ersetzt durch die Individuen `lp:LP_2000005` und `lp:LP_2000006`.
> 5. `data:kb-gott-inhalt-1-hinweis`: Klasse von CE-Hinweis (LP_0000852) auf Beschreibung (LP_0030003) korrigiert — behebt sowohl die SHACL-Meldung „Ziel ohne geforderte Klasse“ als auch die daran hängende „Pflichtangabe fehlt — ist Teil von“ (die nur für CE-Hinweis-Knoten gilt).
>
> Keine IRI wurde verändert; die 15 als Reasoner-Artefakt markierten Hinweise wurden unangetastet gelassen, wie im Bericht verlangt.
>
> Gestützt habe ich die Korrekturen auf drei Dinge: die im Bericht angegebenen Soll-Muster (Pattern 2 für Titel/Beschreibung, Pattern 5 für Jahrgangsstufen) samt der Ontologie-Doku-Links; die Referenzdatei `references/beispiel.ttl`, aus der `nachbessern.ttl` laut Kopfkommentar absichtlich kaputt abgeleitet wurde und die für die betroffenen Knoten (Titel- und Beschreibungstexte, Jahrgangsstufen-Individuen) die exakten Originalwerte lieferte; und die explizite Vorgabe, nur Werte/Typen zu ändern bzw. den in Fehler 5 beschriebenen Zusatzknoten typmäßig zu korrigieren, ohne irgendeine IRI anzufassen.

(Beide Läufe stammen von unterschiedlichen Subagenten, formulieren die Fehlerliste aber
nahezu deckungsgleich — plausibel, weil beide dieselben zwei Quellen hatten: den Bericht
und `beispiel.ttl`.)

## Szenario 3 — Nachschlagen

### Lauf 1 (`szenario-3-lauf-1.md`)

- 548 Wörter
- Nennt `LP_0030280`: 13×
- Nennt den „blinden Fleck“ aus `mem-explorer/CLAUDE.md`: 2×
- Quellen laut Datei: `mem-knowledge-base/MEM.md`, `mem-knowledge-base/reference/lp-terms.tsv`, `mem-knowledge-base/vendor/`, `relidesk-mem-lehrplan-transformation/schleswig-holstein/`

Begründung (wörtlich):

> Kurzfassung: Die Klasse ist `lp:LP_0030280` („Mögliches Thema und Inhalt (SH)“), in der SH-Praxis für „Mögliche Konkretionen“ verwendet. Sie hängt nur über eine anonyme OWL-Intersection (nicht per direktem `rdfs:subClassOf`) an `lp:LP_0002103` („Element (SH)“), definiert über `lp:LP_0000483` (hat Funktion) mit Wert `lp:LP_0001014` (Hinweisbeschreibungsfunktion) — einer der beiden im mem-explorer-CLAUDE.md dokumentierten blinden Flecken (`LP_0030278`/`LP_0030280`). Für ihre Teile (`obo:BFO_0000051`, has part) definiert die Ontologie **keine** Einschränkung — weder OWL-Restriktion noch SHACL-Shape nennt `LP_0030280` als Domain einer Part-Regel (zum Vergleich: die SH-Wurzelklasse `LP_0000824` schränkt ihre Teile explizit per SHACL auf `LP_0002103` ein). In der realen SH-Ev.-Religion-Transformation enthalten Konkretions-Container über `BFO_0000051` weitere Knoten, die wieder vom selben Typ `LP_0030280` sind — das ist Datenkonvention, keine Ontologie-Vorschrift.
>
> Die Angaben stammen aus den gespiegelten Originalquellen in `~/coding/mem-knowledge-base/vendor/lehrplan-ontologie/` (`lp.ttl`, `lp-land-SH-full.owl`, `shapes/auto-shapes/auto-shapes-open.ttl`) und der Term-Referenz `~/coding/mem-knowledge-base/reference/lp-terms.tsv`; die reale Verwendung stammt aus `~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl`, auf das auch `MEM.md` als Beispielprojekt verweist.

### Lauf 2 (`szenario-3-lauf-2.md`)

- 420 Wörter
- Nennt `LP_0030280`: 17×
- Nennt den „blinden Fleck“ aus `mem-explorer/CLAUDE.md`: 2×
- Quellen laut Datei: `mem-knowledge-base/MEM.md`, `mem-knowledge-base/vendor/lehrplan-ontologie/lp-base.ttl`, `relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl`, `src/lib/ontology/generated/{terms.json,shapes.ttl}`

Begründung (wörtlich):

> **Klasse:** `LP_0030280` — „Mögliches Thema und Inhalt (SH)“. Ontologisch definiert als Schnittmenge aus `LP_0002103` („Element (SH)“) und der Bedingung `LP_0000483` (hat Funktion) `= LP_0001014` (Hinweisbeschreibungsfunktion). Bestätigt durch echte Nutzdaten: `Kompetenzbereich (SH)` = `LP_0030070` hat über `obo:BFO_0000051` (has part) `LP_0030280`-Knoten mit Label „Mögliche Konkretionen (Jahrgangsstufe …)“ als Teile.
>
> **Was er als Teile haben darf:** Die Ontologie schränkt das gar nicht ein — `LP_0030280` trägt keine eigene has-part-Restriktion, und da sein Obertyp nur ein anonymer OWL-Ausdruck ist (keine benannte Oberklasse außer `LP_0002103`), gibt es keine vererbte Beschränkung; auch im generierten `shapes.ttl` taucht `LP_0030280` an keiner Stelle als Shape-Target auf. Das deckt sich exakt mit einem der beiden in `mem-explorer/CLAUDE.md` dokumentierten blinden Flecken (LP_0030278/LP_0030280 ohne benannte Oberklasse). In der Praxis (Konvention, nicht Zwang) sind die Teile eines solchen Knotens wieder `LP_0030280`-Knoten selbst — Container mit einzelnen Konkretions-Einträgen desselben Typs.
>
> Quellen laut Datei: das gespiegelte Ontologie-Original `~/coding/mem-knowledge-base/vendor/lehrplan-ontologie/lp-base.ttl` sowie die generierten Artefakte `src/lib/ontology/generated/{terms.json,shapes.ttl}` des mem-explorer-Repos; zusätzlich verifiziert an echten SH-Curriculumdaten (`relidesk-mem-lehrplan-transformation` und die mem-explorer-Testfixture `sekundarstufe.ttl`).

## Muster

- **Szenario 1 scheitert in beiden Läufen identisch am Wertknoten-Muster**, nicht an der
  ID-Recherche: 0 `hat Wert`-Zeilen, Blank Nodes (4 bzw. 5), `rdfs:label` als alleiniger
  Textträger, ein CE-Hinweis-Knoten (LP_0000852) statt eines Beschreibung-Knotens
  (LP_0030003) — bei gleichzeitig 0 erfundenen IDs (19 von 19 korrekt). Beide Agenten
  begründen das nahezu wortgleich mit einem realen, bereits vorhandenen Referenzdokument
  ("das reale, bereits geprüfte Referenzbeispiel" / "bereits produktiv erstellte
  Referenzdokument"), dessen Muster sie ausdrücklich übernehmen, statt Pattern 2 der
  Ontologie-Dokumentation zu folgen. Das ist der Satz, gegen den `SKILL.md` geschrieben
  werden muss: die Existenz eines lokalen, ungeprüften Referenzdokuments schlägt die
  dokumentierten Muster.
- **Szenario 2 gelingt in beiden Läufen zuverlässig** (Exit 0, IRIs unverändert, keine
  Reasoner-Artefakt-Kante hinzugefügt), wenn der Prüfbericht die Soll-Blöcke zu jedem
  Befund mitliefert — die Agenten zitieren diese Soll-Blöcke wörtlich als Grundlage.
  Mit dem Vorbehalt unten (Fixture-Leck) ist dieses Ergebnis aber nur bedingt belastbar.
- **Szenario 3 nennt in beiden Läufen korrekt `LP_0030280`**, stützt die Antwort aber auf
  den in `mem-explorer/CLAUDE.md` dokumentierten „blinden Fleck“ (fehlende Restriktion,
  keine benannte Oberklasse) — eine Aussage, die laut mem-explorer-Projekt seit Version
  0.4.0 veraltet ist (siehe Vorbehalte).

## Vorbehalte

1. **Kontamination durch lokale Wissensbasis.** Auf dieser Maschine liegen sowohl eine
   kuratierte MEM-Wissensbasis (`~/coding/mem-knowledge-base`) als auch die echte
   SH-Transformation (`relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl`).
   Beide Szenario-1-Agenten haben ihre Muster (Blank-Node-Titel/-Beschreibung mit
   `rdfs:label`, CE-Hinweis LP_0000852, Datennamensraum `https://lp-sh.org/resource/`)
   wörtlich aus dieser SH-Datei übernommen und sie als „bereits geprüft“/„bereits
   produktiv“ bezeichnet — die Baseline misst hier also „Agent mit lokalem Vorwissen“, nicht
   „Agent ohne jede Vorlage“. Ebenso berufen sich beide Szenario-3-Agenten auf den
   „blinden Fleck“-Hinweis aus `mem-explorer/CLAUDE.md`, der seit Explorer 0.4.0 (durch die
   aus `owl:intersectionOf` abgeleiteten Hierarchie-Kanten) veraltet ist — eine lokal
   vorhandene, aber überholte Aussage wurde ungeprüft übernommen.
2. **Fixture-Leck bei Szenario 2.** Der Kopfkommentar von `nachbessern.ttl` nennt
   `references/beispiel.ttl` ausdrücklich als Quelle der Fixture. Beide Szenario-2-Agenten
   haben `beispiel.ttl` gelesen und daraus die exakten Originaltexte übernommen
   („1 Die Frage nach Gott“, der Beschreibungssatz), die im Fixture selbst nicht mehr
   stehen. Ihr Exit 0 ist damit teilweise kopiert statt selbst hergeleitet. Das ist als
   Grenze des Szenario-Designs zu werten, nicht als Fehlverhalten der Agenten — für
   GREEN-Läufe (mit Skill) wäre zu erwägen, diesen Quellenhinweis aus dem Kopfkommentar der
   Fixture zu entfernen (hier nur vermerkt, nicht umgesetzt).
