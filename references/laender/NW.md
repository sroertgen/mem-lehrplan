# Nordrhein-Westfalen (NW)

Bundesland-Individuum: `lp:LP_3000044` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `NW_` in `references/terms/sf-terms.tsv` (69 Einträge; Wurzel `NW_0000000`).
Schulart-IDs: Präfix `NW_` in `references/terms/sa-terms.tsv` (7 Einträge; Wurzel `NW_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`NW_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (21)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0001000 | Kernlehrplan (NW) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002186 | Lehrplanfragment (NW) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002187 | Kompetenzbereich (NW) | Aus dem Kernlehrplan: “Kompetenzbereiche repräsentieren die Grunddimensionen des fachlichen Handelns. Sie dienen dazu, die einzelnen Teiloperationen entlang der fachlichen Kerne zu strukturieren und den Zugriff für die am Lehr-Lernprozess Beteiligten zu verdeutlichen.” |
| LP_0002190 | Teilkompetenzbereich (NW) | Fach Moderne Fremdsprachen - Englisch und Französisch |
| LP_0002191 | Inhaltsfeld (NW) | Aus dem Kernlehrplan: “Inhaltsfelder systematisieren mit ihren jeweiligen inhaltlichen Schwerpunkten die im Unterricht der Realschule verbindlichen und unverzichtbaren Gegenstände und liefern Hinweise für die inhaltliche Ausrichtung des Lehrens und Lernens.” |
| LP_0030073 | Bereich (NW) | Fach Englisch, Primar |
| LP_0030077 | Basiskonzept (NW) | Fach Naturwissenschaften (Biologie, Chemie, Physik) -> noch offen, wie wir es definieren! |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0002085 | Element (NW) |  |
| LP_0030009 | Verweis auf Basiskonzept (NW) |  |
| LP_0030187 | Verweis auf Kompetenzerwartung (NW) | in Mathematik und den Naturwissenschaften. Diese treten in Form von Kürzeln in Klammern am Ende einer Kompetenzerwartung auf und verweisen auf (Prozessbezogene/Übergeordnete) Kompetenzerwartungen. |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Der Explorer leitet seit Version 0.4.0 aus dem benannten Glied der anonymen `owl:intersectionOf` eine `subClassOf`-Kante ab (A ⊑ (B ⊓ R) ⇒ A ⊑ B) — SHACL-Shapes der benannten Gliedklasse (z. B. „Element (SH)“) greifen deshalb trotzdem. Unsichtbar bleibt nur eine Klasse, deren Oberklassen-Ausdruck gar kein benanntes Glied enthält; `scripts/klasse.sh <ID>` zeigt, welcher Fall vorliegt.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000162 | Allgemeine Hochschulreife (NW) |  |
| LP_0000178 | Erster Abschluss (NW) |  |
| LP_0000202 | Mittlerer Abschluss (NW) |  |
| LP_0002086 | Fachniveau Sek II (NW) |  |
| LP_0002188 | Kompetenzerwartung (NW) | Aus dem Kernlehrplan: “Kompetenzerwartungen führen Prozesse und Gegenstände zusammen und beschreiben die fachlichen Anforderungen und intendierten Lernergebnisse..“ |
| LP_0002192 | Inhaltlicher Schwerpunkt (NW) |  |
| LP_0030005 | Ergänzung zu einem Basiskonzept (NW) | Der Begriff kommt so nicht im Lehrplan vor. Kommt nur in den Naturwissenschaften vor. Ist eine Ergänzung zu den Bezügen zu den Basiskonzepten und ergänzt gleichzeitig die davor genannten inhaltlichen Schwerpunkte. |
| LP_0030006 | Möglicher Kontext (NW) |  |
| LP_0030074 | Fachliche Konkretisierung (NW) | Fach Englisch |
| LP_0030075 | Inhalt (NW) | Fach Sachunterricht Primar. Inhalte stehen in Klammern hinter den Kompetenzerwartungen. |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0030041 | Bildungsgangniveau (NW) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (15)

| ID | Bezeichnung |
|---|---|
| LP_0000130 | Erweiterungskurs (NW) |
| LP_0000131 | Gesamt-/Sekundarschulniveau (NW) |
| LP_0000132 | Gymnasialniveau Sek I (NW) |
| LP_0000134 | Hauptschulniveau (NW) |
| LP_0000138 | Niveau Mittlerer Schulabschluss (NW) |
| LP_0000142 | Realschulniveau (NW) |
| LP_0000373 | Allgemeinbildender Schulabschluss (NW) |
| LP_0000374 | Erster Schulabschluss (NW) |
| LP_0000375 | Erweiterter Erster Schulabschluss (NW) |
| LP_0000376 | Mittlerer Schulabschluss (NW) |
| LP_0000377 | Mittlerer Schulabschluss mit Berechtigung zur gymnasialen Oberstufe (NW) |
| LP_0000521 | Grundkurs (NW) |
| LP_0000522 | Leistungskurs (NW) |
| LP_0030351 | Gymnasialniveau Sek II (NW) |
| LP_0030370 | Grundschulniveau (NW) |
