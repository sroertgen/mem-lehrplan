# Zwei Tabellenspalten „Kompetenzen“ / „Mögliche Inhalte“ nach MEM modellieren

## Kernaussage

Für die Zuordnung „welche Inhalte gehören zu welcher Kompetenz“ gibt es **keine eigene
Property, die die beiden verknüpft**. MEM hängt beide Spalten als **Geschwister** desselben
Kompetenzbereichs (CE-Bereich) an `hat Teil` (`obo:BFO_0000051`) — die Zeilenzugehörigkeit
bleibt nur über die Reihenfolge lesbar, nicht über eine semantische Kante zwischen Kompetenz
und Inhalt.

Quelle: `references/arbeitsablauf.md`, Abschnitt „Tabellenspalten trennen Klassen“ /
„Eine Kompetenz mit ‚ihren‘ möglichen Inhalten aus derselben Tabellenzeile verknüpfen“
(`/home/laoc/coding/comenius/mem-lehrplan/.worktrees/skill/references/arbeitsablauf.md`,
Zeilen 53–75):

> „Eine Kompetenz mit ‚ihren‘ möglichen Inhalten aus derselben Tabellenzeile verknüpfen
> heißt nicht, ein Paar zu modellieren — dafür gibt es keine Property. MEM hängt Kompetenz
> und Mögliche Inhalte als Geschwister desselben Bereichs an `hat Teil`
> (`obo:BFO_0000051`) […]. Die Zeilenzugehörigkeit bleibt über `hat Position`
> (LP_0000460) und, wenn die Vorlage Zeilen nummeriert, über gleiche `hat Nummer`
> (LP_0030057) lesbar.“

## Die Struktur im Detail

```
Kompetenzbereich (CE-Bereich)
 ├─ hat Teil → Kompetenz-Knoten (Spalte „Kompetenzen“)
 ├─ hat Teil → Inhalt-Knoten 1 (Spalte „Mögliche Inhalte“, Zeile 1)
 └─ hat Teil → Inhalt-Knoten 2 (Spalte „Mögliche Inhalte“, Zeile 2)
```

Beide Spalten hängen als Kinder desselben Bereichsknotens unter `hat Teil`
(`obo:BFO_0000051`, Pattern 6 „Hierarchie der curricularen Elemente“ in
`references/muster.md`). Innerhalb der Zeile bleibt die Reihenfolge/Zuordnung über
`hat Position` (LP_0000460, `xsd:int`) erhalten; nummeriert die Vorlage die Zeilen selbst
(z. B. „1a“/„1b“), wird zusätzlich an beiden Knoten dieselbe `hat Nummer`-ID (LP_0030057)
vergeben.

Das ist auch der technische Grund, warum eine direkte Verschachtelung „Inhalt hängt an
Kompetenz“ falsch wäre: Nach der Klassendefinition von CE-Lerninhalt (LP_0000332) in
`references/lp-base.ttl` darf ein CE-Lerninhalt nur „ist Teil von“ (`obo:BFO_0000050`)
einem **CE-Lerninhalt oder CE-Bereich** sein — eine CE-Kompetenzspezifikation ist als
Elternteil nicht erlaubt:

```
owl:onProperty obo:BFO_0000050 „ist Teil von“ ;
owl:someValuesFrom [ owl:unionOf ( LP_0000332 „CE-Lerninhalt“ LP_0000349 „CE-Bereich“ ) ]
```

Quelle: `scripts/klasse.sh LP_0000332` gegen
`references/lp-base.ttl`.

Macht die Vorlage einen **ausdrücklichen** Querverweis (nicht bloß „gleiche Zeile“, sondern
im Text markiert), gibt es dafür Pattern 7 (CE-Verweis): die Kompetenzspezifikation trägt
`hat Verweis` (LP_0030071) zu einem eigenen Verweis-Knoten, der mit `verweist auf`
(LP_0030072) auf das Ziel zeigt. Welche länderspezifische Verweis-Klasse dabei erlaubt ist,
zeigt `scripts/klasse.sh <ID>`. Für die reine Tabellenzeilen-Zuordnung ist das aber der
Ausnahmefall, nicht der Normalfall.

## Die Properties mit ID

| Property/Klasse | ID | Rolle |
|---|---|---|
| hat Teil | `obo:BFO_0000051` | hängt Kompetenz- und Inhalt-Knoten als Geschwister unter denselben Kompetenzbereich |
| hat Position | `LP_0000460` | hält die Zeilenreihenfolge fest (`xsd:int`, nicht `xsd:integer`) |
| hat Nummer | `LP_0030057` | optional, nur wenn die Vorlage Zeilen selbst nummeriert — gleiche Nummer an Kompetenz- und Inhalt-Knoten derselben Zeile |
| hat Verweis / verweist auf | `LP_0030071` / `LP_0030072` | nur bei einem ausdrücklichen Querverweis im Text (Pattern 7), nicht für die bloße Zeilenzuordnung |
| CE-Kompetenzspezifikation (Ontologie-Klasse) | `LP_0000263` | allgemeine Klasse für die Spalte „Kompetenzen“; im jeweiligen Land meist eine spezifischere Unterklasse |
| CE-Lerninhalt (Ontologie-Klasse) | `LP_0000332` | allgemeine Klasse für die Spalte „Mögliche Inhalte“; im jeweiligen Land meist eine spezifischere Unterklasse |

**Welche konkrete Klasse pro Land**, statt der allgemeinen `LP_0000263`/`LP_0000332`, hängt
vom Bundesland und Fach ab und steht in `references/laender/<XX>.md`; `scripts/klasse.sh
<ID>` zeigt, welche Funktion (`hat Funktion`, LP_0000483) eine Klasse laut Ontologie trägt.
Beispiel Schleswig-Holstein, Religion (`references/beispiel.ttl`, Abschnitt „Kompetenzbereich
Gott“, ab Zeile 67):

- Spalte „Kompetenzen“ → `LP_0030278` „Prozessbezogene Kompetenz (SH)“ (trägt laut
  `klasse.sh` `hat Funktion` → `LP_0000479` „Kompetenzbeschreibungsfunktion“ und →
  `LP_0000500` „Prozessbezugsfunktion“)
- Spalte „Mögliche Inhalte“ → `LP_0030280` „Mögliches Thema und Inhalt (SH)“ (trägt
  `hat Funktion` → `LP_0001014` „Hinweisbeschreibungsfunktion“ — **nicht** die
  Lerninhaltsbeschreibungsfunktion `LP_0000480` von CE-Lerninhalt; `LP_0030280` ist also
  keine echte CE-Lerninhalt-Unterklasse, sondern eine CE-Hinweis-artige SH-Klasse)
- beide hängen mit `hat Teil` unter demselben Kompetenzbereich-Knoten (`LP_0030070`
  „Kompetenzbereich (SH)“, in der Datei `data:kb-gott`)
- jeder Knoten trägt `hat Position` (`LP_0000460`): Kompetenz „1“, Inhalt 1 „2“, Inhalt 2
  „3“ — die fortlaufende Zählung über beide Spalten hinweg bewahrt die Zeilen-/
  Lesereihenfolge aus der Vorlage.

Achtung, kein Namensraten: `LP_0030059` „Möglicher Inhalt (SH)“ sieht identisch strukturiert
aus, trägt aber laut `editorialNote` (Spalte 7 der Termtabelle) „Englisch Primar“ — für
andere Fächer/Themenbereiche in SH ist das die falsche Klasse. Die editorialNote entscheidet,
nicht der Name (`scripts/lookup.sh "Möglicher Inhalt"`).

## Quellen (Skripte/Dateien)

- `SKILL.md` — Ablauf (Schritte 1–3) und Schnellreferenz
- `references/arbeitsablauf.md` (Zeilen 53–75) — die eigentliche Antwort: Tabellenspalten →
  Klassen, keine Paar-Property, `hat Teil`/`hat Position`/`hat Nummer`, Pattern-7-Ausnahme
- `references/muster.md` — Pattern 6 (Hierarchie über `hat Teil`), Pattern 7 (CE-Verweis),
  Abschnitt „Reihenfolge mit `hat Position`“
- `references/beispiel.ttl` (Zeilen 67–114) — reales Beispiel Kompetenzbereich „Die Frage
  nach Gott“ mit Prozessbezogener Kompetenz und zwei Inhalten als Geschwister
- `scripts/lookup.sh Inhalt` / `scripts/lookup.sh Kompetenz` — Kandidatenliste mit IDs,
  Land-Kürzeln und `editorialNote`
- `scripts/klasse.sh LP_0000263` / `LP_0000332` / `LP_0030278` / `LP_0030280` gegen
  `references/lp-base.ttl` — Restriktionen (`ist Teil von`, `hat Funktion`) der beteiligten
  Klassen
