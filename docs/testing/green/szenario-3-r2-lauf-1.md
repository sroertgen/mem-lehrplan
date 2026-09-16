# Konkretion (möglicher Inhalt zu einem Kompetenzbereich) — Schleswig-Holstein

## Kurzantwort

Die vorgesehene Klasse ist **`LP_0030059` „Möglicher Inhalt (SH)“**
(`https://w3id.org/lehrplan/ontology/LP_0030059`).

Sie hat laut Ontologie **keine** definierten Teile: es gibt keine `owl:Restriction` auf
`obo:BFO_0000051` (`hat Teil`) in ihrer Definition. Der Knoten ist strukturell ein
Blattelement der Gliederungskette.

## Herleitung

### 1. Klasse gesucht

`scripts/lookup.sh "möglicher inhalt"` liefert für Schleswig-Holstein genau einen Treffer:

```
LP_0030059 · Class · Möglicher Inhalt (SH) ·  · parent= · note=Englisch Primar  (lp)
```

Das ist der wörtlichste Treffer zur Formulierung „einen möglichen Inhalt zu einem
Kompetenzbereich“. `references/laender/SH.md` bestätigt den Eintrag in der Tabelle der
37 Landesklassen, unter der Rubrik „Oberklasse ist ein anonymer OWL-Ausdruck“ (mit
`editorialNote` „Englisch Primar“).

**Wichtig:** SH hat keine einzige fachübergreifende „Konkretion“-Klasse. Es gibt mehrere
strukturgleiche Schwesterklassen — je Fach eine eigene ID, nur durch die
`skos:editorialNote` unterscheidbar (SKILL-Rotflagge: „Zwei Klassen heißen fast gleich —
die editorialNote entscheidet, nicht der Name“):

| ID | Klasse | Fach (editorialNote) |
|---|---|---|
| LP_0030059 | Möglicher Inhalt (SH) | Englisch Primar |
| LP_0030079 | Mögliche Textsorte / Kommunikationssituation (SH) | Englisch Sek I |
| LP_0030281 | Mögliches Thema (SH) | Englisch Sek II |
| LP_0030280 | Mögliches Thema und Inhalt (SH) | Sachunterricht |
| LP_0030276 | Beispielinhalt (SH) | Physik |

Alle fünf sind über `scripts/klasse.sh <ID>` gegen dasselbe Muster geprüft: Unterklasse von
`LP_0002103` „Element (SH)“ (= Curriculares Element, `von Bundesland` = SH) mit
`hat Funktion` (`LP_0000483`) → `hasValue` `LP_0001014` „Hinweisbeschreibungsfunktion“.
Damit entsprechen sie strukturell dem Muster von **CE-Hinweis** (`LP_0000852`), nicht von
CE-Lerninhalt (`LP_0000332`, `hasValue` `LP_0000480` „Lerninhaltsbeschreibungsfunktion“) —
obwohl der Name „Inhalt“ trägt. Das passt inhaltlich: „möglich“/„Vorschlag“ ist laut
`rdfs:comment` von CE-Hinweis genau dessen Charakter („Der CE-Hinweis hat einen
Empfehlungscharakter“), während CE-Lerninhalt den verbindlichen Lehrinhalt beschreibt.

Der zugehörige Kompetenzbereich ist `LP_0030070` „Kompetenzbereich (SH)“ — die einzige
Klasse der SH-Tabelle unter „unter CE-Bereich (LP_0000349)“ ohne Fach-Einschränkung in der
`editorialNote`, also die generische Bereichsklasse, der die „Möglicher Inhalt“-Knoten
zugeordnet werden.

### 2. Erlaubte Teile

`scripts/klasse.sh LP_0030059` gibt den vollständigen Definitionsblock aus `lp-base.ttl`
zurück:

```
LP_0030059 „Möglicher Inhalt (SH)“ rdf:type owl:Class ;
    rdfs:subClassOf [ owl:intersectionOf ( LP_0002103 „Element (SH)“
                                           [ rdf:type owl:Restriction ;
                                             owl:onProperty LP_0000483 „hat Funktion“ ;
                                             owl:hasValue LP_0001014 „Hinweisbeschreibungsfunktion“
                                           ]
                                         ) ;
                      rdf:type owl:Class
                    ] ;
    rdfs:label "Möglicher Inhalt (SH)"@de ;
    skos:editorialNote "Englisch Primar" .
```

Es taucht **kein** `owl:Restriction`-Block mit `owl:onProperty obo:BFO_0000051`
(„hat Teil“) auf — weder in diesem Block noch (per `grep -n "BFO_0000051"
references/lp-base.ttl`) irgendwo sonst mit dieser oder einer der vier Schwesterklassen als
Kontext. Solche `hat Teil`-Restriktionen kommen im Datensatz nur bei den obersten
Strukturebenen vor (z. B. `LP_0000824` „Fachanforderung (SH)“, die Lehrplanwurzel für SH),
nicht bei den CE-Hinweis-artigen Inhaltsklassen.

`references/muster.md`, Abschnitt „Hierarchie über hat Teil“ (Pattern 6), zeigt am
Beispiel dieselbe Struktur informell:

```turtle
ex:CE-Bereich_2 hat_Teil: ex:CE-Lerninhalt_1, ex:CE-Kompetenzspezifikation_1 .
ex:CE-Lerninhalt_1 hat_Teil: ex:CE-Lerninhalt_2 .
ex:CE-Lerninhalt_2 hat_Teil: ex:CE-Hinweis_1 .
ex:CE-Kompetenzspezifikation_1 hat_Teil: ex:CE-Hinweis_2 .
```

CE-Hinweis steht dort am Ende jeder Kette — nie als Quelle einer eigenen `hat_Teil`-Kante.
Damit ist der Befund konsistent: **„Möglicher Inhalt (SH)“ (und seine vier
Schwesterklassen) sind laut Ontologie Blattknoten; ihnen ist keine erlaubte oder
vorgeschriebene Teile-Menge zugewiesen.** Was sie selbst enthalten dürfen, ist also nicht
„nichts Bestimmtes, aber irgendetwas“, sondern schlicht nicht definiert — es gibt keine
Vorgabe, die ein solcher Knoten laut Ontologie erfüllen müsste oder dürfte.

## Verwendete Quellen

- `scripts/lookup.sh` (Suche „möglicher inhalt“, „inhalt“, „konkretion“, ID-Nachschlag
  `LP_0001014`)
- `scripts/klasse.sh LP_0030059`, `LP_0030070`, `LP_0030079`, `LP_0030280`, `LP_0030281`,
  `LP_0030276`, `LP_0000332`, `LP_0000852`, `LP_0000349`, `LP_0000261`, `LP_0002103`,
  `LP_0030022` (Kontrollkandidat „Konkretisierung (SH)“, verworfen — editorialNote bezieht
  sich auf Bildungsstandard/Inhalt-und-Wissbestand, nicht auf Kompetenzbereich)
- `references/laender/SH.md` (Klassentabelle des Landes, 37 Klassen)
- `references/muster.md` (Pattern 6 „Hierarchie über hat Teil“)
- `references/arbeitsablauf.md` (Zeile zu „Mögliche Inhalte“/„Konkretionen“ als
  Tabellenspalten)
- `references/lp-base.ttl` (`grep -n "BFO_0000051"` zur Bestätigung, dass keine
  `hat Teil`-Restriktion bei den betroffenen Klassen steht)
