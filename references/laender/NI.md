# Niedersachsen (NI)

Bundesland-Individuum: `lp:LP_3000043` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `NI_` in `references/terms/sf-terms.tsv` (51 Einträge; Wurzel `NI_0000000`).
Schulart-IDs: Präfix `NI_` in `references/terms/sa-terms.tsv` (8 Einträge; Wurzel `NI_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`NI_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (49)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse |
|---|---|
| LP_0000823 | Kerncurriculum (NI) |

### unter CE-Fragment (LP_0001015)

| ID | Klasse |
|---|---|
| LP_0001006 | Lehrplanfragment (NI) |

### unter CE-Bereich (LP_0000349)

| ID | Klasse |
|---|---|
| LP_0002203 | Kompetenzbereich (NI) |
| LP_0002205 | Kernkompetenz (NI) |
| LP_0002208 | Lernbereich (NI) |
| LP_0002209 | Thema (NI) |
| LP_0030201 | Kommunikative Teilkompetenz (NI) |
| LP_0030202 | Sprachliches Mittel (NI) |
| LP_0030203 | Leitidee (NI) |
| LP_0030207 | Themenfeld (NI) |
| LP_0030208 | Teilaspekt (NI) |
| LP_0030209 | Fachliche Perspektive (NI) |
| LP_0030211 | Themenbereich (NI) |
| LP_0030217 | Inhaltsbereich (NI) |
| LP_0030221 | Rahmenthema (NI) |
| LP_0030222 | Pflichtmodul (NI) |
| LP_0030223 | Wahlpflichtmodul (NI) |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse |
|---|---|
| LP_0002101 | Element (NI) |
| LP_0030212 | Verweis auf Vernetzungsmöglichkeiten (NI) |
| LP_0030233 | Verweis auf Inhaltsbezogene Kompetenzbereiche (NI) |
| LP_0030234 | Verweis auf Prozessbezogene Kompetenzbereiche (NI) |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse |
|---|---|
| LP_0000161 | Allgemeine Hochschulreife (NI) |
| LP_0000177 | Erster Abschluss (NI) |
| LP_0000201 | Mittlerer Abschluss (NI) |
| LP_0001003 | Erwartete Kompetenz (NI) |
| LP_0001007 | Kerninhalt (NI) |
| LP_0001009 | Ergänzender Hinweis (NI) |
| LP_0002206 | Beispiel (NI) |
| LP_0002207 | Umsetzung im Unterricht (NI) |
| LP_0030014 | Ergänzung zur Kompetenz (NI) |
| LP_0030055 | Fachniveau Sek II (NI) |
| LP_0030204 | Methodenkompetenz (NI) |
| LP_0030205 | Lernstrategie und Arbeitstechnik (NI) |
| LP_0030213 | Prozessbezogene Kompetenz (NI) |
| LP_0030215 | Inhaltsbezogene Kompetenz (NI) |
| LP_0030216 | Verweis auf Fachbezug (NI) |
| LP_0030218 | Verbindlicher Unterrichtsinhalt (NI) |
| LP_0030219 | Autor und Textgruppe (NI) |
| LP_0030220 | Empfohlene Schreibform und Übung (NI) |
| LP_0030224 | Verbindlicher Unterrichtsaspekt (NI) |
| LP_0030225 | Möglicher Unterrichtsaspekt (NI) |
| LP_0030226 | Sprachbildung (NI) |
| LP_0030227 | Weiterführende Anforderung (NI) |
| LP_0030228 | Hinweis zum Einsatz digitaler Medien und Werkzeuge (NI) |
| LP_0030229 | Unterrichtsidee zur Handlungsorientierung online (NI) |
| LP_0030230 | Fakultative Erweiterung (NI) |
| LP_0030231 | Hinweis zum Einsatz digitaler Mathematikwerkzeuge (NI) |
| LP_0030232 | Online-Material (NI) |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0030080 | Bildungsgangniveau (NI) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (18)

| ID | Bezeichnung |
|---|---|
| LP_0000103 | Erhöhte Anforderungen (E-Kurs) (NI) |
| LP_0000104 | Grundlegende Anforderungen (G-Kurs) (NI) |
| LP_0000107 | Gymnasialniveau Sek I (NI) |
| LP_0000108 | Hauptschulniveau (NI) |
| LP_0000110 | Oberschulniveau (NI) |
| LP_0000116 | Realschulniveau (NI) |
| LP_0000117 | Vertiefendes Niveau (NI) |
| LP_0000118 | Zusätzliche Anforderungen (Z-Kurs) (NI) |
| LP_0000129 | Zusätzliche Voraussetzungen für den Erwerb des Mittleres Schulabschlusses (NI) |
| LP_0001116 | Grundlegendes Anforderungsniveau (NI) |
| LP_0001117 | Erhöhtes Anforderungsniveau (NI) |
| LP_0002020 | Allgemeinbildender Schulabschluss (NI) |
| LP_0002021 | Hauptschulabschluss (NI) |
| LP_0002022 | Realschulabschluss (NI) |
| LP_0002023 | Erweiterter Sekundarabschluss I (NI) |
| LP_0002109 | Hauptschulabschluss 10 (NI) |
| LP_0030352 | Oberstufenniveau (NI) |
| LP_0030369 | Grundschulniveau (NI) |
