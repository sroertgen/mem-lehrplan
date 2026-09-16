# GREEN — Läufe mit Skill

Dieselben sechs Läufe wie in `docs/testing/baseline.md` (RED), diesmal mit vorangestelltem
Satz „Lies zuerst `SKILL.md` und arbeite genau danach.“ Geprüft mit mem-explorer 0.4.0
(`node ~/coding/comenius/mem-explorer/bin/mem-explorer.mjs check`). Runde 1 (Szenario 1–3,
Skill-Stand `ae11dcb`) bestand Szenario 3 nicht; Runde 2 (Szenario 3 erneut, Skill-Stand
`dca2c23`, nach dem REFACTOR gegen die Schwesterklassen-Lücke) bestand. Zahlen aus
`.superpowers/sdd/2026-09-14-mem-lehrplan-skill/task-6-green-scores.md`
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

Begründung (wörtlich, ohne die Pfadangabe zur Turtle-Datei):

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
> einen direkten Sprung von der Fachanforderungs-Wurzel zum Kompetenzbereich erlaubt, da
> LP_0030070 über eine anonyme Intersection ebenfalls als Element (SH) gilt — deshalb habe
> ich anders als im Beispiel keine erfundene Lehrplanfragment-Ebene eingefügt, weil der
> Auszug keinen übergeordneten Abschnittstitel nennt. Der dritte Themenpunkt aus der Aufgabe
> („Gottesvorstellungen in anderen Religionen“) fehlte im Beispiel und wurde als drittes
> `LP_0030280`-Element mit eigener Position ergänzt.

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

Begründung (wörtlich, ohne die Pfadangabe zur Turtle-Datei):

> Ich bin genau dem Ablauf aus `SKILL.md` gefolgt: `references/muster.md` lieferte die
> Strukturmuster (Pattern 1 Lehrplanwurzel, Pattern 2 Titel/Beschreibung/Nummer als eigene
> Wertknoten, Pattern 6 Hierarchie über `hat Teil`, plus `hat Position`), `references/konventionen.md`
> die projektspezifischen Regeln (eigener `data:`-Namensraum, lesbare Slugs, Text wörtlich
> ohne Sprachtag, Seitenkommentar je Knoten), und `references/laender/SH.md` die
> Landesklassenliste, aus der ich LP_0000824 (Fachanforderung SH), LP_0030070
> (Kompetenzbereich SH), LP_0030278 (Prozessbezogene Kompetenz SH) und LP_0030280
> (Mögliches Thema und Inhalt SH) auswählte. `references/beispiel.ttl` diente als
> Strukturvorlage, weil es denselben Fall (SH, Ev. Religion, „Die Frage nach Gott") bereits
> einmal durchbuchstabiert — den Inhalt (drei statt zwei Themen-Bullets, abweichender
> Beschreibungstext) habe ich aber wörtlich aus dem gegebenen Auszug übernommen statt es zu
> kopieren. Jede ID habe ich mit `scripts/lookup.sh` (Schulfach SH_0000008, Schulart
> SH_0000003, alle LP_-Klassen) verifiziert und die drei Landesklassen zusätzlich mit
> `scripts/klasse.sh` gegen ihre OWL-Definition in `lp-base.ttl` geprüft, um zu bestätigen,
> dass sie als Teile eines Kompetenzbereichs zulässig sind. Bewusst weggelassen habe ich eine
> Lehrplanfragment-Zwischenebene, weil der Auszug keine übergeordnete Abschnittsangabe
> enthält und ich nichts erfinden wollte, was nicht im Text steht.

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

Begründung (wörtlich):

> Beide Originaldateien sind unverändert (nur gelesen, nicht geschrieben).
>
> **Was ich geändert habe, je Befundgruppe:**
>
> - **Literal an ObjectProperty / hat Titel** (`fachanforderung`): Den Literal
>   `"Fachanforderungen Evangelische Religion"` von der Kante entfernt und stattdessen einen
>   neuen Knoten `data:fachanforderung-titel` (`a lp:LP_0000346`, `hat Wert`) eingehängt.
> - **Wertknoten als Blank Node / hat Beschreibung** (`kb-gott`): Den Blank Node
>   `[ a lp:LP_0030003 ; rdfs:label … ]` durch den benannten Knoten `data:kb-gott-beschreibung`
>   mit `hat Wert` ersetzt.
> - **Text nicht an „hat Wert“** (`kb-gott-titel`): Dem vorhandenen, benannten Titel-Knoten
>   das fehlende `lp:LP_0000344 "1 Die Frage nach Gott"` ergänzt, `rdfs:label` blieb stehen.
> - **Literal an ObjectProperty / hat Jahrgangsstufe** (`kb-gott-pk-1`): Das Literal `"5-6"`
>   durch die beiden Individuen `lp:LP_2000005 , lp:LP_2000006` ersetzt.
> - **Ziel ohne geforderte Klasse + Pflichtangabe fehlt / ist Teil von**
>   (`kb-gott-inhalt-1-hinweis`): Nur den Typ von `lp:LP_0000852` (CE-Hinweis) auf
>   `lp:LP_0030003` (Beschreibung) umgesetzt — IRI und die `hat Beschreibung`-Kante blieben
>   unverändert; das behebt zugleich die zugehörige fehlende `ist Teil von`-Pflichtangabe,
>   weil diese Shape nur an CE-Hinweis-Knoten gilt.
>
> Gestützt habe ich mich auf `references/befunde.md` (Soll-Muster je Regel, inkl. der
> Beispiele, die wörtlich auf diese Datei zugeschnitten sind), das Original
> `references/beispiel.ttl` als Referenzwert für die genauen Titel-/Beschreibungstexte, sowie
> `scripts/lookup.sh` zur Bestätigung der Klassen-/Property-IDs (LP_0000346, LP_0030003,
> LP_0000344, LP_2000005/6, LP_0000852). Verifiziert mit `node bin/mem-explorer.mjs check` im
> Projekt `mem-explorer`: Exit 0, 0 Fehler, 0 Warnungen, nur noch die erwarteten 17
> Reasoner-Artefakt-Hinweise. Keine IRI wurde umbenannt oder entfernt.

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

Begründung (wörtlich):

> Der Explorer bestätigt Exit 0: 0 Fehler, 0 Warnungen, alle 17 verbleibenden Hinweise sind
> Reasoner-Artefakte (kein Handlungsbedarf, gemäß `references/befunde.md`).
>
> **Was ich je Befundgruppe geändert habe:**
>
> 1. **Literal an ObjectProperty — hat Titel** (`fachanforderung`): Das Literal
>    `"Fachanforderungen Evangelische Religion"` direkt an `lp:LP_0030056` durch einen neuen
>    benannten Knoten `data:fachanforderung-titel` (Klasse `lp:LP_0000346` „Titel") mit dem
>    Text an `lp:LP_0000344` ersetzt — Pattern 2.
> 2. **Wertknoten als Blank Node + Text nicht an „hat Wert"** (`kb-gott`, hat Beschreibung):
>    Den `[ a lp:LP_0030003 ; rdfs:label "…" ]`-Blank-Node durch den benannten Knoten
>    `data:kb-gott-beschreibung` ersetzt, mit `hat Wert` ergänzt. Sowie separat
>    `data:kb-gott-titel` um das fehlende `lp:LP_0000344` ergänzt (rdfs:label blieb als
>    technische Kurzbezeichnung stehen, Titeltext kam separat dazu — Konvention aus
>    `konventionen.md`).
> 3. **Literal an ObjectProperty — hat Jahrgangsstufe** (`kb-gott-pk-1`): `"5-6"` durch die
>    Individuen `lp:LP_2000005 , lp:LP_2000006` ersetzt (Pattern 5).
> 4. **Ziel ohne geforderte Klasse + Pflichtangabe „ist Teil von"**
>    (`kb-gott-inhalt-1-hinweis`): Den Knoten von `lp:LP_0000852` (CE-Hinweis) auf
>    `lp:LP_0030003` (Beschreibung) umgetypt, IRI und Kante unverändert. Mit
>    `scripts/klasse.sh LP_0000852` bzw. `LP_0030003` geprüft, dass nur CE-Hinweis eine
>    `obo:BFO_0000050`-Restriktion trägt (deshalb löste die Umtypung beide gemeldeten Befunde
>    gleichzeitig, ohne eine Kante ergänzen zu müssen) — bestätigt durch den Vergleich mit
>    `references/beispiel.ttl`, wo der analoge Knoten `kb-gott-beschreibung` denselben Befund
>    nicht hat.
>
> **Grundlage/Werkzeuge:** `SKILL.md`-Ablauf, `references/befunde.md` (Soll-Blöcke je Regel),
> `references/muster.md` (Pattern 2/5), `references/konventionen.md` (Label vs. Titel),
> `references/beispiel.ttl` als unbeschädigte Vorlage desselben Ausschnitts für die neuen
> Textwerte, `scripts/klasse.sh` zur Bestätigung der Klassen-Restriktionen, sowie
> `node bin/mem-explorer.mjs check` (aus `/home/laoc/coding/comenius/mem-explorer`) zur
> Schlussprüfung — Exit 0.
>
> Beide Originaldateien wurden nicht verändert; die korrigierte Datei liegt unter
> `/tmp/claude-1000/-home-laoc-coding-comenius-mem-explorer/89cfbaf0-2f8e-4e41-9688-22b9b56c69a4/scratchpad/green/szenario-2-lauf-2.ttl`.

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

Begründung (wörtlich, ohne die Pfadangabe zur Antwortdatei):

> **Kernaussage:** Für eine „Konkretion“ (möglicher Inhalt zu einem Kompetenzbereich) in
> Schleswig-Holstein ist die Klasse `LP_0030059` „Möglicher Inhalt (SH)“ vorgesehen; sie
> enthält jedoch **keine** `owl:Restriction` auf `hat Teil` (`obo:BFO_0000051`) — weder
> direkt noch in ihrer gesamten Oberklassenkette (`LP_0002103` „Element (SH)“ →
> `LP_0000261` „Curriculares Element“) — die Ontologie schreibt also nicht vor, was ein
> solcher Knoten als Teile haben darf oder muss. Auffällig: der Funktionswert der Klasse
> (`hat Funktion` LP_0000483 = `LP_0001014` „Hinweisbeschreibungsfunktion“) ist derselbe,
> der die generische Klasse `LP_0000852` „CE-Hinweis“ definiert, nicht der Wert von
> `LP_0000332` „CE-Lerninhalt“ (`LP_0000480`) — trotz des Namens ist der SH-Knoten also
> funktional eher ein Hinweis- als ein Lerninhalt-Typ, und auch CE-Hinweis regelt nirgends,
> was es enthalten darf.
>
> **Herkunft der Angaben:** Die Klassenzuordnung stammt aus `scripts/lookup.sh "Möglicher
> Inhalt"` und aus `references/laender/SH.md` bzw. `references/arbeitsablauf.md` (Zuordnung
> „Konkretionen“ → Lerninhalt-Klasse des Landes). Die Definitionsblöcke und die Prüfung auf
> fehlende `hat Teil`-Restriktionen stammen aus
> `scripts/klasse.sh LP_0030059/LP_0002103/LP_0000261/LP_0000332/LP_0000852`, gegengeprüft
> direkt gegen `references/lp-base.ttl`. Das generische Hierarchiemuster (`hat Teil` von
> Lehrplan bis CE-Hinweis) stammt aus `references/patterns/pattern6.ttl`. Ich habe genau
> nach `SKILL.md` gearbeitet: nur `lookup.sh`/`klasse.sh` und die referenzierten Dateien,
> keine ID aus dem Gedächtnis, keine Subagenten.

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

Begründung (wörtlich, ohne die Pfadangabe zur Antwortdatei):

> **Kernaussage:** Für eine „Konkretion" (möglicher Inhalt zu einem Kompetenzbereich) in
> Schleswig-Holstein ist die Klasse `lp:LP_0030280` („Mögliches Thema und Inhalt (SH)“)
> vorgesehen; die Ontologie schränkt aber nicht ein, was ein solcher Knoten als Teile
> (`obo:BFO_0000051`, hat Teil) haben darf — weder eine OWL-Restriktion an der Klasse selbst
> noch eine SHACL-Shape existiert dafür. In den echten Daten (Datenkonvention, nicht
> Ontologie-Zwang) enthalten Konkretions-Container weitere Knoten desselben Typs `LP_0030280`.
>
> **Woher die Angaben stammen:**
> - Die Klassenidentität kommt aus den echten SH-Nutzdaten
>   `~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl`
>   (dort tragen die „Mögliche Konkretionen“-Container und ihre Stichpunkte durchgängig
>   `rdf:type lp:LP_0030280`) — Namenserraten aus `references/laender/SH.md` allein reichte
>   nicht, da mehrere Klassen „Inhalt“ im Namen tragen.
> - Label/Typ bestätigt mit `scripts/lookup.sh LP_0030280`.
> - Die vollständige Klassendefinition (anonyme `owl:intersectionOf`, keine
>   `hat Teil`-Restriktion) kommt aus `scripts/klasse.sh LP_0030280`, `LP_0002103`,
>   `LP_0000261`, sowie einem gezielten `grep` über `references/lp-base.ttl` nach
>   `owl:onProperty obo:BFO_0000051` — die einzige derartige Restriktion in der
>   SH-Hierarchie sitzt an der Wurzelklasse `LP_0000824`, nicht an `LP_0030280`.
> - Zusätzlich geprüft gegen `src/lib/ontology/generated/shapes.ttl` und `hierarchy.ttl` im
>   mem-explorer-Repo: keine SHACL-Shape zielt auf `LP_0030280`.

Lauf 2 nennt die richtige Klasse, aber — im eigenen Wortlaut oben — nur, weil eine externe,
ungeprüfte Nutzdatendatei (`relidesk-mem-lehrplan-transformation/…`) als Schiedsrichter
zwischen den beiden gleich aussehenden Kandidaten diente: dieselbe Rationalisierung
(„ein reales, vorhandenes Dokument entscheidet“), die schon in der Baseline zum
Szenario-1-Scheitern führte, jetzt mit richtigem statt falschem Ergebnis. Die vollständige
Antwortdatei (`docs/testing/green/szenario-3-lauf-2.md`, nicht Teil der obigen
Selbstauskunft-Zusammenfassung) geht darüber hinaus und zitiert zusätzlich den in
`mem-explorer/CLAUDE.md` dokumentierten „blinden Fleck“ als Beleg für die fehlende
Oberklasse — denselben, den `references/fallstricke.md` (Regel 8, aus der Baseline) bereits
als seit mem-explorer 0.4.0 überholt markiert; die Skill-Regel dazu war zum Zeitpunkt dieses
Laufs bereits im Skill-Stand `ae11dcb` vorhanden und wurde trotzdem nicht befolgt (siehe
Vorbehalte). Die oben genannte Kennzahl zum „blinden Fleck“ (2×) stammt aus dieser
vollständigen Antwortdatei, nicht aus der hier zitierten Kurz-Selbstauskunft.

## Vergleich Baseline → GREEN

| Szenario | Kennzahl | Baseline (RED) | GREEN (Runde 1) | GREEN (Runde 2) | GREEN (Bestätigung `65828ed`) |
|---|---|---|---|---|---|
| 1 | Exit | 1 / 1 | 0 / 0 | – | 0 |
| 1 | Blank Nodes | 4 / 5 | 0 / 0 | – | 0 |
| 1 | `hat Wert`-Zeilen | 0 / 0 | 8 / 8 | – | 8 |
| 1 | CE-Hinweis (LP_0000852) als Typ | 1× / 1× | 0× / 0× | – | 0× |
| 1 | Erfundene IDs | 0/19 · 0/19 | 0/24 · 0/24 | – | 0/28 |
| 2 | Exit | 0 / 0 | 0 / 0 | – | – (nicht erneut gelaufen) |
| 2 | Blank Nodes | 0 / 0 | 0 / 0 | – | – (nicht erneut gelaufen) |
| 2 | IRIs verändert | nein / nein | nein / nein | – | – (nicht erneut gelaufen) |
| 2 | Reasoner-Artefakt „repariert“ | 0 / 0 | 0 / 0 | – | – (nicht erneut gelaufen) |
| 3 | Nennt LP_0030280 | 14× / 19× (beide richtig, aber via blinden Fleck) | 0× (falsche Klasse) / 26× (richtig, via lokale Datei) | 2× / 3× (beide zusätzlich mit LP_0030059) | – (nicht erneut gelaufen) |
| 3 | Nennt LP_0030059 | – (nicht erhoben) | 12× (statt LP_0030280) / 1× | 7× / 3× | – (nicht erneut gelaufen) |
| 3 | editorialNote genannt | – (gab es noch nicht) | – (gab es noch nicht) | 7× / 7× | – (nicht erneut gelaufen) |
| 3 | Zitiert „blinden Fleck“ | 2× / 2× | 0× / 2× | 0× / 0× | – (nicht erneut gelaufen) |
| 3 | Lokale Datendatei/Wissensbasis als Quelle | ja / ja | nein / ja | nein / nein | – (nicht erneut gelaufen) |
| 4 | Erfolgsmaß bestanden (kein Baseline-Lauf) | – (Szenario gab es noch nicht) | 2/2 | – | 1/1 |

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
war. 26 der 37 SH-Klassen tragen eine solche Note.

Der REFACTOR-Commit dieser Fix-Runde (`editorialNote`-Spalte in `gen-terms.py`,
`gen-laender.py`, `scripts/lookup.sh`; neunte Regel in `references/fallstricke.md`; je ein
Satz in `references/muster.md` und `references/arbeitsablauf.md`) adressiert genau diese
Lücke. Eine zweite GREEN-Runde für Szenario 3 — mit dem in dieser Fix-Runde aktualisierten
Erfolgsmaß aus `docs/testing/szenarien.md` (beide Kandidatenklassen mit editorialNote
nennen, `scripts/klasse.sh` für die Teile-Restriktion, keine lokale Datendatei als Quelle) —
steht noch aus.

## Runde 2

Zwei neue Läufe für Szenario 3, Skill-Stand `dca2c23` (nach dem REFACTOR: editorialNote-Spalte,
aktualisiertes Erfolgsmaß in `szenarien.md`, korrigierter „unsichtbar“-Satz in
`laender/*.md`). Gleicher Prompt wie in Runde 1/Baseline, mit vorangestelltem
Skill-Hinweis. Zahlen aus dem Abschnitt „Szenario 3 — Runde 2“ von `task-6-green-scores.md`,
Zitate aus den Abschnitten `szenario-3-r2-lauf-1`/`-2` von `task-6-green-agent-returns.md`;
Rohausgaben unter `docs/testing/green/szenario-3-r2-lauf-1.md` und `-2.md`.

### Lauf 1 (`szenario-3-r2-lauf-1.md`)

- 612 Wörter
- Nennt LP_0030280: 2 Vorkommen; nennt LP_0030059: 7 Vorkommen — beide Kandidatenklassen genannt
- editorialNote genannt: 7 Vorkommen
- Lokale Datendatei/Wissensbasis als Quelle: 0
- „blinder Fleck“ zitiert: 0
- Teile-Restriktion: keine gefunden — `scripts/klasse.sh LP_0030059` zeigt keinen
  `owl:Restriction`-Block auf `obo:BFO_0000051`; der Knoten ist laut Lauf 1 ein Blatt der
  Gliederung
- Quellen laut Datei: `references/arbeitsablauf.md`, `references/laender/SH.md`,
  `references/lp-base.ttl`, `references/muster.md`, `scripts/klasse.sh`, `scripts/lookup.sh`
- benutzte Skripte (Selbstauskunft): `scripts/lookup.sh "möglicher inhalt"`,
  `scripts/klasse.sh` (für `LP_0030059`, `LP_0030070`, `LP_0000332`, `LP_0000852` und
  weitere Vergleichskandidaten), `grep -n "BFO_0000051" references/lp-base.ttl`

Begründung (wörtlich, ohne die Pfadangabe zur Antwortdatei):

> **Kernaussage:** Für eine „Konkretion“ (möglicher Inhalt zu einem Kompetenzbereich) in SH
> ist `LP_0030059` „Möglicher Inhalt (SH)“ vorgesehen — Unterklasse von `LP_0002103`
> „Element (SH)“ mit `hat Funktion` → `Hinweisbeschreibungsfunktion` (`LP_0001014`),
> strukturell also vom Typ CE-Hinweis (`LP_0000852`), nicht CE-Lerninhalt. SH hat dafür
> keine einzige fachübergreifende Klasse, sondern vier strukturgleiche Schwestern (Englisch
> Sek I/II, Sachunterricht, Physik), unterschieden nur durch `skos:editorialNote`. Laut
> Ontologie sind diesem Knotentyp **keine Teile** zugewiesen: `scripts/klasse.sh LP_0030059`
> zeigt keinen `owl:Restriction`-Block auf `obo:BFO_0000051` (hat Teil) — der Knoten ist ein
> Blatt der Gliederung.
>
> Woher die Angaben stammen: die Klassen-ID über `scripts/lookup.sh "möglicher inhalt"`; die
> Definitionsblöcke (inkl. Bestätigung des fehlenden hat-Teil-Restriktion) über
> `scripts/klasse.sh` für `LP_0030059`, `LP_0030070` (Kompetenzbereich SH), `LP_0000332`
> (CE-Lerninhalt), `LP_0000852` (CE-Hinweis) und weitere Vergleichskandidaten; die
> Landesklassentabelle aus `references/laender/SH.md`; das allgemeine Hierarchiemuster aus
> `references/muster.md` (Pattern 6); die Bestätigung über
> `grep -n "BFO_0000051" references/lp-base.ttl`, dass keine solche Restriktion bei den
> betroffenen Klassen vorkommt — alles im Worktree
> `/home/laoc/coding/comenius/mem-lehrplan/.worktrees/skill`.

(Pfad des damaligen Worktrees)

### Lauf 2 (`szenario-3-r2-lauf-2.md`)

- 721 Wörter
- Nennt LP_0030280: 3 Vorkommen; nennt LP_0030059: 3 Vorkommen — beide Kandidatenklassen genannt
- editorialNote genannt: 7 Vorkommen
- Lokale Datendatei/Wissensbasis als Quelle: 0
- „blinder Fleck“ zitiert: 0
- Teile-Restriktion: nach Rolle differenziert — eine Klasse mit CE-Lerninhalt-Rolle darf
  laut Ontologie nur einen weiteren CE-Lerninhalt-artigen Knoten als Teil haben (kein
  CE-Bereich, keine CE-Kompetenzspezifikation), praktisch ergänzt um einen CE-Hinweis-Knoten
  (Pattern 6); eine Klasse mit CE-Hinweis-Rolle trägt keine eigene `hat Teil`-Restriktion und
  ist strukturell ein Blattknoten
- nennt zusätzliche strukturgleiche Klassen zum Vergleich: LP_0030282 „Inhalt (SH)“,
  LP_0030254 „Thema und Inhalt (SH)“ (CE-Lerninhalt-Rolle)
- Quellen laut Datei: `references/arbeitsablauf.md`, `references/fallstricke.md`,
  `references/laender/SH.md`, `references/lp-base.ttl`, `references/muster.md`,
  `references/patterns/pattern…`, `references/terms/lp-terms.tsv`, `scripts/klasse.sh`,
  `scripts/lookup.sh`
- benutzte Skripte (Selbstauskunft): `scripts/klasse.sh` (für `LP_0030070`, `LP_0002103`,
  alle „Inhalt/Thema/Möglich…“-Kandidaten, `LP_0000332`, `LP_0000852`), `scripts/lookup.sh`

Begründung (wörtlich, ohne die Pfadangabe zur Antwortdatei):

> **Kernaussage:** Der Kompetenzbereich selbst ist `LP_0030070` „Kompetenzbereich (SH)“.
> Für die „Konkretion" (Kompetenzbereich-Inhalt) gibt es in Schleswig-Holstein **keine
> einzige Klasse**, sondern mehrere strukturgleiche Schwesterklassen (`owl:intersectionOf`
> aus `LP_0002103` „Element (SH)" + einer Funktions-Restriktion auf `LP_0000483`
> „hat Funktion"), die je nach Fach entweder die Rolle von `LP_0000332` „CE-Lerninhalt"
> (Lerninhaltsbeschreibungsfunktion `LP_0000480`, z. B. `LP_0030282` Inhalt SH, `LP_0030254`
> Thema und Inhalt SH) oder von `LP_0000852` „CE-Hinweis" (Hinweisbeschreibungsfunktion
> `LP_0001014`, z. B. `LP_0030059` Möglicher Inhalt SH – Englisch Primar, `LP_0030280`
> Mögliches Thema und Inhalt SH – Sachunterricht) übernehmen; unterschieden wird
> ausschließlich über die `editorialNote` (Fach), nicht über den Namen. Als Teile darf eine
> Klasse mit CE-Lerninhalt-Rolle laut Ontologie nur einen weiteren CE-Lerninhalt-artigen
> Knoten haben (kein CE-Bereich, keine CE-Kompetenzspezifikation), praktisch ergänzt um
> einen CE-Hinweis-Knoten (Pattern 6); eine Klasse mit CE-Hinweis-Rolle trägt keine eigene
> `hat Teil`-Restriktion und ist strukturell ein Blattknoten.
>
> **Herkunft der Angaben:** Klassenliste und editorialNotes aus `references/laender/SH.md`;
> jede genannte ID einzeln mit `scripts/klasse.sh <ID>` gegen `references/lp-base.ttl`
> geprüft (LP_0030070, LP_0002103, alle „Inhalt/Thema/Möglich…"-Kandidaten, LP_0000332
> CE-Lerninhalt, LP_0000852 CE-Hinweis); IDs zusätzlich mit `scripts/lookup.sh`
> gegenkontrolliert; Kommentartexte aus `references/terms/lp-terms.tsv`; der Begriff
> „Konkretion" als generischer Workflow-Ausdruck sowie das Hierarchie-Muster aus
> `references/arbeitsablauf.md` und `references/patterns/pattern6.ttl`/`references/muster.md`.
> `references/fallstricke.md` (Zeile 21/34) dokumentiert diese Verwechslungsgefahr exakt für
> dieses Szenario — wurde zur Einordnung gelesen, die dort genannte "richtige" ID aber nicht
> ungeprüft übernommen, sondern jede Kandidaten-ID erneut selbst über `klasse.sh` verifiziert,
> da im aktuellen Auftrag kein Fach genannt ist.

Beide Läufe bestehen das in der Fix-Runde 1 aktualisierte Erfolgsmaß aus
`docs/testing/szenarien.md` (2/2): beide Kandidatenklassen mit editorialNote genannt, keine
Teile-Restriktion per `scripts/klasse.sh` unbelegt behauptet, Quellen ausschließlich aus der
Skill selbst, keine lokale Datendatei, kein „blinder Fleck“ zitiert. Lauf 2 geht über das
Erfolgsmaß hinaus und ordnet die strukturgleichen Schwesterklassen zusätzlich nach ihrer
Funktion (Lerninhalts- vs. Hinweisbeschreibungsfunktion), mit zwei weiteren Beispielen zum
Vergleich (LP_0030282, LP_0030254).

## Szenario 4 — Retrieval (nach Task 7)

Neues Szenario, ergänzt nach dem Gegenlesen (Fresh-Eyes-Read) von Task 7 — dafür gibt es
**keinen Baseline-Lauf**, das Szenario entstand erst danach. Zwei Läufe, Skill-Stand
`a4618dc` (Task 7, vor der Fix-Runde 1 dieses Dokuments). Gleicher Aufbau wie Szenario 3:
Prompt aus `docs/testing/szenarien.md`, Zahlen aus dem Abschnitt „Szenario 4 — Retrieval“ von
`task-6-green-scores.md`, Zitate aus den Abschnitten `szenario-4-lauf-1`/`-2` von
`task-6-green-agent-returns.md`; Rohausgaben unter `docs/testing/green/szenario-4-lauf-1.md`
und `-2.md`.

### Lauf 1 (`szenario-4-lauf-1.md`)

- 615 Wörter
- `hat Teil` (`obo:BFO_0000051`) genannt: 5 Zeilen
- `hat Position` (LP_0000460) genannt: 5
- `hat Nummer` (LP_0030057) genannt: 3
- Pattern 7 (`hat Verweis`/`verweist auf`, LP_0030071/72) genannt: 2
- Ontologie-IDs: 11, davon erfunden: 0
- Lokale Datendatei/Wissensbasis als Quelle: 0
- Quellen laut Datei: `references/arbeitsablauf.md`, `references/beispiel.ttl`,
  `references/fallstricke.md`, `references/laender/`, `references/muster.md`,
  `scripts/klasse.sh`, `scripts/lookup.sh`
- benutzte Skripte (Selbstauskunft): `scripts/lookup.sh` (für `hat Position`, `hat Nummer`,
  `hat Verweis`, `verweist auf`, die Basisklassen)

Begründung (wörtlich, ohne die Pfadangabe zur Antwortdatei):

> **Kernaussage:** Für „diese Kompetenz gehört zu diesen Inhalten“ gibt es in MEM keine
> eigene Verknüpfungs-Property — Kompetenz- und Inhalts-Zeilen werden stattdessen als
> gleichrangige Geschwister desselben Kompetenzbereichs an `hat Teil` (`obo:BFO_0000051`)
> gehängt, wobei die Spalte „Kompetenzen“ zur Kompetenzspezifikations-Klasse des Landes
> (Basisklasse LP_0000263, z. B. SH-Unterklasse LP_0030278) und „Mögliche Inhalte“ zur
> Lerninhalt-Klasse des Landes (Basisklasse LP_0000332, z. B. LP_0030280) wird; die
> Zeilenzugehörigkeit bleibt implizit über `hat Position` (LP_0000460) bzw. gleiche
> `hat Nummer` (LP_0030057) lesbar, ein ausdrücklicher Querverweis liefe über Pattern 7 mit
> `hat Verweis` (LP_0030071) und `verweist auf` (LP_0030072).
>
> Herkunft jeder Angabe: die Tabellen-/Verknüpfungsregel selbst steht wörtlich in
> `references/arbeitsablauf.md` und wird in `references/fallstricke.md` (Regel
> „Tabellenspalten trennen Klassen“) begründet; das Turtle-Muster („Hierarchie über
> hat Teil“, Pattern 6/7) kommt aus `references/muster.md`; das konkrete, bereits geprüfte
> Vorbild (Kompetenzbereich „Die Frage nach Gott“) aus `references/beispiel.ttl`; die
> konkreten IDs für `hat Position`, `hat Nummer`, `hat Verweis`, `verweist auf` sowie die
> Basisklassen wurden mit `scripts/lookup.sh` verifiziert, nicht aus dem Gedächtnis
> übernommen. Die Warnung zur editorialNote-Disambiguierung strukturgleicher Landesklassen
> stammt ebenfalls aus `references/fallstricke.md`, belegt mit einem dokumentierten Fehllauf
> (GREEN Szenario 3, Lauf 1).

Lauf 1 nennt „Mögliche Inhalte“ eine „Lerninhalt-Klasse des Landes (Basisklasse
LP_0000332)“ — das ist sachlich falsch: `LP_0030280` trägt laut `scripts/klasse.sh` die
Hinweisbeschreibungsfunktion (LP_0001014), nicht die Lerninhaltsbeschreibungsfunktion
(LP_0000480) von CE-Lerninhalt (LP_0000332); trotz des ähnlichen Namens sind die beiden
Klassen funktional verschieden (dieselbe Unterscheidung wie in Szenario 3, Runde 2, Lauf 2).
Die falsche Zuordnung stammt wörtlich aus der Formulierung „Lerninhalt-Klasse des Landes“ in
`references/arbeitsablauf.md`, Abschnitt „Vom PDF zur Struktur“ — eine Fehlleitung durch den
Skill-Text, nicht ein Fehler des Agenten. Mit dieser Fix-Runde (Task 7, Runde 1) ist die
Formulierung korrigiert: die Spalte wird zur Inhaltsklasse des Landes, die nicht zwingend ein
CE-Lerninhalt ist; `scripts/klasse.sh` zeigt die tatsächliche Funktion.

### Lauf 2 (`szenario-4-lauf-2.md`)

- 725 Wörter
- `hat Teil` (`obo:BFO_0000051`) genannt: 4 Zeilen
- `hat Position` (LP_0000460) genannt: 6
- `hat Nummer` (LP_0030057) genannt: 2
- Pattern 7 (`hat Verweis`/`verweist auf`, LP_0030071/72) genannt: 1
- Ontologie-IDs: 12, davon erfunden: 0
- Lokale Datendatei/Wissensbasis als Quelle: 0
- Quellen laut Datei: `references/arbeitsablauf.md`, `references/beispiel.ttl`,
  `references/fallstricke.md`, `references/laender/`, `references/muster.md`,
  `scripts/klasse.sh`, `scripts/lookup.sh`
- benutzte Skripte (Selbstauskunft): `scripts/lookup.sh` (für `hat Position`, `hat Nummer`),
  `scripts/klasse.sh LP_0000263`/`LP_0000332`

Begründung (wörtlich, ohne die Pfadangabe zur Antwortdatei):

> **Kernaussage:** MEM hat keine Property, die Kompetenz und Inhalt einer Tabellenzeile als
> Paar verknüpft — beide werden als Geschwister unter demselben Kompetenzbereich an
> `hat Teil` (`obo:BFO_0000051`) gehängt, und die Zeilenzugehörigkeit bleibt nur implizit
> über gleiche `hat Position` (`LP_0000460`) bzw. gleiche `hat Nummer` (`LP_0030057`) lesbar;
> ein expliziter Querverweis liefe über `hat Verweis`/`verweist auf` (`LP_0030071`/
> `LP_0030072`), ist hier aber nicht der Regelfall.
>
> Woher die Angaben stammen: Der Kern kommt wörtlich aus `references/arbeitsablauf.md`
> (Abschnitt „Vom PDF zur Struktur“), das konkrete Beispiel aus `references/beispiel.ttl`
> (geprüfter SH-Lehrplan, `mem-explorer check` Exit 0), die Property-IDs habe ich mit
> `scripts/lookup.sh` bestätigt (`hat Position`, `hat Nummer`; `hat Teil`/`obo:BFO_0000051`
> liefert dort erwartungsgemäß keinen Treffer, da kein `lp:`-Term — bestätigt stattdessen
> durch `references/muster.md` Pattern 6 und den Kommentar in `beispiel.ttl`), und die
> Klassendefinitionen von CE-Kompetenzspezifikation (`LP_0000263`) und CE-Lerninhalt
> (`LP_0000332`) mit `scripts/klasse.sh`, die zeigen, dass beide nur „Teil eines CE-Bereichs“
> sein dürfen und keine Kante zueinander vorsehen. Die Warnung zu mehrdeutigen Länderklassen
> stammt aus `references/fallstricke.md` (Fallbeispiel GREEN Szenario 3).

Lauf 2 macht denselben Fehler nicht: Er nennt keine „Lerninhalt-Klasse“ für die
Inhalte-Spalte und prüft stattdessen mit `scripts/klasse.sh`, was CE-Kompetenzspezifikation
und CE-Lerninhalt an Teilen zulassen.

Beide Läufe erfüllen das Erfolgsmaß aus `docs/testing/szenarien.md` (2/2 in dieser ersten
Runde): Geschwister über `hat Teil`, Ordnung über `hat Position`/`hat Nummer`, Pattern 7 nur
als Möglichkeit bei ausdrücklichem Querverweis, Quellen genannt, keine erfundene Property.
Lauf 1 zeigt zugleich eine reale Lücke im damaligen Skill-Text (`references/arbeitsablauf.md`
nannte die Inhalte-Spalte unbedingt eine „Lerninhalt-Klasse“) — der Anlass für die Fix-Runde
1 dieses Commits; Lauf 2 belegt, dass derselbe Fehler nicht zwingend auftritt, auch ohne die
Korrektur.

## Bestätigungsläufe auf dem Endstand (65828ed)

Befund 6 der Gesamtdurchsicht (`final-review.md`): keines der bisherigen Szenarien lief auf
dem ausgelieferten Skill-Stand — Szenario 1 und 2 auf `ae11dcb`, Szenario 3 (Runde 2) auf
`dca2c23`, Szenario 4 auf `a4618dc`, danach änderte sich der Skill-Text weiter bis `65828ed`
(Fix-Runde nach der Gesamtdurchsicht). Zur Schließung ein Bestätigungslauf je Szenario 1 und
4, Skill-Stand `65828ed`: Prompt wie in `docs/testing/szenarien.md`, mit vorangestelltem Satz
„Lies zuerst `SKILL.md`“ plus der zusätzlichen Anweisung, aus einem leeren Verzeichnis
außerhalb des Skill-Ordners heraus zu arbeiten — das prüft Befund 1 der Gesamtdurchsicht
(Pfadbasis) als beobachtetes Verhalten, nicht nur als Text in SKILL.md. Modell
claude-sonnet-5. Zahlen aus
`.superpowers/sdd/2026-09-14-mem-lehrplan-skill/final-confirm-scores.md`
(Controller-Messung), Zitate aus `final-confirm-agent-returns.md`; Rohausgaben unter
`docs/testing/green/szenario-1-final.ttl` und `-4-final.md`, Bericht zur Turtle-Datei in
`szenario-1-final-bericht.md`.

### Szenario 1 (`szenario-1-final.ttl`)

- Exit: 0
- Kopfzeile: 15 Befunde · 0 davon mehrfach bestätigt · 0 Fehler, 0 Warnungen, 15 Hinweise (15 Reasoner-Artefakte)
- Befundgruppen (ohne Reasoner-Artefakte): keine
- Blank Nodes: 0
- `hat Wert` (LP_0000344) vorhanden: 8 Zeilen
- `rdfs:label`-Zeilen gesamt (alle Knoten): 14 Zeilen
- CE-Hinweis (LP_0000852) verwendet: 0
- Jahrgangsstufe als Literal: 0
- Datennamensraum: `data: <https://example.org/lehrplan/sh/ev-religion-gymnasium/>`
- Ontologie-IDs verwendet: 28, davon nicht in den Termtabellen (erfunden): 0

Begründung (wörtlich, ohne die Pfadangabe zur Turtle-Datei):

> Ich habe mich strikt an den Ablauf aus `SKILL.md` gehalten: `references/muster.md`
> (Pattern 1, 2, 6), `references/konventionen.md`, `references/laender/SH.md` und
> `references/beispiel.ttl` gelesen, dann jede ID mit `scripts/lookup.sh` (u. a. `Religion`,
> `Gymnasium`, `LP_2000005/6`, `LP_0000045`, `SH_0000003`) und den Klasseninhalt mit
> `scripts/klasse.sh` für LP_0000824, LP_0030070, LP_0030278, LP_0030280 nachgeschlagen. Für
> „Mögliche Themen und Inhalte“ trägt keine der drei SH-Kandidatenklassen (LP_0030254/79/80)
> eine editorialNote für Religion — die Wahl von LP_0030280 stützt sich auf zwei unabhängige
> Belege: `references/arbeitsablauf.md` nennt sie explizit als SH-Klasse mit
> Hinweisbeschreibungsfunktion, und `references/beispiel.ttl` (dasselbe Land/Fach) setzt sie
> ebenso ein; das ist im Dateikommentar begründet. Anders als im Beispiel habe ich die
> Lehrplanfragment-Ebene weggelassen (der Auszug nennt keinen übergeordneten Abschnitt) und
> `uri` (LP_0000463) offen gelassen, weil keine echte Quell-URL bekannt war und ich keine
> erfinden wollte — beides ebenfalls kommentiert.
>
> Kein Skript-Aufruf oder Pfad aus der Skill selbst ist fehlgeschlagen (`lookup.sh`,
> `klasse.sh`, der `npx`-Aufruf für `check` liefen alle beim ersten Versuch); die einzige
> Reibung war ein eigener zusammengesetzter Bash-Befehl (`cat …; echo ===MUSTER===; cat …`),
> an dem meine zsh-Shell wegen der `===`-Zeichenfolge stolperte — ein Problem meines eigenen
> Befehls, nicht der Skill.

### Szenario 4 (`szenario-4-final.md`)

- 776 Wörter
- `hat Teil` (`obo:BFO_0000051`) genannt: 4 Zeilen
- `hat Position` (LP_0000460) genannt: 4
- `hat Nummer` (LP_0030057) genannt: 3
- Pattern 7 (`hat Verweis`/`verweist auf`, LP_0030071/72) genannt: 3
- Erfundene IDs: 0 (geprüft)
- Lokale Datendatei/Wissensbasis als Quelle: 0
- Quellen laut Datei: `references/arbeitsablauf.md`, `references/beispiel.ttl`,
  `references/laender/`, `references/lp-base.ttl`, `references/muster.md`,
  `scripts/klasse.sh`, `scripts/lookup.sh`

Begründung (wörtlich, ohne die Pfadangabe zur Antwortdatei):

> **Kernaussage:** Es gibt keine eigene Property, die eine Kompetenz mit „ihren“ Inhalten aus
> derselben Tabellenzeile paart. Beide Spalten hängen als Geschwister desselben
> Kompetenzbereichs an `hat Teil` (`obo:BFO_0000051`); die Zeilenzugehörigkeit bleibt nur über
> `hat Position` (LP_0000460) und ggf. gleiche `hat Nummer` (LP_0030057) lesbar — bestätigt
> durch die Klassendefinition von CE-Lerninhalt (LP_0000332), die als Elternteil nur
> CE-Lerninhalt/CE-Bereich erlaubt, keine CE-Kompetenzspezifikation. Nur ein im Text
> ausdrücklicher Querverweis würde Pattern 7 (`hat Verweis`/`verweist auf`,
> LP_0030071/LP_0030072) nutzen.
>
> **Herkunft der Angaben:** Der entscheidende Satz steht wörtlich in
> `references/arbeitsablauf.md` (Abschnitt „Eine Kompetenz mit ihren möglichen Inhalten …“);
> die Struktur-Muster stammen aus `references/muster.md` (Pattern 6/7) und dem realen Beleg
> `references/beispiel.ttl` (Kompetenzbereich „Die Frage nach Gott“, SH). Die Property- und
> Klassen-IDs habe ich mit `scripts/lookup.sh Inhalt` bzw. `scripts/lookup.sh Kompetenz`
> gesucht und die konkreten Restriktionen der Klassen LP_0000263, LP_0000332, LP_0030278 und
> LP_0030280 mit `scripts/klasse.sh <ID>` gegen `references/lp-base.ttl` geprüft — insbesondere
> den Unterschied zwischen „Inhalt“-Klassen mit Lerninhaltsbeschreibungsfunktion (LP_0000480)
> und solchen mit Hinweisbeschreibungsfunktion (LP_0001014), damit ich nicht wie in den
> dokumentierten Fehlläufen eine strukturgleiche, aber falsche Schwesterklasse wähle.
>
> **Zu Skill-Pfaden:** Alles lief auf Anhieb — SKILL.md, `references/*.md`,
> `references/beispiel.ttl` sowie `scripts/lookup.sh` und `scripts/klasse.sh` waren alle exakt
> an den in der Skill genannten Pfaden erreichbar; ich habe per `cd` in den Skill-Ordner
> gewechselt statt mit vollen Pfaden zu arbeiten, was laut SKILL.md ebenfalls zulässig ist.

Beide Agenten bestätigen im eigenen Wortlaut, dass jeder Pfad und Skript-Aufruf aus der Skill
beim ersten Versuch funktionierte — Szenario 4 per `cd` in den Skill-Ordner, Szenario 1 über
`lookup.sh`, `klasse.sh` und den `npx`-Aufruf für `check`, beide aus einem cwd außerhalb des
Skill-Ordners gestartet. Das beantwortet Befund 1 der Gesamtdurchsicht als beobachtetes
Verhalten auf dem ausgelieferten Stand, nicht nur als Satz in SKILL.md: der im Fix-Commit
`65828ed` ergänzte Pfadbasis-Satz hatte die Wahl (voller Pfad oder `cd` in den Skill-Ordner)
offengelassen, und beide Agenten haben beide Wege ohne Fehlschlag benutzt.

## Ergebnis

Alle vier Szenarien bestehen jetzt zwei aufeinanderfolgende Läufe: Szenario 1 und 2 bereits
in Runde 1 (Skill-Stand `ae11dcb`, siehe „Runde 1: Befund“), Szenario 3 erst in Runde 2, nach
dem REFACTOR, Szenario 4 — erst nach Task 7 ergänzt, kein Baseline-Lauf — direkt in seiner
ersten Runde (2/2, Skill-Stand `a4618dc`). Damit ist die im Plan festgelegte
Abbruchbedingung erfüllt: „Abbruch, wenn zwei aufeinanderfolgende Läufe je Szenario
bestehen“ (`docs/superpowers/plans/2026-09-14-mem-lehrplan-skill.md`, Task 6, Step 8).

Was zwischen Runde 1 und Runde 2 für Szenario 3 geändert wurde, steht in zwei Commits:

- `75b8f8e` — REFACTOR: `editorialNote`-Spalte in `scripts/gen-terms.py`/`gen-laender.py`/
  `scripts/lookup.sh`, neunte Regel in `references/fallstricke.md`, je ein Satz in
  `references/muster.md`/`references/arbeitsablauf.md`, aktualisiertes Erfolgsmaß in
  `docs/testing/szenarien.md`.
- `dca2c23` — den seit mem-explorer 0.4.0 falschen „für SHACL unsichtbar“-Satz in
  `references/laender/*.md` (u. a. `SH.md`, von wo aus der Szenario-3-Agent die
  Landesklassen liest) durch die korrekte Zwei-Satz-Erklärung ersetzt.

Ohne diese beiden Commits bestand Szenario 3 keinen der vier bis dahin gemessenen Läufe
(Baseline nannte die richtige Klasse nur über den veralteten „blinden Fleck“, Runde 1 einmal
falsch und einmal nur über eine externe Datendatei); mit beiden Commits bestehen beide
Runde-2-Läufe unabhängig voneinander und ohne externe Quelle (siehe Vorbehalt 4 unten für
eine Einschränkung dieser Aussage bei Lauf 2).

Diese vier Läufe (und die Runde-2-Läufe für Szenario 3) liefen alle auf zwischenzeitlichen
Skill-Ständen, nicht auf dem ausgelieferten: Szenario 1 und 2 auf `ae11dcb`, Szenario 3
(Runde 2) auf `dca2c23`, Szenario 4 auf `a4618dc`. Der Skill-Text änderte sich danach weiter
(u. a. `54c5b76` schrieb alle Pfadangaben in SKILL.md um, `75b8f8e` ergänzte die
`note`-Spalte, `a4618dc` und `c6cb7d3` korrigierten die Schnellreferenz bzw.
`arbeitsablauf.md`, `9623d1b` die Pattern-5-Fußnote, und die Fix-Runde nach der
Gesamtdurchsicht selbst). Der ausgelieferte Stand `65828ed` ist bestätigt durch je einen
Bestätigungslauf für Szenario 1 und 4 (siehe „Bestätigungsläufe auf dem Endstand (65828ed)“
oben, beide bestehen). **Szenario 2 und 3 wurden auf `65828ed` nicht erneut gelaufen** — für
sie gilt weiterhin nur der Beleg auf dem jeweils zwischenzeitlichen Stand.

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
4. **Szenario 3, Runde 2, Lauf 2: liest im Skill exakt die Beschreibung des eigenen Tests.**
   `references/fallstricke.md` beschreibt seit dem REFACTOR (neunte Regel plus
   Rationalisierungstabellen-Zeile) genau dieses Szenario — mit beiden Kandidaten-IDs und der
   „richtigen“ Antwort aus Runde 1. Lauf 2 liest diese Datei ausdrücklich zur Einordnung, hält
   aber selbst fest, dass er die dort genannte ID nicht einfach übernommen hat: „…
   `references/fallstricke.md` (Zeile 21/34) dokumentiert diese Verwechslungsgefahr exakt für
   dieses Szenario — wurde zur Einordnung gelesen, die dort genannte "richtige" ID aber nicht
   ungeprüft übernommen, sondern jede Kandidaten-ID erneut selbst über `klasse.sh` verifiziert,
   da im aktuellen Auftrag kein Fach genannt ist.“ Das ist eine ehrliche Grenze dieser
   Testrunde: die Skill wird hier teilweise auf genau dem Fall geprüft, gegen den sie
   geschrieben wurde (Skill-TDD), nicht auf einem unabhängigen. Der Lauf zeigt zwar gutes
   Verhalten (Verifikation über `klasse.sh` statt Kopie der genannten ID), belegt aber nicht,
   dass ein unabhängiges drittes Szenario mit derselben Art von Ambiguität ebenso bestehen
   würde.
