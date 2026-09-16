# Fallstricke

Neun Regeln, jede mit ihrer Begründung. Wo die Ausgangsläufe ohne Skill
(`docs/testing/baseline.md`, RED) den Fehler tatsächlich gezeigt haben, steht das dabei —
das ist die Rechtfertigung, warum die Regel überhaupt in dieser Skill steht (Skill-TDD).
Zwei Regeln beantworten stattdessen eine Nachschlage-Aufgabe, für die es in der Baseline
keinen eigenen Fehlerfall gab; das ist ebenfalls zulässig und so vermerkt. Die neunte Regel
stammt aus der ersten GREEN-Runde (`docs/testing/green.md`), nicht aus der Baseline —
Szenario 3 bestand dort nicht.

| Regel | Warum |
|---|---|
| Text am Titel-/Beschreibungsknoten an `hat Wert`, nicht `rdfs:label` | Pattern 2; der Store tut es anders, ist aber nicht die Autorität. Beobachtet: beide Szenario-1-Läufe schrieben 0 `hat Wert`-Zeilen, den Text nur an `rdfs:label` (Szenario 1, Lauf 1 und Lauf 2). |
| Beschreibungen sind Klasse Beschreibung (LP_0030003), nicht CE-Hinweis (LP_0000852) | Range von `hat Beschreibung`; CE-Hinweis löst zudem SHACL-Abbrüche aus (Issue 12). Beobachtet: beide Szenario-1-Läufe verwendeten je 1× CE-Hinweis statt Beschreibung (Szenario 1, Lauf 1 und Lauf 2); beide Szenario-2-Läufe korrigierten denselben Fehlertyp in der Fixture (Szenario 2, Lauf 1 und Lauf 2). |
| Jahrgangsstufen sind Individuen, keine Literale `"5-6"` | Pattern 5. Beobachtet: die Fixture `nachbessern.ttl` enthielt das Literal `"5-6"` als absichtlichen Fehler; beide Szenario-2-Läufe ersetzten es durch die Individuen `lp:LP_2000005`/`lp:LP_2000006` (Szenario 2, Lauf 1 und Lauf 2). |
| Keine Blank Nodes | Nicht verweisbar, nicht prüfbar, nicht im Prüfstand. Beobachtet: beide Szenario-1-Läufe schrieben 4 bzw. 5 Blank Nodes für Wertknoten (Szenario 1, Lauf 1 und Lauf 2); Szenario 2 ersetzte den Blank Node aus der Fixture durch einen benannten Knoten (Szenario 2, Lauf 1 und Lauf 2). |
| IDs nie erfinden, nie aus dem Gedächtnis | Opak; Termanfragen an redaktion@mem.schule. (Referenz-Retrieval; kein Baseline-Fall — in allen sechs Läufen waren 0 der verwendeten Ontologie-IDs erfunden, weil alle Läufe konsequent nachgeschlagen haben.) |
| `hat Funktionsspezifikation` nicht von Hand schreiben | Ist OWL-Restriktion der Klasse, kein Datentripel (structure.md). (Referenz-Retrieval; kein Baseline-Fall) |
| Die Gegenrichtung `ist Teil von` nicht schreiben | Ein Reasoner leitet sie ab; SHACL-Meldungen dazu sind Reasoner-Artefakte. Beobachtet: in beiden Szenario-2-Läufen wurde keine `ist Teil von`- oder `hat Funktion`-Kante ergänzt; beide Läufe halten ausdrücklich fest, dass kein Reasoner-Artefakt „repariert“ wurde (Szenario 2, Lauf 1 und Lauf 2). |
| Der „blinde Fleck“ LP_0030278/LP_0030280 (keine benannte Oberklasse) ist seit mem-explorer 0.4.0 geschlossen | Die Hierarchie enthält jetzt die aus `owl:intersectionOf` abgeleiteten Kanten; SHACL sieht beide Klassen. Eine gegenteilige Notiz in einem anderen Projekt ist veraltet, nicht die Ontologie. Beobachtet: beide Szenario-3-Läufe stützten ihre Antwort ausdrücklich auf genau diesen inzwischen überholten Hinweis aus `mem-explorer/CLAUDE.md` (Szenario 3, Lauf 1 und Lauf 2). |
| Strukturgleiche Schwesterklassen eines Landes per `editorialNote` unterscheiden, nie den Namen raten | Strukturgleiche Schwesterklassen eines Landes unterscheidet nur die editorialNote (das Fach, für das sie angelegt wurde). Passt keine Note zum Fach: alle Kandidaten mit Note nennen, eine wählen, die Wahl im Kommentar begründen und im ganzen Lehrplan einheitlich bleiben. Die Datenkonvention eines vorhandenen Lehrplans desselben Landes und Fachs darf die Wahl entscheiden — sie ist kein Muster, nur die Auflösung einer Gleichheit. Beobachtet: GREEN Szenario 3 traf zwei verschiedene Antworten auf dieselbe Frage — Lauf 1 wählte LP_0030059 „Möglicher Inhalt (SH)“, deren editorialNote „Englisch Primar“ lautet (GREEN, Szenario 3, Lauf 1); Lauf 2 wählte die richtige Klasse LP_0030280 „Mögliches Thema und Inhalt (SH)“ (editorialNote „Sachunterricht“), aber nur über die lokale SH-Nutzdatendatei, nicht über die Termtabellen — wörtlich: Namenserraten aus `references/laender/SH.md` allein reichte nicht, da mehrere Klassen „Inhalt“ im Namen tragen (GREEN, Szenario 3, Lauf 2). |

## Rationalisierungstabelle

Wörtliche Begründungen aus den Ausgangsläufen (linke Spalte, mit Szenario und Lauf), und
die Antwort, die diese Skill dagegenhält.

| Begründung (wörtlich) | Antwort |
|---|---|
| „… habe ich mich eng an das reale, bereits geprüfte Referenzbeispiel … gehalten, das exakt denselben Lehrplan … bereits modelliert — daher dieselben Muster …“ (Szenario 1, Lauf 1) | Ein lokal gefundenes Dokument ist nicht geprüft, nur vorhanden. Muster kommen aus `references/muster.md`, nicht aus einer Datei, die zufällig im selben Dateibaum liegt — auch wenn sie denselben Lehrplan behandelt. |
| „… auf das reale, bereits produktiv erstellte Referenzdokument … dessen Muster ich übernommen habe …“ (Szenario 1, Lauf 2) | „Produktiv“ heißt nicht „richtig“. Ob eine Datei den Mustern folgt, entscheidet `mem-explorer check`, nicht ihr Vorhandensein oder ihr Einsatzstatus. |
| „… einer der beiden im mem-explorer-CLAUDE.md dokumentierten blinden Flecken (LP_0030278/LP_0030280) …“ (Szenario 3, Lauf 1) | Der Hinweis ist mit mem-explorer 0.4.0 veraltet. Aktuellen Stand mit `scripts/klasse.sh` und `references/laender/SH.md` prüfen, nicht eine fremde `CLAUDE.md` aus einem anderen Projekt zitieren. |
| „Das deckt sich exakt mit einem der beiden in mem-explorer/CLAUDE.md dokumentierten blinden Flecken (LP_0030278/LP_0030280 ohne benannte Oberklasse).“ (Szenario 3, Lauf 2) | Dieselbe Antwort: Notizen in anderen Projekten haben ein Datum. `klasse.sh` zeigt den aktuellen Stand, nicht den Stand, zu dem die Notiz geschrieben wurde. |
| „Namenserraten aus `references/laender/SH.md` allein reichte nicht, da mehrere Klassen „Inhalt“ im Namen tragen“ (GREEN, Szenario 3, Lauf 2) | Genau dafür gibt es jetzt die `note`-Spalte: `scripts/lookup.sh` und `references/laender/<XX>.md` zeigen die editorialNote direkt, ohne den Umweg über eine lokale Nutzdatendatei. Lauf 1 hatte diesen Hinweis noch nicht — wörtlich: Die Klassenzuordnung stammt aus `scripts/lookup.sh "Möglicher Inhalt"` und aus `references/laender/SH.md` bzw. `references/arbeitsablauf.md` (Zuordnung „Konkretionen“ → Lerninhalt-Klasse des Landes) (GREEN, Szenario 3, Lauf 1) — und wählte ohne editorialNote die strukturgleiche, aber falsche Klasse LP_0030059 „Möglicher Inhalt (SH)“ (editorialNote „Englisch Primar“) — genau die Verwechslung, die die Note jetzt sichtbar macht. |
