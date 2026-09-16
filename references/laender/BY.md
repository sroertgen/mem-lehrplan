# Bayern (BY)

Bundesland-Individuum: `lp:LP_3000051` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `BY_` in `references/terms/sf-terms.tsv` (119 Einträge; Wurzel `BY_0000000`).
Schulart-IDs: Präfix `BY_` in `references/terms/sa-terms.tsv` (13 Einträge; Wurzel `BY_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`BY_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (31)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse |
|---|---|
| LP_0000819 | LehrplanPLUS (BY) |

### unter CE-Fragment (LP_0001015)

| ID | Klasse |
|---|---|
| LP_0002043 | Fachlehrplan (BY) |
| LP_0002044 | Lehrplanfragment (BY) |
| LP_0030304 | Bildungs- und Erziehungsauftrag (BY) |
| LP_0030305 | Übergreifende Bildungs- und Erziehungsziele (BY) |
| LP_0030306 | Fachprofil (BY) |
| LP_0030307 | Grundlegende Kompetenzen (Jahrgangsstufenprofil) (BY) |
| LP_0030308 | Bayerische Leitlinie für die Bildung und Erziehung von Kindern bis zum Ender der Grundschulzeit (BY) |

### unter CE-Bereich (LP_0000349)

| ID | Klasse |
|---|---|
| LP_0002046 | Lernbereich (BY) |
| LP_0030309 | Kompetenzbereich (BY) |
| LP_0030310 | Prozessbezogene Kompetenz (BY) |
| LP_0030311 | Gegenstandsbereich (BY) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse |
|---|---|
| LP_0000434 | Element (BY) |
| LP_0030180 | Verweis auf DaZ (BY) |
| LP_0030181 | Verweis auf übergreifende Ziele (BY) |
| LP_0030182 | Verweis auf Querverweise (BY) |
| LP_0030183 | Verweis auf Servicematerialien (BY) |
| LP_0030299 | Verweis auf Aufgabe (BY) |
| LP_0030300 | Verweis auf Material (BY) |
| LP_0030301 | Verweis auf mebis (BY) |
| LP_0030302 | Verweis auf Erläuterung (BY) |
| LP_0030331 | Übergreifendes Bildungs- und Erziehungsziel (BY) |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse |
|---|---|
| LP_0000169 | Allgemeine Hochschulreife (BY) |
| LP_0000183 | Erster Abschluss (BY) |
| LP_0000207 | Mittlerer Abschluss (BY) |
| LP_0000435 | Fachniveau Sek II (BY) |
| LP_0002048 | Kompetenzerwartung und Inhalt (BY) |
| LP_0002049 | Kompetenzerwartung (BY) |
| LP_0002050 | Inhalt zu den Kompetenzen (BY) |
| LP_0030053 | Bildungsgangniveau (BY) |
| LP_0030303 | Erläuterung (BY) |

## Individuen des Landes (17)

| ID | Bezeichnung |
|---|---|
| LP_0000023 | Gymnasialniveau Sek I (BY) |
| LP_0000025 | Mittelschulniveau (BY) |
| LP_0000027 | Mittlere-Reife-Klasse (BY) |
| LP_0000030 | Realschulniveau (BY) |
| LP_0000031 | Regelklasse (BY) |
| LP_0000152 | Qualifizierender Abschluss der Mittelschule (BY) |
| LP_0000153 | Erfolgreicher Abschluss der Mittelschule (BY) |
| LP_0000154 | Mittlerer Schulabschluss der Mittelschule (BY) |
| LP_0000155 | Mittlerer Schulabschluss der Realschule (BY) |
| LP_0000156 | Mittlerer Schulabschluss der Wirtschaftsschule (BY) |
| LP_0000157 | Allgemeinbildender Schulabschluss (BY) |
| LP_0000192 | Mittlerer Schulabschluss Gymnasium (BY) |
| LP_0000512 | Grundlegendes Anforderungsniveau (BY) |
| LP_0000513 | Vertiefungskurs (BY) |
| LP_0000525 | Erhöhtes Anforderungsniveau (BY) |
| LP_0030346 | Gymnasialniveau Sek II (BY) |
| LP_0030363 | Grundschulniveau (BY) |
