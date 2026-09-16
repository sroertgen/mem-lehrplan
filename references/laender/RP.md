# Rheinland-Pfalz (RP)

Bundesland-Individuum: `lp:LP_3000046` — `von Bundesland` (LP_0000029) zeigt darauf.

Schulfach-IDs: Präfix `RP_` in `references/terms/sf-terms.tsv` (64 Einträge; Wurzel `RP_0000000`).
Schulart-IDs: Präfix `RP_` in `references/terms/sa-terms.tsv` (5 Einträge; Wurzel `RP_0000000`).

Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen (`RP_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.

## Klassen des Landes (42)

### unter Lehrplan (Wurzel) (LP_0000438)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000433 | Lehrplan (RP) |  |

### unter CE-Fragment (LP_0001015)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000353 | Lehrplanfragment (RP) |  |

### unter CE-Bereich (LP_0000349)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000328 | Thema (RP) | kommt in Mathematik Sek II vor. s. außerdem Moderne Fremdsprache - Englisch Sek I. |
| LP_0000345 | Teilthema (RP) | wird nicht so im LP benannt. Löschen? |
| LP_0000352 | Unterteilthema (RP) | wird nicht so im LP benannt. Löschen? |
| LP_0000431 | Kompetenzbereich (RP) |  |
| LP_0002196 | Leitidee (RP) | nur in Mathematik (s. Bistas) |
| LP_0002202 | Kernbereich (RP) | kommt in Deutsch Sek I vor |
| LP_0030027 | Erfahrungbereich (RP) | kommt vor in Grundschule Sachunterricht |
| LP_0030030 | Themenfeld (RP) | kommt in Physik Sek I vor |
| LP_0030034 | Thematischer Leitgedanke (RP) | kommt in Fremdsprache (Englisch) Primar vor |
| LP_0030035 | Lernbereich (RP) | kommt in Englisch Sek II vor |
| LP_0030098 | Lehrplanbaustein (RP) | kommt in Physik Sek II vor |
| LP_0030101 | Teilkompetenzbereich (RP) | wird nicht so im LP benannt. Löschen? |
| LP_0030102 | Teilteilkompetenzbereich (RP) | wird nicht so im LP benannt. Löschen? |
| LP_0030104 | Teilleitgedanke (RP) | wird nicht so im LP benannt. Löschen? Kommt in Fremdsprache (Englisch) Primar vor. |
| LP_0030105 | Teillernbereich (RP) | wird nicht so im LP benannt. Löschen? Kommt in Englisch Sek II vor. |
| LP_0030106 | Teilteillernbereich (RP) | wird nicht so im LP benannt. Löschen? Kommt in Englisch Sek II vor. |
| LP_0030107 | Teilerfahrungsberich (RP) | wird nicht so im LP benannt. Löschen? Kommt in Sachunterricht Primar vor. |

### unter Curriculares Element (direkt) (LP_0000261)

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000342 | Element (RP) |  |

### Oberklasse ist ein anonymer OWL-Ausdruck

Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Der Explorer leitet seit Version 0.4.0 aus dem benannten Glied der anonymen `owl:intersectionOf` eine `subClassOf`-Kante ab (A ⊑ (B ⊓ R) ⇒ A ⊑ B) — SHACL-Shapes der benannten Gliedklasse (z. B. „Element (SH)“) greifen deshalb trotzdem. Unsichtbar bleibt nur eine Klasse, deren Oberklassen-Ausdruck gar kein benanntes Glied enthält; `scripts/klasse.sh <ID>` zeigt, welcher Fall vorliegt.

| ID | Klasse | Hinweis (editorialNote) |
|---|---|---|
| LP_0000164 | Allgemeine Hochschulreife (RP) |  |
| LP_0000180 | Erster Abschluss (RP) |  |
| LP_0000204 | Mittlerer Abschluss (RP) |  |
| LP_0000350 | Lernziel (RP) | kommt in Gemeinschaftskunde Sek II vor |
| LP_0000432 | Kompetenz (RP) |  |
| LP_0001018 | Fachniveau Sek II (RP) |  |
| LP_0002195 | Inhalt zum Erwerb der Kompetenzen (RP) | kommt in Mathematik Primar vor |
| LP_0002197 | Inhalt (RP) | kommt in Mathematik Sek I vor (=Lernbeschreibungsfunktion) kommt in Physik Sek II vor (=Lernbeschreibungsfunktion) kommt in Englisch Grundschule vor (=Kompetenzspezifikationsfunktion) s. außerdem Englisch Sek I (=Lernbeschreibungsfunktion?) |
| LP_0002198 | Hinweis und Vernetzung (RP) | kommt in Mathematik Sek I vor |
| LP_0002200 | Ziel / Inhalt (Sach- und Methodenkompetenz) (RP) | kommt in Mathematik Sek II vor |
| LP_0002201 | Hinweis zur Unterrichtsgestaltung und Methodenkompetenz (RP) | kommt in Mathematik Sek II vor |
| LP_0030036 | Fähigkeit (RP) | kommt vor in Englisch Sek II |
| LP_0030099 | Hinweis zur unterrichtlichen Umsetzung (RP) | kommt in Physik Sek II vor |
| LP_0030100 | Inhalt und Zusammenhang (RP) | Kommt in Naturwissenschaften Orientierungsstufe vor |
| LP_0030103 | Anwendungsfähiges Wissen (RP) | kommt in Fremdsprache (Englisch) Primar vor |
| LP_0030108 | Fachbegriff (RP) | kommt in Physik Sek I vor |
| LP_0030109 | Entwicklung des Konzepts (RP) | Was machen wir mit den Basiskonzepten in den Naturwissenschaften? Gleichsetzen mit Kompetenzbereich, Themenfeld oder Lerninhalt? Kommen aus den Bistas. |
| LP_0030110 | Kontext (RP) | Kommt vor in Naturwissenschaften Orientierungsstufe. |
| LP_0030111 | Beitrag zur Entwicklung der Basiskonzepte (RP) | Was machen wir mit den Basiskonzepten in den Naturwissenschaften? Gleichsetzen mit Kompetenzbereich, Themenfeld oder Lerninhalt? Kommen aus den Bistas. |
| LP_0030112 | Erschließung des Themenfeldes durch Kontextorientierung (RP) | Kommt vor in Physik Sek I. |
| LP_0030113 | Differenzierungsmöglichkeit (RP) | Kommt vor in Physik Sek I. |

### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)

| ID | Klasse | Oberklasse |
|---|---|---|
| LP_0001019 | Bildungsgangniveau (RP) | LP_0000028 „Bildungsgangniveau“ |

## Individuen des Landes (10)

| ID | Bezeichnung |
|---|---|
| LP_0000143 | Erhöhtes Kompetenzniveau (RP) |
| LP_0000147 | Grundlegendes Kompetenzniveau (RP) |
| LP_0000151 | Mittleres Kompetenzniveau (RP) |
| LP_0000280 | Allgemeinbildender Schulabschluss (RP) |
| LP_0000281 | Qualifizierter Sekundarabschluss I (RP) |
| LP_0000282 | Berufsreife (RP) |
| LP_0001020 | Grundkurs (RP) |
| LP_0001021 | Leistungskurs (RP) |
| LP_0030353 | Niveau Sekundarstufe II (RP) |
| LP_0030371 | Grundschulniveau (RP) |
