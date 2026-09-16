# mem-lehrplan

Agent-Skill für das Schreiben und Nachbessern von MEM-Lehrplandaten — Turtle nach der
[Lehrplan-Ontologie des FWU](https://github.com/FWU-DE/lehrplan-ontologie) (Stand
1.0.0rc4). Für Claude Code und andere Werkzeuge, die das
[Agent-Skills-Format](https://agentskills.io) lesen.

Was drin ist: die Muster der Ontologie-Doku als Soll, Term-Tabellen für alle 2003 IDs (988
Lehrplan-, 910 Schulfach- und 105 Schulart-Terme), Klassenprofile je Bundesland, ein
vollständiges gültiges Beispiel, Skripte zum Nachschlagen und die Fallstricke, die in
echten Transformationen aufgetreten sind. Die Term-Tabellen führen auch die
`skos:editorialNote` der Ontologie (Spalte `note`) mit — das einzige, was strukturgleiche
Länder-Klassen wie LP_0030280 „Mögliches Thema und Inhalt (SH)“ (Note „Sachunterricht“)
und LP_0030059 „Möglicher Inhalt (SH)“ (Note „Englisch Primar“) auseinanderhält. Geprüft
wird mit `mem-explorer check` ([MEM Explorer](https://git.edufeed.org/laoc/mem-explorer)).

## Installation

```sh
# Claude Code
git clone https://github.com/sroertgen/mem-lehrplan ~/.claude/skills/mem-lehrplan
# Codex, Copilot CLI, Gemini CLI und andere
git clone https://github.com/sroertgen/mem-lehrplan ~/.agents/skills/mem-lehrplan
```

Voraussetzungen: Node 22+, bash, grep, awk. Optional `pdftotext` für den Weg vom PDF. Der
MEM Explorer wird über die Forgejo-Paketregistry aufgerufen, nicht über npmjs.org — ein
nacktes `npx mem-explorer` findet das Paket nicht:

```sh
npx --registry=https://git.edufeed.org/api/packages/edufeed/npm/ mem-explorer check datei.ttl
```

## Benutzung

Der Agent liest `SKILL.md` und folgt dem Ablauf. Von Hand nützlich:

```sh
scripts/lookup.sh "hat Jahrgangsstufe"     # Wort -> ID
scripts/lookup.sh LP_0030280               # ID -> Bedeutung, inkl. editorialNote
scripts/klasse.sh LP_0030280               # Definition mit Restriktionen, Labels aufgeloest
npx --registry=https://git.edufeed.org/api/packages/edufeed/npm/ mem-explorer check datei.ttl   # Pruefbericht, Exit 0 = kein Fehler
```

## Referenzen aktualisieren

```sh
scripts/update-references.sh               # klont die FWU-Repos nach .vendor/ und erzeugt references/
scripts/update-references.sh ~/pfad/lehrplan-ontologie   # oder aus einem eigenen Checkout
git diff --stat references/                # was sich in der Ontologie geaendert hat
```

`references/VERSION` nennt den Stand (aktuell Ontologie 1.0.0rc4).

## Tests

Vier Szenarien (Transformieren, Nachbessern, Nachschlagen, Retrieval) in
`docs/testing/szenarien.md`, drei davon je zweimal ohne Skill als Ausgangslauf
(`docs/testing/baseline.md`, sechs Läufe) und einmal mit Skill (`docs/testing/green.md`).
Alle vier Szenarien bestehen dort zwei aufeinanderfolgende Läufe: Szenario 1 und 2 bereits
in der ersten Runde, Szenario 3 erst nach einem Refactor in der zweiten Runde, Szenario 4
— erst nach Task 7 ergänzt, ohne eigenen Baseline-Lauf — direkt in seiner ersten Runde.

## Herkunft und Lizenz

CC BY-SA 4.0. `references/patterns/`, `references/lp-base.ttl` und die Term-Tabellen stammen
aus FWU-DE/lehrplan-ontologie, schulfach-ontologie und schulart-ontologie (CC BY-SA 4.0,
© FWU Institut für Film und Bild in Wissenschaft und Unterricht). Entwurf und Tests:
`docs/`.
