# Konkretion in Schleswig-Holstein — zuständige Klasse

## Klasse

`lp:LP_0030280` — Label „Mögliches Thema und Inhalt (SH)“ (`skos:editorialNote`: „Sachunterricht“).

Definition in `lp-base.ttl`:

```turtle
ontology:LP_0030280 rdf:type owl:Class ;
    rdfs:subClassOf [ owl:intersectionOf ( ontology:LP_0002103
                                            [ owl:onProperty ontology:LP_0000483 ;
                                              owl:hasValue ontology:LP_0001014 ] ) ] ;
    rdfs:label "Mögliches Thema und Inhalt (SH)"@de .
```

`LP_0030280` ist also die Schnittmenge aus `LP_0002103` („Element (SH)“, dem
SH-spezifischen `LP_0000261`/„Curriculares Element“) und der Bedingung, dass
`LP_0000483` („hat Funktion“) den Wert `LP_0001014` („Hinweisbeschreibungsfunktion“)
trägt.

Dass `LP_0030280` tatsächlich die „Konkretion" ist, zeigt der reale
Datenbestand: `Kompetenzbereich (SH)` = `LP_0030070` hat über
`obo:BFO_0000051` (has part) Knoten des Typs `LP_0030280` als Teile, die im
Label „Mögliche Konkretionen (Jahrgangsstufe …)“ heißen; diese Container-Knoten
haben wiederum einzelne Sachinhalte (ebenfalls `LP_0030280`) als Teile, z. B.
„Gottesvorstellungen (anthropomorph, symbolisch, allmächtig, gütig)“. Belegt in
`~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl`
und in der mem-explorer-Testfixture `tests/fixtures/sekundarstufe.ttl`.

## Was ein solcher Knoten als Teile haben darf

**Die Ontologie schränkt das nicht ein.** `LP_0030280` selbst trägt keine
`obo:BFO_0000051`-Restriktion, und da sein Obertyp nur der anonyme
OWL-Ausdruck oben ist (keine benannte Oberklasse außer `LP_0002103`), gibt es
auch dort und in `LP_0000261` („Curriculares Element“, IAO_0000030) keine
has-part-Beschränkung, die vererbt würde. Weder eine `rdfs:range`-Angabe für
`LP_0000483`/`BFO_0000051` in diesem Zweig noch eine SHACL-Shape für
`LP_0030280` existiert — im generierten `shapes.ttl` des mem-explorer taucht
`LP_0030280` an keiner Stelle als Shape-Target auf.

Das ist genau einer der zwei in `CLAUDE.md` des mem-explorer-Projekts
dokumentierten blinden Flecken: `LP_0030278` und `LP_0030280` (die
SH-Länderklassen) haben keine benannte Oberklasse, nur einen anonymen
OWL-Ausdruck — `rdfs:subClassOf*` endet dort im Blank Node, keine Shape greift.

In der Praxis (Konvention, nicht Ontologie-Zwang) sind die Teile eines
`LP_0030280`-Knotens wieder `LP_0030280`-Knoten selbst: ein Container-Knoten
„Mögliche Konkretionen (Jahrgangsstufe X)“ hat als Teile einzelne
Konkretions-Einträge desselben Typs `LP_0030280`.

## Beteiligte IDs im Überblick

| ID | Bedeutung |
|---|---|
| `LP_0030280` | Mögliches Thema und Inhalt (SH) — die „Konkretion“ |
| `LP_0030070` | Kompetenzbereich (SH) — hat `LP_0030280`-Knoten als Teile |
| `LP_0002103` | Element (SH) — SH-spezifisches Curriculares Element, Obertyp von `LP_0030280` |
| `LP_0000261` | Curriculares Element — allgemeine Oberklasse (IAO_0000030) |
| `LP_0000483` | hat Funktion (ObjectProperty) |
| `LP_0001014` | Hinweisbeschreibungsfunktion (Individual) |
| `obo:BFO_0000051` | has part — trägt die Lehrplan-Hierarchie, auch zwischen `LP_0030070` und `LP_0030280` bzw. zwischen `LP_0030280`-Knoten untereinander |

---

Die Angaben stammen aus dem gespiegelten Ontologie-Original
`~/coding/mem-knowledge-base/vendor/lehrplan-ontologie/lp-base.ttl` (Klassendefinitionen,
Restriktionen) sowie der kuratierten Referenz `~/coding/mem-knowledge-base/MEM.md` und den
generierten Artefakten `src/lib/ontology/generated/{terms.json,shapes.ttl}` im
mem-explorer-Repo. Dass `LP_0030280` konkret für „Konkretion“ zu einem Kompetenzbereich
steht, habe ich zusätzlich an echten Nutzdaten verifiziert
(`~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl`
und die mem-explorer-Testfixture), und die fehlende Teile-Beschränkung deckt sich mit dem
dokumentierten blinden Fleck in `mem-explorer/CLAUDE.md`.
