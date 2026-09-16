# Berlin (BE)

Bundesland-Individuum: `lp:LP_3000048` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `BE_` in `references/terms/sf-terms.tsv` (51 Einträge; Wurzel `BE_0000000`).
Schulart-IDs: Präfix `BE_` in `references/terms/sa-terms.tsv` (5 Einträge; Wurzel `BE_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`BE_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (37)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0030004 | Rahmenlehrplan (BE) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0001223 | Lehrplanfragment (BE) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0001224 | Leitidee (BE) | Kommt in den Lehrplänen der Sek II für das Fach Mathematik vor. (In den Lehrplänen der Primarstufe und der Sek I für das Fach Mathematik werden stattdessen die Begriffe “Inhaltsbezogene mathematische Standards” oder “Themenbereiche” verwendet.) Der Begriff kommt aus den Bildungsstandards und bezeichnet dort einen inhaltsbezogenen Kompetenzbereich im Fach Mathematik. |
| LP_0001448 | Thema (BE) | kommt u.a. in Englisch vor |
| LP_0001449 | Themenfeld (BE) | kommt u.a. in Englisch und Physik vor. "Themenbereich" in Mathe |
| LP_0001459 | Kompetenzbereich (BE) |  |
| LP_0030123 | Basiskonzept (BE) | Kommt in den Naturwissenschaften vor. |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000423 | Verweis auf standardillustrierende Aufgaben (BE) | Verlinkung zu Dokument |
| LP_0000424 | Verweis auf vernetzte Kompetenzen  (BE) | Verlinkung zu Kompetenzen anderer Fächer (meist zu "Medienbildung") |
| LP_0000425 | Verweis auf Materialien (BE) | Verlinkung zu Materialsammlung (=Dokumente) |
| LP_0001441 | Element (BE) | Die Unterschiede zw. Berlin und Brandenburg müssten evtl. noch mal genauer geprüft werden. Ggf. sind die Klassen hier noch zu trennen. |
| LP_0001451 | Übung (BE) |  |
| LP_0030045 | Verweis auf Bezüge zu den Basiskonzepten (BE) | NaWis |
| LP_0030332 | Fachübergreifendes Thema (BE) |  |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000105 | Mittlerer Abschluss (BE) |  |
| LP_0000106 | Erster Abschluss (BE) |  |
| LP_0000109 | Allgemeine Hochschulreife (BE) |  |
| LP_0001169 | Fachniveau Sek II (BE) |  |
| LP_0001226 | Eingangsvoraussetzung (BE) | Sek II |
| LP_0001227 | Unterrichtsanregung (BE) | Sachunterricht |
| LP_0001228 | Gegenstand (BE) | Kommt bisher nur in Deutsch Sek II vor. |
| LP_0001445 | Inhalt (BE) |  |
| LP_0001446 | Lernmaterial (BE) |  |
| LP_0001447 | Standard (BE) | Inhaltsbezogener mathematischer Standard (BE) |
| LP_0001450 | Zusatzmaterial (BE) |  |
| LP_0030044 | Beispiel zu einem Basiskonzept (BE) | NaWis |
| LP_0030068 | Vertiefungsmöglichkeit (BE) | Englisch |
| LP_0030116 | Möglicher Kontext (BE) | Kommt in Physik Sek I und Sek II vor. "weiterer Kontext" in NaWi 7-10 |
| LP_0030117 | Fachbegriff (BE) | Kommt in den Naturwissenschaften / Physik Sek I vor. |
| LP_0030118 | Beispiel für Differenzierungsmöglichkeiten (BE) | Kommt in Physik Sek I vor. |
| LP_0030119 | Experiment/Untersuchung (BE) | Kommt in den Naturwissenschaften vor. |
| LP_0030120 | Technik (BE) | NaWi 5/6 |
| LP_0030122 | Fachmethode (BE) | NaWi 5/6 |
| LP_0030124 | Beispiel für Unterrichtseinheiten (BE) | NaWi 7-10 |
| LP_0030248 | Kompetenzerwerb im Themenfeld (BE) |  |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0000572 | Bildungsgangniveau (BE) | LP_0000028 „Bildungsgangniveau“ |
| LP_0000577 | Gymnasialniveau Sek I (BE) | LP_0000572 „Bildungsgangniveau (BE)“ |

## Individuen des Landes (7)

| ID | Bezeichnung |
|---|---|
| LP_0000133 | Allgemeinbildender Schulabschluss (BE) |
| LP_0000135 | Berufsbildungsreife (BE) |
| LP_0000136 | Erweiterte Berufsbildungsreife (BE) |
| LP_0000137 | Mittlerer Schulabschluss (BE) |
| LP_0001516 | Grundkursfach (BE) |
| LP_0001517 | Leistungskursfach (BE) |
| LP_0030377 | Oberstufenniveau (BE) |
