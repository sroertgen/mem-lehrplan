# Bremen (HB)

Bundesland-Individuum: `lp:LP_3000056` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `HB_` in `references/terms/sf-terms.tsv` (47 Einträge; Wurzel `HB_0000000`).
Schulart-IDs: Präfix `HB_` in `references/terms/sa-terms.tsv` (5 Einträge; Wurzel `HB_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`HB_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (28)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse |
|---|---|
| LP_0000821 | Bildungsplan (HB) |

### unter CE-Fragment (LP_0001015)

| ID | Klasse |
|---|---|
| LP_0002122 | Lehrplanfragment (HB) |

### unter CE-Bereich (LP_0000349)

| ID | Klasse |
|---|---|
| LP_0002126 | Aufgabenbereich (HB) |
| LP_0002130 | Themenbereich (HB) |
| LP_0002133 | Themenfeld (HB) |
| LP_0002135 | Kompetenzbereich (HB) |
| LP_0002193 | Sachgebiet (HB) |
| LP_0030238 | Rahmenthema (HB) |
| LP_0030239 | Basiskonzept (HB) |
| LP_0030242 | Inhaltsbereich (HB) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse |
|---|---|
| LP_0002118 | Element (HB) |
| LP_0030011 | Verweis auf Basiskonzept (HB) |
| LP_0030012 | Verweis auf Orientierungsrahmen (HB) |
| LP_0030013 | Verweis auf Kompetenz (HB) |
| LP_0030153 | Orientierungsrahmen (HB) |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse |
|---|---|
| LP_0000174 | Allgemeine Hochschulreife (HB) |
| LP_0000188 | Erster Abschluss (HB) |
| LP_0000212 | Mittlerer Abschluss (HB) |
| LP_0002119 | Fachniveau Sek II (HB) |
| LP_0002128 | Anforderung (HB) |
| LP_0002129 | Inhalt (HB) |
| LP_0002134 | Kommentar (HB) |
| LP_0030001 | Schwerpunktthema (HB) |
| LP_0030206 | Standard (HB) |
| LP_0030235 | Prozessbezogene Anforderung (HB) |
| LP_0030236 | Inhaltsbezogene Anforderung (HB) |
| LP_0030243 | Erweiterungsbaustein (Zugangswege/Anwendungsbereiche/Vertiefungen) (HB) |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0001105 | Bildungsgangniveau (HB) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (12)

| ID | Bezeichnung |
|---|---|
| LP_0000034 | Erweitertes Anforderungsniveau (HB) |
| LP_0000035 | Grundlegendes Anforderungsniveau (HB) |
| LP_0000038 | Gymnasialniveau Sek I (HB) |
| LP_0000044 | Oberschulniveau (HB) |
| LP_0000245 | Allgemeinbildender Schulabschluss (HB) |
| LP_0000246 | Erweiterte Berufsbildungsreife (HB) |
| LP_0000247 | Berufsbildungsreife (HB) |
| LP_0000248 | Mittlerer Schulabschluss (HB) |
| LP_0002120 | Anforderungsniveau Grundkurs (HB) |
| LP_0002121 | Anforderungsniveau Leistungskurs (HB) |
| LP_0030347 | Oberstufenniveau (HB) |
| LP_0030364 | Grundschulniveau (HB) |
