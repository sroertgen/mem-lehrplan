# Mecklenburg-Vorpommern (MV)

Bundesland-Individuum: `lp:LP_3000052` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `MV_` in `references/terms/sf-terms.tsv` (46 Einträge; Wurzel `MV_0000000`).
Schulart-IDs: Präfix `MV_` in `references/terms/sa-terms.tsv` (6 Einträge; Wurzel `MV_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`MV_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (23)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002164 | Rahmenplan (MV) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002136 | Lehrplanfragment (MV) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002139 | Kompetenzbereich (MV) |  |
| LP_0002143 | Themenbereich (MV) | Arbeitsbereich in Deustch "Gegenstandsfeld" in Kunst "Lebens- und Lernbereich" in Fremdsprache Primar Aus dem Lehrplan Deutsch Gesamtschule (2024) zu “Arbeitsbereich”: “Im Rahmenplan werden Arbeitsbereiche ausgewiesen, denen inhaltlich verbundene Themen zugeordnet werden. Die Fortführung der Arbeitsbereiche in den aufsteigenden Klassen ermöglicht Anknüpfungspunkte für die Lernenden im Sinne eine |
| LP_0002147 | Thema (MV) | Aus dem Lehrplan Deutsch Gesamtschule (2024) zu “Themen”: “Für den Unterricht werden in Abschnitt 2.3 verbindliche und/oder wahlobligatorische Themen benannt und im Tabellenkopf hervorgehoben. Die Reihenfolge der Themen hat keinen normativen, sondern empfehlenden Charakter.” Kommen u.a. im Fach Mathematik, Biologie und Englisch vor. |
| LP_0030002 | Grundfertigkeit (MV) | Englisch |
| LP_0030054 | Leitidee (MV) | Mathe Primar |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002080 | Element (MV) |  |
| LP_0002149 | Verweis auf Möglichkeiten der Verknüpfung (MV) | verweist auf andere Arbeitsbereiche und Querschnittsthemen |
| LP_0030199 | Verweis auf Kompetenzbereich (MV) |  |
| LP_0030328 | Querschnittsthema (MV) |  |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000170 | Allgemeine Hochschulreife (MV) |  |
| LP_0000184 | Erster Abschluss (MV) |  |
| LP_0000208 | Mittlerer Abschluss (MV) |  |
| LP_0002081 | Fachniveau Sek II (MV) |  |
| LP_0002140 | Kompetenz (MV) | Fachspezifische Kompetenz in Mathe Primar |
| LP_0002144 | Verbindlicher Inhalt (MV) | Aus dem Lehrplan Deutsch Gesamtschule (2024) zu “verbindliche Inhalte”: “Die Konkretisierung der Themen erfolgt in Form der Ausweisung verbindlicher Inhalte in Abschnitt 2.3.” |
| LP_0002145 | Hinweis und Anregung (MV) | Aus dem Lehrplan Deutsch Gesamtschule (2024) “Hinweise und Anregungen”: “Neben Anregungen für die Umsetzung im Unterricht werden sowohl didaktische und methodische Hinweise zur Auseinandersetzung mit den verbindlichen Inhalten gegeben als auch exemplarisch Möglichkeiten für die fachübergreifende und fächerverbindende Arbeit sowie fachinterne Verknüpfungen aufgezeigt.” Sie sind einem verbindlichen  |
| LP_0002151 | Konkretisierung (MV) |  |
| LP_0002153 | Standard (MV) | KMK-Bildungsstandard bisher nur in Fach Deutsch, Schulstufe Sek II gefunden. Ist gleichzusetzen mit Kompetenzen. Aus dem Lehrplan Deutsch Gesamtschule (2024) zu "Kompetenzen": “Im Zentrum des Fachunterrichts steht der Kompetenzerwerb. Die Kompetenzen werden in der Auseinandersetzung mit den verbindlichen Themen entwickelt. In Abschnitt 2.2 werden die zu erreichenden Kompetenzen benannt. “ |
| LP_0002163 | Beispiel Verknüpfung von Inhalt und Kompetenzbereich (MV) | Ist einem Themenbereich (o.ä.) untergeordnet (bzw. einem verbindlichen Inhalt oder einem Hinweis zugeordnet) und zusätzlich einem Kompetenzbereich zugeordnet. |
| LP_0030048 | Verbindliches Ziel (MV) |  |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0001011 | Bildungsgangniveau (MV) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (12)

| ID | Bezeichnung |
|---|---|
| LP_0000032 | Orientierungsstufe (MV) |
| LP_0000099 | Gymnasialniveau Sek I (MV) |
| LP_0000100 | Bildungsgangniveau Berufsreife (MV) |
| LP_0000101 | Bildungsgangniveau Mittlere Reife (MV) |
| LP_0000102 | Orientierungsstufenniveau (MV) |
| LP_0000361 | Allgemeinbildender Schulabschluss (MV) |
| LP_0000362 | Berufsreife (MV) |
| LP_0000363 | Mittlere Reife (MV) |
| LP_0000519 | Grundkurs (MV) |
| LP_0000520 | Leistungskurs (MV) |
| LP_0030350 | Gymnasialniveau Sek II (MV) |
| LP_0030368 | Grundschulniveau (MV) |
