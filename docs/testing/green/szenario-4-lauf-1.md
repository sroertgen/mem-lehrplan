# Kompetenzen und Mögliche Inhalte aus einer Lehrplantabelle modellieren

## Kernaussage

Für eine Zuordnung „diese Kompetenz gehört zu diesen Inhalten“ gibt es **keine eigene
Property** — MEM modelliert das nicht als Paar. Beide Spalten werden zu Knoten
unterschiedlicher Klassen und hängen als **Geschwister desselben Kompetenzbereichs**
an `hat Teil` (`obo:BFO_0000051`). Die Zugehörigkeit zur selben Tabellenzeile bleibt nur
implizit über `hat Position` (LP_0000460) lesbar, bei nummerierten Zeilen zusätzlich über
gleiche `hat Nummer` (LP_0030057). Nur wenn die Vorlage selbst einen ausdrücklichen
Querverweis macht (z. B. „siehe Inhalt 2“), kommt Pattern 7 (CE-Verweis) zum Einsatz.

## Die Properties im Einzelnen

| Property/Verhältnis | ID | Woher |
|---|---|---|
| „Kompetenzen“-Spalte → Knoten der Kompetenzspezifikations-Klasse des Landes | Basisklasse **LP_0000263** (CE-Kompetenzspezifikation), im Land eine strukturgleiche Unterklasse, z. B. **LP_0030278** „Prozessbezogene Kompetenz (SH)“ | `references/fallstricke.md` Regel „Tabellenspalten trennen Klassen“; konkrete Landesklasse in `references/laender/<XX>.md`, per `scripts/lookup.sh` bzw. `scripts/klasse.sh` verifiziert |
| „Mögliche Inhalte“/„Konkretionen“-Spalte → Knoten der Lerninhalt-Klasse des Landes | Basisklasse **LP_0000332** (CE-Lerninhalt), im Land eine strukturgleiche Unterklasse, z. B. **LP_0030280** „Mögliches Thema und Inhalt (SH)“ | dieselbe Regel in `references/fallstricke.md`; Landesklasse aus `references/laender/<XX>.md` |
| Kompetenz und Inhalte als Geschwister an den Kompetenzbereich hängen | **`hat Teil`** = `obo:BFO_0000051` | `references/arbeitsablauf.md` Abschnitt „Eine Kompetenz mit ‚ihren‘ möglichen Inhalten … verknüpfen“; dasselbe Muster als Turtle-Block in `references/muster.md` (Pattern 6 „Hierarchie über hat Teil“) |
| Zeilenzugehörigkeit sichtbar halten | **`hat Position`** = **LP_0000460** (`rdfs:range xsd:int`, nicht `xsd:integer`) | `references/muster.md` Abschnitt „Reihenfolge mit hat Position“ |
| Bei nummerierten Zeilen zusätzlich gleiche Nummer an Kompetenz und Inhalt | **`hat Nummer`** = **LP_0030057** (ObjectProperty, `parent=LP_0000024`) | `references/muster.md` Pattern 2; ID verifiziert mit `scripts/lookup.sh "hat Nummer"` |
| Falls die Vorlage einen ausdrücklichen Querverweis macht (Pattern 7, CE-Verweis) | **`hat Verweis`** = **LP_0030071** (ObjectProperty, `parent=LP_0000024`), **`verweist auf`** = **LP_0030072** (ObjectProperty, `parent=obo:IAO_0000136`) | `references/muster.md` Pattern 7 „Verweise“; IDs verifiziert mit `scripts/lookup.sh "hat Verweis"` / `scripts/lookup.sh "verweist auf"`; auch in `references/arbeitsablauf.md` genannt |

## Konkretes Vorbild in `references/beispiel.ttl`

Der Kompetenzbereich „Die Frage nach Gott“ (S. 12) zeigt das Muster wörtlich:

```turtle
data:kb-gott a lp:LP_0030070 ;                     # Kompetenzbereich (SH)
    obo:BFO_0000051 data:kb-gott-pk-1 ,             # Prozessbezogene Kompetenz
                     data:kb-gott-inhalt-1 ,        # Mögliches Thema und Inhalt 1
                     data:kb-gott-inhalt-2 .        # Mögliches Thema und Inhalt 2

data:kb-gott-pk-1 a lp:LP_0030278 ;                 # Prozessbezogene Kompetenz (SH)
    lp:LP_0000460 "1"^^xsd:int ; …                  # hat Position

data:kb-gott-inhalt-1 a lp:LP_0030280 ;             # Mögliches Thema und Inhalt (SH)
    lp:LP_0000460 "2"^^xsd:int ; …                  # hat Position
```

Kompetenz und beide Inhalte hängen als gleichrangige Geschwister unter demselben
Kompetenzbereich-Knoten (`data:kb-gott`) an `obo:BFO_0000051` — nicht die Kompetenz zeigt
auf den Inhalt oder umgekehrt.

## Wichtiger Fallstrick

Strukturgleiche Landesklassen wie LP_0030278/LP_0030280 unterscheidet **nur die
`editorialNote`** (welches Fach die Klasse trägt), nie der Name — mehrere Klassen im
selben Land tragen „Inhalt“ im Namen. Das steht so in `references/fallstricke.md`
(Regel „Strukturgleiche Schwesterklassen … per editorialNote unterscheiden“) und wird
dort mit einem dokumentierten Fehllauf belegt (GREEN Szenario 3, Lauf 1 wählte fälschlich
LP_0030059 „Möglicher Inhalt (SH)“, editorialNote „Englisch Primar“, statt LP_0030280).
Die passende Landesklasse ist also immer über `scripts/lookup.sh`/`scripts/klasse.sh`
und `references/laender/<XX>.md` zu bestätigen, nicht aus dem Namen zu raten.

## Genutzte Quellen

- `SKILL.md` — Ablaufvorgabe (Schritt 1–4)
- `references/muster.md` — Pattern 2 (Titel/Beschreibung/Nummer), Pattern 5 (Jahrgangsstufe),
  Pattern 6 (Hierarchie über hat Teil), Pattern 7 (Verweise)
- `references/arbeitsablauf.md` — Abschnitt zu Tabellenspalten und Zeilenverknüpfung
- `references/fallstricke.md` — Regel „Tabellenspalten trennen Klassen“ und Regel zu
  editorialNote-Disambiguierung samt dokumentiertem Fehllauf
- `references/beispiel.ttl` — Kompetenzbereich „Die Frage nach Gott“ (S. 12–13) als
  geprüftes Vorbild (`mem-explorer check` läuft dort mit Exit 0)
- `scripts/lookup.sh` — IDs verifiziert: „hat Position“ → LP_0000460, „hat Nummer“ →
  LP_0030057, „hat Verweis“ → LP_0030071, „verweist auf“ → LP_0030072,
  „Kompetenzspezifikation“ → LP_0000263, „Lerninhalt“ → LP_0000332 (`hat Teil` selbst
  liegt außerhalb des lp-Namensraums als `obo:BFO_0000051` und ist nur in
  `references/muster.md` als IRI dokumentiert, nicht über `lookup.sh` auffindbar)
