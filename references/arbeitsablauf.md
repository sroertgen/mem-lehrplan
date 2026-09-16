# Arbeitsablauf

Die sechs Schritte aus `SKILL.md`, ausformuliert — plus der Weg vom PDF zur Struktur, der
dort keinen Platz hat.

## Die Schleife

1. **Lesen.** `references/muster.md`, `references/konventionen.md` und
   `references/laender/<XX>.md` des Landes lesen, bevor die erste Zeile Turtle entsteht.
   `references/beispiel.ttl` ist die Vorlage, die kopiert wird — nicht irgendeine andere
   Turtle-Datei, die im Dateisystem gefunden wird und geprüft oder produktiv aussieht. Ein
   lokal vorhandenes Dokument ist nicht dasselbe wie ein geprüftes.
2. **Nachschlagen.** Jede ID, die im Text vorkommt, mit `scripts/lookup.sh <Wort|ID>`
   bestätigen. Was eine Klasse an `hat Teil` enthalten darf oder muss, mit
   `scripts/klasse.sh <LP_ID>` nachsehen. Keine ID aus dem Gedächtnis oder aus einer
   fremden Datei übernehmen, auch wenn sie richtig aussieht — IDs sind opake Zahlen, aus
   der Zahlenfolge selbst ist nichts abzulesen.
3. **Schreiben.** Benannte Knoten mit IRI im eigenen Namensraum (`references/konventionen.md`);
   Titel, Beschreibung und Nummer als eigene Wertknoten mit `hat Wert` (LP_0000344), nie als
   Literal direkt am Element und nie als Blank Node; Jahrgangsstufen als Individuen
   (LP_2000001–13); die Gliederung über `hat Teil` (obo:BFO_0000051); die Geschwisterfolge
   über `hat Position` (LP_0000460).
4. **Prüfen.** `npx --registry=https://git.edufeed.org/api/packages/edufeed/npm/ mem-explorer check datei.ttl`
   ausführen. Exit 0 heißt: kein Fehler. Das ist kein Schritt am Ende, sondern nach jedem
   fertig geschriebenen Abschnitt — ein Fehler, der sofort auffällt, ist billiger als einer,
   der sich über dreißig Knoten fortpflanzt.
5. **Nachbessern.** Den Bericht gruppenweise abarbeiten, mit dem **Soll**-Block jeder Gruppe
   als Vorgabe (`references/befunde.md`). Gruppen mit „Reasoner-Artefakt“ bleiben unverändert
   — sie sind keine Datenfehler. IRIs werden dabei nie umbenannt.
6. **Wiederholen und übergeben.** Schritt 4 und 5, bis Exit 0. Dann Bericht und Datei dem
   Menschen für den Abgleich mit dem PDF geben: Texttreue und Vollständigkeit prüft das
   Werkzeug nicht, nur die Struktur gegen die Ontologie.

## Vom PDF zur Struktur

Ein Lehrplan-PDF wird nicht am Stück gelesen, sondern seitenweise — sonst geht die
Zuordnung von Text zu Seite verloren, die für den späteren menschlichen Abgleich und die
`# S. 12`-Kommentare gebraucht wird:

```bash
pdftotext -f 12 -l 13 -layout datei.pdf -
```

`-layout` erhält Spalten und Einrückung; `-f`/`-l` grenzen auf die Seiten ein, die gerade
bearbeitet werden. Für einen schnellen Blick auf eine einzelne Zeile reicht auch
`pdftotext -layout datei.pdf - | sed -n '12,13p'`.

Danach die Übersetzung von Layout in Struktur:

- **Überschriften der Gliederungsebenen** werden zu Fragment- und Bereichsknoten
  (`hat Teil`, Pattern 6); die Nummerierung der Überschrift (z. B. „1“, „2.1“) landet am
  Nummer-Knoten (`hat Nummer`, LP_0030057), nicht im Titeltext.
- **Tabellenspalten trennen Klassen.** Eine Spalte „Kompetenzen“ wird zu Knoten der
  Kompetenzspezifikations-Klasse des Landes; eine Spalte „Mögliche Inhalte“ oder
  „Konkretionen“ zu Knoten der Inhaltsklasse des Landes — das ist nicht zwingend ein
  CE-Lerninhalt (LP_0000332) im Sinn der Ontologie: in SH trägt `LP_0030280` „Mögliches
  Thema und Inhalt (SH)“ die Hinweisbeschreibungsfunktion (LP_0001014), nicht die
  Lerninhaltsbeschreibungsfunktion (LP_0000480) von CE-Lerninhalt. `scripts/klasse.sh <ID>`
  zeigt, welche Funktion eine Klasse trägt; welche Klasse im jeweiligen Land infrage kommt,
  steht in `references/laender/<XX>.md`. Strukturgleiche Schwesterklassen eines Landes
  unterscheidet nur die editorialNote (das Fach, für das sie angelegt wurde); passt keine
  Note zum Fach, alle Kandidaten mit Note nennen, eine wählen, die Wahl im Kommentar
  begründen und im ganzen Lehrplan einheitlich bleiben — siehe `references/muster.md` und
  `references/fallstricke.md`.
- **Eine Kompetenz mit „ihren“ möglichen Inhalten aus derselben Tabellenzeile verknüpfen**
  heißt nicht, ein Paar zu modellieren — dafür gibt es keine Property. MEM hängt Kompetenz
  und Mögliche Inhalte als Geschwister desselben Bereichs an `hat Teil` (obo:BFO_0000051):
  `references/beispiel.ttl` zeigt die Prozessbezogene Kompetenz und die Inhalte beide unter
  demselben Kompetenzbereich. Die Zeilenzugehörigkeit bleibt über `hat Position`
  (LP_0000460) und, wenn die Vorlage Zeilen nummeriert, über gleiche `hat Nummer`
  (LP_0030057) lesbar. Macht die Vorlage einen ausdrücklichen Querverweis, zeigt Pattern 7
  (CE-Verweis) den Mechanismus dafür: eine Kompetenzspezifikation trägt `hat Verweis`
  (LP_0030071) zu einem eigenen Verweis-Knoten, der mit `verweist auf` (LP_0030072) auf das
  Ziel zeigt — welche Zielklasse dabei erlaubt ist, bestimmt die länderspezifische
  Verweis-Klasse (`scripts/klasse.sh <ID>`).
- **Ein Knoten je Aufzählungspunkt** der Vorlage, kein Knoten je Satz und keiner, der
  mehrere Punkte zusammenfasst — sonst geht die Position (Schritt 3, `hat Position`)
  durcheinander und der Text ist nicht mehr wörtlich einem Punkt zuzuordnen.
- **Jahrgangsstufen aus der Tabellen- oder Abschnittsüberschrift** übernehmen (z. B.
  „Jahrgangsstufen 5–6“) und als mehrwertige Individuen schreiben (Pattern 5), nicht als
  Textspanne am Knoten.
- **Seitenzahl in den Kommentar** jedes Knotens, der von dieser Seite stammt — das ist die
  einzige Spur zurück zum Original, die im Turtle selbst steht.
- **Nach jedem Bereich prüfen** (Schritt 4), nicht erst nach der ganzen Datei.
