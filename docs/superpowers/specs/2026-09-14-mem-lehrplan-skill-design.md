# mem-lehrplan — Entwurf

Eine Agent-Skill für das Schreiben und Nachbessern von MEM-Lehrplandaten (Turtle), plus
das Kommandozeilenwerkzeug, auf das sie sich stützt. Zwei Teile in zwei Repositories:

- **Teil A** — `mem-explorer` bekommt eine Kommandozeile: `npx mem-explorer check datei.ttl`.
- **Teil B** — das Repository `mem-lehrplan` ist die Skill selbst.

Stand: 2026-09-14. Entscheidungen aus dem Gespräch mit laoc, Herkunft der Fakten am Ende.

## 1. Zweck

Wer Lehrpläne der Länder nach dem MEM-Modell transformiert — von Hand oder mit einem
LLM — braucht drei Dinge, die es bisher nur verstreut gibt: die verbindlichen Muster der
Lehrplan-Ontologie, die IDs ohne Raten, und eine Prüfung, die sagt, was falsch ist und
wie es richtig aussieht. Der MEM Explorer liefert die Prüfung im Browser; der Bericht
nennt seit 0.2.0 zu jedem Befund das Soll aus der Doku. Was fehlt, ist die Fassung für
den Agenten: eine Prüfung, die er selbst aufrufen kann, und eine Skill, die ihm sagt,
wie er arbeitet, bevor er die erste Zeile schreibt.

Der Anlass ist dokumentiert: Die SH-Fassung 6.0 folgte dem Befund „Literal an
ObjectProperty“ und schrieb dann Blank Nodes mit `rdfs:label`, nach dem Vorbild der
Store-Importe statt der Doku. Ein Agent mit dieser Skill hätte den Titel-Knoten aus
Pattern 2 kopiert, die IDs nachgeschlagen und das Ergebnis geprüft, bevor jemand es
ansieht.

## 2. Rahmen

**Zielgruppe:** LLM-Agenten (Claude Code und andere agentskills-kompatible Werkzeuge) und
die Menschen, die sie beim Transformieren begleiten. Deutsch, wie Ontologie-Doku und
Explorer.

**Aufgabe der Skill:** Transformieren und Nachbessern. Aus einem PDF (oder Textauszug)
MEM-Turtle schreiben, das die Muster der Doku einhält; einen Explorer-Bericht abarbeiten,
bis keine Fehler mehr gemeldet werden.

**Autorität:** Die Dokumentation der Lehrplan-Ontologie (FWU-DE/lehrplan-ontologie).
Nicht der MEM-Store — dessen Importe weichen von den Mustern ab (Titel mit `rdfs:label`
statt `hat Wert`, 1,8 Mio. Fälle). Nicht das Gedächtnis des Agenten — IDs sind opak und
werden nachgeschlagen.

### Nicht-Ziele

- Kein SPARQL gegen den MEM-Store. Das ist Abfragen, nicht Schreiben; eigene Skill.
- Keine Kopie der Explorer-Regeln in der Skill. Die Prüfung läuft über die CLI, sonst
  laufen zwei Regelsätze auseinander.
- Kein Bündeln der Prosa-Doku (`structure.md`, `patterns.md`, zusammen 10.000 Wörter).
  Die Skill destilliert, was ein Autor braucht, und verlinkt den Rest.
- Kein Ersatz für den Abgleich mit dem PDF. Texttreue und Vollständigkeit prüft ein
  Mensch im Explorer; die Skill sorgt dafür, dass er dabei nicht über Modellierungsfehler
  stolpert.

## 3. Teil A — Kommandozeile im mem-explorer

### 3.1 Aufruf und Verhalten

```
npx mem-explorer check <datei.ttl> [--json]
```

- Läuft `parseTurtle`, `buildModel`, Regeln R1–R13 und SHACL exakt wie der Browser und
  gibt den Markdown-Bericht (`toMarkdown`) auf stdout aus — mit Vorspann „Für die
  Weiterverarbeitung“ und den Soll-Blöcken. `--json` gibt `toJson` aus.
- Prüfstand: leer (`newSession`). Der Abschnitt „Beanstandungen“ sagt „Keine.“ — auf der
  Kommandozeile gibt es keinen Prüfstand, und der Bericht soll trotzdem dieselbe Form
  haben wie der Export aus dem Browser.
- Kopf: Dateiname, Datum, Werkzeug- und Ontologie-Version, sha256 der Datei.
- SHACL-Status im Bericht ist „abgeschlossen“ oder „fehlgeschlagen“; „läuft noch“ kommt
  auf der Kommandozeile nicht vor.

**Exit-Codes** — damit ein Agent schleifen kann:

| Code | Bedeutung |
|---|---|
| 0 | kein Befund mit Schwere „Fehler“ |
| 1 | mindestens ein Befund mit Schwere „Fehler“ |
| 2 | Datei nicht lesbar, nicht parsebar oder falscher Aufruf |

Warnungen und Hinweise (auch Reasoner-Artefakte) ändern den Exit-Code nicht. Sie stehen
im Bericht.

### 3.2 Aufbau

```
src/lib/cli/check.ts      runCheck(text, fileName, opts) → { markdown, json, exitCode }
src/cli/main.ts           liest argv und Datei, ruft runCheck, schreibt stdout, setzt Exit
bin/mem-explorer.mjs      eine Zeile: import('../dist/cli/mem-explorer.mjs')
vite.cli.config.ts        Library-Build für Node, Ziel dist/cli/
```

`runCheck` ist rein und getestet: gegen `tests/fixtures/sekundarstufe.ttl` (42 Fehler →
Exit 1), gegen eine Datei ohne Fehler (Exit 0), gegen `broken.ttl` (Exit 2), und der
Markdown ist bis auf Datum und Hash gleich dem `toMarkdown`-Export mit leerem Prüfstand.
Der Build wird nicht im Test ausgeführt; ein Rauchtest des gebauten Binaries auf den
Fixtures gehört zur Freigabe.

**Warum Library-Build:** Die einzigen Vite-Spezifika in `lib/` sind die beiden
`?raw`-Importe der Turtle-Artefakte. Der Library-Build inliniert sie; das npm-Paket ist
damit offline vollständig. `n3`, `rdf-ext`, `rdf-validate-shacl` bleiben externe
Abhängigkeiten. Alternativen — `tsx` mit Loader-Hook oder ein eigenes Paket für `lib/` —
sind verworfen: das eine bringt eine Laufzeit-Abhängigkeit für `npx`, das andere macht
aus dem Explorer ein Monorepo für einen Konsumenten.

**Laufzeit:** `crypto.subtle` für den Hash braucht Node ≥ 19; `engines` steht bereits auf
≥ 22. SHACL auf einer 400-Knoten-Datei dauert in Node wenige Sekunden; für eine Schleife,
die ein Agent eine Handvoll Male durchläuft, ist das in Ordnung.

### 3.3 Paket

`package.json`: `bin`, `files` (`dist/cli`, `bin`, `README.md`, `LICENSE`), `exports`
nur für die CLI. Der Paketname `mem-explorer` ist auf npm frei (geprüft 2026-09-14).
Version 0.3.0. Veröffentlichung durch Forgejo Actions auf `git.edufeed.org/laoc/mem-explorer`
(`.forgejo/workflows/publish-npm.yml`, Auslöser Tag `vX.Y.Z`, Secret `NPM_TOKEN`; Stand
2026-09-15). Der Comenius-Spiegel bleibt Quelle des Homelab-Deploys; der Pin kann auf v0.3.0
nachziehen, damit Kopfzeile und npm-Version übereinstimmen.

README bekommt einen Abschnitt „Kommandozeile“. Die Explorer-Spec bekommt einen Abschnitt
5.6 mit dem Inhalt von 3.1–3.3.

### 3.4 Voraussetzung: zwei weitere Reasoner-Artefakte einordnen

Gemessen am 2026-09-14: Eine nach Pattern 1 und 2 korrekt geschriebene SH-Wurzel mit
einem Titel-Knoten bekommt vom Explorer zwei SHACL-Treffer, darunter einen „Fehler“ —
der Exit-Code der CLI wäre damit für jede richtige Datei 1.

1. **`sh:class` auf ein Ontologie-Individuum.** Die Shape für `von Bundesland` verlangt
   die Klasse „Bundesland Bezeichnung“ (LP_0000040) am Ziel. `lp:LP_3000054` ist in
   `lp-base.ttl` nur als `owl:NamedIndividual` deklariert, ohne Klasse; die Zugehörigkeit
   folgt erst durch einen Reasoner aus der `rdfs:range` von `von Bundesland`. Keine
   Datei kann das erfüllen, und keine soll den Typ eines Ontologie-Individuums selbst
   behaupten. Einordnung: `ClassConstraintComponent`, Ziel ist laut `terms.json` ein
   Individuum → Hinweis, „SHACL · Reasoner-Artefakt“, Regel `shacl:Class · Individuum`.
   Nachgeprüft, nicht vermutet: die Prüfung sieht in der Term-Tabelle nach.
2. **`sh:minCount` auf `is about` (IAO_0000136) am Textknoten.** Die Shape für textuelle
   Entitäten fordert, dass jeder Titel-/Beschreibungsknoten „über etwas“ ist. Kein
   Muster schreibt das; `lp.owl` deklariert IAO_0000136 als Inverse von „wird
   beschrieben von“ (LP_0000024), und `hat Titel`, `hat Beschreibung`, `hat Nummer`
   sind dessen Unterproperties. Ein Reasoner leitet `is about` aus der eingehenden
   `hat Titel`-Kante ab. Einordnung wie bei `ist Teil von`: Hinweis, Reasoner-Artefakt,
   wenn auf den Knoten über LP_0000024 oder eine Unterproperty gezeigt wird. Die
   Unterproperty-Kette wird über `terms.json` (`parents`) aufgelöst.

Erwartete Messung danach an `sekundarstufe.ttl`: weiterhin 55 SHACL-Treffer, davon
`typ-falsch` 2 statt 3 und 29 statt 28 Reasoner-Artefakte; zusammengeführt weiterhin 73.
Diese Zahlen werden beim Umsetzen gemessen und in Tests, CLAUDE.md und Explorer-Spec
nachgezogen.

## 4. Teil B — die Skill `mem-lehrplan`

### 4.1 Form

agentskills.io-Format: Ordner = Skill-Name, `SKILL.md` mit YAML-Frontmatter, optionale
Ordner `references/`, `scripts/`. Repository-Wurzel ist der Skill-Ordner — so finden es
Claude Code, die anderen Laufzeiten und openskills.cc.

Frontmatter:

```yaml
name: mem-lehrplan
description: >
  Use when writing or fixing MEM curriculum data (Lehrplan-Turtle nach der
  FWU Lehrplan-Ontologie): transforming a Lehrplan PDF into Turtle, working off a
  MEM-Explorer report, choosing LP_/SF_/SA_ IDs or Länder classes, or when SHACL/
  Explorer findings mention hat Titel, hat Beschreibung, hat Wert, Blank Nodes,
  Jahrgangsstufe, hat Teil.
license: CC-BY-SA-4.0
compatibility: Node 22+ for `npx mem-explorer check`; grep and awk for the lookup
  scripts; pdftotext optional.
metadata:
  author: sroertgen
  ontology: 1.0.0rc4
```

Die description nennt nur Auslöser, keinen Arbeitsablauf (sonst folgt der Agent der
description statt der Skill). Englische Schlüsselwörter, weil Agenten auf Englisch
suchen; der Inhalt ist deutsch.

### 4.2 Layout

```
mem-lehrplan/
  SKILL.md                         < 500 Wörter: Kernregel, Ablauf in sechs Zeilen,
                                   Schnellreferenz, rote Flaggen, Verweise
  references/
    arbeitsablauf.md               die Schleife ausformuliert, PDF → Struktur
    muster.md                      das Soll je Situation, aus Pattern 1, 2, 5, 6, 7
    konventionen.md                Namensraum, IRIs, Literale, Kommentare, Dateischnitt
    fallstricke.md                 Regeln mit Begründung; Rationalisierungstabelle
    befunde.md                     jede Befundart des Explorers → Soll
    beispiel.ttl                   ein vollständiger, gültiger Minimal-Lehrplan
    beispiel-bericht.md            der CLI-Bericht dazu — so sieht „sauber“ aus
    laender/XX.md                  je Land: Wurzel-, Fragment-, Bereichs-, Kompetenz-,
                                   Inhaltsklassen; Präfix der Schulfach-/Schulart-IDs
    terms/lp-terms.tsv             988 LP_-Terme: id, type, label_de, label_en, parent, comment_de
    terms/sf-terms.tsv             911 Schulfach-Terme
    terms/sa-terms.tsv             106 Schulart-Terme
    patterns/pattern1..14.ttl      wörtlich aus FWU-DE/lehrplan-ontologie (CC BY-SA 4.0)
    lp-base.ttl                    die Ontologie (763 KB), nie ganz gelesen, nur per Skript
    VERSION                        Ontologie-Version, Commit, Datum der Erzeugung
  scripts/
    lookup.sh                      ID → Bedeutung, Label → ID, über die drei Tabellen
    klasse.sh                      Block einer Klasse aus lp-base.ttl: Label, Oberklasse,
                                   hat-Teil-Restriktionen
    update-references.sh           klont/aktualisiert die FWU-Repos, erzeugt terms/,
                                   laender/, kopiert patterns/ und lp-base.ttl, schreibt VERSION
  docs/testing/baseline.md         die Ausgangsläufe ohne Skill, wörtlich
  docs/superpowers/specs/          dieser Entwurf
  LICENSE                          CC BY-SA 4.0
  README.md                        Installation, Aktualisierung, Herkunft
```

Alles unter `references/terms`, `laender`, `patterns`, `lp-base.ttl` und `VERSION` ist
**erzeugt** und eingecheckt — die Skill soll ohne Netz funktionieren, und ein Diff nach
`update-references.sh` zeigt, was sich in der Ontologie geändert hat.

### 4.3 Was in SKILL.md steht

Die Kernregel, ein Absatz: Die Doku der Ontologie ist die Autorität, nicht der Store,
nicht das Gedächtnis. Jede ID kommt aus `lookup.sh`. Jede Strukturentscheidung kommt aus
einem Muster. Jeder Befund wird gegen sein Soll behoben.

Der Ablauf, sechs Zeilen, mit Verweis auf `arbeitsablauf.md`:

1. `muster.md` und `laender/XX.md` lesen, bevor die erste Zeile Turtle entsteht.
2. Jede ID mit `scripts/lookup.sh` nachschlagen. Keine ID aus dem Gedächtnis.
3. Benannte Knoten mit IRI im eigenen Namensraum; Titel und Beschreibung als Wertknoten
   mit `hat Wert`; Jahrgangsstufen als Individuen; Hierarchie über `hat Teil`;
   keine Blank Nodes.
4. `npx mem-explorer check datei.ttl`.
5. Bericht gruppenweise mit den Soll-Blöcken abarbeiten. Reasoner-Artefakte bleiben.
6. Wiederholen bis Exit 0; dann den Bericht dem Menschen für den PDF-Abgleich geben.

Eine Schnellreferenz-Tabelle: die zehn Prädikate und Klassen, die in jeder Datei
vorkommen (`hat Teil`, `hat Titel`, `hat Beschreibung`, `hat Wert`, `hat Nummer`, `hat
Position`, `hat Jahrgangsstufe`, `von Bundesland`, `hat Schulfach`, `für Schulart`) mit
ID und einem Beispielwert.

Rote Flaggen — Gedanken, bei denen der Agent anhält: „Der Store schreibt es so“, „die ID
sieht richtig aus“, „Blank Nodes sind kürzer“, „ich prüfe am Ende“, „der Explorer zeigt
den Text, also passt es“.

### 4.4 Die Referenzen im Einzelnen

**`muster.md`** — je Situation ein Turtle-Block, wörtlich aus den Pattern-Dateien, mit
dem Link auf den Abschnitt der Doku:

- Lehrplanwurzel (Pattern 1): Klasse des Landes, `von Bundesland`, `hat Schulfach`,
  `für Schulart`, `hat Schulstufe`, `uri`.
- Titel, Beschreibung, Nummer (Pattern 2): benannte Knoten der Klassen Titel
  (LP_0000346), Beschreibung (LP_0030003), Identifikationsnummer (LP_0000347), Text an
  `hat Wert` (LP_0000344).
- Jahrgangsstufe und Schulstufe (Pattern 5): Individuen LP_2000001–LP_2000013, mehrwertig;
  Schulstufe über `hat Schulstufe`.
- Hierarchie (Pattern 6): `hat Teil` (obo:BFO_0000051) von der Wurzel abwärts; welche
  Klasse was enthalten darf, steht in der Klassendefinition (`klasse.sh`).
- Verweise (Pattern 7): CE-Verweis mit `verweist auf`.
- Reihenfolge: `hat Position` (LP_0000460) — RDF bewahrt keine Reihenfolge; die
  Geschwisterfolge aus dem PDF geht sonst verloren.

**`konventionen.md`** — als *unsere* Konvention gekennzeichnet, weil die Doku dazu
schweigt:

- Ein eigener Namensraum je Land und Projekt (`https://lp-sh.org/resource/` in SH),
  lesbare stabile Slugs, eine IRI je Knoten. IRIs werden zwischen Iterationen nie
  umbenannt — der Prüfstand des Explorers hängt an ihnen.
- Literale ohne Sprachtag, wie in den Pattern-Dateien.
- `rdfs:label` ist die technische Kurzbezeichnung; der Titel-Knoten trägt den Wortlaut
  des Dokuments.
- Text wörtlich aus dem PDF, nie paraphrasiert, nie gekürzt.
- Ein Kommentar `# S. 12` mit der PDF-Seite an jedem Knoten, für den Abgleich.
- Eine Datei je Lehrplan; Schnitt nach Schulstufe (`Bundesland/schulstufe.ttl`).
- Präfixblock zum Kopieren: `lp`, `obo`, `rdf`, `rdfs`, `xsd`, eigener `data:`.

**`arbeitsablauf.md`** — die Schleife und der Weg vom PDF zur Struktur: `pdftotext
-layout` seitenweise; Überschriften werden Fragmente und Bereiche, Tabellenspalten
trennen Kompetenzen von Konkretionen; was ein Knoten ist (ein Punkt der Vorlage, nicht
ein Satz); wo `hat Nummer` die Nummerierung der Vorlage bewahrt.

**`fallstricke.md`** — Regeln mit Begründung, aus der Praxis (Herkunft in §9):

| Regel | Warum |
|---|---|
| Text am Titel-/Beschreibungsknoten an `hat Wert`, nicht `rdfs:label` | Pattern 2; der Store tut es anders, ist aber nicht die Autorität |
| Beschreibungen sind Klasse Beschreibung (LP_0030003), nicht CE-Hinweis (LP_0000852) | Range von `hat Beschreibung`; CE-Hinweis löst zudem SHACL-Abbrüche aus (Issue 12) |
| Jahrgangsstufen sind Individuen, keine Literale `"5-6"` | Pattern 5 |
| Keine Blank Nodes | nicht verweisbar, nicht prüfbar, nicht im Prüfstand |
| IDs nie erfinden, nie aus dem Gedächtnis | opak; Termanfragen an redaktion@mem.schule |
| `hat Funktionsspezifikation` nicht von Hand schreiben | ist OWL-Restriktion der Klasse, kein Datentripel (structure.md) |
| Die Gegenrichtung `ist Teil von` nicht schreiben | ein Reasoner leitet sie ab; SHACL-Meldungen dazu sind Artefakte |
| SH-Klassen LP_0030278/LP_0030280 sind für SHACL unsichtbar | keine benannte Oberklasse; die Explorer-Regeln greifen trotzdem |

Dazu die **Rationalisierungstabelle**, gefüllt aus den Ausgangsläufen (§5), nicht aus der
Vorstellung.

**`befunde.md`** — für jede Befundart des Explorers (R1–R13, `shacl:Class`,
`shacl:MinCount`, die beiden Reasoner-Artefakte) das Soll und der Handgriff. Inhaltlich
dasselbe wie `guidance.ts` im Explorer; die Skill-Fassung ist ausführlicher und darf
Beispiele aus `beispiel.ttl` zitieren.

**`beispiel.ttl`** — Land SH, ein Lehrplan mit Wurzel, einem Fragment, einem
Kompetenzbereich mit Titel- und Beschreibungsknoten, einer Kompetenz mit zwei
Jahrgangsstufen, einer Konkretion, `hat Nummer` und `hat Position`. Geprüft mit der CLI:
Exit 0. Der Bericht dazu (`beispiel-bericht.md`) zeigt die Reasoner-Artefakte, die auch
bei einer sauberen Datei bleiben — damit niemand versucht, sie wegzumodellieren.

**`laender/XX.md`** — erzeugt aus `lp-terms.tsv`: alle Klassen mit Suffix `(XX)`,
gruppiert nach Oberklasse (Lehrplan, Lehrplanfragment, CE-Bereich, Kompetenz-
spezifikation, Lerninhalt, Hinweis, Verweis), plus der ID-Präfix in `sf-terms.tsv` und
`sa-terms.tsv`. 16 Dateien; SH hat 48 Klassen, SL 86, HE 27.

### 4.5 Skripte

- `lookup.sh <ID|Suchwort>` — grep über die drei Tabellen; ID-Treffer exakt, Wort-Treffer
  case-insensitiv über `label_de`/`label_en`; Ausgabe `id · type · label_de · parent`.
- `klasse.sh <LP_ID>` — druckt den `###  <IRI>`-Block aus `lp-base.ttl` und löst die IDs
  in `owl:onProperty`/`owl:someValuesFrom` über `lookup.sh` auf, damit der Agent liest
  „hat Teil → Mögliches Thema und Inhalt (SH)“ statt nackter IDs.
- `update-references.sh [pfad-zum-checkout]` — ohne Argument klont es
  FWU-DE/lehrplan-ontologie, schulfach-ontologie, schulart-ontologie flach nach `.vendor/`
  (gitignored); mit Argument benutzt es einen vorhandenen Checkout. Erzeugt die Tabellen
  (Portierung von `gen-term-maps.py` aus der Wissensbasis), `laender/`, kopiert
  `patterns/` und `lp-base.ttl`, schreibt `VERSION`. Python 3 ohne weitere Pakete.

## 5. Tests — die Skill wird gegen Ausgangsläufe geschrieben

Skill-Schreiben ist TDD an Prozessdokumentation: erst ansehen, was ein Agent ohne Skill
tut, dann die Skill gegen genau diese Fehler schreiben, dann wieder prüfen.

### 5.1 Drei Szenarien

1. **Transformieren.** Ein Textauszug (ein Kompetenzbereich mit Beschreibung, drei
   Konkretionen, Jahrgangsstufen 5–6, Land SH, eine Seite Vorlage) → „Schreibe das als
   MEM-Turtle.“ Erfolgsmaß: `mem-explorer check` Exit 0, alle IDs in den Tabellen
   vorhanden, Titel/Beschreibung als Wertknoten mit `hat Wert`, Jahrgangsstufen als
   Individuen, keine Blank Nodes, `hat Position` gesetzt.
2. **Nachbessern.** Eine Datei mit den fünf Fehlerklassen der SH-Fassungen (Literal an
   ObjectProperty, Blank-Node-Wertknoten, `rdfs:label` statt `hat Wert`, Jahrgangsstufe
   als Literal, CE-Hinweis statt Beschreibung) plus ihr CLI-Bericht → „Behebe die
   Befunde.“ Erfolgsmaß: Exit 0, IRIs unverändert, Reasoner-Artefakte nicht angefasst.
3. **Nachschlagen.** „Welche Klasse hat eine Konkretion in SH, und was darf sie
   enthalten?“ Erfolgsmaß: Antwort aus `laender/SH.md` und `klasse.sh`, mit IDs, ohne
   Raten; der Agent zeigt, welches Skript er benutzt hat.

### 5.2 Ablauf

- **RED:** alle drei Szenarien an Subagenten ohne Skill, Ergebnis und Begründungen
  wörtlich nach `docs/testing/baseline.md`. Erwartet aus der Erfahrung mit der SH-Datei:
  Literale an ObjectProperties, erinnerte oder erfundene IDs, Jahrgangsstufe als String,
  Blank Nodes, Typisierung aus dem Store. Zeigt ein Szenario ohne Skill keinen Fehler,
  wird das festgehalten und die Skill dort nicht aufgeblasen.
- **GREEN:** dieselben Szenarien mit Skill. Bestanden heißt: Erfolgsmaß erreicht.
- **REFACTOR:** neue Ausreden aus den Läufen in die Rationalisierungstabelle; Wortlaut
  straffen, bis die Läufe konvergieren.

Diese Läufe sind kein Ersatz für den Blick eines Menschen auf `beispiel.ttl` und die
Muster — sie prüfen, ob ein Agent mit der Skill richtig arbeitet, nicht, ob die Skill
schön ist.

## 6. Verteilung

- Origin: `ssh://git@git.edufeed.org/laoc/mem-lehrplan-skill.git` (angelegt 2026-09-15; zur
  Benennung siehe §8). Spiegel: `github.com/sroertgen/mem-lehrplan`, öffentlich — openskills.cc
  listet nur GitHub-Repos mit `SKILL.md` an der Wurzel. Der Spiegel ist ein zweiter
  Remote, kein CI.
- Installation (README): Claude Code `git clone … ~/.claude/skills/mem-lehrplan`;
  andere Laufzeiten `~/.agents/skills/mem-lehrplan`; openskills.cc bietet zusätzlich
  den Zip-Download an.
- Listing auf openskills.cc: kein Einreichformular gefunden; Einträge wirken von GitHub
  geerntet. Link an den Betreiber (Kontakt im Footer), sonst abwarten.
- Versionierung: Git-Tags `v0.1.0` …; `metadata.version` im Frontmatter;
  `references/VERSION` nennt den Ontologie-Stand.
- FWU informieren: nach dem ersten Tag, per Mail an redaktion@mem.schule oder Discussion
  im Ontologie-Repo. Nicht in Issue 12.

## 7. Reihenfolge

Teil A zuerst, weil Szenario 1 und 2 die CLI brauchen.

1. **A0** Die zwei Reasoner-Artefakte aus §3.4 einordnen, Zahlen neu messen und pinnen.
2. **A1** `runCheck` mit Tests; `main.ts`; Bin; Vite-CLI-Build; README; Explorer-Spec §5.6.
3. **A2** Rauchtest des Binaries auf Fixtures und SH-Fassung 6.0; Version 0.3.0; Tag; Push;
   `npm publish` durch laoc.
4. **B1** Repo `mem-lehrplan` anlegen; `update-references.sh` und Erzeugung von
   `references/` aus `~/coding/fwu/lehrplan-ontologie`; LICENSE; Remotes.
5. **B2** `beispiel.ttl` schreiben und mit der CLI auf Exit 0 bringen; Bericht ablegen.
6. **B3** RED: drei Szenarien ohne Skill, `baseline.md`.
7. **B4** GREEN: `SKILL.md` und Referenzen schreiben; Szenarien mit Skill; REFACTOR.
8. **B5** README; Tag v0.1.0; Push zu beiden Remotes; openskills-Kontakt; Notiz an FWU.

## 8. Offene Punkte

- **npm-Konto.** `npm whoami` meldet keine Anmeldung. Veröffentlichung macht laoc.
- **Textauszug für Szenario 1.** Am besten eine Seite der SH-Fachanforderungen; ob das
  PDF lokal vorliegt, ist nicht geprüft. Ersatz: ein selbst geschriebener Auszug in
  derselben Form.
- **Konvention Namensraum.** `https://lp-sh.org/resource/` ist die Wahl der
  relidesk-Transformation, keine FWU-Vorgabe. Ob FWU eine Empfehlung aussprechen will,
  wäre eine Frage an die Redaktion.
- **Repo-Name.** Die agentskills-Spezifikation verlangt `name` = Name des Skill-Ordners.
  Der Zip-Download von openskills.cc trägt den Repo-Namen. Heißt das Repo
  `mem-lehrplan-skill`, muss die Skill so heißen — oder das Repo wird in `mem-lehrplan`
  umbenannt (Forgejo leitet den alten Namen weiter). Entscheidung von laoc ausstehend.
- **Lizenz.** CC BY-SA 4.0 für das ganze Repo, weil FWU-Material gebündelt wird. Der
  eigene Text ist damit ebenfalls share-alike.

## 9. Herkunft der Fakten

Aus der Sitzung vom 2026-09-14 im mem-explorer, alle nachgeprüft:

- SH-Fassung 6.0: 381 Knoten, 0 Titel/Beschreibungen ohne die Explorer-Änderungen,
  477 übersprungene Blank-Node-Aussagen; nach 0.2.0: 48/111, R12/R13 je 159.
- MEM-Store: 1.843.584 Titel-Knoten mit `rdfs:label`, 0 mit `hat Wert` (SPARQL,
  sparql.mem.edufeed.org).
- Auto-Shapes mit `sh:path []`: FWU-DE/lehrplan-ontologie Issue 12; Quelle
  `lehrplan-core.owl` Zeilen 957 und 1331.
- `hat Position` LP_0000460, `hat Nummer` LP_0030057, `uri` LP_0000463 aus `lp-terms.tsv`.
- Pattern-Dateien: Literale ohne Sprachtag; Namensraum in der Doku nicht geregelt.
- agentskills.io-Spezifikation: Felder `name`, `description`, `license`, `compatibility`,
  `metadata`, `allowed-tools`; Ordner `scripts/`, `references/`, `assets/`.
- openskills.cc: Verzeichnis, verlinkt GitHub-`SKILL.md`, kein Einreichformular.
