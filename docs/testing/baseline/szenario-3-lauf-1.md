# Konkretion (SH) in der Lehrplan-Ontologie

## Die Klasse

`lp:LP_0030280` — offizielles Label laut Ontologie: **„Mögliches Thema und
Inhalt (SH)“@de** (`skos:editorialNote "Sachunterricht"`, d. h. ursprünglich für
das Fach Sachunterricht geprägt).

In der Praxis wird genau diese Klasse für „Konkretion“ verwendet: In der
realen Schleswig-Holstein-Transformation (Ev. Religion, Sek I/II,
`~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/
sekundarstufe.ttl`) tragen alle Knoten mit `rdfs:label "Mögliche
Konkretionen …"` bzw. den einzelnen Stichpunkten darunter den `rdf:type
lp:LP_0030280` — unabhängig vom Fach, für das die Klasse ursprünglich benannt
wurde.

Formale Herkunft (aus `lp-base.ttl`/`lp.ttl`):

```turtle
ontology:LP_0030280 rdf:type owl:Class ;
    rdfs:subClassOf [ owl:intersectionOf (
        ontology:LP_0002103                       # Element (SH)
        [ a owl:Restriction ;
          owl:onProperty ontology:LP_0000483 ;     # hat Funktion
          owl:hasValue ontology:LP_0001014 ] ) ] ;  # Hinweisbeschreibungsfunktion
    rdfs:label "Mögliches Thema und Inhalt (SH)"@de .
```

`LP_0030280` hängt also nur über eine **anonyme** OWL-Klasse (Blank Node,
`owl:intersectionOf`) an ihrer Oberklasse `lp:LP_0002103` („Element (SH)“,
selbst `subClassOf lp:LP_0000261` „Curriculares Element“). Ein einfacher
`rdfs:subClassOf`-Pfad ohne Auflösung dieses Blank Node führt ins Leere — das
ist in `mem-explorer` als einer der beiden dokumentierten blinden Flecken
festgehalten (`LP_0030278`/`LP_0030280`, siehe `CLAUDE.md`): SHACL-Shapes, die
über `rdf:type/rdfs:subClassOf*` auflösen, greifen hier nicht.

## Was darf so ein Knoten als Teile haben?

**Die Ontologie schränkt das für `LP_0030280` nicht ein.** Weder in
`lp-base.ttl`/`lp.ttl`/`lp-land-SH-full.owl` noch in den mitgelieferten
SHACL-Shapes (`shapes/auto-shapes/auto-shapes-open.ttl`, generiert per
`owl2shacl`) existiert eine Restriktion auf der Property `obo:BFO_0000051`
(*has part* — die Property, die laut Ontologie die Lehrplanhierarchie trägt)
mit `LP_0030280` als Subjekt/Domain. Eine Suche nach `LP_0030280` in den
Auto-Shapes liefert keinen Treffer; die Klasse taucht dort überhaupt nicht als
`sh:NodeShape` auf.

Zum Vergleich, damit die Abwesenheit einer Regel nicht wie ein Versehen der
Recherche wirkt: Die SH-Wurzelklasse `lp:LP_0000824` („Fachanforderung (SH)“)
**ist** eingeschränkt — ihre `obo:BFO_0000051`-Teile müssen laut
Auto-Shape von der Klasse `lp:LP_0002103` („Element (SH)“) sein:

```turtle
:LP_0000824-http___purl.obolibrary.org_obo_BFO_0000051
    a sh:PropertyShape ;
    sh:class :LP_0002103 ;
    sh:path  <http://purl.obolibrary.org/obo/BFO_0000051> .
```

Für `LP_0030280` selbst fehlt eine entsprechende Regel — formal darf ein
Konkretions-Knoten laut Ontologie also **beliebige** Ressourcen als Teile
tragen, es gibt keine deklarierte Klassen- oder Kardinalitätsbeschränkung.

**Reale Praxis (Konvention, keine Ontologie-Vorschrift):** In den
tatsächlichen SH-Daten enthält ein „Mögliche Konkretionen“-Container über
`obo:BFO_0000051` eine Liste von Einzel-Stichpunkten, die **wieder** vom
Typ `lp:LP_0030280` sind — die Klasse wird also sowohl für den
Sammelknoten als auch für seine Teile verwendet:

```turtle
data:si-kb1-inhalt56
    rdf:type lp:LP_0030280 ; rdfs:label "Mögliche Konkretionen (Jahrgangsstufe 5-6)" ;
    obo:BFO_0000051 data:si-kb1-56-001, data:si-kb1-56-002, … .

data:si-kb1-56-001 rdf:type lp:LP_0030280 ;
    rdfs:label "Gottesvorstellungen (anthropomorph, symbolisch, allmächtig, allwissend, gütig)" .
```

## Beteiligte IDs

| ID | Rolle |
|---|---|
| `lp:LP_0030280` | Konkretion (SH) — Klasse „Mögliches Thema und Inhalt (SH)“ |
| `lp:LP_0002103` | Oberklasse „Element (SH)“ (nur über anonyme Intersection erreichbar) |
| `lp:LP_0000261` | Großoberklasse „Curriculares Element“ |
| `lp:LP_0000483` | Property „hat Funktion“ (Teil der definierenden Restriktion) |
| `lp:LP_0001014` | Individuum „Hinweisbeschreibungsfunktion“ (Wert der Restriktion) |
| `obo:BFO_0000051` | Property *has part* — trägt die Teile-Beziehung |
| `lp:LP_0000824` | „Fachanforderung (SH)“ — zum Vergleich: dort ist `BFO_0000051` per SHACL auf `LP_0002103` eingeschränkt, bei `LP_0030280` nicht |
| `lp:LP_0030278` | zweite dokumentierte SH-Länderklasse mit demselben blinden Fleck (zum Vergleich, nicht Teil der Antwort) |

## Herkunft der Angaben

Die Klassendefinition und die fehlende Teile-Restriktion stammen aus den
gespiegelten Originalquellen in `~/coding/mem-knowledge-base/vendor/
lehrplan-ontologie/` (`lp.ttl`, `lp-land-SH-full.owl`,
`shapes/auto-shapes/auto-shapes-open.ttl`) sowie aus der Term-Referenz
`~/coding/mem-knowledge-base/reference/lp-terms.tsv`; die reale Verwendung
für „Konkretion“ und die Beispieldaten sind aus der SH-Transformation
`~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/
sekundarstufe.ttl` entnommen, auf die auch `~/coding/mem-knowledge-base/MEM.md`
(§5) als reales Beispiel verweist.
