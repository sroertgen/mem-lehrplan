# Baden-Württemberg (BW)

Bundesland-Individuum: `lp:LP_3000049` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `BW_` in `references/terms/sf-terms.tsv` (77 Einträge; Wurzel `BW_0000000`).
Schulart-IDs: Präfix `BW_` in `references/terms/sa-terms.tsv` (7 Einträge; Wurzel `BW_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`BW_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (24)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse |
|---|---|
| LP_0000806 | Bildungsplan (BW) |

### unter CE-Fragment (LP_0001015)

| ID | Klasse |
|---|---|
| LP_0002052 | Lehrplanfragment (BW) |

### unter CE-Bereich (LP_0000349)

| ID | Klasse |
|---|---|
| LP_0002057 | Prozessbezogene Kompetenz (BW) |
| LP_0002059 | Inhaltsbezogene Kompetenz (BW) |
| LP_0002063 | Leitidee (BW) |
| LP_0030049 | Themenfeld (BW) |
| LP_0030069 | Thema (BW) |
| LP_0030114 | Experiment (BW) |
| LP_0030174 | Kompetenzbereich (BW) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse |
|---|---|
| LP_0002051 | Element (BW) |
| LP_0030175 | Verweis auf die prozessbezogenen Kompetenzen (BW) |
| LP_0030176 | Verweis auf andere Standards für inhaltsbezogene Kompetenzen desselben Fachs (BW) |
| LP_0030177 | Verweis auf Leitperspektiven (BW) |
| LP_0030178 | Verweis auf andere Fächer (BW) |
| LP_0030179 | Umsetzungshilfen (BW) |
| LP_0030334 | Leitperspektive (BW) |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse |
|---|---|
| LP_0000144 | Erster Abschluss (BW) |
| LP_0000145 | Mittlerer Abschluss (BW) |
| LP_0000146 | Allgemeine Hochschulreife (BW) |
| LP_0002060 | Denkanstoß (BW) |
| LP_0002061 | Teilkompetenz (BW) |
| LP_0002064 | Fachniveau Sek II (BW) |
| LP_0030247 | Standard (BW) |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0001101 | Bildungsgangniveau (BW) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (12)

| ID | Bezeichnung |
|---|---|
| LP_0000014 | E Niveau (BW) |
| LP_0000016 | G Niveau (BW) |
| LP_0000018 | Gymnasialniveau Sek I (BW) |
| LP_0000022 | M Niveau (BW) |
| LP_0000148 | Allgemeinbildender Schulabschluss (BW) |
| LP_0000149 | Hauptschulabschluss (BW) |
| LP_0000150 | Mittlerer Schulabschluss (BW) |
| LP_0000510 | Leistungsfach (BW) |
| LP_0000511 | Basisfach (BW) |
| LP_0030345 | Gymnasialniveau Sek II (BW) |
| LP_0030360 | Oberstufenniveau (BW) |
| LP_0030362 | Grundschulniveau (BW) |
