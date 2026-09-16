# Konkretion (möglicher Inhalt zu einem Kompetenzbereich) in Schleswig-Holstein

## Klasse

`LP_0030059` — **„Möglicher Inhalt (SH)“**

Gefunden über `scripts/lookup.sh "Möglicher Inhalt"`:

```
LP_0030008 · Class · Möglicher Inhalt (BB) ·  · parent=  (lp)
LP_0030059 · Class · Möglicher Inhalt (SH) ·  · parent=  (lp)
LP_0030284 · Class · Möglicher inhaltlicher Aspekt (TH) ·  · parent=  (lp)
```

`references/laender/SH.md` listet `LP_0030059 | Möglicher Inhalt (SH)` unter den Klassen
ohne benannte Oberklasse (Oberklasse ist ein anonymer OWL-Ausdruck). `references/arbeitsablauf.md`
(Abschnitt „Vom PDF zur Struktur“) bestätigt die Zuordnung generisch: eine Tabellenspalte
„Mögliche Inhalte“/„Konkretionen“ wird zu einem Knoten der „Lerninhalt-Klasse des Landes“ —
welche Klasse das je Land ist, steht in `references/laender/<XX>.md`. Für SH ist das `LP_0030059`.

## Definition (aus `lp-base.ttl`, via `scripts/klasse.sh LP_0030059`)

```turtle
LP_0030059 „Möglicher Inhalt (SH)“ rdf:type owl:Class ;
    rdfs:subClassOf [ owl:intersectionOf ( LP_0002103 „Element (SH)“
                                            [ rdf:type owl:Restriction ;
                                              owl:onProperty LP_0000483 „hat Funktion“ ;
                                              owl:hasValue LP_0001014 „Hinweisbeschreibungsfunktion“
                                            ] ) ;
                       rdf:type owl:Class
                     ] ;
    rdfs:label "Möglicher Inhalt (SH)"@de ;
    skos:editorialNote "Englisch Primar" .
```

`LP_0002103` „Element (SH)“ ist ihrerseits `LP_0000261` „Curriculares Element“, eingeschränkt
auf `von Bundesland` (LP_0000029) `hasValue` `LP_3000054` (Schleswig-Holstein) — geprüft mit
`scripts/klasse.sh LP_0002103` und `scripts/klasse.sh LP_0000261`.

## Was der Knoten laut Ontologie als Teile haben darf

**Nichts ist vorgeschrieben oder eingeschränkt.** Weder im Definitionsblock von `LP_0030059`
selbst noch in der gesamten Oberklassenkette (`LP_0002103` „Element (SH)“ → `LP_0000261`
„Curriculares Element“ → `obo:IAO_0000030`) steht eine `owl:Restriction` auf
`obo:BFO_0000051` („hat Teil“) — geprüft mit `scripts/klasse.sh` auf jeder Stufe der Kette
und zusätzlich per `grep -n "LP_0002103\|LP_0000261"` gegen `references/lp-base.ttl`
direkt (identisches Ergebnis, keine Restriktion übersehen). Die einzige Restriktion, die
`LP_0030059` definiert, betrifft `hat Funktion` (LP_0000483) — nicht `hat Teil`.

Bemerkenswert dabei: Der Funktionswert `LP_0001014` „Hinweisbeschreibungsfunktion“ ist
derselbe Wert, über den die generische, nicht-landesspezifische Klasse `LP_0000852`
„CE-Hinweis“ definiert ist (`scripts/klasse.sh LP_0000852`) — nicht der Wert
`LP_0000480` „Lerninhaltsbeschreibungsfunktion“, der `LP_0000332` „CE-Lerninhalt“
auszeichnet (`scripts/klasse.sh LP_0000332`). Trotz des Labels „Möglicher Inhalt“ ist der
SH-Knoten damit über seine Funktions-Restriktion an die Hinweis-Familie angelehnt, nicht an
die Lerninhalt-Familie. Und `CE-Hinweis` selbst trägt ebenfalls keine Restriktion auf
`hat Teil` — es definiert nur, wovon es ein Teil sein darf (`ist Teil von`,
`obo:BFO_0000050`, someValuesFrom Union aus CE-Kompetenzspezifikation/CE-Lerninhalt/
CE-Bereich), nicht was es selbst enthalten darf. Zum Vergleich, wo die Ontologie so etwas
tatsächlich regelt: `CE-Lerninhalt` (LP_0000332) trägt in seinem `rdfs:comment` ausdrücklich
die Vorgabe „kann einen anderen CE-Lerninhalt enthalten, aber kein anderes Element“ — eine
Aussage dieser Art fehlt bei `LP_0030059`/`LP_0000852` vollständig.

Damit gilt für `LP_0030059`: Er kann — wie jedes Curriculare Element generisch — per
`hat Teil` (`obo:BFO_0000051`) weitere Knoten tragen (z. B. Wertknoten für Titel/Beschreibung/
Nummer über `hat Wert`, LP_0000344), aber die Ontologie schreibt für diese Klasse weder vor
noch schränkt sie ein, welche Klassen das sein müssten oder dürften.

## Quellen

- `scripts/lookup.sh "Möglicher Inhalt"`, `scripts/lookup.sh Konkretisierung`
- `scripts/klasse.sh LP_0030059`, `LP_0002103`, `LP_0000261`, `LP_0000332`, `LP_0000852`
- `references/laender/SH.md` (Abschnitt „Oberklasse ist ein anonymer OWL-Ausdruck“)
- `references/arbeitsablauf.md` (Abschnitt „Vom PDF zur Struktur“, Zeile 53–56)
- `references/lp-base.ttl` direkt gegengeprüft (Zeilen um 6287ff. für LP_0030059; Blöcke für
  LP_0002103 und LP_0000261 per `grep`/`awk`)
- `references/patterns/pattern6.ttl` als generisches Beispiel der `hat Teil`-Hierarchie
  (Lehrplan → CE-Fragment → CE-Bereich → CE-Lerninhalt/CE-Kompetenzspezifikation → CE-Hinweis)
