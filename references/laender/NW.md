# Nordrhein-Westfalen (NW)

Bundesland-Individuum: `lp:LP_3000044` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `NW_` in `references/terms/sf-terms.tsv` (69 Einträge; Wurzel `NW_0000000`).
Schulart-IDs: Präfix `NW_` in `references/terms/sa-terms.tsv` (7 Einträge; Wurzel `NW_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`NW_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (21)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse |
|---|---|
| LP_0001000 | Kernlehrplan (NW) |

### unter CE-Fragment (LP_0001015)

| ID | Klasse |
|---|---|
| LP_0002186 | Lehrplanfragment (NW) |

### unter CE-Bereich (LP_0000349)

| ID | Klasse |
|---|---|
| LP_0002187 | Kompetenzbereich (NW) |
| LP_0002190 | Teilkompetenzbereich (NW) |
| LP_0002191 | Inhaltsfeld (NW) |
| LP_0030073 | Bereich (NW) |
| LP_0030077 | Basiskonzept (NW) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse |
|---|---|
| LP_0002085 | Element (NW) |
| LP_0030009 | Verweis auf Basiskonzept (NW) |
| LP_0030187 | Verweis auf Kompetenzerwartung (NW) |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse |
|---|---|
| LP_0000162 | Allgemeine Hochschulreife (NW) |
| LP_0000178 | Erster Abschluss (NW) |
| LP_0000202 | Mittlerer Abschluss (NW) |
| LP_0002086 | Fachniveau Sek II (NW) |
| LP_0002188 | Kompetenzerwartung (NW) |
| LP_0002192 | Inhaltlicher Schwerpunkt (NW) |
| LP_0030005 | Ergänzung zu einem Basiskonzept (NW) |
| LP_0030006 | Möglicher Kontext (NW) |
| LP_0030074 | Fachliche Konkretisierung (NW) |
| LP_0030075 | Inhalt (NW) |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0030041 | Bildungsgangniveau (NW) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (15)

| ID | Bezeichnung |
|---|---|
| LP_0000130 | Erweiterungskurs (NW) |
| LP_0000131 | Gesamt-/Sekundarschulniveau (NW) |
| LP_0000132 | Gymnasialniveau Sek I (NW) |
| LP_0000134 | Hauptschulniveau (NW) |
| LP_0000138 | Niveau Mittlerer Schulabschluss (NW) |
| LP_0000142 | Realschulniveau (NW) |
| LP_0000373 | Allgemeinbildender Schulabschluss (NW) |
| LP_0000374 | Erster Schulabschluss (NW) |
| LP_0000375 | Erweiterter Erster Schulabschluss (NW) |
| LP_0000376 | Mittlerer Schulabschluss (NW) |
| LP_0000377 | Mittlerer Schulabschluss mit Berechtigung zur gymnasialen Oberstufe (NW) |
| LP_0000521 | Grundkurs (NW) |
| LP_0000522 | Leistungskurs (NW) |
| LP_0030351 | Gymnasialniveau Sek II (NW) |
| LP_0030370 | Grundschulniveau (NW) |
