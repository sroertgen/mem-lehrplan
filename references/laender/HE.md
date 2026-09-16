# Hessen (HE)

Bundesland-Individuum: `lp:LP_3000050` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `HE_` in `references/terms/sf-terms.tsv` (39 Einträge; Wurzel `HE_0000000`).
Schulart-IDs: Präfix `HE_` in `references/terms/sa-terms.tsv` (9 Einträge; Wurzel `HE_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`HE_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (17)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse |
|---|---|
| LP_0002184 | Kerncurriculum (HE) |

### unter CE-Fragment (LP_0001015)

| ID | Klasse |
|---|---|
| LP_0001001 | Lehrplanfragment (HE) |

### unter CE-Bereich (LP_0000349)

| ID | Klasse |
|---|---|
| LP_0001002 | Inhaltsfeld (HE) |
| LP_0001005 | Kompetenzbereich (HE) |
| LP_0030038 | Themenfeld (HE) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse |
|---|---|
| LP_0002076 | Element (HE) |
| LP_0030192 | Verweis auf Bezüge zu Kompetenzbereichen / Standards (HE) |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse |
|---|---|
| LP_0000168 | Allgemeine Hochschulreife (HE) |
| LP_0000182 | Erster Abschluss (HE) |
| LP_0000206 | Mittlerer Abschluss (HE) |
| LP_0002077 | Fachniveau Sek II (HE) |
| LP_0002169 | Bildungsstandard (HE) |
| LP_0002228 | Lernzeitbezogene Kompetenzerwartung (HE) |
| LP_0030037 | Schwerpunktsetzung (HE) |
| LP_0030076 | Inhalt zu einem Inhaltsfeld (HE) |
| LP_0030245 | Hinweis zu Bezüge zu Kompetenzbereichen / Standards (HE) |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0030039 | Bildungsgangniveau (HE) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (10)

| ID | Bezeichnung |
|---|---|
| LP_0000090 | Gymnasialniveau Sek I (HE) |
| LP_0000091 | Hauptschulniveau (HE) |
| LP_0000092 | Realschulniveau (HE) |
| LP_0000515 | Grundlegendes Anforderungsniveau (HE) |
| LP_0000516 | Erhöhtes Anforderungsniveau (HE) |
| LP_0002000 | Allgemeinbildender Schulabschluss (HE) |
| LP_0002001 | Hauptschulabschluss (HE) |
| LP_0002002 | Realschulabschluss (HE) |
| LP_0030348 | Oberstufenniveau (HE) |
| LP_0030365 | Grundschulniveau (HE) |
