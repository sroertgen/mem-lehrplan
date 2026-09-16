# Zwei-Spalten-Tabelle „Kompetenzen“ / „Mögliche Inhalte“ nach MEM modellieren

## Kernaussage

MEM kennt **keine eigene Property, die eine Kompetenz mit „ihren“ möglichen Inhalten aus
derselben Tabellenzeile verknüpft**. Die Zeilenpaarung aus der Vorlage wird nicht als Paar
modelliert, sondern beide Spaltentypen hängen als **Geschwister** unter demselben
Kompetenzbereich an `hat Teil`. Die Zeilenzugehörigkeit bleibt implizit — lesbar über
gleiche `hat Position` bzw., wenn die Vorlage nummeriert, gleiche `hat Nummer`.

Quelle: `references/arbeitsablauf.md`, Abschnitt „Vom PDF zur Struktur“:

> „Eine Kompetenz mit ‚ihren‘ möglichen Inhalten aus derselben Tabellenzeile verknüpfen“
> heißt nicht, ein Paar zu modellieren — dafür gibt es keine Property. MEM hängt Kompetenz
> und Mögliche Inhalte als Geschwister desselben Bereichs an `hat Teil`
> (obo:BFO_0000051): `references/beispiel.ttl` zeigt die Prozessbezogene Kompetenz und die
> Inhalte beide unter demselben Kompetenzbereich. Die Zeilenzugehörigkeit bleibt über `hat
> Position` (LP_0000460) und, wenn die Vorlage Zeilen nummeriert, über gleiche `hat
> Nummer` (LP_0030057) lesbar.

## Die Properties, mit ID und Herkunft

| Property / Knotenart | ID | Woher |
|---|---|---|
| **hat Teil** (Hierarchie: Bereich → Kompetenz, Bereich → Inhalt) | `obo:BFO_0000051` (external, OBO-Namespace) | `references/muster.md`, Pattern 6 „Hierarchie über hat Teil“; bestätigt in `references/beispiel.ttl` (Zeile mit `obo:BFO_0000051 „hat Teil“ ist in lp-base.ttl als owl:ObjectProperty definiert (Zeile 110)“); nicht über `scripts/lookup.sh`, da kein `lp:`-Term (`lookup.sh "BFO_0000051"` → „kein Treffer“, geprüft) |
| **hat Position** (Reihenfolge / implizite Zeilenzugehörigkeit) | `LP_0000460` | `scripts/lookup.sh "hat Position"` → `LP_0000460 · DatatypeProperty · hat Position`; Pattern „Reihenfolge mit hat Position“ in `references/muster.md`: `rdfs:range xsd:int`, also `"n"^^xsd:int`, nicht `xsd:integer` |
| **hat Nummer** (Zeilenzugehörigkeit, wenn die Vorlage die Zeilen nummeriert) | `LP_0030057` | `scripts/lookup.sh "hat Nummer"` → `LP_0030057 · ObjectProperty · hat Nummer · has number · parent=LP_0000024`; führt zu einem eigenen Nummer-Wertknoten der Klasse „Identifikationsnummer“ `LP_0000347`, nicht zum Literal direkt |
| **Klasse für die Spalte „Kompetenzen“** (länderspezifisch) | z. B. `LP_0000263` CE-Kompetenzspezifikation als Basisklasse, in Schleswig-Holstein konkret `LP_0030278` „Prozessbezogene Kompetenz (SH)“ | `scripts/klasse.sh LP_0000263`: Definition/Comment „A CE-Kompetenzspezifikation is a Curriculares Element that describes a competence …“; welche Landesklasse konkret gilt, steht in `references/laender/<XX>.md` (`references/arbeitsablauf.md`: „Welche Klasse das im jeweiligen Land ist, steht in references/laender/<XX>.md“) |
| **Klasse für die Spalte „Mögliche Inhalte“** (länderspezifisch) | z. B. `LP_0000332` CE-Lerninhalt als Basisklasse, in Schleswig-Holstein konkret `LP_0030280` „Mögliches Thema und Inhalt (SH)“ | `scripts/klasse.sh LP_0000332`: Definition/Comment „A CE-Lerninhalt is a curricular element that describes a learning content …“; ebenfalls über `references/laender/<XX>.md` bestimmt — **Vorsicht:** mehrere Klassen tragen „Inhalt“ im Namen, strukturgleiche Schwesterklassen eines Landes unterscheidet nur die `editorialNote`, nie der Name (`references/fallstricke.md`, Fallbeispiel GREEN Szenario 3) |
| **hat Verweis / verweist auf** (nur bei explizitem Querverweis der Vorlage, kein Ersatz für die Zeilenpaarung) | `LP_0030071` / `LP_0030072` | Pattern 7 „Verweise“ in `references/muster.md`; `references/arbeitsablauf.md`: „Macht die Vorlage einen ausdrücklichen Querverweis, zeigt Pattern 7 (CE-Verweis) den Mechanismus dafür“ |

## Konkretes Beispiel (Schleswig-Holstein, geprüft mit `mem-explorer check`, Exit 0)

Aus `references/beispiel.ttl`:

```turtle
data:kb-gott
    a lp:LP_0030070 ;                               # Kompetenzbereich (SH)
    lp:LP_0000460 "1"^^xsd:int ;
    obo:BFO_0000051 data:kb-gott-pk-1 , data:kb-gott-inhalt-1 , data:kb-gott-inhalt-2 .

data:kb-gott-pk-1
    a lp:LP_0030278 ;                               # Prozessbezogene Kompetenz (SH)
    lp:LP_0000460 "1"^^xsd:int .                    # hat Position

data:kb-gott-inhalt-1
    a lp:LP_0030280 ;                               # Mögliches Thema und Inhalt (SH)
    lp:LP_0000460 "2"^^xsd:int .                    # hat Position

data:kb-gott-inhalt-2
    a lp:LP_0030280 ;
    lp:LP_0000460 "3"^^xsd:int .
```

Kompetenz und Inhalte hängen alle über `hat Teil` (`obo:BFO_0000051`) unter demselben
Kompetenzbereich `data:kb-gott` — nicht als Paar, sondern als Geschwister. Welche Inhalte
„zu“ welcher Kompetenz gehören, bleibt implizit über die gemeinsame Tabellenzeile/den
gemeinsamen Bereich und über `hat Position`/`hat Nummer` lesbar, nicht über eine eigene
Kante.

## Ontologische Begründung (warum keine direkte Property existiert)

`scripts/klasse.sh LP_0000263` (CE-Kompetenzspezifikation) und
`scripts/klasse.sh LP_0000332` (CE-Lerninhalt) zeigen: beide Klassen sind über
`owl:Restriction` auf `obo:BFO_0000050` („ist Teil von“, die Inverse zu `hat Teil`) auf
„Teil eines CE-Bereichs“ (bzw. beim Lerninhalt zusätzlich „Teil eines anderen
CE-Lerninhalts“) beschränkt — keine der beiden Klassendefinitionen sieht eine Kante
zwischen einer Kompetenzspezifikation und einem Lerninhalt vor. Der `rdfs:comment` beider
Klassen (identischer Beispielblock) bestätigt das Muster ausdrücklich:

> „CE-Kompetenzspezifikation: Die Schülerinnen und Schüler setzen sich … auseinander.
> CE-Lerninhalt: Kanada: Einblicke in Geographie und Gesellschaft; Inuit/First People“

— zwei nebeneinanderstehende, aber nicht durch eine Property verbundene Elemente.

## Rote Flagge aus `references/fallstricke.md`

Bei der Wahl der länderspezifischen Inhalt-Klasse hilft der Name allein nicht: GREEN
Szenario 3 zeigt, dass in Schleswig-Holstein sowohl `LP_0030059` „Möglicher Inhalt (SH)“
(editorialNote „Englisch Primar“) als auch `LP_0030280` „Mögliches Thema und Inhalt (SH)“
(editorialNote „Sachunterricht“) existieren — strukturgleich, aber fachspezifisch. Nur die
`editorialNote` aus `scripts/lookup.sh`/`references/laender/<XX>.md` entscheidet, nicht der
Klassenname.
