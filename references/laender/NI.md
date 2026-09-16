# Niedersachsen (NI)

Bundesland-Individuum: `lp:LP_3000043` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `NI_` in `references/terms/sf-terms.tsv` (51 Einträge; Wurzel `NI_0000000`).
Schulart-IDs: Präfix `NI_` in `references/terms/sa-terms.tsv` (8 Einträge; Wurzel `NI_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`NI_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (49)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000823 | Kerncurriculum (NI) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0001006 | Lehrplanfragment (NI) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002203 | Kompetenzbereich (NI) | Prozessbezogener Kompetenzbereich (NI) |
| LP_0002205 | Kernkompetenz (NI) | Mathe |
| LP_0002208 | Lernbereich (NI) | Mathe Sek I & II |
| LP_0002209 | Thema (NI) | Kommt bisher nur in Sek I Integrierte Gesamtschule in Mathe vor. |
| LP_0030201 | Kommunikative Teilkompetenz (NI) | Englisch |
| LP_0030202 | Sprachliches Mittel (NI) | Englisch |
| LP_0030203 | Leitidee (NI) | Mathematik |
| LP_0030207 | Themenfeld (NI) | Englisch Sek II |
| LP_0030208 | Teilaspekt (NI) | Englisch Sek II |
| LP_0030209 | Fachliche Perspektive (NI) | Sachunterricht Primar |
| LP_0030211 | Themenbereich (NI) | Sachunterricht Primar Naturwissenschaften Sek I |
| LP_0030217 | Inhaltsbereich (NI) | Physik Sek II |
| LP_0030221 | Rahmenthema (NI) | Deutsch Sek II |
| LP_0030222 | Pflichtmodul (NI) | Deutsch Sek II |
| LP_0030223 | Wahlpflichtmodul (NI) | Deutsch Sek II |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002101 | Element (NI) |  |
| LP_0030212 | Verweis auf Vernetzungsmöglichkeiten (NI) | = Verweis auf Perspektive Aus dem Lehrplan: “Der Sachunterricht ist vielperspektivisch angelegt. Für die Planung des Unterrichts ist es daher grundlegend, die fünf Perspektiven mit ihren erwarteten Kompetenzen und die fachübergreifenden Bildungsbereiche zu vernetzen. Beispiele für Vernetzungsmöglichkeiten werden durch Pfeile in den Tabellen aufgezeigt.” |
| LP_0030233 | Verweis auf Inhaltsbezogene Kompetenzbereiche (NI) | Mathematik Oberschule, Hauptschule, Realschule, Gymnasium, Oberstufe |
| LP_0030234 | Verweis auf Prozessbezogene Kompetenzbereiche (NI) | Mathematik Oberschule, Hauptschule, Realschule |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Der Explorer leitet seit Version 0.4.0 aus dem benannten Glied der anonymen `owl:intersectionOf` eine `subClassOf`-Kante ab (A ⊑ (B ⊓ R) ⇒ A ⊑ B) — SHACL-Shapes der benannten Gliedklasse (z. B. „Element (SH)“) greifen deshalb trotzdem. Unsichtbar bleibt nur eine Klasse, deren Oberklassen-Ausdruck gar kein benanntes Glied enthält; `scripts/klasse.sh <ID>` zeigt, welcher Fall vorliegt.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000161 | Allgemeine Hochschulreife (NI) |  |
| LP_0000177 | Erster Abschluss (NI) |  |
| LP_0000201 | Mittlerer Abschluss (NI) |  |
| LP_0001003 | Erwartete Kompetenz (NI) |  |
| LP_0001007 | Kerninhalt (NI) | Mathe |
| LP_0001009 | Ergänzender Hinweis (NI) | Deutsch Primar |
| LP_0002206 | Beispiel (NI) | Englisch Primar |
| LP_0002207 | Umsetzung im Unterricht (NI) | Mathe Primar |
| LP_0030014 | Ergänzung zur Kompetenz (NI) | (Deutsch Oberschule, Bezeichnung kommt so nicht im Lehrplan vor |
| LP_0030055 | Fachniveau Sek II (NI) |  |
| LP_0030204 | Methodenkompetenz (NI) | Englisch |
| LP_0030205 | Lernstrategie und Arbeitstechnik (NI) | Englisch "Lernstrategie und Arbeitstechnik" - Gesamtschule und Gymnasium. "Kompetenzspezifische Strategie und Arbeitstechnik" - Oberstufe. Kompetenzspezifische Strategie und Arbeitstechnik (NI) |
| LP_0030213 | Prozessbezogene Kompetenz (NI) | Naturwissenschaften |
| LP_0030215 | Inhaltsbezogene Kompetenz (NI) | mathe, Naturwissenschaften. In Deutsch "domänenspezifische Kompetenz" |
| LP_0030216 | Verweis auf Fachbezug (NI) | Naturwissenschaften Sek I |
| LP_0030218 | Verbindlicher Unterrichtsinhalt (NI) | Deustch Sek II |
| LP_0030219 | Autor und Textgruppe (NI) | Deutsch Sek II |
| LP_0030220 | Empfohlene Schreibform und Übung (NI) | Deutsch Sek II |
| LP_0030224 | Verbindlicher Unterrichtsaspekt (NI) | Deutsch Sek II |
| LP_0030225 | Möglicher Unterrichtsaspekt (NI) | Deutsch Sek II |
| LP_0030226 | Sprachbildung (NI) |  |
| LP_0030227 | Weiterführende Anforderung (NI) | Mathematik Oberschule, Hauptschule, Realschule |
| LP_0030228 | Hinweis zum Einsatz digitaler Medien und Werkzeuge (NI) | Mathematik Oberschule, Hauptschule, Realschule |
| LP_0030229 | Unterrichtsidee zur Handlungsorientierung online (NI) | Mathematik Integrierte Gesamtschule |
| LP_0030230 | Fakultative Erweiterung (NI) | Mathematik Gymnasium, Oberstufe |
| LP_0030231 | Hinweis zum Einsatz digitaler Mathematikwerkzeuge (NI) | Mathematik Gymnasium, Oberstufe |
| LP_0030232 | Online-Material (NI) | Mathematik Oberstufe |

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
