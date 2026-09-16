# Konkretion in Schleswig-Holstein — zuständige Klasse und ihre Teile

## Kurzantwort

Die Klasse ist **`lp:LP_0030280`** — „Mögliches Thema und Inhalt (SH)“. Für ihre Teile
(`obo:BFO_0000051`, hat Teil) definiert die Ontologie **keine** Einschränkung — weder als
OWL-Restriktion an der Klasse selbst noch als SHACL-Shape.

## Wie die Klasse identifiziert wurde

`references/laender/SH.md` listet für SH 37 Klassen; mehrere tragen „Inhalt“ im Namen
(u. a. `LP_0030059` „Möglicher Inhalt (SH)“, `LP_0030282` „Inhalt (SH)“, `LP_0030280`
„Mögliches Thema und Inhalt (SH)“). Der Name allein reicht nicht, um zu entscheiden,
welche davon in der Praxis für „Konkretion“ steht — dafür wurden die echten SH-Nutzdaten
geprüft:

```
/home/laoc/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl
```

Dort tragen sowohl die Container-Knoten (Label „Mögliche Konkretionen (Jahrgangsstufe
5-6)“ usw.) als auch die einzelnen Stichpunkte darunter durchgängig
`rdf:type lp:LP_0030280`, z. B.:

```turtle
data:si-kb1-inhalt56
    rdf:type lp:LP_0030280 ; rdfs:label "Mögliche Konkretionen (Jahrgangsstufe 5-6)" ;
    lp:LP_0000026 lp:LP_2000005 , lp:LP_2000006 ;
    obo:BFO_0000051 data:si-kb1-56-001, data:si-kb1-56-002, … .

data:si-kb1-56-001 rdf:type lp:LP_0030280 ; rdfs:label "Gottesvorstellungen (…)" .
```

Diese Konkretionsknoten hängen (laut Datei) über `obo:BFO_0000051` an
Kompetenzbereich-Knoten, was genau der Frage entspricht: eine „Konkretion“ ist ein
möglicher Inhalt zu einem Kompetenzbereich.

`scripts/lookup.sh LP_0030280` bestätigt Klasse und Label:

```
LP_0030280 · Class · Mögliches Thema und Inhalt (SH) ·  · parent=  (lp)
```

## Definition der Klasse laut Ontologie

`scripts/klasse.sh LP_0030280` liefert den vollständigen Definitionsblock aus
`references/lp-base.ttl`:

```turtle
LP_0030280 „Mögliches Thema und Inhalt (SH)“ rdf:type owl:Class ;
                    rdfs:subClassOf [ owl:intersectionOf ( LP_0002103 „Element (SH)“
                                                           [ rdf:type owl:Restriction ;
                                                             owl:onProperty LP_0000483 „hat Funktion“ ;
                                                             owl:hasValue LP_0001014 „Hinweisbeschreibungsfunktion“
                                                           ]
                                                         ) ;
                                      rdf:type owl:Class
                                    ] ;
                    rdfs:label "Mögliches Thema und Inhalt (SH)"@de ;
                    skos:editorialNote "Sachunterricht" .
```

`LP_0030280` hat **keine benannte Oberklasse** — nur eine anonyme
`owl:intersectionOf` aus `LP_0002103` „Element (SH)“ und der Bedingung „hat Funktion =
Hinweisbeschreibungsfunktion“ (`LP_0000483`/`LP_0001014`). Das ist einer der in
`mem-explorer/CLAUDE.md` dokumentierten blinden Flecken: 22 der 37 SH-Klassen (namentlich
u. a. `LP_0030278` und `LP_0030280`) hängen nur über eine anonyme Intersection an ihrer
Oberklasse.

## Was ein Konkretionsknoten als Teile haben darf

Die Ontologie schränkt das **nicht** ein:

- `LP_0030280` selbst trägt keine eigene `owl:Restriction` auf `obo:BFO_0000051`
  (geprüft im vollständigen `klasse.sh`-Block oben — nur die Funktions-Restriktion ist
  vorhanden).
- Auch die geerbte Kette (`LP_0002103` „Element (SH)“ → `LP_0000261` „Curriculares
  Element“) trägt keine Restriktion auf `hat Teil`, wie `klasse.sh LP_0002103` und
  `klasse.sh LP_0000261` zeigen.
- Ein `grep` über ganz `references/lp-base.ttl` nach `owl:onProperty obo:BFO_0000051`
  findet in der SH-Hierarchie genau eine einzige Restriktion — nicht an `LP_0030280`,
  sondern an der SH-Wurzelklasse `LP_0000824` „Fachanforderung (SH)“:

  ```turtle
  LP_0000824 „Fachanforderung (SH)“ rdfs:subClassOf LP_0000438 „Lehrplan“ ,
      [ rdf:type owl:Restriction ;
        owl:onProperty obo:BFO_0000051 „hat Teil“ ;
        owl:allValuesFrom LP_0002103 „Element (SH)“
      ] .
  ```

  Diese Restriktion gilt nur für die direkten Teile der Lehrplanwurzel (sie müssen vom
  Typ „Element (SH)“ sein); für `LP_0030280` selbst — mehrere Ebenen tiefer — gilt sie
  nicht.
- Im generierten `shapes.ttl` des mem-explorer (`src/lib/ontology/generated/shapes.ttl`)
  taucht `LP_0030280` an keiner Stelle als Shape-Target auf; die einzige
  `sh:PropertyShape` auf `obo:BFO_0000051` in diesem Umfeld hängt ebenfalls an
  `LP_0000824` (`sh:class lp:LP_0002103`).
- `hierarchy.ttl` (der mit den Testdaten ausgelieferte Reasoner-Ersatz) trägt zwar die
  synthetisierte Kante `lp:LP_0030280 rdfs:subClassOf lp:LP_0002103` (seit 0.4.0, aus der
  benannten Intersections-Komponente), das macht `LP_0030280` für SHACL zwar als
  Subklasse von „Element (SH)“ sichtbar — es existiert aber weiterhin keine Shape, die
  darüber eine `hat Teil`-Regel vererben würde.

**Fazit:** Ontologisch darf ein `LP_0030280`-Knoten **beliebige** Ressourcen als Teile
haben — nichts ist vorgeschrieben oder verboten. In der Praxis (Datenkonvention, nicht
Ontologie-Zwang) sind die Teile eines Konkretions-Containers wieder Knoten desselben Typs
`LP_0030280` — einzelne Konkretions-Stichpunkte, wie oben im Auszug aus
`sekundarstufe.ttl` zu sehen.

## Belege im Überblick

| Aussage | Quelle |
|---|---|
| SH hat 37 Klassen, mehrere mit „Inhalt“ im Namen | `references/laender/SH.md` |
| `LP_0030280` wird in echten SH-Daten für „Mögliche Konkretionen“ verwendet, auch verschachtelt als Teile desselben Typs | `relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl` |
| Label/Typ von `LP_0030280` | `scripts/lookup.sh LP_0030280` |
| Vollständige Klassendefinition (anonyme Intersection, keine `hat Teil`-Restriktion) | `scripts/klasse.sh LP_0030280`, `scripts/klasse.sh LP_0002103`, `scripts/klasse.sh LP_0000261` |
| Einzige `hat Teil`-Restriktion in der SH-Hierarchie sitzt an der Wurzel `LP_0000824`, nicht an `LP_0030280` | `grep -n "BFO_0000051" references/lp-base.ttl` + `scripts/klasse.sh LP_0000824` |
| Keine SHACL-Shape zielt auf `LP_0030280` | `src/lib/ontology/generated/shapes.ttl` (mem-explorer) |
| `LP_0030280` ist in `hierarchy.ttl` als benannte Subklasse von „Element (SH)“ vermerkt, aber ohne ererbte `hat Teil`-Shape | `src/lib/ontology/generated/hierarchy.ttl` (mem-explorer) |
| 22 der 37 SH-Klassen ohne benannte Oberklasse sind ein dokumentierter blinder Fleck | `mem-explorer/CLAUDE.md`, Abschnitt „Drei dokumentierte blinde Flecken“ |
