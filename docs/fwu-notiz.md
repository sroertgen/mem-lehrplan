# Entwurf — nicht gesendet

An: redaktion@mem.schule
Betreff: Agent-Skill für MEM-Lehrplan-Turtle, zwei Rückmeldungen zur Ontologie

Hallo,

wir haben einen Agent-Skill veröffentlicht, der LLM-Agenten beim Schreiben und Nachbessern
von MEM-Lehrplandaten (Turtle nach der Lehrplan-Ontologie des FWU) anleitet. Die
Dokumentation der Ontologie ist darin die alleinige Autorität — Muster, Klassen und
Konventionen kommen aus `docs/` bzw. den Referenzdateien des FWU-Repos, nicht aus einem
Store-Export oder aus Vermutung. Der Skill steht unter CC BY-SA 4.0:
https://github.com/sroertgen/mem-lehrplan

Zwei Punkte dazu:

**Rückmeldung erbeten zu Projektkonventionen.** Die Ontologie legt Klassen, Properties und
die sechs Muster fest, sagt aber nichts zu Namensraum, Knotenbenennung oder Dateizuschnitt.
Wir haben dafür eigene Konventionen festgelegt (`references/konventionen.md` im Repo) —
unter anderem: ein eigener `data:`-Namensraum je Land und Projekt statt eines geteilten
Namensraums; `rdfs:label` als technische Kurzbezeichnung neben dem Titel-Knoten aus
Pattern 2, nicht als dessen Ersatz; Geschwisterreihenfolge über `hat Position`. Uns
interessiert, ob das aus Ihrer Sicht zur Ontologie passt oder wo es sich mit einer eigenen,
schon bestehenden Konvention reibt.

**Zwei Beobachtungen aus der Arbeit mit der Ontologie:**

1. Mehrere strukturgleiche Länder-Klassen lassen sich nur über `skos:editorialNote`
   unterscheiden, nicht über Struktur oder Namen allein — zum Beispiel LP_0030280
   „Mögliches Thema und Inhalt (SH)“ (Note „Sachunterricht“) und LP_0030059 „Möglicher
   Inhalt (SH)“ (Note „Englisch Primar“). Das war in unseren Tests eine reale
   Fehlerquelle (falsche Klasse gewählt, weil der Name passend schien); der Skill zeigt
   die editorialNote inzwischen direkt bei jeder Klassenauskunft an.
2. `docs/patterns/pattern5.ttl` deklariert `@prefix hat_Teil: <> .` mit leerer IRI, obwohl
   der Block `hat_Teil:` tatsächlich verwendet
   (`Sekundarbereich_II: hat_Teil: G8_Einführungsphase:, …`). Alle anderen Patterns (z. B.
   pattern6.ttl) schreiben dafür `@prefix hat_Teil: <http://purl.obolibrary.org/obo/BFO_0000051> .`
   — die IRI fehlt hier vermutlich nur versehentlich. Wer den Block wörtlich kopiert,
   bekommt ungültiges Turtle.

Über eine Rückmeldung würden wir uns freuen.

Viele Grüße
