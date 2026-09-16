# Brandenburg (BB)

Bundesland-Individuum: `lp:LP_3000057` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `BB_` in `references/terms/sf-terms.tsv` (55 Einträge; Wurzel `BB_0000000`).
Schulart-IDs: Präfix `BB_` in `references/terms/sa-terms.tsv` (5 Einträge; Wurzel `BB_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`BB_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (37)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse |
|---|---|
| LP_0000807 | Rahmenlehrplan (BB) |

### unter CE-Fragment (LP_0001015)

| ID | Klasse |
|---|---|
| LP_0002223 | Lehrplanfragment (BB) |

### unter CE-Bereich (LP_0000349)

| ID | Klasse |
|---|---|
| LP_0000448 | Thema (BB) |
| LP_0000449 | Themenfeld (BB) |
| LP_0000459 | Kompetenzbereich (BB) |
| LP_0002224 | Leitidee (BB) |
| LP_0030047 | Basiskonzept (BB) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse |
|---|---|
| LP_0000441 | Element (BB) |
| LP_0000451 | Übung (BB) |
| LP_0030042 | Verweis auf Bezüge zu den Basiskonzepten (BB) |
| LP_0030255 | Verweis auf Materialien (BB) |
| LP_0030257 | Verweis auf vernetzte Kompetenzen (BB) |
| LP_0030259 | Verweis auf standardillustrierende Aufgaben (BB) |
| LP_0030333 | Fachübergreifendes Thema (BB) |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse |
|---|---|
| LP_0000175 | Allgemeine Hochschulreife (BB) |
| LP_0000189 | Erster Abschluss (BB) |
| LP_0000213 | Mittlerer Abschluss (BB) |
| LP_0000445 | Inhalt (BB) |
| LP_0000446 | Lernmaterial (BB) |
| LP_0000447 | Standard (BB) |
| LP_0000450 | Zusatzmaterial (BB) |
| LP_0002069 | Fachniveau Sek II (BB) |
| LP_0002225 | Eingangsvoraussetzung (BB) |
| LP_0002226 | Gegenstand (BB) |
| LP_0002227 | Unterrichtsanregung (BB) |
| LP_0030007 | Kompetenzerwerb im Themenfeld (BB) |
| LP_0030008 | Möglicher Inhalt (BB) |
| LP_0030043 | Beispiel zu einem Basiskonzept (BB) |
| LP_0030052 | Experiment/Untersuchung (BB) |
| LP_0030066 | Vertiefungsmöglichkeit (BB) |
| LP_0030210 | Fachbegriff (BB) |
| LP_0030214 | Beispiel für Unterrichtseinheiten (BB) |
| LP_0030246 | Beispiel für Differenzierungsmöglichkeiten (BB) |
| LP_0030250 | Fachmethode (BB) |
| LP_0030251 | Technik (BB) |
| LP_0030253 | Möglicher Kontext (BB) |
| LP_0030366 | Bildungsgangniveau (BB) |

## Individuen des Landes (8)

| ID | Bezeichnung |
|---|---|
| LP_0000231 | Berufsbildungsreife (BB) |
| LP_0000232 | Erweiterte Berufsbildungsreife (BB) |
| LP_0000233 | Fachoberschulreife (BB) |
| LP_0000234 | Berechtigung zum Besuch der gymnasialen Oberstufe (BB) |
| LP_0000235 | Allgemeinbildender Schulabschluss (BB) |
| LP_0000506 | Grundkursfach (BB) |
| LP_0000507 | Leistungskursfach (BB) |
| LP_0030403 | Oberstufenniveau (BB) |
