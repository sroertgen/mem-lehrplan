# Sachsen-Anhalt (ST)

Bundesland-Individuum: `lp:LP_3000053` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `ST_` in `references/terms/sf-terms.tsv` (39 Einträge; Wurzel `ST_0000000`).
Schulart-IDs: Präfix `ST_` in `references/terms/sa-terms.tsv` (7 Einträge; Wurzel `ST_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`ST_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (33)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000826 | Lehrplan (ST) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002174 | Lehrplanfragment (ST) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002175 | Kompetenzbereich (ST) |  |
| LP_0002181 | Kompetenzschwerpunkt (ST) |  |
| LP_0030078 | Themenbereich (ST) | Englisch Primar |
| LP_0030085 | Sprachliches Mittel (ST) | Englisch Gymnasium, Sekundarschule (Vergügung über ...) und Grundschule (Flexibel anwendbares Grundwissen zu ...) Kommt in dem Fach Englisch vor: In der Grundschule unter “Inhaltsbezogene Kompetenzen” und in der Sekundarschule und im Gymnasium unter dem Kompetenzbereich “Funktional-kommunikative Kompetenzen”. Beispiel für sprachliche Mittel sind “Wortschatz” oder “Grammatik”. |
| LP_0030087 | Bereich (ST) | Sachunterricht Prmiar |
| LP_0030096 | Inhaltsbereich (ST) | Mathe Sek I |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002093 | Element (ST) |  |
| LP_0030017 | Verweis auf Möglichkeit zur Abstimmung (ST) |  |
| LP_0030088 | Verweis auf Bezüge zu fächerübergreifenden Themen (ST) |  |
| LP_0030198 | Verweis auf allgemeine mathematische Kompetenzen (ST) | Kommt nur im Fach Mathematik vor |
| LP_0030318 | Schlüsselkompetenz (ST) | in Grundsatzband Gymnasium enthalten |
| LP_0030330 | Fachübergreifendes Thema (ST) | in Grundsatzband Grundschule enthalten |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Der Explorer leitet seit Version 0.4.0 aus dem benannten Glied der anonymen `owl:intersectionOf` eine `subClassOf`-Kante ab (A ⊑ (B ⊓ R) ⇒ A ⊑ B) — SHACL-Shapes der benannten Gliedklasse (z. B. „Element (SH)“) greifen deshalb trotzdem. Unsichtbar bleibt nur eine Klasse, deren Oberklassen-Ausdruck gar kein benanntes Glied enthält; `scripts/klasse.sh <ID>` zeigt, welcher Fall vorliegt.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000171 | Allgemeine Hochschulreife (ST) |  |
| LP_0000185 | Erster Abschluss (ST) |  |
| LP_0000209 | Mittlerer Abschluss (ST) |  |
| LP_0002094 | Fachniveau Sek II (ST) |  |
| LP_0002177 | Kompetenz (ST) |  |
| LP_0002178 | Flexibel anwendbares Grundwissen (ST) | Primar (Deutsch, Mathe, Sachunterricht) |
| LP_0002179 | Grundlegender Wissensbestand (ST) | (Sek I und II) |
| LP_0002182 | Gegenstandsfeld (ST) | Kommt bisher nur in Sek II Deutsch vor |
| LP_0030081 | Kommunikative Kompetenz (ST) | Englisch Primar und Sekundarschule. Hinweis: Die Überschrift “Kommunikative Kompetenz” selbst ist ein Kompetenzbereich (= CE-Bereich). |
| LP_0030082 | Inhaltsbezogene Kompetenz (ST) | kommt vor in Priamr für die Fächer Englisch, Sachunterricht und Mathe (hier heißen sie "inhaltliche mathematische Kompetenzen") |
| LP_0030083 | Prozessbezogene Kompetenz (ST) | kommt vor in Priamr für die Fächer Englisch, Sachunterricht und Mathe (hier heißen sie "allgemeine mathematische Kompetenzen") |
| LP_0030086 | Soziokulturelles Orientierungswissen (ST) | Kommt in dem Fach Englisch für die Sekundarschule und das Gymnasium vor unter dem Kompetenzbereich “Interkulturelle Kompetenzen”. |
| LP_0030089 | Verbindliches Schülerexperiment (ST) | Physik Sek II |
| LP_0030090 | Kommunikativer Inhalt (ST) | Kommt in dem Fach Englisch für die Sekundarschule und das Gymnasium vor. "Inhalt und Gegenstand der Kommunikation" ist in der Primarstufe einem Themenbereich untergeordnet (dem auch inhaltsbezogene Kompetenzen untergeordnet sind). |
| LP_0030184 | Interkulturelle Kompetenz (ST) | Englisch Primar. Hinweis: Die Überschrift “Interkulturelle Kompetenz” selbst ist ein Kompetenzbereich (= CE-Bereich). |
| LP_0030185 | Sprachlernkompetenz (ST) | Englisch Primar. Hinweis: Die Überschrift “Sprachlernkompetenz” selbst ist ein Kompetenzbereich (= CE-Bereich). |
| LP_0030186 | Text- und Medienkompetenz (ST) | Englisch Primar. Hinweis: Die Überschrift “Text- und Medienkompetenz” selbst ist ein Kompetenzbereich (= CE-Bereich). |
| LP_0030200 | Textsorte (ST) | Englisch Sekundarschule unter dem Kompetenzbereich “Funktional-kommunikative Kompetenzen” (und im Gymnasium unter dem Kompetenzbereich “Text- und Medienkompetenz” aufgeteilt in “Textsorten nur rezeptiv” und “Textsorten produktiv (rezeptive Beherrschung ist eingeschlossen)” als zwei von mehreren Unterbereichen.) |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0001035 | Bildungsgangniveau (ST) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (13)

| ID | Bezeichnung |
|---|---|
| LP_0000296 | Gymnasialniveau Sek I (ST) |
| LP_0000297 | Hauptschulabschlussbezogener Unterricht (ST) |
| LP_0000298 | Realschulabschlussbezogener Unterricht (ST) |
| LP_0000299 | Sekundarschulniveau (ST) |
| LP_0000402 | Allgemeinbildender Schulabschluss (ST) |
| LP_0000403 | Hauptschulabschluss (ST) |
| LP_0000404 | Qualifizierter Hauptschulabschluss (ST) |
| LP_0000405 | Realschulabschluss (ST) |
| LP_0000406 | Erweiterter Realschulabschluss (ST) |
| LP_0000526 | Grundlegendes Anforderungsniveau (ST) |
| LP_0000527 | Erhöhtes Anforderungsniveau (ST) |
| LP_0030357 | Gymnasialniveau Sek II (ST) |
| LP_0030375 | Grundschulniveau (ST) |
