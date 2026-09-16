# Hamburg (HH)

Bundesland-Individuum: `lp:LP_3000045` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `HH_` in `references/terms/sf-terms.tsv` (52 Einträge; Wurzel `HH_0000000`).
Schulart-IDs: Präfix `HH_` in `references/terms/sa-terms.tsv` (4 Einträge; Wurzel `HH_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`HH_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (35)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000822 | Bildungsplan (HH) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002210 | Lehrplanfragment (HH) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000428 | Inhalt (HH) |  |
| LP_0002211 | Leitidee (HH) |  |
| LP_0002212 | Kompetenzbereich (HH) |  |
| LP_0002218 | Thema (HH) |  |
| LP_0002219 | Modul (HH) | In Mathematik Sek II unter Inhalte. |
| LP_0002220 | Sachgebiet (HH) | Kommt bisher nur in Sek II Mathematik vor. |
| LP_0030144 | Themenbereich (HH) | Themenfeld (HH) |
| LP_0030169 | Redemittel und grammatische Grundlagen (HH) | kommt nur in Englisch Primar vor |
| LP_0030170 | Basisgrammatik (HH) | kommt nur in Englisch Sek I vor |
| LP_0030171 | Fachperspektive (HH) | nur in Sachunterricht Primar |
| LP_0030173 | Basiskonzept (HH) | nur in den NaWis |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000426 | Element (HH) |  |
| LP_0030167 | Verweis auf Leitperspektiven (HH) | Unter "Übergreifend" |
| LP_0030168 | Verweis auf Kompetenzen (HH) | Unter "Fachbezogen" |
| LP_0030193 | Verweis auf Aufgabengebiete (HH) | Unter "Übergreifend" |
| LP_0030194 | Verweis auf Sprachbildung (HH) | Unter "Übergreifend" |
| LP_0030195 | Verweis auf fachübergreifende Bezüge (HH) | Unter "Übergreifend" |
| LP_0030196 | Verweis auf Fachbegriffe (HH) | Unter "Fachbezogen" |
| LP_0030197 | Verweis auf fachinterne Bezüge (HH) | Unter "Fachbezogen" |
| LP_0030327 | Leitperspektive (HH) |  |
| LP_0030336 | Aufgabengebiet (HH) |  |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000163 | Allgemeine Hochschulreife (HH) |  |
| LP_0000179 | Erster Abschluss (HH) |  |
| LP_0000203 | Mittlerer Abschluss (HH) |  |
| LP_0002072 | Fachniveau Sek II (HH) |  |
| LP_0002214 | Beobachtungskriterium (HH) | Beobachtungsfragen in Sachunterrricht Primar Kommt nur in der Primarstufe für die Jahrgänge 1-2 vor. |
| LP_0002215 | Regelanforderung (HH) | Kommt nur in der Primarstufe für die Jahrgänge 3-4 vor. |
| LP_0002221 | Kompetenz (HH) |  |
| LP_0030115 | Anforderung (HH) |  |
| LP_0030165 | Leitgedanke (HH) | Oder eher Beschreibung von dem Themengebiet/Themenfeld/etc.? |
| LP_0030166 | Beitrag zur Leitperspektive (HH) | Ist auch CE-Verweis? |
| LP_0030172 | Bildungsstandard (HH) | Sachunterricht Primar |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0001108 | Bildungsgangniveau (HH) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (14)

| ID | Bezeichnung |
|---|---|
| LP_0000060 | Allgemeinbildender Schulabschluss (HH) |
| LP_0000093 | Erhöhte Anforderungen (HH) |
| LP_0000094 | Gymnasialniveau Sek I (HH) |
| LP_0000095 | Mindestanforderungen (HH) |
| LP_0000096 | Mindestanforderungen für den ersten allgemeinbildenden Schulabschluss (HH) |
| LP_0000097 | Mindestanforderungen für den mittleren Schulabschluss (HH) |
| LP_0000098 | Mindestanforderungen für den Übergang in die Studienstufe (HH) |
| LP_0000270 | Mittlerer Schulabschluss (HH) |
| LP_0000271 | Erster allgemeinbildender Schulabschluss (HH) |
| LP_0000272 | Erweiterter erste allgemeinbildender Schulabschluss (HH) |
| LP_0000517 | Erhöhtes Anforderungsniveau (HH) |
| LP_0000518 | Grundlegendes Anforderungsniveau (HH) |
| LP_0030349 | Studienstufenniveau (HH) |
| LP_0030367 | Grundschulniveau (HH) |
