# Sachsen (SN)

Bundesland-Individuum: `lp:LP_3000047` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `SN_` in `references/terms/sf-terms.tsv` (51 Einträge; Wurzel `SN_0000000`).
Schulart-IDs: Präfix `SN_` in `references/terms/sa-terms.tsv` (7 Einträge; Wurzel `SN_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`SN_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (18)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000818 | Lehrplan (SN) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002110 | Lehrplanfragment (SN) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002113 | Lernbereich (SN) |  |
| LP_0002114 | Wahlbereich (SN) |  |
| LP_0030050 | Allgemeines fachliches Ziel (SN) |  |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002089 | Element (SN) |  |
| LP_0030188 | Verweis auf Lernbereich des gleichen Faches der gleichen Klassenstufe (SN) |  |
| LP_0030189 | Verweis auf Lernbereich des gleichen Faches einer anderen Klassenstufe (SN) |  |
| LP_0030190 | Verweis auf Klassenstufe, Lernbereich eines anderen Faches (SN) |  |
| LP_0030191 | Verweis auf ein überfachliches Bildungs- und Erziehungsziel (SN) |  |
| LP_0030329 | Bildungs- und Erziehungsziel (SN) |  |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000165 | Allgemeine Hochschulreife (SN) |  |
| LP_0000181 | Erster Abschluss (SN) |  |
| LP_0000205 | Mittlerer Abschluss (SN) |  |
| LP_0002090 | Fachniveau Sek II (SN) |  |
| LP_0002115 | Lernziel und Lerninhalt (SN) |  |
| LP_0002116 | Bemerkung (SN) |  |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0001032 | Bildungsgangniveau (SN) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (12)

| ID | Bezeichnung |
|---|---|
| LP_0000279 | Gymnasialniveau Sek I (SN) |
| LP_0000293 | Hauptschulbildungsgangniveau (SN) |
| LP_0000294 | Oberschulniveau (SN) |
| LP_0000295 | Realschulbildungsgangniveau (SN) |
| LP_0000389 | Allgemeinbildender Schulabschluss (SN) |
| LP_0000390 | Hauptschulabschluss (SN) |
| LP_0000391 | Qualifizierender Hauptschulabschluss (SN) |
| LP_0000392 | Realschulabschluss (SN) |
| LP_0000523 | Grundkurs (SN) |
| LP_0000524 | Leistungskurs (SN) |
| LP_0030356 | Gymnasialniveau Sek II (SN) |
| LP_0030374 | Grundschulniveau (SN) |
