# Muster

Die sechs Situationen, die beim Schreiben von MEM-Lehrplan-Turtle immer wieder vorkommen.
Jeder Turtle-Block ist wörtlich aus `references/patterns/patternN.ttl` übernommen — der
Namensraum `ex:` bleibt als Platzhalter stehen, im eigenen Dokument wird daraus `data:`.

## Lehrplanwurzel

Der Wurzelknoten eines Lehrplans trägt die Klasse des Landes, das Bundesland, Schulfach,
Schulart und die Schulstufe, plus den Titel als Wertknoten.

```turtle
@prefix ex: <https://www.example.org/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

@prefix lp: <https://w3id.org/lehrplan/ontology/> .

# Klassen
@prefix Lehrplan: <https://w3id.org/lehrplan/ontology/LP_0000438> .
@prefix Titel: <https://w3id.org/lehrplan/ontology/LP_0000346> .

# Instanzen
@prefix Sachsen: <https://w3id.org/lehrplan/ontology/LP_3000047> .
@prefix Mathematik: <https://w3id.org/schulfach/SN_0000012> .
@prefix Oberschule: <https://w3id.org/schulart/SN_0000003> .
@prefix Sekundarbereich_II: <https://w3id.org/lehrplan/ontology/LP_0000046> .

# properties
@prefix hat_Titel: <https://w3id.org/lehrplan/ontology/LP_0030056> .
@prefix von_Bundesland: <https://w3id.org/lehrplan/ontology/LP_0000029> .
@prefix hat_Schulfach: <https://w3id.org/lehrplan/ontology/LP_0000537> .
@prefix für_Schulart: <https://w3id.org/lehrplan/ontology/LP_0000812>.
@prefix hat_Schulstufe: <https://w3id.org/lehrplan/ontology/LP_0000047>.
@prefix hat_Wert: <https://w3id.org/lehrplan/ontology/LP_0000344> .

ex:Lehrplan a Lehrplan: ;
            hat_Titel: ex:Titel ;
            von_Bundesland: Sachsen: ;
            hat_Schulfach: Mathematik: ;
            für_Schulart: Oberschule: ;
            hat_Schulstufe: Sekundarbereich_II: . 

ex:Titel a Titel: ;
        hat_Wert:  "Lehrplan Oberschule Mathematik" .
```

Dokumentation: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-1-lehrplan-eines-bundeslandes

## Titel, Beschreibung, Nummer

Titel, Beschreibung und Identifikationsnummer sind eigene benannte Knoten, nie Literale
direkt am Element und nie Blank Nodes; der Text hängt an `hat Wert` (LP_0000344).

```turtle
@prefix ex: <https://www.example.org/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

@prefix lp: <https://w3id.org/lehrplan/ontology/> .

# Klassen
@prefix Bildungsplan_BW: <https://w3id.org/lehrplan/ontology/LP_0000806> .
@prefix Lehrplanfragment_BW: <https://w3id.org/lehrplan/ontology/LP_0002052> .
@prefix Titel: <https://w3id.org/lehrplan/ontology/LP_0000346> .
@prefix Beschreibung: <https://w3id.org/lehrplan/ontology/LP_0030003> .
@prefix Identifikationsnummer: <https://w3id.org/lehrplan/ontology/LP_0000347> .
@prefix Kompetenzbereich_BW: <https://w3id.org/lehrplan/ontology/LP_0030174> .


# properties
@prefix hat_Titel: <https://w3id.org/lehrplan/ontology/LP_0030056> .
@prefix hat_Teil: <http://purl.obolibrary.org/obo/BFO_0000051> .
@prefix hat_Nummer: <https://w3id.org/lehrplan/ontology/LP_0030057> .
@prefix hat_Beschreibung: <https://w3id.org/lehrplan/ontology/LP_0030051> .
@prefix hat_Wert: <https://w3id.org/lehrplan/ontology/LP_0000344> .

ex:Lehrplan a Bildungsplan_BW: ;
            hat_Teil: ex:Fragment ;
            hat_Titel: ex:Titel_1 .
ex:Fragment a Lehrplanfragment_BW: ;
            hat_Teil: ex:Bereich ;
            hat_Titel: ex:Titel_2 .

ex:Bereich  a Kompetenzbereich_BW: ;
            hat_Titel: ex:Titel_3 ;
            hat_Nummer: ex:Nummer ;
            hat_Beschreibung: ex:Beschreibung .

ex:Titel_1 a Titel: ;
    hat_Wert: "Bildungsplan Sekundarstufe I - Deutsch" .

ex:Titel_2 a Titel: ;
    hat_Wert: "Prozessbezogene Kompetenzen" .

ex:Titel_3 a Titel: ;
    hat_Wert: "Sprechen und Zuhören" .


ex:Beschreibung a Beschreibung: ;
    hat_Wert: "Die Schülerinnen und Schüler erwerben kommunikative Kompetenz ..."  .

ex:Nummer a Identifikationsnummer: ;
    hat_Wert: "2.1" .
```

Dokumentation: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-2-titel-beschreibung-und-identifikationsnummer

## Jahrgangsstufe und Schulstufe

Jahrgangsstufen sind bundeslandunabhängige Individuen (LP_2000001 bis LP_2000013),
mehrwertig für Spannen wie „5–6“; ganze Abschnitte hängen über `hat Schulstufe`
(LP_0000047) an den Individuen der Schulstufen und Phasen.

```turtle
@prefix ex: <https://www.example.org/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

@prefix lp: <https://w3id.org/lehrplan/ontology/> .

# Klassen
@prefix Schulstufe: <https://w3id.org/lehrplan/ontology/LP_0000020> .
@prefix Oberstufenphase: <https://w3id.org/lehrplan/ontology/LP_0000043> .
@prefix Einführungsphase: <https://w3id.org/lehrplan/ontology/LP_0000056> .
@prefix Qualifikationsphase: <https://w3id.org/lehrplan/ontology/LP_0000057> .
@prefix Jahrgangsstufe: <https://w3id.org/lehrplan/ontology/LP_0000009> .

# Individuen
@prefix Sekundarbereich_II: <https://w3id.org/lehrplan/ontology/LP_0000046> .
@prefix Sekundarbereich_I: <https://w3id.org/lehrplan/ontology/LP_0000045> .
@prefix Primarbereich: <https://w3id.org/lehrplan/ontology/LP_0000036> .
@prefix G8_Einführungsphase: <https://w3id.org/lehrplan/ontology/LP_0000051> .
@prefix G8_Qualifikationsphase: <https://w3id.org/lehrplan/ontology/LP_0000050> .
@prefix G9_Einführungsphase: <https://w3id.org/lehrplan/ontology/LP_0000055> .
@prefix G9_Qualifikationsphase: <https://w3id.org/lehrplan/ontology/LP_0000052> .
@prefix Jahrgangsstufe_10: <https://w3id.org/lehrplan/ontology/LP_2000010> .
@prefix Jahrgangsstufe_11: <https://w3id.org/lehrplan/ontology/LP_2000011> .
@prefix Jahrgangsstufe_12: <https://w3id.org/lehrplan/ontology/LP_2000012> .
@prefix Jahrgangsstufe_13: <https://w3id.org/lehrplan/ontology/LP_2000013> .

# properties
@prefix hat_Jahrgangsstufe: <https://w3id.org/lehrplan/ontology/LP_0000026> .
@prefix hat_Teil: <> .
G8_Einführungsphase: a Einführungsphase: ;
                      hat_Jahrgangsstufe: Jahrgangsstufe_10: .
G9_Einführungsphase: a Einführungsphase: ;
                      hat_Jahrgangsstufe: Jahrgangsstufe_11: .
G8_Qualifikationsphase: a Qualifikationsphase: ;
                        hat_Jahrgangsstufe: Jahrgangsstufe_11: ,
                                            Jahrgangsstufe_12: .
G9_Qualifikationsphase: a Qualifikationsphase: ;
                        hat_Jahrgangsstufe: Jahrgangsstufe_12: ,
                                            Jahrgangsstufe_13: .                     
Jahrgangsstufe_10: a Jahrgangsstufe: .
Jahrgangsstufe_11: a Jahrgangsstufe: .
Jahrgangsstufe_12: a Jahrgangsstufe: .
Jahrgangsstufe_13: a Jahrgangsstufe: .
Einführungsphase: rdfs:subClassOf Oberstufenphase: .
Qualifikationsphase: rdfs:subClassOf Oberstufenphase: .
Sekundarbereich_II: a Schulstufe: ;
                    hat_Teil: G8_Einführungsphase: ,
                              G9_Einführungsphase: ,
                              G8_Qualifikationsphase: ,
                              G9_Qualifikationsphase: .
Sekundarbereich_I: a Schulstufe: .
Primarbereich: a Schulstufe: .
```

Dokumentation: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-5-jahrgangstufeschulstufe-und-phasen-der-sekundarstufe-ii

## Hierarchie über hat Teil

Die gesamte Gliederung eines Lehrplans — von der Wurzel bis zum Hinweis — hängt an
`hat Teil` (obo:BFO_0000051), nicht an eigenen Objektproperties je Ebene.

```turtle
@prefix ex: <https://www.example.org/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

@prefix lp: <https://w3id.org/lehrplan/ontology/> .

# Klassen
@prefix Lehrplan: <https://w3id.org/lehrplan/ontology/LP_0000438> .
@prefix CE-Fragment: <https://w3id.org/lehrplan/ontology/LP_0001015> .
@prefix CE-Bereich: <https://w3id.org/lehrplan/ontology/LP_0000349> .
@prefix CE-Lerninhalt: <https://w3id.org/lehrplan/ontology/LP_0000332> .
@prefix CE-Kompetenzspezifikation: <https://w3id.org/lehrplan/ontology/LP_0000263> .
@prefix CE-Hinweis: <https://w3id.org/lehrplan/ontology/LP_0000852> .

# properties
@prefix hat_Teil: <http://purl.obolibrary.org/obo/BFO_0000051> .

ex:Lehrplan hat_Teil: ex:CE-Fragment_1 .
ex:CE-Fragment_1 hat_Teil: ex:CE-Bereich_1 .
ex:CE-Bereich_1 hat_Teil: ex:CE-Bereich_2 .
ex:CE-Bereich_2 hat_Teil: ex:CE-Lerninhalt_1 ,
                          ex:CE-Kompetenzspezifikation_1 .                   
ex:CE-Lerninhalt_1 hat_Teil: ex:CE-Lerninhalt_2 .
ex:CE-Lerninhalt_2 hat_Teil: ex:CE-Hinweis_1 .
ex:CE-Kompetenzspezifikation_1 hat_Teil: ex:CE-Hinweis_2 .
```

Dokumentation: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-6-hierarchie-der-curricularen-elemente

Was eine Klasse an dieser Kante enthalten darf, steht nicht in diesem Muster, sondern in
ihrer Definition: `scripts/klasse.sh <ID>`.

## Verweise

Ein CE-Verweis zeigt mit `verweist auf` (LP_0030072) auf ein anderes curriculares Element;
er trägt selbst eine eigene, länderspezifische Verweis-Klasse und darf eine Beschreibung
haben.

```turtle
@prefix ex: <https://www.example.org/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

@prefix lp: <https://w3id.org/lehrplan/ontology/> .

# Klassen
@prefix Curriculares_Element: <https://w3id.org/lehrplan/ontology/LP_0000261> .
@prefix CE-Bereich: <https://w3id.org/lehrplan/ontology/LP_0000349> .
@prefix CE-Kompetenzspezifikation: <https://w3id.org/lehrplan/ontology/LP_0000263> .
@prefix CE-Verweis: <https://w3id.org/lehrplan/ontology/LP_0030065> .
@prefix Verweis_auf_Lernbereich_des_gleichen_Faches_einer_anderen_Klassenstufe_SN: <https://w3id.org/lehrplan/ontology/LP_0030188> .

# properties
@prefix hat_Verweis: <https://w3id.org/lehrplan/ontology/LP_0030071> .
@prefix verweist_auf: <https://w3id.org/lehrplan/ontology/LP_0030072> .
@prefix hat_Beschreibung: <https://w3id.org/lehrplan/ontology/LP_0030051> .

ex:Kompetenz_1 a CE-Kompetenzspezifikation: ;
                hat_Verweis: ex:Verweis_1 .
ex:Verweis_1 a Verweis_auf_Lernbereich_des_gleichen_Faches_einer_anderen_Klassenstufe_SN: ;
              verweist_auf: ex:Lernbereich_1 ;
              hat_Beschreibung: ex:Beschreibung_1 .
ex:Lernbereich_1 a CE-Bereich: .
CE-Kompetenzspezifikation: rdfs:subClassOf Curriculares_Element: .
Verweis_auf_Lernbereich_des_gleichen_Faches_einer_anderen_Klassenstufe_SN: rdfs:subClassOf CE-Verweis: .
```

Dokumentation: https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-7-ce-verweis

## Reihenfolge mit hat Position

Kein eigenes Pattern der Doku, aber notwendig: RDF bewahrt keine Reihenfolge unter
Geschwistern. Ohne `hat Position` (LP_0000460) geht die Geschwisterfolge der Vorlage —
Aufzählungspunkte, nummerierte Abschnitte — beim Einlesen verloren. `hat Position` hat
`rdfs:range xsd:int` (nicht `xsd:integer`, siehe `references/beispiel.ttl`):

```turtle
data:kb-gott-inhalt-1 lp:LP_0000460 "2"^^xsd:int .
data:kb-gott-inhalt-2 lp:LP_0000460 "3"^^xsd:int .
```

Was eine Klasse enthalten darf, steht nicht in den Mustern, sondern in ihrer Definition:
`scripts/klasse.sh <ID>`.
