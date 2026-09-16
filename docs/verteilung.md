# Verteilung

## openskills.cc

Kein Einreichformular. Nachricht an den Betreiber (X-Handle im Footer der Seite) mit dem
GitHub-Link:

> Open-source Agent Skill (CC BY-SA 4.0) for writing German curriculum data (MEM / FWU
> Lehrplan-Ontologie): https://github.com/sroertgen/mem-lehrplan

laoc schickt sie.

## Release-Checkliste (durch den Controller / laoc, nicht Teil dieser Aufgabe)

- [ ] `metadata.version` in `SKILL.md` liest `0.1.0` — geprüft am 2026-09-16: ja, bereits
      so gesetzt. Nicht verändern.
- [ ] Branch `skill` nach `main` mergen.
- [ ] Annotierten Tag `v0.1.0` setzen:

  ```
  mem-lehrplan 0.1.0

  Erste Fassung: SKILL.md, Muster und Konventionen, Term-Tabellen und
  Laenderprofile (Ontologie 1.0.0rc4), beispiel.ttl mit Exit 0, lookup.sh
  und klasse.sh, gegen Ausgangslaeufe getestet.
  ```

- [ ] `git push origin main v0.1.0`
- [ ] `git push github main v0.1.0`
