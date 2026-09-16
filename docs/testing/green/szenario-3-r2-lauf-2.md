# Konkretion zu einem Kompetenzbereich (SH)

## Kurzantwort

Der übergeordnete Kompetenzbereich in Schleswig-Holstein ist **LP_0030070 „Kompetenzbereich
(SH)“** (`subClassOf` LP_0000349 „CE-Bereich“). Für die „Konkretion“ selbst — den Knoten, der
laut `references/arbeitsablauf.md` (Zeile 55) aus einer Tabellenspalte „Mögliche Inhalte“ oder
„Konkretionen“ entsteht — gibt es in SH **keine einzelne Klasse**, sondern mehrere
strukturgleiche Schwesterklassen, die sich nur durch `skos:editorialNote` (das Fach)
unterscheiden. Genau das ist die in `references/fallstricke.md` (Zeile 21/34) dokumentierte
Falle für dieses Szenario: Namensraten aus `references/laender/SH.md` allein reicht nicht.

Da die vorliegende Frage kein Fach nennt, kann keine einzelne ID als *die* richtige Antwort
behauptet werden — stattdessen die verifizierte Kandidatenliste mit Fach-Zuordnung.

## Struktur: wie eine „Konkretion“ in der Ontologie gebaut ist

Alle Kandidaten sind `owl:intersectionOf` aus:

- **LP_0002103 „Element (SH)“** (Curriculares Element mit `von Bundesland` → LP_3000054
  Schleswig-Holstein), und
- einer `owl:Restriction` auf **LP_0000483 „hat Funktion“** mit `owl:hasValue` entweder
  - **LP_0000480 „Lerninhaltsbeschreibungsfunktion“** — die Klasse spielt die Rolle von
    **LP_0000332 „CE-Lerninhalt“**, oder
  - **LP_0001014 „Hinweisbeschreibungsfunktion“** — die Klasse spielt die Rolle von
    **LP_0000852 „CE-Hinweis“**.

Quelle: `scripts/klasse.sh <ID>` gegen `references/lp-base.ttl`, für jede Kandidaten-ID einzeln
geprüft (siehe unten).

## Kandidaten mit Fachbezug (editorialNote), geprüft mit `scripts/klasse.sh`

Rolle **CE-Lerninhalt** (Lerninhaltsbeschreibungsfunktion):

| ID | Klasse | Fach (editorialNote) |
|---|---|---|
| LP_0030282 | Inhalt (SH) | Naturwissenschaften/Mathe Sek I & II: CE-Lerninhalt-Rolle; Englisch Sek I: CE-Hinweis-Rolle (doppelt belegt, beide Restriktionen stehen in derselben Intersection) |
| LP_0030254 | Thema und Inhalt (SH) | Mathe, Deutsch Sek I |
| LP_0030021 | Inhalt und Wissbestand (SH) | Deutsch Sek II |

Rolle **CE-Hinweis** (Hinweisbeschreibungsfunktion):

| ID | Klasse | Fach (editorialNote) |
|---|---|---|
| LP_0030059 | Möglicher Inhalt (SH) | Englisch Primar |
| LP_0030280 | Mögliches Thema und Inhalt (SH) | Sachunterricht |
| LP_0030281 | Mögliches Thema (SH) | Englisch Sek II |
| LP_0030079 | Mögliche Textsorte / Kommunikationssituation (SH) | Englisch Sek I |
| LP_0030276 | Beispielinhalt (SH) | Physik |
| LP_0030260 | Vorgabe und Hinweis (SH) | Mathe, Physik |
| LP_0030023 | Themenvorschlag (SH) | Deutsch Sek II |
| LP_0030022 | Konkretisierung – Hinweis und Vorschlag (SH) (`skos:altLabel` **„Konkretisierung (SH)“** — lexikalisch die einzige Klasse, deren Name „Konkretion“ direkt entspricht) | Deutsch; laut editorialNote entweder auf einen Bildungsstandard oder auf „Inhalt und Wissbestand“ bezogen, nicht direkt auf den Kompetenzbereich |

Keine dieser Klassen ist fachneutral — jede ist laut `editorialNote` für genau ein Fach/eine
Stufe angelegt. Ohne Fachangabe im Auftrag ist die Wahl nicht eindeutig zu treffen; laut
Konvention (`references/fallstricke.md` Zeile 21) müssten bei fehlendem Fachbezug alle
Kandidaten mit Note genannt und die Wahl im Kommentar des Turtle-Dokuments begründet werden.

## Was ein solcher Knoten laut Ontologie als Teile haben darf

Die SH-Klassen selbst tragen keine eigene `hat Teil`-Restriktion (nur die
Funktions-Restriktion oben); ihr erlaubter Inhalt ergibt sich aus der Rolle, die sie über
„hat Funktion“ übernehmen:

- **CE-Lerninhalt-Rolle** (z. B. LP_0030282 in Naturwissenschaften/Mathe, LP_0030254,
  LP_0030021): laut `rdfs:comment` von **LP_0000332 „CE-Lerninhalt“** darf ein solcher Knoten
  „einen anderen CE-Lerninhalt enthalten, aber kein anderes Element (wie z. B. CE-Bereich oder
  CE-Kompetenzspezifikation)“ — also über `obo:BFO_0000051` („hat Teil“) höchstens einen
  weiteren Knoten derselben CE-Lerninhalt-Rolle. `references/patterns/pattern6.ttl` (Pattern 6,
  in `references/muster.md` als Hierarchie-Muster referenziert) zeigt in der Praxis zusätzlich
  einen CE-Hinweis-Knoten als Teil eines CE-Lerninhalt-Knotens
  (`ex:CE-Lerninhalt_2 hat_Teil: ex:CE-Hinweis_1`).
- **CE-Hinweis-Rolle** (die meisten „Möglich…“-Klassen, s. o.): **LP_0000852 „CE-Hinweis“**
  trägt in `lp-base.ttl` nur eine `ist Teil von`-Restriktion (wovon er Teil sein darf: CE-Bereich
  LP_0000349, CE-Lerninhalt LP_0000332, CE-Kompetenzspezifikation LP_0000263) — keine eigene
  `hat Teil`-Restriktion. Die Ontologie definiert für ihn also keine erlaubten Unterknoten; er
  ist strukturell ein Blatt (ergänzender Hinweis-/Empfehlungstext).

Der übergeordnete Kompetenzbereich LP_0030070 selbst darf laut `rdfs:comment` von
LP_0000349 „CE-Bereich“ als Teile andere CE-Bereiche, CE-Kompetenzspezifikationen und/oder
CE-Lerninhalte zusammenfassen — die „Konkretion“-Klassen der CE-Lerninhalt-Rolle hängen also
direkt unter ihm.

## Quellen

- `references/laender/SH.md` — Klassenliste des Landes, editorialNotes
- `scripts/lookup.sh Kompetenzbereich` / `"Möglicher Inhalt"` — IDs und Notes gegenprüfen
- `scripts/klasse.sh <ID>` gegen `references/lp-base.ttl` — für LP_0030070, LP_0002103,
  LP_0030282, LP_0030059, LP_0030254, LP_0030280, LP_0030271, LP_0030278, LP_0030260,
  LP_0030256, LP_0030022, LP_0030021, LP_0030023, LP_0030281, LP_0030079, LP_0030276,
  LP_0000332 (CE-Lerninhalt), LP_0000852 (CE-Hinweis)
- `references/terms/lp-terms.tsv` — Kommentartexte zu LP_0000349, LP_0000332, LP_0002103,
  LP_0030070, LP_0030059, LP_0030254, LP_0030280, LP_0030282
- `references/arbeitsablauf.md` (Zeile ~53–57) — Herkunft des Begriffs „Konkretion“ als
  generischer Workflow-Begriff für Tabellenspalten
- `references/patterns/pattern6.ttl` und `references/muster.md` — Hierarchie-Muster (Pattern 6)
- `references/fallstricke.md` (Zeile 21, 34) — dokumentierte Verwechslungsgefahr in genau
  diesem Szenario (GREEN Szenario 3), zur Einordnung gelesen, aber nicht als Antwort
  übernommen — stattdessen jede genannte ID erneut mit `scripts/klasse.sh` verifiziert.
