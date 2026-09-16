# Schleswig-Holstein (SH)

Bundesland-Individuum: `lp:LP_3000054` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `SH_` in `references/terms/sf-terms.tsv` (36 Einträge; Wurzel `SH_0000000`).
Schulart-IDs: Präfix `SH_` in `references/terms/sa-terms.tsv` (4 Einträge; Wurzel `SH_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`SH_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (37)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000824 | Fachanforderung (SH) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0030033 | Lehrplanfragment (SH) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0030020 | Textsorte (SH) | Deutsch |
| LP_0030067 | Inhaltsbereich (SH) | Mathe Primar |
| LP_0030070 | Kompetenzbereich (SH) |  |
| LP_0030084 | Themenbereich (SH) | Englisch Sek I & II ("Verbindlicher Themenbereich" in Sek II) |
| LP_0030095 | Themenfeld (SH) | Sachunterricht |
| LP_0030249 | Sachgebiet (SH) | Pyhsik Sek I Mathe Sek II |
| LP_0030252 | Thema (SH) | Englisch Prim und Sek I: CE-Lerninhalt; Physik Sek II: Themen = CE-Lerninhalt; mögliche Vertiefungsthemen = CE-Hinweis |
| LP_0030258 | Leitidee (SH) | Mathe Sek I |
| LP_0030270 | Basiskonzept (SH) | NaWis |
| LP_0030273 | Bereich (SH) | Physik Sek II |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002103 | Element (SH) |  |
| LP_0030274 | Verweis auf Basiskonzept (SH) | NaWi |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Der Explorer leitet seit Version 0.4.0 aus dem benannten Glied der anonymen `owl:intersectionOf` eine `subClassOf`-Kante ab (A ⊑ (B ⊓ R) ⇒ A ⊑ B) — SHACL-Shapes der benannten Gliedklasse (z. B. „Element (SH)“) greifen deshalb trotzdem. Unsichtbar bleibt nur eine Klasse, deren Oberklassen-Ausdruck gar kein benanntes Glied enthält; `scripts/klasse.sh <ID>` zeigt, welcher Fall vorliegt.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000172 | Allgemeine Hochschulreife (SH) |  |
| LP_0000186 | Erster Abschluss (SH) |  |
| LP_0000210 | Mittlerer Abschluss (SH) |  |
| LP_0030010 | Fachniveau Sek II (SH) |  |
| LP_0030018 | KMK-Bildungsstandard (SH) | Deutsch |
| LP_0030021 | Inhalt und Wissbestand (SH) | Deutsch Sek II |
| LP_0030022 | Konkretisierung - Hinweis und Vorschlag (SH) | Deutsch sind entweder auf einen Bildungsstandard bezogen oder auf einen Inhalt und Wissensbestand |
| LP_0030023 | Themenvorschlag (SH) | Deutsch Sek II |
| LP_0030059 | Möglicher Inhalt (SH) | Englisch Primar |
| LP_0030079 | Mögliche Textsorte / Kommunikationssituation (SH) | Englisch Sek I |
| LP_0030254 | Thema und Inhalt (SH) | Mathe Deutsch Sek I |
| LP_0030256 | Kompetenz (SH) |  |
| LP_0030260 | Vorgabe und Hinweis (SH) | Mathe, Physik |
| LP_0030271 | Inhaltsbezogene Kompetenz (SH) | NaWis und Mathe |
| LP_0030272 | Verbindlicher Inhalt (SH) | Verbindlicher Fachinhalt Naturwissenschaften Sek I "Verbindlicher Inhalt" Physik Sek I & II |
| LP_0030275 | Aspekt (SH) | Physik |
| LP_0030276 | Beispielinhalt (SH) | Physik |
| LP_0030278 | Prozessbezogene Kompetenz (SH) |  |
| LP_0030279 | Verbindliches Thema und Inhalt (SH) | Mathe |
| LP_0030280 | Mögliches Thema und Inhalt (SH) | Sachunterricht |
| LP_0030281 | Mögliches Thema (SH) | Englisch Sek II |
| LP_0030282 | Inhalt (SH) | Englisch Sek I: CE-Hinweis; Naturwissenschaften: CE-Lerninhalt; Mathe Sek I & II: CE-Lerninhalt |

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
