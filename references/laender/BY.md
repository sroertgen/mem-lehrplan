# Bayern (BY)

Bundesland-Individuum: `lp:LP_3000051` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `BY_` in `references/terms/sf-terms.tsv` (119 Einträge; Wurzel `BY_0000000`).
Schulart-IDs: Präfix `BY_` in `references/terms/sa-terms.tsv` (13 Einträge; Wurzel `BY_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`BY_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (31)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000819 | LehrplanPLUS (BY) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002043 | Fachlehrplan (BY) | enthält Lernbereiche auf verschiedenen Ebenen, Kompetenzerwartungen und Inhalte |
| LP_0002044 | Lehrplanfragment (BY) |  |
| LP_0030304 | Bildungs- und Erziehungsauftrag (BY) | für jede Schulart einheitlich einen Bildungs- und Erziehungsauftrag |
| LP_0030305 | Übergreifende Bildungs- und Erziehungsziele (BY) |  |
| LP_0030306 | Fachprofil (BY) | für jede Schulart und jedes Fach ein Fachprofil |
| LP_0030307 | Grundlegende Kompetenzen (Jahrgangsstufenprofil) (BY) | für jede Schulart, jede JS ein Profil (alle Kompetenzen aufgelistet) |
| LP_0030308 | Bayerische Leitlinie für die Bildung und Erziehung von Kindern bis zum Ender der Grundschulzeit (BY) | nur für Grundschule und Förderschule |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002046 | Lernbereich (BY) |  |
| LP_0030309 | Kompetenzbereich (BY) | Begriff kommt nicht in den Fachlehrplänen vor! (da gibt es nur Lernbereiche) Sondern in den Kompetenzstrukturmodellen der jeweiligen Fächer (z.B. deutsch und Moderne Fremdsprache) (an die Bistas angelehnt) |
| LP_0030310 | Prozessbezogene Kompetenz (BY) | Begriff kommt nicht in den Fachlehrplänen vor! (da gibt es nur Lernbereiche) Sondern in den Kompetenzstrukturmodellen der jeweiligen Fächer (Mathematik udn Nawis) (an die Bistas angelehnt) |
| LP_0030311 | Gegenstandsbereich (BY) | Begriff kommt nicht in den Fachlehrplänen vor! (da gibt es nur Lernbereiche) Sondern in den Kompetenzstrukturmodellen der jeweiligen Fächer (Mathematik udn Nawis) (an die Bistas angelehnt) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000434 | Element (BY) |  |
| LP_0030180 | Verweis auf DaZ (BY) | Verweis zum Lehrplan Deutsch als Zweitsprache -> also auf Lernbereiche eines anderen Lehrplans |
| LP_0030181 | Verweis auf übergreifende Ziele (BY) | Verweis zu den Übergreifenden Zielen ("Schulart- und fächerübergreifende Bildungs- und Erziehungsziele sowie Alltagskompetenz und Lebensökonomie") -> also auf Prosatextteil? |
| LP_0030182 | Verweis auf Querverweise (BY) | Verweis auf die Fachlehrpläne anderer Fächer -> also auf Lernbereiche eines anderen Lehrplans |
| LP_0030183 | Verweis auf Servicematerialien (BY) | Verlinkung zu Dokumenten (Unterrichtsmaterial). Hierzu gibt manchmal noch "Erläuterungen" -> Frage, ob man diese als CE-Hinweis interpreteierne kann. |
| LP_0030299 | Verweis auf Aufgabe (BY) | z.B. PDF-Dokument zum Downloaden (Arbeitsblätter o.ä.) |
| LP_0030300 | Verweis auf Material (BY) | z.B. Verlinkung auf Mundo zu einem spzifischen Material da |
| LP_0030301 | Verweis auf mebis (BY) | Verlinkung zu mebis -> Einloggen über ByCS |
| LP_0030302 | Verweis auf Erläuterung (BY) | Verweist auf Erläuterungen -> Erläuterungen selbst sind CE-Hinweise |
| LP_0030331 | Übergreifendes Bildungs- und Erziehungsziel (BY) |  |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000169 | Allgemeine Hochschulreife (BY) |  |
| LP_0000183 | Erster Abschluss (BY) |  |
| LP_0000207 | Mittlerer Abschluss (BY) |  |
| LP_0000435 | Fachniveau Sek II (BY) | in Bayern genannt Anforderungsniveau |
| LP_0002048 | Kompetenzerwartung und Inhalt (BY) |  |
| LP_0002049 | Kompetenzerwartung (BY) |  |
| LP_0002050 | Inhalt zu den Kompetenzen (BY) |  |
| LP_0030303 | Erläuterung (BY) |  |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0030053 | Bildungsgangniveau (BY) | LP_0000028 „Bildungsgangniveau“ |

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
