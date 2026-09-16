# GREEN — Läufe mit Skill, Runde 1

Dieselben sechs Läufe wie in `docs/testing/baseline.md` (RED), diesmal mit vorangestelltem
Satz „Lies zuerst `SKILL.md` und arbeite genau danach.“ Geprüft mit mem-explorer 0.4.0
(`node ~/coding/comenius/mem-explorer/bin/mem-explorer.mjs check`), Skill-Stand `ae11dcb`.
Zahlen aus `.superpowers/sdd/2026-09-14-mem-lehrplan-skill/task-6-green-scores.md`
(Controller-Messung) und `task-6-green-agent-returns.md` (Selbstauskunft der Agenten, daraus
auch die Spalte „benutzte Skripte“); Rohausgaben liegen unter `docs/testing/green/`.

## Szenario 1 — Transformieren

### Lauf 1 (`szenario-1-lauf-1.ttl`)

- Exit: 0
- Kopfzeile: 15 Befunde · 0 mehrfach bestätigt · 0 Fehler, 0 Warnungen, 15 Hinweise (15 Reasoner-Artefakte)
- Befundgruppen (ohne Reasoner-Artefakte): keine
- Erfundene IDs: 0 von 24 verwendeten Ontologie-IDs
- Blank Nodes: nein (0 `[`)
- Jahrgangsstufe als Literal: nein
- Textträger am Titelknoten: `hat Wert` vorhanden (8 Zeilen); `rdfs:label` gesamt 14 Zeilen
- CE-Hinweis (LP_0000852) verwendet: 0
- Datennamensraum: `data: <https://example.org/lehrplan/sh/religion-gymnasium/>` (eigen gewählt)
- benutzte Skripte (Selbstauskunft): `scripts/lookup.sh`, `scripts/klasse.sh LP_0000824`

Begründung (wörtlich):

> Ich bin dem Ablauf aus `SKILL.md` gefolgt: erst `references/muster.md` (Pattern 1
> Lehrplanwurzel, Pattern 2 Titel/Beschreibung/Nummer, Pattern 6 Hierarchie über `hat Teil`)
> und `references/konventionen.md` (eigener `data:`-Namensraum, lesbare Slugs, Text
> wörtlich ohne Sprachtag, Kommentar mit PDF-Seite) gelesen, dann `references/beispiel.ttl`
> als Vorlage kopiert — sie behandelt zufällig denselben Kompetenzbereich „Die Frage nach
> Gott" für SH/Ev. Religion/Gymnasium. Jede ID habe ich trotzdem selbst mit
> `scripts/lookup.sh` nachgeschlagen (u. a. LP_0000824 Fachanforderung SH, LP_0030070
> Kompetenzbereich SH, LP_0030278 Prozessbezogene Kompetenz SH, LP_0030280 Mögliches Thema
> und Inhalt SH, LP_3000054 Schleswig-Holstein, SH_0000008 Evangelische Religion, SH_0000003
> Gymnasium) statt sie aus der Vorlage zu übernehmen. Mit `scripts/klasse.sh LP_0000824` habe
> ich geprüft, dass die Restriktion `hat Teil → allValuesFrom LP_0002103 „Element (SH)“`
> einen direkten Sprung von der Fachanforderungs-Wurzel zum Kompetenzbereich erlaubt […] —
> deshalb habe ich anders als im Beispiel keine erfundene Lehrplanfragment-Ebene eingefügt,
> weil der Auszug keinen übergeordneten Abschnittstitel nennt. Der dritte Themenpunkt aus der
> Aufgabe […] fehlte im Beispiel und wurde als drittes `LP_0030280`-Element mit eigener
> Position ergänzt.

### Lauf 2 (`szenario-1-lauf-2.ttl`)

- Exit: 0
- Kopfzeile: 15 Befunde · 0 mehrfach bestätigt · 0 Fehler, 0 Warnungen, 15 Hinweise (15 Reasoner-Artefakte)
- Befundgruppen (ohne Reasoner-Artefakte): keine
- Erfundene IDs: 0 von 24 verwendeten Ontologie-IDs
- Blank Nodes: nein (0 `[`)
- Jahrgangsstufe als Literal: nein
- Textträger am Titelknoten: `hat Wert` vorhanden (8 Zeilen); `rdfs:label` gesamt 14 Zeilen
- CE-Hinweis (LP_0000852) verwendet: 0
- Datennamensraum: `data: <https://example.org/lehrplan/sh/ev-religion/>` (eigen gewählt)
- benutzte Skripte (Selbstauskunft): `scripts/lookup.sh`, `scripts/klasse.sh`

Begründung (wörtlich):

> Ich bin genau dem Ablauf aus `SKILL.md` gefolgt: `references/muster.md` lieferte die
> Strukturmuster (Pattern 1 Lehrplanwurzel, Pattern 2 Titel/Beschreibung/Nummer als eigene
> Wertknoten, Pattern 6 Hierarchie über `hat Teil`, plus `hat Position`), … und
> `references/laender/SH.md` die Landesklassenliste, aus der ich LP_0000824 …, LP_0030070 …,
> LP_0030278 … und LP_0030280 … auswählte. `references/beispiel.ttl` diente als
> Strukturvorlage, weil es denselben Fall (SH, Ev. Religion, „Die Frage nach Gott") bereits
> einmal durchbuchstabiert — den Inhalt (drei statt zwei Themen-Bullets, abweichender
> Beschreibungstext) habe ich aber wörtlich aus dem gegebenen Auszug übernommen statt es zu
> kopieren. Jede ID habe ich mit `scripts/lookup.sh` … verifiziert und die drei Landesklassen
> zusätzlich mit `scripts/klasse.sh` gegen ihre OWL-Definition in `lp-base.ttl` geprüft, um zu
> bestätigen, dass sie als Teile eines Kompetenzbereichs zulässig sind. Bewusst weggelassen
> habe ich eine Lehrplanfragment-Zwischenebene, weil der Auszug keine übergeordnete
> Abschnittsangabe enthält und ich nichts erfinden wollte, was nicht im Text steht.

## Szenario 2 — Nachbessern

### Lauf 1 (`szenario-2-lauf-1.ttl`)

- Exit: 0
- Kopfzeile: 17 Befunde · 0 mehrfach bestätigt · 0 Fehler, 0 Warnungen, 17 Hinweise (17 Reasoner-Artefakte)
- Befundgruppen (ohne Reasoner-Artefakte): keine
- Erfundene IDs: 0 von 28 verwendeten Ontologie-IDs
- Blank Nodes: nein (0 `[`)
- Jahrgangsstufe als Literal: nein — durch die Individuen ersetzt
- Textträger am Titelknoten: `hat Wert` vorhanden (10 Zeilen); `rdfs:label` gesamt 17 Zeilen
- CE-Hinweis (LP_0000852) im Ergebnis: 1 Vorkommen, aber nur im erklärenden Kommentar —
  der Knoten selbst trägt `a lp:LP_0030003` (Beschreibung), korrekt behoben
- IRI-Diff gegen die Fixture: 0 fehlende Fixture-Subjekte; 2 neue Subjekte
  (`data:fachanforderung-titel`, `data:kb-gott-beschreibung`)
- inverse Kanten/`hat Funktion` ergänzt (Artefakt „repariert“): 0
- benutzte Skripte (Selbstauskunft): `scripts/lookup.sh`; Prüfschleife über
  `node bin/mem-explorer.mjs check`

Begründung (wörtlich, gekürzt):

> **Was ich geändert habe, je Befundgruppe:** […] Gestützt habe ich mich auf
> `references/befunde.md` (Soll-Muster je Regel, inkl. der Beispiele, die wörtlich auf diese
> Datei zugeschnitten sind), das Original `references/beispiel.ttl` als Referenzwert für die
> genauen Titel-/Beschreibungstexte, sowie `scripts/lookup.sh` zur Bestätigung der
> Klassen-/Property-IDs […]. Verifiziert mit `node bin/mem-explorer.mjs check` im Projekt
> `mem-explorer`: Exit 0 […]. Keine IRI wurde umbenannt oder entfernt.

### Lauf 2 (`szenario-2-lauf-2.ttl`)

- Exit: 0
- Kopfzeile: 17 Befunde · 0 mehrfach bestätigt · 0 Fehler, 0 Warnungen, 17 Hinweise (17 Reasoner-Artefakte)
- Befundgruppen (ohne Reasoner-Artefakte): keine
- Erfundene IDs: 0 von 28 verwendeten Ontologie-IDs
- Blank Nodes: nein (0 `[`)
- Jahrgangsstufe als Literal: nein — durch die Individuen ersetzt
- Textträger am Titelknoten: `hat Wert` vorhanden (10 Zeilen); `rdfs:label` gesamt 19 Zeilen
- CE-Hinweis (LP_0000852) im Ergebnis: 4 Vorkommen, alle vier in erklärenden Kommentaren
  (Fehlerbeschreibung, `klasse.sh`-Beleg) — der Knoten selbst trägt `a lp:LP_0030003`
- IRI-Diff gegen die Fixture: 0 fehlende Fixture-Subjekte; 2 neue Subjekte
  (`data:fachanforderung-titel`, `data:kb-gott-beschreibung`)
- inverse Kanten/`hat Funktion` ergänzt (Artefakt „repariert“): 0
- benutzte Skripte (Selbstauskunft): `scripts/klasse.sh LP_0000852` bzw. `LP_0030003`;
  Prüfschleife über `node bin/mem-explorer.mjs check`

Begründung (wörtlich, gekürzt):

> **Was ich je Befundgruppe geändert habe:** […] 4. **Ziel ohne geforderte Klasse +
> Pflichtangabe „ist Teil von"** (`kb-gott-inhalt-1-hinweis`): Den Knoten von `lp:LP_0000852`
> (CE-Hinweis) auf `lp:LP_0030003` (Beschreibung) umgetypt, IRI und Kante unverändert. Mit
> `scripts/klasse.sh LP_0000852` bzw. `LP_0030003` geprüft, dass nur CE-Hinweis eine
> `obo:BFO_0000050`-Restriktion trägt […] — bestätigt durch den Vergleich mit
> `references/beispiel.ttl`, wo der analoge Knoten `kb-gott-beschreibung` denselben Befund
> nicht hat. **Grundlage/Werkzeuge:** `SKILL.md`-Ablauf, `references/befunde.md` […],
> `references/beispiel.ttl` als unbeschädigte Vorlage desselben Ausschnitts für die neuen
> Textwerte […]. Beide Originaldateien wurden nicht verändert.

## Szenario 3 — Nachschlagen

### Lauf 1 (`szenario-3-lauf-1.md`)

- 505 Wörter
- Nennt LP_0030280: 0 Vorkommen — **nennt die falsche Klasse**
- Nennt LP_0030059 „Möglicher Inhalt (SH)“: 12 Vorkommen
- Nennt den „blinden Fleck“ aus `mem-explorer/CLAUDE.md`: 0×
- Quellen laut Datei: `references/arbeitsablauf.md`, `references/laender/`,
  `references/laender/SH.md`, `references/lp-base.ttl`, `references/patterns/pattern…`,
  `scripts/klasse.sh`, `scripts/lookup.sh`
- benutzte Skripte (Selbstauskunft): `scripts/lookup.sh "Möglicher Inhalt"`,
  `scripts/klasse.sh LP_0030059/LP_0002103/LP_0000261/LP_0000332/LP_0000852`

Begründung (wörtlich):

> **Kernaussage:** Für eine „Konkretion“ […] in Schleswig-Holstein ist die Klasse
> `LP_0030059` „Möglicher Inhalt (SH)“ vorgesehen; sie enthält jedoch **keine**
> `owl:Restriction` auf `hat Teil` […] — die Ontologie schreibt also nicht vor, was ein
> solcher Knoten als Teile haben darf oder muss. […] **Herkunft der Angaben:** Die
> Klassenzuordnung stammt aus `scripts/lookup.sh "Möglicher Inhalt"` und aus
> `references/laender/SH.md` bzw. `references/arbeitsablauf.md` (Zuordnung „Konkretionen“ →
> Lerninhalt-Klasse des Landes). […] Ich habe genau nach `SKILL.md` gearbeitet: nur
> `lookup.sh`/`klasse.sh` und die referenzierten Dateien, keine ID aus dem Gedächtnis, keine
> Subagenten.

Lauf 1 folgt dem Ablauf sauber (nur nachgeschlagene IDs, keine erfundene ID, keine lokale
Datendatei) und landet trotzdem bei der falschen von zwei strukturgleichen Klassen: der
deutsche Wortlaut „Möglicher Inhalt“ trifft die Aufgabenformulierung näher als „Mögliches
Thema und Inhalt“, und ohne die editorialNote (die es zu diesem Zeitpunkt noch nicht gab)
ist nichts in den Termtabellen, das LP_0030059 als „Englisch Primar“ und damit als falsch
für einen fachneutralen Prompt ausweist.

### Lauf 2 (`szenario-3-lauf-2.md`)

- 710 Wörter
- Nennt LP_0030280: 26 Vorkommen — die richtige Klasse
- Nennt LP_0030059: 1 Vorkommen
- Nennt den „blinden Fleck“ aus `mem-explorer/CLAUDE.md`: 2×
- Quellen laut Datei: `references/laender/SH.md`, `references/lp-base.ttl`,
  `relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl`,
  `scripts/klasse.sh`, `scripts/lookup.sh`,
  `src/lib/ontology/generated/hierarchy.ttl`, `src/lib/ontology/generated/shapes.ttl`
- benutzte Skripte (Selbstauskunft): `scripts/lookup.sh LP_0030280`,
  `scripts/klasse.sh LP_0030280`/`LP_0002103`/`LP_0000261`, `grep` über `references/lp-base.ttl`

Begründung (wörtlich):

> **Klasse:** … `LP_0030280` … Bestätigt durch echte Nutzdaten: … Die Klassenidentität
> kommt aus den echten SH-Nutzdaten
> `~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl`
> (dort tragen die „Mögliche Konkretionen"-Container und ihre Stichpunkte durchgängig
> `rdf:type lp:LP_0030280`) — **Namenserraten aus `references/laender/SH.md` allein reichte
> nicht, da mehrere Klassen „Inhalt" im Namen tragen.** Label/Typ bestätigt mit
> `scripts/lookup.sh LP_0030280`. […] `LP_0030280` hat **keine benannte Oberklasse** — nur
> eine anonyme `owl:intersectionOf` […]. Das ist einer der in `mem-explorer/CLAUDE.md`
> dokumentierten blinden Flecken: 22 der 37 SH-Klassen […] hängen nur über eine anonyme
> Intersection an ihrer Oberklasse.

Lauf 2 nennt die richtige Klasse, aber — im eigenen Wortlaut — nur, weil eine externe,
ungeprüfte Nutzdatendatei (`relidesk-mem-lehrplan-transformation/…`) als Schiedsrichter
zwischen den beiden gleich aussehenden Kandidaten diente: dieselbe Rationalisierung
(„ein reales, vorhandenes Dokument entscheidet“), die schon in der Baseline zum
Szenario-1-Scheitern führte, jetzt mit richtigem statt falschem Ergebnis. Zusätzlich
zitiert dieser Lauf erneut den in `mem-explorer/CLAUDE.md` dokumentierten „blinden Fleck“ —
denselben, den `references/fallstricke.md` (Regel 8, aus der Baseline) bereits als seit
mem-explorer 0.4.0 überholt markiert; die Skill-Regel dazu war zum Zeitpunkt dieses Laufs
bereits im Skill-Stand `ae11dcb` vorhanden und wurde trotzdem nicht befolgt (siehe
Vorbehalte).

## Vergleich Baseline → GREEN

| Szenario | Kennzahl | Baseline (RED) | GREEN (Runde 1) |
|---|---|---|---|
| 1 | Exit | 1 / 1 | 0 / 0 |
| 1 | Blank Nodes | 4 / 5 | 0 / 0 |
| 1 | `hat Wert`-Zeilen | 0 / 0 | 8 / 8 |
| 1 | CE-Hinweis (LP_0000852) als Typ | 1× / 1× | 0× / 0× |
| 1 | Erfundene IDs | 0/19 · 0/19 | 0/24 · 0/24 |
| 2 | Exit | 0 / 0 | 0 / 0 |
| 2 | Blank Nodes | 0 / 0 | 0 / 0 |
| 2 | IRIs verändert | nein / nein | nein / nein |
| 2 | Reasoner-Artefakt „repariert“ | 0 / 0 | 0 / 0 |
| 3 | Nennt LP_0030280 | 14× / 19× (beide richtig, aber via blinden Fleck) | 0× (falsche Klasse) / 26× (richtig, via lokale Datei) |
| 3 | Zitiert „blinden Fleck“ | 2× / 2× | 0× / 2× |

Szenario 1 und 2 sind gegenüber der Baseline eindeutig verbessert (Szenario 1 kippt von
Exit 1 mit Blank Nodes und Nulltreffern bei `hat Wert` auf Exit 0 ohne Blank Nodes;
Szenario 2 war bereits grün und bleibt es, jetzt ohne echten CE-Hinweis-Typ im Ergebnis,
nur noch als erklärender Kommentar). Szenario 3 verschiebt das Problem, löst es aber nicht:
Baseline nannte beide Male die richtige Klasse aus dem falschen Grund (blinder Fleck),
GREEN Runde 1 nennt einmal die falsche Klasse aus Mangel an Unterscheidungsmerkmal und
einmal die richtige Klasse wieder aus einem nicht belastbaren Grund (lokale Datendatei statt
Termtabelle).

## Runde 1: Befund

Szenario 1 und 2 bestehen beide Läufe (2/2) gegen das in `docs/testing/szenarien.md`
definierte Erfolgsmaß: Exit 0, keine erfundene ID, in Szenario 2 zusätzlich unveränderte
IRIs und keine „reparierten“ Reasoner-Artefakte. Szenario 3 besteht nach Controller-Urteil
keinen der beiden Läufe (0/2): Lauf 1 nennt LP_0030280 nicht — er nennt die strukturgleiche,
aber falsche Schwesterklasse LP_0030059; Lauf 2 nennt LP_0030280 korrekt, aber stützt die
Auswahl im eigenen Wortlaut auf eine externe, ungeprüfte Nutzdatendatei statt auf die
mitgelieferten Referenzen, und zitiert zusätzlich den überholten „blinden Fleck“ aus einem
fremden Projekt.

Ursache ist die in dieser Runde entdeckte Schwesterklassen-Lücke: LP_0030059 und LP_0030280
sind strukturell identisch (`Element (SH)` ⊓ `hat Funktion = Hinweisbeschreibungsfunktion`)
und ließen sich vor dieser Runde nur über die `skos:editorialNote` unterscheiden (das Fach,
für das die Klasse angelegt wurde) — eine Angabe, die in `references/terms/lp-terms.tsv`,
`scripts/lookup.sh` und `references/laender/*.md` bis zu diesem Zeitpunkt nicht sichtbar
war. 21 der 46 SH-Klassen tragen eine solche Note.

Der REFACTOR-Commit dieser Fix-Runde (`editorialNote`-Spalte in `gen-terms.py`,
`gen-laender.py`, `scripts/lookup.sh`; neunte Regel in `references/fallstricke.md`; je ein
Satz in `references/muster.md` und `references/arbeitsablauf.md`) adressiert genau diese
Lücke. Eine zweite GREEN-Runde für Szenario 3 — mit dem in dieser Fix-Runde aktualisierten
Erfolgsmaß aus `docs/testing/szenarien.md` (beide Kandidatenklassen mit editorialNote
nennen, `scripts/klasse.sh` für die Teile-Restriktion, keine lokale Datendatei als Quelle) —
steht noch aus.

## Runde 2

Steht aus.

## Vorbehalte

1. **Szenario 1: derselbe Kompetenzbereich wie in `beispiel.ttl`.** Der Prompt-Auszug
   „Die Frage nach Gott“ (SH, Ev. Religion, Sek I) ist genau der Kompetenzbereich, den
   `references/beispiel.ttl` bereits modelliert — ein Zufall der Szenario-Konstruktion, kein
   Verdienst des Skills. Beide Läufe benennen das selbst und nutzen die Datei ausdrücklich
   als Vorlage: Lauf 1 „dann `references/beispiel.ttl` als Vorlage kopiert — sie behandelt
   zufällig denselben Kompetenzbereich […]“; Lauf 2 „`references/beispiel.ttl` diente als
   Strukturvorlage, weil es denselben Fall […] bereits einmal durchbuchstabiert“. Beide
   grenzen sich aber ausdrücklich ab (eigener Namensraum, eigene ID-Nachschlagung, Lauf 2
   übernimmt den Inhalt „wörtlich aus dem gegebenen Auszug […] statt es zu kopieren“) — ein
   Unterschied zur Baseline, wo dieselbe Nähe zu einem lokalen Dokument zum Scheitern führte
   (Blank Nodes, `rdfs:label` statt `hat Wert`, CE-Hinweis). Für eine belastbarere Messung
   müsste Szenario 1 einen Kompetenzbereich verwenden, den `beispiel.ttl` nicht abdeckt.
2. **Szenario 2: exakte Texte wieder aus `beispiel.ttl`.** Wie schon in der Baseline (siehe
   dortiger Vorbehalt „Fixture-Leck“) ziehen beide Läufe die korrekten Titel-/
   Beschreibungstexte aus `references/beispiel.ttl`, nicht aus einer unabhängigen Quelle:
   Lauf 1 nennt „das Original `references/beispiel.ttl` als Referenzwert für die genauen
   Titel-/Beschreibungstexte“; Lauf 2 „`references/beispiel.ttl` als unbeschädigte Vorlage
   desselben Ausschnitts für die neuen Textwerte“. Der Kopfkommentar von `nachbessern.ttl`
   nennt `beispiel.ttl` weiterhin ausdrücklich als Quelle der Fixture (siehe Baseline-
   Vorbehalt — die dort erwogene Entfernung des Hinweises wurde nicht umgesetzt). Exit 0 in
   Szenario 2 ist damit weiterhin teilweise durch Textkopie statt durch Ableitung aus dem
   Bericht allein erklärt, nicht durch Fehlverhalten der Agenten.
3. **Szenario 3, Lauf 2: der überholte „blinde Fleck“ erneut zitiert.** Obwohl der
   Skill-Stand dieser Runde (`ae11dcb`) `references/fallstricke.md` mit der Regel „Der
   blinde Fleck LP_0030278/LP_0030280 … ist seit mem-explorer 0.4.0 geschlossen“ bereits
   enthielt, zitiert Lauf 2 im eigenen Wortlaut erneut „einer der in `mem-explorer/CLAUDE.md`
   dokumentierten blinden Flecken“ als Beleg dafür, dass die Ontologie keine Teile-Restriktion
   für `LP_0030280` definiert (was in der Sache richtig ist, aber aus der falschen,
   veralteten Begründung folgt). Das zeigt, dass eine Regel im Skill zu haben nicht dasselbe
   ist wie sie tatsächlich befolgt zu bekommen — ein Befund für eine mögliche künftige
   Runde, nicht Teil des REFACTORs dieser Fix-Runde.
