# Berlin (BE)

Bundesland-Individuum: `lp:LP_3000048` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `BE_` in `references/terms/sf-terms.tsv` (51 Einträge; Wurzel `BE_0000000`).
Schulart-IDs: Präfix `BE_` in `references/terms/sa-terms.tsv` (5 Einträge; Wurzel `BE_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`BE_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (37)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse |
|---|---|
| LP_0030004 | Rahmenlehrplan (BE) |

### unter CE-Fragment (LP_0001015)

| ID | Klasse |
|---|---|
| LP_0001223 | Lehrplanfragment (BE) |

### unter CE-Bereich (LP_0000349)

| ID | Klasse |
|---|---|
| LP_0001224 | Leitidee (BE) |
| LP_0001448 | Thema (BE) |
| LP_0001449 | Themenfeld (BE) |
| LP_0001459 | Kompetenzbereich (BE) |
| LP_0030123 | Basiskonzept (BE) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse |
|---|---|
| LP_0000423 | Verweis auf standardillustrierende Aufgaben (BE) |
| LP_0000424 | Verweis auf vernetzte Kompetenzen  (BE) |
| LP_0000425 | Verweis auf Materialien (BE) |
| LP_0001441 | Element (BE) |
| LP_0001451 | Übung (BE) |
| LP_0030045 | Verweis auf Bezüge zu den Basiskonzepten (BE) |
| LP_0030332 | Fachübergreifendes Thema (BE) |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse |
|---|---|
| LP_0000105 | Mittlerer Abschluss (BE) |
| LP_0000106 | Erster Abschluss (BE) |
| LP_0000109 | Allgemeine Hochschulreife (BE) |
| LP_0001169 | Fachniveau Sek II (BE) |
| LP_0001226 | Eingangsvoraussetzung (BE) |
| LP_0001227 | Unterrichtsanregung (BE) |
| LP_0001228 | Gegenstand (BE) |
| LP_0001445 | Inhalt (BE) |
| LP_0001446 | Lernmaterial (BE) |
| LP_0001447 | Standard (BE) |
| LP_0001450 | Zusatzmaterial (BE) |
| LP_0030044 | Beispiel zu einem Basiskonzept (BE) |
| LP_0030068 | Vertiefungsmöglichkeit (BE) |
| LP_0030116 | Möglicher Kontext (BE) |
| LP_0030117 | Fachbegriff (BE) |
| LP_0030118 | Beispiel für Differenzierungsmöglichkeiten (BE) |
| LP_0030119 | Experiment/Untersuchung (BE) |
| LP_0030120 | Technik (BE) |
| LP_0030122 | Fachmethode (BE) |
| LP_0030124 | Beispiel für Unterrichtseinheiten (BE) |
| LP_0030248 | Kompetenzerwerb im Themenfeld (BE) |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0000572 | Bildungsgangniveau (BE) | LP_0000028 „Bildungsgangniveau“ |
| LP_0000577 | Gymnasialniveau Sek I (BE) | LP_0000572 „Bildungsgangniveau (BE)“ |

## Individuen des Landes (7)

| ID | Bezeichnung |
|---|---|
| LP_0000133 | Allgemeinbildender Schulabschluss (BE) |
| LP_0000135 | Berufsbildungsreife (BE) |
| LP_0000136 | Erweiterte Berufsbildungsreife (BE) |
| LP_0000137 | Mittlerer Schulabschluss (BE) |
| LP_0001516 | Grundkursfach (BE) |
| LP_0001517 | Leistungskursfach (BE) |
| LP_0030377 | Oberstufenniveau (BE) |
