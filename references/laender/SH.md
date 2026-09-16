# Schleswig-Holstein (SH)

Bundesland-Individuum: `lp:LP_3000054` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `SH_` in `references/terms/sf-terms.tsv` (36 Einträge; Wurzel `SH_0000000`).
Schulart-IDs: Präfix `SH_` in `references/terms/sa-terms.tsv` (4 Einträge; Wurzel `SH_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`SH_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (37)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse |
|---|---|
| LP_0000824 | Fachanforderung (SH) |

### unter CE-Fragment (LP_0001015)

| ID | Klasse |
|---|---|
| LP_0030033 | Lehrplanfragment (SH) |

### unter CE-Bereich (LP_0000349)

| ID | Klasse |
|---|---|
| LP_0030020 | Textsorte (SH) |
| LP_0030067 | Inhaltsbereich (SH) |
| LP_0030070 | Kompetenzbereich (SH) |
| LP_0030084 | Themenbereich (SH) |
| LP_0030095 | Themenfeld (SH) |
| LP_0030249 | Sachgebiet (SH) |
| LP_0030252 | Thema (SH) |
| LP_0030258 | Leitidee (SH) |
| LP_0030270 | Basiskonzept (SH) |
| LP_0030273 | Bereich (SH) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse |
|---|---|
| LP_0002103 | Element (SH) |
| LP_0030274 | Verweis auf Basiskonzept (SH) |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse |
|---|---|
| LP_0000172 | Allgemeine Hochschulreife (SH) |
| LP_0000186 | Erster Abschluss (SH) |
| LP_0000210 | Mittlerer Abschluss (SH) |
| LP_0030010 | Fachniveau Sek II (SH) |
| LP_0030018 | KMK-Bildungsstandard (SH) |
| LP_0030021 | Inhalt und Wissbestand (SH) |
| LP_0030022 | Konkretisierung - Hinweis und Vorschlag (SH) |
| LP_0030023 | Themenvorschlag (SH) |
| LP_0030059 | Möglicher Inhalt (SH) |
| LP_0030079 | Mögliche Textsorte / Kommunikationssituation (SH) |
| LP_0030254 | Thema und Inhalt (SH) |
| LP_0030256 | Kompetenz (SH) |
| LP_0030260 | Vorgabe und Hinweis (SH) |
| LP_0030271 | Inhaltsbezogene Kompetenz (SH) |
| LP_0030272 | Verbindlicher Inhalt (SH) |
| LP_0030275 | Aspekt (SH) |
| LP_0030276 | Beispielinhalt (SH) |
| LP_0030278 | Prozessbezogene Kompetenz (SH) |
| LP_0030279 | Verbindliches Thema und Inhalt (SH) |
| LP_0030280 | Mögliches Thema und Inhalt (SH) |
| LP_0030281 | Mögliches Thema (SH) |
| LP_0030282 | Inhalt (SH) |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0030091 | Bildungsgangniveau (SH) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (11)

| ID | Bezeichnung |
|---|---|
| LP_0000193 | Anforderungen für den Ersten allgemeinbildenden Schulabschluss (SH) |
| LP_0000216 | Anforderungen für den Mittleren Schulabschluss (SH) |
| LP_0000236 | Anforderungen für die Allgemeine Hochschulreife Sek I (SH) |
| LP_0000249 | Sekundarstufenniveau (SH) |
| LP_0002033 | Allgemeinbildender Schulabschluss (SH) |
| LP_0002034 | Erster allgemeinbildender Schulabschluss (SH) |
| LP_0002035 | Mittlerer Schulabschluss (SH) |
| LP_0030040 | Grundlegendes Niveau (SH) |
| LP_0030046 | Erhöhtes Niveau (SH) |
| LP_0030354 | Anforderungen für die Allgemeine Hochschulreife Sek II (SH) |
| LP_0030372 | Grundschulniveau (SH) |
