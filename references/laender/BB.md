# Brandenburg (BB)

Bundesland-Individuum: `lp:LP_3000057` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `BB_` in `references/terms/sf-terms.tsv` (55 Einträge; Wurzel `BB_0000000`).
Schulart-IDs: Präfix `BB_` in `references/terms/sa-terms.tsv` (5 Einträge; Wurzel `BB_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`BB_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (37)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000807 | Rahmenlehrplan (BB) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002223 | Lehrplanfragment (BB) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000448 | Thema (BB) | kommt u.a. in Englisch vor |
| LP_0000449 | Themenfeld (BB) | kommt u.a. in Englisch  und Physik vor. "Themenbereich" in Mathe |
| LP_0000459 | Kompetenzbereich (BB) |  |
| LP_0002224 | Leitidee (BB) | Kommt in den Lehrplänen der Sek II für das Fach Mathematik vor. (In den Lehrplänen der Primarstufe und der Sek I für das Fach Mathematik werden stattdessen die Begriffe “Inhaltsbezogene mathematische Standards” oder “Themenbereiche” verwendet.) Der Begriff kommt aus den Bildungsstandards und bezeichnet dort einen inhaltsbezogenen Kompetenzbereich im Fach Mathematik. |
| LP_0030047 | Basiskonzept (BB) | NaWis |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000441 | Element (BB) | Die Unterschiede zw. Berlin und Brandenburg müssten evtl. noch mal genauer geprüft werden. Ggf. sind die Klassen hier noch zu trennen. |
| LP_0000451 | Übung (BB) |  |
| LP_0030042 | Verweis auf Bezüge zu den Basiskonzepten (BB) | NaWis |
| LP_0030255 | Verweis auf Materialien (BB) | Verlinkung zu Materialsammlung (=Dokumente) |
| LP_0030257 | Verweis auf vernetzte Kompetenzen (BB) | Verlinkung zu Kompetenzen anderer Fächer (meist zu "Medienbildung") |
| LP_0030259 | Verweis auf standardillustrierende Aufgaben (BB) | Verlinkung zu Dokument |
| LP_0030333 | Fachübergreifendes Thema (BB) |  |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Der Explorer leitet seit Version 0.4.0 aus dem benannten Glied der anonymen `owl:intersectionOf` eine `subClassOf`-Kante ab (A ⊑ (B ⊓ R) ⇒ A ⊑ B) — SHACL-Shapes der benannten Gliedklasse (z. B. „Element (SH)“) greifen deshalb trotzdem. Unsichtbar bleibt nur eine Klasse, deren Oberklassen-Ausdruck gar kein benanntes Glied enthält; `scripts/klasse.sh <ID>` zeigt, welcher Fall vorliegt.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000175 | Allgemeine Hochschulreife (BB) |  |
| LP_0000189 | Erster Abschluss (BB) |  |
| LP_0000213 | Mittlerer Abschluss (BB) |  |
| LP_0000445 | Inhalt (BB) |  |
| LP_0000446 | Lernmaterial (BB) |  |
| LP_0000447 | Standard (BB) | Inhaltsbezogener mathematischer Standard (BB) |
| LP_0000450 | Zusatzmaterial (BB) |  |
| LP_0002069 | Fachniveau Sek II (BB) |  |
| LP_0002225 | Eingangsvoraussetzung (BB) | Sek II |
| LP_0002226 | Gegenstand (BB) | Kommt bisher nur in Deutsch Sek II vor. |
| LP_0002227 | Unterrichtsanregung (BB) | Sachunterricht |
| LP_0030007 | Kompetenzerwerb im Themenfeld (BB) | Englisch Sek II |
| LP_0030008 | Möglicher Inhalt (BB) |  |
| LP_0030043 | Beispiel zu einem Basiskonzept (BB) | NaWis |
| LP_0030052 | Experiment/Untersuchung (BB) | NaWis |
| LP_0030066 | Vertiefungsmöglichkeit (BB) | Englisch |
| LP_0030210 | Fachbegriff (BB) | Kommt in den Naturwissenschaften vor. |
| LP_0030214 | Beispiel für Unterrichtseinheiten (BB) | NaWi 7-10 |
| LP_0030246 | Beispiel für Differenzierungsmöglichkeiten (BB) | Physik Sek I |
| LP_0030250 | Fachmethode (BB) | NaWi 5/6 |
| LP_0030251 | Technik (BB) | NaWi 5/6 |
| LP_0030253 | Möglicher Kontext (BB) | Kommt in Physik Sek I und Sek II vor. "weiterer Kontext" in NaWi 7-10 |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0030366 | Bildungsgangniveau (BB) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (8)

| ID | Bezeichnung |
|---|---|
| LP_0000231 | Berufsbildungsreife (BB) |
| LP_0000232 | Erweiterte Berufsbildungsreife (BB) |
| LP_0000233 | Fachoberschulreife (BB) |
| LP_0000234 | Berechtigung zum Besuch der gymnasialen Oberstufe (BB) |
| LP_0000235 | Allgemeinbildender Schulabschluss (BB) |
| LP_0000506 | Grundkursfach (BB) |
| LP_0000507 | Leistungskursfach (BB) |
| LP_0030403 | Oberstufenniveau (BB) |
