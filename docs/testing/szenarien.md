# Testszenarien für die Skill

Vier Aufgaben, jeweils ohne Skill (Baseline) und mit Skill. Die Prompts werden wörtlich an
einen frischen Subagenten (general-purpose) gegeben; der Baseline-Prompt erwähnt die Skill
nicht und untersagt sie nicht — er ist der Normalfall eines Agenten, der die Aufgabe bekommt.

## Szenario 1 — Transformieren

> Du transformierst Lehrpläne nach dem MEM-Modell (Lehrplan-Ontologie des FWU,
> https://github.com/FWU-DE/lehrplan-ontologie). Schreibe für den folgenden Auszug aus den
> Fachanforderungen Evangelische Religion Schleswig-Holstein (Sekundarstufe I, Gymnasium)
> eine Turtle-Datei. Der Lehrplan gilt für Schleswig-Holstein, Fach Evangelische Religion,
> Schulart Gymnasium. Gib nur Turtle aus, keine Erklärungen.
>
> ---
> **1 Die Frage nach Gott** (S. 12)
>
> Die Frage nach Gott wird als existentielle Frage aufgeworfen. Sie konkretisiert sich
> für die Schülerinnen und Schüler im Kontext religiöser und kultureller Vielfalt.
>
> *Prozessbezogene Kompetenz (Jahrgangsstufen 5–6):* Die Schülerinnen und Schüler nehmen
> unterschiedliche Gottesvorstellungen wahr und beschreiben sie.
>
> *Mögliche Themen und Inhalte (Jahrgangsstufen 5–6):*
> - Gottesvorstellungen (anthropomorph, symbolisch, allmächtig, gütig)
> - Gottesvorstellungen in anderen Religionen
> - Metaphorisches Sprechen von Gott (personal; apersonal)
> ---

Erfolgsmaß: `mem-explorer check` Exit 0 · jede `lp:`/`schulfach:`/`schulart:`-ID existiert in
`references/terms/` · Titel und Beschreibung als benannte Knoten mit `hat Wert` · Jahrgangsstufen
als Individuen · keine Blank Nodes · `hat Position` an den Geschwistern · Text wörtlich.

## Szenario 2 — Nachbessern

> Hier ist eine MEM-Turtle-Datei und der Prüfbericht des MEM Explorers dazu. Behebe die
> gemeldeten Befunde. Ändere keine IRIs. Gib die vollständige korrigierte Datei aus.
>
> [Datei: docs/testing/fixtures/nachbessern.ttl] [Bericht: docs/testing/fixtures/nachbessern-bericht.md]

`nachbessern.ttl` enthält absichtlich die fünf Fehlerklassen der SH-Fassungen 5 und 6:
Titel als Literal direkt am Element · Beschreibung als Blank Node mit rdfs:label ·
benannter Titel-Knoten mit rdfs:label statt hat Wert · Jahrgangsstufe als Literal `"5-6"` ·
Beschreibungsknoten der Klasse CE-Hinweis (LP_0000852).

Erfolgsmaß: Exit 0 · IRIs unverändert (Diff der Subjekte leer) · Reasoner-Artefakt-Gruppen
nicht „behoben“ (kein `ist Teil von`, kein `hat Funktion` hinzugefügt).

## Szenario 3 — Nachschlagen

> Welche Klasse der Lehrplan-Ontologie ist für eine „Konkretion“ (einen möglichen Inhalt zu
> einem Kompetenzbereich) in Schleswig-Holstein vorgesehen, und was darf ein solcher Knoten
> laut Ontologie als Teile haben? Nenne die IDs.

Erfolgsmaß: Antwort nennt LP_0030280 („Mögliches Thema und Inhalt (SH)“) und LP_0030059
(„Möglicher Inhalt (SH)“) als strukturgleiche Kandidaten mit ihrer editorialNote, stellt
mit `scripts/klasse.sh` fest, dass die Ontologie für sie keine Teile-Restriktion definiert,
und zeigt, woher jede Angabe stammt; kein Raten, keine lokale Datendatei als Quelle.

## Szenario 4 — Nachschlagen (Retrieval)

> Eine Lehrplantabelle hat zwei Spalten, „Kompetenzen“ und „Mögliche Inhalte“, mit mehreren
> Zeilen. Wie modelliere ich nach MEM, welche Inhalte zu welcher Kompetenz gehören? Nenne
> die Properties mit ID und woher die Angabe stammt.

Erfolgsmaß: Antwort sagt, dass Kompetenz und Mögliche Inhalte als Geschwister desselben
Bereichs über `hat Teil` (obo:BFO_0000051) hängen, die Zeilenordnung über `hat Position`
(LP_0000460) und — bei nummerierten Zeilen — über gleiche `hat Nummer` (LP_0030057) lesbar
bleibt, und Pattern 7 (CE-Verweis, `hat Verweis` LP_0030071 / `verweist auf` LP_0030072) nur
bei einem ausdrücklichen Querverweis der Vorlage greift; keine erfundene Property, jede
Quelle genannt (`references/arbeitsablauf.md`, `references/muster.md`,
`references/beispiel.ttl`). Dieses Szenario kam nach dem Gegenlesen von Task 7 dazu und hat
noch keinen Baseline-Lauf.
