# Saarland (SL)

Bundesland-Individuum: `lp:LP_3000055` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `SL_` in `references/terms/sf-terms.tsv` (65 Einträge; Wurzel `SL_0000000`).
Schulart-IDs: Präfix `SL_` in `references/terms/sa-terms.tsv` (6 Einträge; Wurzel `SL_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`SL_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (74)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000825 | Lehrplan (SL) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002229 | Lehrplanfragment (SL) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002230 | Leitidee (SL) | Mathematik |
| LP_0002234 | Themenfeld (SL) | u.a Mathematik Sek I, Physik |
| LP_0002241 | Lernbereich (SL) | Mathematik Sek II |
| LP_0002243 | Kompetenzbereich (SL) |  |
| LP_0030092 | Themenbereich (SL) | Französisch Primar |
| LP_0030126 | Verfügung über sprachliche Mittel (SL) | Englisch Sek I Gemeinschaftsschule |
| LP_0030139 | Themenkomplex (SL) | Sachunterricht Primar |
| LP_0030142 | Basiskonzept (SL) | Naturwissenschaften und Physik -> kommt aus den Bistas |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002102 | Element (SL) |  |
| LP_0030015 | Verweis auf Basiskonzept (SL) | Nawis |
| LP_0030016 | Verweis auf thematische Querverbindungen im Lehrplan (SL) | Mathe |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln greifen trotzdem.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000173 | Allgemeine Hochschulreife (SL) |  |
| LP_0000187 | Erster Abschluss (SL) |  |
| LP_0000211 | Mittlerer Abschluss (SL) |  |
| LP_0001025 | Fachniveau Sek II (SL) |  |
| LP_0002232 | Kompetenzerwartung (SL) | Kompetenz (SL) |
| LP_0002233 | Hinweis zur Umsetzung (SL) |  |
| LP_0002235 | Verbindliches Fachwissen (SL) |  |
| LP_0002238 | Verbindlicher Kompetenzschwerpunkt (SL) | Mathematik Gemeinschaftsschule, Oberstufe |
| LP_0002239 | Vorschlag und Hinweis (SL) | Kommt vor im Fach Mathematik in der Gemeinschaftsschule und im Gymnasium in der Sek I und Sek II. Und im Fach Deutsch in der Primarstufe, in der Sek I in der Gemeinschaftsschule und in der Sek II in der gymasialen Oberstufe. Ist oft nochmal untergliedert. In Deutsch untergliedert in z.B.: "Zur Unterrichtsgestaltung", ""Zu Methoden und Arbeitstechniken", "Zur Aufgabenstellung", "Zu Leistungsfestste |
| LP_0002240 | Basisbegriff (SL) | kommt vor im Fach Mathematik im Gymnasium Sek I und Naturwissenschaften/ Physik Gemeinschaftsschule |
| LP_0030058 | Aufgabenstellung (SL) | kommt vor im Fach Deutsch Gemeinschaftsschule und Gymnasiale Oberstufe |
| LP_0030060 | Literaturhinweis (SL) | Deutsch Sek II |
| LP_0030061 | Verbindliche Form mündlicher Kommunikation (SL) | Deutsch Gemeinschaftschule |
| LP_0030062 | Verbindliche fachspezifische Fertigkeit/Fähigkeit und fachspezifische Methode (SL) | Deutsch Sek I & II |
| LP_0030063 | Verbindlicher Lerngegenstand (SL) | Deutsch Gymnasium Sek I und Sek II |
| LP_0030064 | Vorschlag und Hinweis zu Inhalten und Methoden (SL) | Deutsch Sek II |
| LP_0030093 | Sprachanlass (SL) | Französisch Primar |
| LP_0030094 | Redemittel (SL) | Französisch Primar |
| LP_0030121 | Verbindliche Form des Schreibens (SL) | Deutsch Gemeinschaftsschule |
| LP_0030125 | Inhaltsbezogene Kompetenz (SL) | mathematik |
| LP_0030127 | Inhalt und Thema (SL) | Englisch Sek I Gymnasium "verbindlicher Inhalt" in Sachunterricht Primar, Deutsch Gymnasiale Oberstufe Hauptphase Verbindlicher Inhalt (SL) |
| LP_0030128 | Beispiel (SL) | Englisch Sek I und II Gymnasium |
| LP_0030129 | Methodenkompetenz/Lern- und Kommunikationsstrategie (SL) | Englisch Sek I Gymnasium |
| LP_0030130 | Orientierungswissen (SL) | Englisch Sek I und II Gymnasium |
| LP_0030131 | Begegnungssituaton (SL) | Englisch Sek I und II Gymnasium |
| LP_0030132 | Einstellung (SL) | Englisch Sek I und II Gymnasium |
| LP_0030133 | Relevantes Genre (SL) | Englisch Sek I Gymnasium |
| LP_0030134 | Wortschatz (SL) | Englisch |
| LP_0030135 | Geeignete Methode / Anlass für das exemplarische Arbeiten (SL) | Englisch Sek I und II Gymnasium |
| LP_0030136 | Hinweis für die Konzeption von Lernaufgaben mit IK-Schwerpunkt  (SL) | Englisch Sek I und II Gymnasium |
| LP_0030137 | Mögliche Sprecharrangements und Genres (SL) | Nur in Englisch Sek II Gymnaisum |
| LP_0030138 | Literatur und Film im Unterricht der Hauptphase (SL) | Englisch Sek II |
| LP_0030140 | Verbindliche Textsorte (SL) | Deutsch Gemeinschaftsschule |
| LP_0030141 | Vorgabe zum Erwerb von Methodenkompetenz (SL) | Sachunterricht Primar |
| LP_0030143 | Standard für den Kompetenzbereich Fachwissen (SL) | Naturwissenschaften und Physik Gemeinschaftsschule |
| LP_0030145 | Verwendung von Lehrwerken (SL) | Naturwissenschaft und Physik Gemeinschaftschule |
| LP_0030146 | Möglicher Einstieg / Motivation / Kontext (SL) | Naturwissenschaft/Physik Gemeinschaftsschule und Gymnasium Sek I und II |
| LP_0030147 | Zusammenarbeit mit anderen Fächern (SL) | Naturwissenschaften und Physik Gemeinschaftsschule |
| LP_0030148 | Außerschulischer Lernort und außerunterrichtliche Veranstaltung (SL) | Naturwissenschaften und Physik Gemeinschaftsschule und Gymnasium Sek I und II |
| LP_0030149 | Berufsorientierender Aspekt (SL) | Naturwissenschaften/Physik Gemeinschaftsschule und Gymnasium Sek II |
| LP_0030150 | Unterstützungsangebot (SL) | Naturwissenschaften und Physik Gemeinschaftsschule |
| LP_0030151 | Prozessbezogene Kompetenz (SL) | Physik Gymnasium Sek I |
| LP_0030152 | Hinweis zum sprachsensiblen Fachunterricht (SL) | Physik und Mathe Gymnasium Sek I |
| LP_0030154 | Fachübergreifender und fächerverbindender Bezug (SL) | Physik Gymnasium Sek I und II. Und Mathematik |
| LP_0030155 | Geeignetes (Schüler-)Experiment (SL) | Physik Gymnasium Sek I und II |
| LP_0030156 | Projekt (SL) |  |
| LP_0030157 | Sach-, Erkenntnisgewinnungs-, Kommunikations- und Bewertungskompetenz (SL) | Physik Gymnasium Sek II |
| LP_0030158 | Bildung für nachhaltige Entwicklung (SL) | Physik Gymnasium Sek II |
| LP_0030159 | Medienbildung (SL) | Physik Gymnasium Sek II |
| LP_0030160 | Hinweis zur Unterrichtsgestaltung (SL) | Deutsch |
| LP_0030161 | Hinweis zu Methoden und Arbeitstechniken (SL) | Deutsch |
| LP_0030162 | Methodik und Fachdidaktik (SL) | Mathematik Methodik und Fachdidaktik - Gymnasium Sek I Methodischer Hinweis - Gemeinschaftsschule Methodische und fachdidaktische Erläuterungen - Oberstufe |
| LP_0030163 | Einsatz digitaler Mathematikwerkzeuge (SL) | Mathematik |
| LP_0030164 | Anregung zur selbstständigen Schülerarbeit (SL) | Mathe Oberstufe |
| LP_0030237 | Fakultativer Inhalt (SL) | Mathe Gymnasium Sek I und Sek II |
| LP_0030240 | Grammatik (SL) | Englisch |
| LP_0030241 | Aussprache und Prosodie (SL) | Englisch |
| LP_0030244 | Verstehen und Handeln (SL) | Englisch |
| LP_0030261 | Dialogisches Sprechen – mündliche Interaktion (SL) | Englisch |
| LP_0030262 | Zusammenhängendes monologisches Sprechen – mündliche Produktion (SL) | Englisch |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0001028 | Bildungsgangniveau (SL) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (12)

| ID | Bezeichnung |
|---|---|
| LP_0000260 | A Kurs (SL) |
| LP_0000264 | E Kurs (SL) |
| LP_0000266 | G Kurs (SL) |
| LP_0000267 | Gemeinschaftsschulniveau (SL) |
| LP_0000269 | Gymnasialniveau Sek I (SL) |
| LP_0000300 | Allgemeinbildender Schulabschluss (SL) |
| LP_0000301 | Hauptschulabschluss (SL) |
| LP_0000302 | Mittlerer Bildungsabschluss (SL) |
| LP_0001026 | Grundkurs (SL) |
| LP_0001027 | Leistungskurs (SL) |
| LP_0030355 | Oberstufenniveau (SL) |
| LP_0030373 | Grundschulniveau (SL) |
