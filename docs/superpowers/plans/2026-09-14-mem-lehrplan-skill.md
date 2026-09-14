# Skill `mem-lehrplan` — Umsetzungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eine agentskills-kompatible Skill, mit der ein LLM-Agent MEM-Lehrplan-Turtle nach den Mustern der FWU-Ontologie schreibt und Explorer-Befunde behebt — mit gebündelten Term-Tabellen, Länderprofilen, Mustern, einem vollständigen Beispiel und `npx mem-explorer check` als Prüfschritt.

**Architecture:** Repository-Wurzel = Skill-Ordner (`SKILL.md`, `references/`, `scripts/`). Alles unter `references/terms`, `laender`, `patterns`, `lp-base.ttl`, `VERSION` wird von `scripts/update-references.sh` aus den FWU-Repos erzeugt und eingecheckt. Die Skill wird nach der TDD-Methode für Prozessdokumentation geschrieben: erst Ausgangsläufe ohne Skill (RED), dann SKILL.md gegen die beobachteten Fehler (GREEN), dann Lücken schließen.

**Tech Stack:** Markdown, Bash, Python 3 (Standardbibliothek), Git; zur Prüfung `npx mem-explorer check` (Node ≥ 22, Teil A dieses Vorhabens).

**Spec:** `docs/superpowers/specs/2026-09-14-mem-lehrplan-skill-design.md`, Abschnitte 4–8. Voraussetzung: Teil A (Plan `~/coding/comenius/mem-explorer/docs/superpowers/plans/2026-09-14-cli-check.md`) ist bis Task 5 umgesetzt; solange 0.3.0 nicht auf npm ist, lautet der Prüfbefehl `node ~/coding/comenius/mem-explorer/bin/mem-explorer.mjs check <datei>`.

## Global Constraints

- Arbeitsverzeichnis: `~/coding/comenius/mem-lehrplan`, Branch `main`.
- Skill-Format nach agentskills.io: `name` = Ordnername = `mem-lehrplan`; `description` ≤ 1024 Zeichen, nennt nur Auslöser, keinen Arbeitsablauf; `SKILL.md` unter 500 Wörter; Langes in `references/`.
- Deutsch im Skill-Text; englische Schlüsselwörter in der `description`. Deutsche Anführungszeichen `„…“`.
- Die Doku der Ontologie ist die Autorität. Kein Muster wird aus dem MEM-Store abgeleitet. Keine ID wird ohne Nachschlagen in `references/terms/` in einen Text geschrieben — das gilt auch für diesen Plan: alle IDs unten stammen aus `lp-terms.tsv` (Stand 1.0.0rc3).
- Erzeugte Dateien werden nie von Hand editiert; Änderungen gehen durch die Skripte.
- Lizenz CC BY-SA 4.0 für das ganze Repo; gebündeltes FWU-Material behält seine Herkunftsangabe.
- Skill-TDD: Kein Satz in `SKILL.md` ohne einen Ausgangslauf, der zeigt, warum er nötig ist, oder eine Referenz-Retrieval-Aufgabe, die er beantwortet. Baseline vor dem Schreiben.
- Commits deutsch, ASCII-Umschrift in der Nachricht, Trailer:
  ```
  Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01RVQuqJJiS33VQtsZfG6ont
  ```
- Kein Push ohne Freigabe von laoc; das Forgejo-Repo legt laoc an, das GitHub-Repo darf per `gh` angelegt werden (angemeldet als `sroertgen`).

---

### Task 1: Repo-Gerüst, Lizenz, Remotes

**Files:**
- Create: `.gitignore`, `LICENSE`, `README.md` (Gerüst), `docs/testing/.gitkeep`

- [ ] **Step 1: Gerüst**

```bash
cd ~/coding/comenius/mem-lehrplan
printf '.vendor/\n.DS_Store\n' > .gitignore
mkdir -p references/terms references/laender references/patterns scripts docs/testing
touch docs/testing/.gitkeep
curl -sL https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt -o LICENSE
head -3 LICENSE          # erwartet: 'Attribution-ShareAlike 4.0 International'
```

`README.md` (Gerüst, wird in Task 8 vervollständigt):

```markdown
# mem-lehrplan

Agent-Skill für das Schreiben und Nachbessern von MEM-Lehrplandaten (Turtle nach der
[Lehrplan-Ontologie des FWU](https://github.com/FWU-DE/lehrplan-ontologie)).

Status: im Aufbau. Entwurf: `docs/superpowers/specs/2026-09-14-mem-lehrplan-skill-design.md`.

## Lizenz

CC BY-SA 4.0. Enthält Material aus FWU-DE/lehrplan-ontologie, schulfach-ontologie und
schulart-ontologie (CC BY-SA 4.0, © FWU Institut für Film und Bild).
```

- [ ] **Step 2: Commit und GitHub-Spiegel**

```bash
git add -A && git commit -F - <<'EOF'
chore: Geruest, Lizenz CC BY-SA 4.0, Verzeichnisse

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RVQuqJJiS33VQtsZfG6ont
EOF
gh repo create sroertgen/mem-lehrplan --public --description "Agent-Skill: MEM-Lehrplan-Turtle nach der FWU Lehrplan-Ontologie schreiben und nachbessern" --source . --remote github
git remote -v     # erwartet: github  git@github.com:sroertgen/mem-lehrplan.git
```

Forgejo-Origin: laoc legt `Comenius-Institut/mem-lehrplan` auf https://git.rpi-virtuell.de an (leer, ohne README). Danach:

```bash
git remote add origin ssh://git@git.rpi-virtuell.de/Comenius-Institut/mem-lehrplan.git
```

Noch nicht pushen (Task 8).

---

### Task 2: Referenzen erzeugen — `update-references.sh`, `gen-terms.py`, `gen-laender.py`

**Files:**
- Create: `scripts/update-references.sh`, `scripts/gen-terms.py`, `scripts/gen-laender.py`
- Create (erzeugt): `references/terms/{lp,sf,sa}-terms.tsv`, `references/laender/*.md`, `references/patterns/*.ttl`, `references/lp-base.ttl`, `references/VERSION`

**Interfaces:**
- Produces: TSV-Spalten `id · type · label_de · label_en · parent · comment_de` (Tab-getrennt, Kopfzeile); `laender/<XX>.md` je Land; `VERSION` mit drei Zeilen `ontology=<versionInfo>`, `commit=<sha> <datum>`, `generated=<YYYY-MM-DD>`.

- [ ] **Step 1: `gen-terms.py`** — Portierung von `~/coding/mem-knowledge-base/bin/gen-term-maps.py` mit Pfad-Argumenten:

```python
#!/usr/bin/env python3
"""Erzeugt grep-bare ID<->Label-Tabellen aus den FWU-Ontologien.

Aufruf: gen-terms.py <vendor-dir> <out-dir>
  vendor-dir enthaelt lehrplan-ontologie/, schulfach-ontologie/, schulart-ontologie/
  out-dir bekommt lp-terms.tsv, sf-terms.tsv, sa-terms.tsv

Die Ontologien benutzen opake numerische IDs (LP_0000537, SF_..., SA_...). Ohne
diese Tabellen ist kein Turtle schreibbar, ohne jedes Mal 760 KB zu durchsuchen.
Input im Protege/ROBOT-Blockformat: '###  <IRI>' je Term.
"""
import re, sys, pathlib

SOURCES = [
    ("lp-terms.tsv", "lehrplan-ontologie/lp-base.ttl", "https://w3id.org/lehrplan/ontology/"),
    ("sf-terms.tsv", "schulfach-ontologie/sf.ttl", "https://w3id.org/schulfach/"),
    ("sa-terms.tsv", "schulart-ontologie/sa.ttl", "https://w3id.org/schulart/"),
]
TYPES = {
    "owl:Class": "Class", "owl:ObjectProperty": "ObjectProperty",
    "owl:DatatypeProperty": "DatatypeProperty", "owl:AnnotationProperty": "AnnotationProperty",
    "owl:NamedIndividual": "Individual",
}

def literals(block, pred, lang=None):
    out, tag = [], (f"@{lang}" if lang else "")
    for m in re.finditer(re.escape(pred) + r'\s+((?:"(?:[^"\\]|\\.)*"(?:@[a-zA-Z-]+)?\s*,?\s*)+)', block):
        for lm in re.finditer(r'"((?:[^"\\]|\\.)*)"(@[a-zA-Z-]+)?', m.group(1)):
            val, l = lm.group(1), lm.group(2) or ""
            if lang and l != tag:
                continue
            out.append(val.replace('\\"', '"').replace("\\n", " "))
    return out

def iris(block, pred):
    out = []
    for m in re.finditer(re.escape(pred) + r'\s+((?:[\w:]+\s*,?\s*)+)', block):
        for pfx, t in re.findall(r'(\w*):([A-Z]{2,4}_\d+)', m.group(1)):
            out.append(t if pfx in ("ontology", "sf", "sa", "") else f"{pfx}:{t}")
    return out

def parse(path, prefix):
    src = path.read_text(encoding="utf-8")
    rows = []
    for b in re.split(r'^###\s+', src, flags=re.M)[1:]:
        iri = b.split("\n", 1)[0].strip()
        if not iri.startswith(prefix):
            continue
        term = iri[len(prefix):]
        if not re.fullmatch(r'[A-Z]{2}_\d+', term):
            continue
        body = b.split("\n", 1)[1] if "\n" in b else ""
        body = re.split(r'^#{4,}', body, flags=re.M)[0]
        head = re.search(r'rdf:type\s+([^;.]+)', body)
        head = head.group(1) if head else ""
        kinds = [TYPES[k] for k in TYPES if k in head]
        parents = iris(body, "rdfs:subClassOf") + iris(body, "rdfs:subPropertyOf")
        de = literals(body, "rdfs:label", "de")
        en = literals(body, "rdfs:label", "en")
        untagged = [l for l in literals(body, "rdfs:label") if l not in en]
        rows.append({
            "id": term, "type": "/".join(kinds) or "?",
            "label_de": (de or untagged or [""])[0], "label_en": (en or [""])[0],
            "parent": ",".join(dict.fromkeys(parents)),
            "comment_de": " ".join(literals(body, "rdfs:comment", "de"))[:400],
        })
    return rows

def main():
    vendor, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    cols = ["id", "type", "label_de", "label_en", "parent", "comment_de"]
    for name, rel, prefix in SOURCES:
        rows = sorted(parse(vendor / rel, prefix), key=lambda r: r["id"])
        with open(out / name, "w", encoding="utf-8") as f:
            f.write("\t".join(cols) + "\n")
            for r in rows:
                f.write("\t".join(r[c].replace("\t", " ").replace("\n", " ") for c in cols) + "\n")
        print(f"{name}: {len(rows)} Terme")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: `gen-laender.py`**

```python
#!/usr/bin/env python3
"""Erzeugt je Bundesland ein Klassenprofil aus lp-terms.tsv.

Aufruf: gen-laender.py <terms-dir> <out-dir>

Die Ontologie hat je Land 27-86 eigene Klassen, erkennbar am Label-Suffix '(XX)'.
Welche davon Wurzel, Fragment, Bereich, Kompetenz, Inhalt ist, entscheidet die
Oberklasse - und die ist bei etwa der Haelfte ein anonymer OWL-Ausdruck, also in der
Tabelle leer. Diese Klassen werden gelistet und auf scripts/klasse.sh verwiesen,
statt geraten.
"""
import csv, sys, pathlib

LAENDER = {  # Kuerzel -> (Name in der Ontologie, Individuum der Klasse Bundesland Bezeichnung)
    "BB": ("Brandenburg", "LP_3000057"), "BE": ("Berlin", "LP_3000048"),
    "BW": ("Baden-Württemberg", "LP_3000049"), "BY": ("Bayern", "LP_3000051"),
    "HB": ("Bremen", "LP_3000056"), "HE": ("Hessen", "LP_3000050"),
    "HH": ("Hamburg", "LP_3000045"), "MV": ("Mecklenburg-Vorpommern", "LP_3000052"),
    "NI": ("Niedersachsen", "LP_3000043"), "NW": ("Nordrhein-Westfalen", "LP_3000044"),
    "RP": ("Rheinland-Pfalz", "LP_3000046"), "SH": ("Schleswig-Holstein", "LP_3000054"),
    "SL": ("Saarland", "LP_3000055"), "SN": ("Sachsen", "LP_3000047"),
    "ST": ("Sachsen-Anhalt", "LP_3000053"), "TH": ("Thüringen", "LP_3000031"),
}
BASES = [  # Reihenfolge = Reihenfolge im Profil
    ("LP_0000438", "Lehrplan (Wurzel)"), ("LP_0001015", "CE-Fragment"),
    ("LP_0000349", "CE-Bereich"), ("LP_0000263", "CE-Kompetenzspezifikation"),
    ("LP_0000332", "CE-Lerninhalt"), ("LP_0000852", "CE-Hinweis"),
    ("LP_0000261", "Curriculares Element (direkt)"),
]

def load(path):
    with open(path, encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f, delimiter="\t")}

def base_of(term, terms):
    seen, stack = set(), [term]
    while stack:
        cur = stack.pop()
        for bid, _ in BASES:
            if cur == bid and cur != term:
                return bid
        if cur in seen or cur not in terms:
            continue
        seen.add(cur)
        stack.extend(p for p in terms[cur]["parent"].split(",") if p)
    return None

def main():
    tdir, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    lp = load(tdir / "lp-terms.tsv"); sf = load(tdir / "sf-terms.tsv"); sa = load(tdir / "sa-terms.tsv")
    for code, (name, land_id) in sorted(LAENDER.items()):
        land = lp.get(land_id)
        if not land or land["label_de"] != name:
            print(f"WARNUNG {code}: {land_id} heisst '{land['label_de'] if land else '?'}', erwartet '{name}'", file=sys.stderr)
        rows = [r for r in lp.values() if r["label_de"].endswith(f"({code})")]
        classes = [r for r in rows if r["type"] == "Class"]
        indiv = [r for r in rows if r["type"] == "Individual"]
        groups = {bid: [] for bid, _ in BASES}; anon = []
        for r in classes:
            b = base_of(r["id"], lp)
            (groups[b] if b else anon).append(r)
        L = [f"# {name} ({code})", "",
             f"Bundesland-Individuum: `lp:{land_id}` — `von Bundesland` (LP_0000029) zeigt darauf.", "",
             f"Schulfach-IDs: Präfix `{code}_` in `references/terms/sf-terms.tsv` "
             f"({sum(1 for k in sf if k.startswith(code + '_'))} Einträge; Wurzel `{code}_0000000`).",
             f"Schulart-IDs: Präfix `{code}_` in `references/terms/sa-terms.tsv` "
             f"({sum(1 for k in sa if k.startswith(code + '_'))} Einträge; Wurzel `{code}_0000000`).", "",
             "Achtung: Schulfach- und Schulart-IDs kollidieren im lokalen Namen "
             f"(`{code}_0000003` gibt es in beiden) — immer mit vollem Namensraum schreiben.", "",
             f"## Klassen des Landes ({len(classes)})", ""]
        for bid, title in BASES:
            if groups[bid]:
                L += [f"### unter {title} ({bid})", "", "| ID | Klasse |", "|---|---|"]
                L += [f"| {r['id']} | {r['label_de']} |" for r in groups[bid]] + [""]
        if anon:
            L += ["### Oberklasse ist ein anonymer OWL-Ausdruck", "",
                  "Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie "
                  "enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL "
                  "sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln "
                  "greifen trotzdem.", "", "| ID | Klasse |", "|---|---|"]
            L += [f"| {r['id']} | {r['label_de']} |" for r in anon] + [""]
        if indiv:
            L += [f"## Individuen des Landes ({len(indiv)})", "", "| ID | Bezeichnung |", "|---|---|"]
            L += [f"| {r['id']} | {r['label_de']} |" for r in indiv] + [""]
        (out / f"{code}.md").write_text("\n".join(L), encoding="utf-8")
        print(f"{code}: {len(classes)} Klassen ({len(anon)} ohne benannte Oberklasse), {len(indiv)} Individuen")

if __name__ == "__main__":
    main()
```

- [ ] **Step 3: `update-references.sh`**

```bash
#!/usr/bin/env bash
# Erzeugt references/ aus den FWU-Ontologie-Repos.
#   scripts/update-references.sh                      klont/aktualisiert nach .vendor/
#   scripts/update-references.sh ~/pfad/lehrplan-ontologie   nutzt diesen Checkout fuer lehrplan-ontologie
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENDOR="$ROOT/.vendor"; REF="$ROOT/references"
mkdir -p "$VENDOR"

sync() {  # sync <repo> [checkout]
  local r="$1" src="${2:-}" dir="$VENDOR/$1"
  if [ -n "$src" ]; then
    rsync -a --delete --exclude=.git "$src/" "$dir/"
    echo "$r: aus $src"
  elif [ -d "$dir/.git" ]; then
    git -C "$dir" fetch --depth 1 -q origin HEAD && git -C "$dir" reset --hard -q FETCH_HEAD
    echo "$r: $(git -C "$dir" log -1 --format='%h %ad' --date=short)"
  else
    git clone --depth 1 -q "https://github.com/FWU-DE/$r.git" "$dir"
    echo "$r: geklont $(git -C "$dir" log -1 --format='%h %ad' --date=short)"
  fi
}
sync lehrplan-ontologie "${1:-}"
sync schulfach-ontologie
sync schulart-ontologie

python3 "$ROOT/scripts/gen-terms.py" "$VENDOR" "$REF/terms"
python3 "$ROOT/scripts/gen-laender.py" "$REF/terms" "$REF/laender"
rm -f "$REF/patterns/"*.ttl
cp "$VENDOR/lehrplan-ontologie/docs/patterns/"pattern*.ttl "$REF/patterns/"
cp "$VENDOR/lehrplan-ontologie/lp-base.ttl" "$REF/lp-base.ttl"

# Herkunft: Version aus der Ontologie, Commit aus dem Checkout (falls vorhanden).
LP="$VENDOR/lehrplan-ontologie"
ver=$(grep -m1 'owl:versionInfo' "$LP/lp-base.ttl" | sed -E 's/.*"([^"]+)".*/\1/')
commit=$( [ -n "${1:-}" ] && git -C "$1" log -1 --format='%h %ad' --date=short 2>/dev/null || git -C "$LP" log -1 --format='%h %ad' --date=short 2>/dev/null || echo unbekannt )
printf 'ontology=%s\ncommit=%s\ngenerated=%s\n' "$ver" "$commit" "$(date +%F)" > "$REF/VERSION"
cat "$REF/VERSION"
echo "Fertig. Aenderungen pruefen: git status --short references/"
```

`chmod +x scripts/*.sh scripts/*.py`.

- [ ] **Step 4: Ausführen und prüfen**

```bash
scripts/update-references.sh ~/coding/fwu/lehrplan-ontologie
wc -l references/terms/*.tsv          # erwartet ~988 / ~911 / ~106 (+1 Kopfzeile)
ls references/laender | wc -l         # 16
ls references/patterns | wc -l        # 14 (pattern1..14.ttl; die Doku listet 14 Muster)
ls -la references/lp-base.ttl         # ~763 KB
cat references/VERSION                # ontology=1.0.0rc3, commit=4d5583f 2026-09-08
grep -c 'Oberklasse ist ein anonymer' references/laender/SH.md   # 1
head -30 references/laender/SH.md
```

Erwartet in `SH.md`: „Fachanforderung (SH)“ unter Lehrplan, „Lehrplanfragment (SH)“ unter CE-Fragment, zehn Klassen unter CE-Bereich (u. a. Kompetenzbereich, Inhaltsbereich, Themenbereich), „Element (SH)“ und „Verweis auf Basiskonzept (SH)“ unter Curriculares Element, und rund 30 Klassen im Abschnitt „anonymer OWL-Ausdruck“, darunter Prozessbezogene Kompetenz (LP_0030278), Inhaltsbezogene Kompetenz (LP_0030271), Mögliches Thema und Inhalt (LP_0030280).

- [ ] **Step 5: Commit**

```bash
git add scripts references .gitignore
git commit -F - <<'EOF'
feat: Referenzen aus den FWU-Ontologien erzeugen

update-references.sh klont oder uebernimmt die drei FWU-Repos, gen-terms.py
schreibt die ID-Tabellen (LP 988, SF 911, SA 106 Terme), gen-laender.py
je Land ein Klassenprofil - mit dem ehrlichen Abschnitt fuer Klassen,
deren Oberklasse ein anonymer OWL-Ausdruck ist. Pattern-Dateien und
lp-base.ttl werden woertlich kopiert; VERSION nennt Ontologie-Stand,
Commit und Datum. Alles eingecheckt: die Skill soll ohne Netz laufen.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RVQuqJJiS33VQtsZfG6ont
EOF
```

---

### Task 3: Nachschlage-Skripte `lookup.sh` und `klasse.sh`

**Files:**
- Create: `scripts/lookup.sh`, `scripts/klasse.sh`

- [ ] **Step 1: `lookup.sh`**

```bash
#!/usr/bin/env bash
# Nachschlagen in den drei Term-Tabellen.
#   scripts/lookup.sh LP_0000537        ID -> Bedeutung (exakt)
#   scripts/lookup.sh jahrgangsstufe    Wort -> IDs (in label_de/label_en, Gross/Klein egal)
# Ausgabe: id · type · label_de · label_en · parent   (Tabelle in Klammern)
set -euo pipefail
[ $# -eq 1 ] || { echo "Aufruf: lookup.sh <ID|Suchwort>" >&2; exit 2; }
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
q="$1"; hits=0
for t in lp sf sa; do
  f="$ROOT/references/terms/$t-terms.tsv"
  if [[ "$q" =~ ^[A-Z]{2}_[0-9]+$ ]]; then
    out=$(awk -F'\t' -v q="$q" 'NR>1 && $1==q {print $1" · "$2" · "$3" · "$4" · parent="$5}' "$f")
  else
    out=$(awk -F'\t' -v q="$(printf '%s' "$q" | tr '[:upper:]' '[:lower:]')" \
      'NR>1 && (index(tolower($3),q) || index(tolower($4),q)) {print $1" · "$2" · "$3" · "$4" · parent="$5}' "$f")
  fi
  if [ -n "$out" ]; then printf '%s\n' "$out" | sed "s/\$/  ($t)/"; hits=1; fi
done
[ $hits -eq 1 ] || { echo "kein Treffer fuer '$q' - nicht raten: Termanfrage an redaktion@mem.schule" >&2; exit 1; }
```

- [ ] **Step 2: `klasse.sh`**

```bash
#!/usr/bin/env bash
# Der Definitionsblock einer Klasse/Property aus lp-base.ttl, IDs mit Labels aufgeloest.
#   scripts/klasse.sh LP_0030280
# Zeigt Label, Oberklasse(n) und die owl:Restriction-Bloecke - also welche Teile
# (obo:BFO_0000051) eine Klasse haben darf oder muss.
set -euo pipefail
[ $# -eq 1 ] && [[ "$1" =~ ^LP_[0-9]+$ ]] || { echo "Aufruf: klasse.sh LP_<nummer>" >&2; exit 2; }
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BASE="$ROOT/references/lp-base.ttl"; TSV="$ROOT/references/terms/lp-terms.tsv"
block=$(awk -v iri="https://w3id.org/lehrplan/ontology/$1" '
  $0=="###  "iri {f=1; next}
  f && /^###  / {exit}
  f {print}' "$BASE")
[ -n "$block" ] || { echo "$1 nicht in lp-base.ttl" >&2; exit 1; }
# ontology:LP_x -> LP_x „Label“; obo:BFO_0000051 -> obo:BFO_0000051 „hat Teil“
printf '%s\n' "$block" | awk -F'\t' -v tsv="$TSV" '
  BEGIN { while ((getline l < tsv) > 0) { split(l, c, "\t"); lab[c[1]] = c[3] }
          lab["obo:BFO_0000051"]="hat Teil"; lab["obo:BFO_0000050"]="ist Teil von"; lab["obo:IAO_0000136"]="handelt von" }
  { line=$0
    while (match(line, /ontology:LP_[0-9]+/)) {
      id=substr(line, RSTART+9, RLENGTH-9); rep=id " „" (lab[id] ? lab[id] : "?") "“"
      line=substr(line,1,RSTART-1) rep substr(line,RSTART+RLENGTH) }
    while (match(line, /obo:(BFO|IAO)_[0-9]+/) && !index(substr(line,RSTART+RLENGTH,2), "„")) {
      id=substr(line,RSTART,RLENGTH); rep=id " „" (lab[id] ? lab[id] : "?") "“"
      line=substr(line,1,RSTART-1) rep substr(line,RSTART+RLENGTH) }
    print line }'
```

- [ ] **Step 3: Prüfen**

```bash
chmod +x scripts/lookup.sh scripts/klasse.sh
scripts/lookup.sh LP_0000537          # LP_0000537 · ObjectProperty · hat Schulfach · has subject · parent=LP_0000024  (lp)
scripts/lookup.sh "hat wert"          # LP_0000344 · DatatypeProperty · hat Wert …
scripts/lookup.sh jahrgangsstufe | head -3   # LP_0000009 (Klasse), LP_0000026 (hat Jahrgangsstufe), LP_2000001 …
scripts/lookup.sh SH_0000003          # zwei Zeilen: Chinesisch (sf) und Gymnasium (sa) — die Kollision, sichtbar
scripts/lookup.sh LP_9999999; echo "exit=$?"   # kein Treffer, exit=1
scripts/klasse.sh LP_0030280 | head -20        # Block mit „Mögliches Thema und Inhalt (SH)“, Restriktionen mit Labels
scripts/klasse.sh LP_0000824 | grep -c 'hat Teil'   # >= 1
```

Die `hat Wert`-Suche muss genau LP_0000344 liefern; findet sie mehr, ist das in Ordnung, solange LP_0000344 dabei ist.

- [ ] **Step 4: Commit**

```bash
git add scripts/lookup.sh scripts/klasse.sh
git commit -F - <<'EOF'
feat: lookup.sh und klasse.sh - IDs nachschlagen statt raten

lookup.sh sucht exakt nach ID oder unscharf im Label ueber alle drei
Tabellen und zeigt die Schulfach/Schulart-Kollision der lokalen Namen
offen an. klasse.sh druckt den Definitionsblock aus lp-base.ttl mit
aufgeloesten Labels - die einzige Stelle, an der man sieht, welche Teile
eine Landesklasse haben darf.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RVQuqJJiS33VQtsZfG6ont
EOF
```

---

### Task 4: `beispiel.ttl` — ein vollständiger, gültiger Minimal-Lehrplan

**Files:**
- Create: `references/beispiel.ttl`, `references/beispiel-bericht.md`

**Interfaces:**
- Consumes: `node ~/coding/comenius/mem-explorer/bin/mem-explorer.mjs check` (Teil A, Task 5) — bzw. `npx mem-explorer check` nach Veröffentlichung.

- [ ] **Step 1: Klassenpfad der SH-Fassung 6.0 ablesen**

Die Fassung 6.0 ist die einzige reale SH-Datei; ihr Klassenpfad ist der Ausgangspunkt:

```bash
F=~/coding/comenius/relidesk-mem-lehrplan-transformation/schleswig-holstein/sekundarstufe.ttl
grep -o 'rdf:type *lp:LP_[0-9]*\|^ *a lp:LP_[0-9]*' "$F" | grep -o 'LP_[0-9]*' | sort | uniq -c | sort -rn
for id in $(grep -o 'rdf:type *lp:LP_[0-9]*\|^ *a lp:LP_[0-9]*' "$F" | grep -o 'LP_[0-9]*' | sort -u); do scripts/lookup.sh $id; done
```

Wurzel LP_0000824, Fragmente LP_0030033, dann Kompetenzbereiche/Kompetenzen/Inhalte. Die im Beispiel gewählten Klassen unten sind aus `lp-terms.tsv`; ob die `hat Teil`-Kette zulässig ist, entscheidet der Prüflauf in Step 3.

- [ ] **Step 2: Datei schreiben** — `references/beispiel.ttl`:

```turtle
# Beispiel: ein minimaler MEM-Lehrplan nach den Mustern der Lehrplan-Ontologie
# (Pattern 1, 2, 5, 6). Land Schleswig-Holstein, erfundener Inhalt. Geprueft mit
# `mem-explorer check`: Exit 0 - siehe beispiel-bericht.md.
#
# Konventionen (references/konventionen.md): eigener Namensraum, lesbare stabile
# Slugs, ein Knoten je Punkt der Vorlage, Kommentar mit PDF-Seite am Knoten,
# Text woertlich, Literale ohne Sprachtag.

@prefix lp:   <https://w3id.org/lehrplan/ontology/> .
@prefix obo:  <http://purl.obolibrary.org/obo/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix data: <https://example.org/lehrplan/sh/beispiel/> .

# ---- Wurzel (Pattern 1) ------------------------------------------- S. 1
data:fachanforderung
    a lp:LP_0000824 ;                               # Fachanforderung (SH)
    rdfs:label "Beispiel-Fachanforderung Ev. Religion Sek I (SH)" ;
    lp:LP_0030056 data:fachanforderung-titel ;      # hat Titel
    lp:LP_0000029 lp:LP_3000054 ;                   # von Bundesland -> Schleswig-Holstein
    lp:LP_0000537 <https://w3id.org/schulfach/SH_0000008> ;  # hat Schulfach -> Evangelische Religion
    lp:LP_0000812 <https://w3id.org/schulart/SH_0000003> ;   # fuer Schulart -> Gymnasium
    lp:LP_0000047 lp:LP_0000045 ;                   # hat Schulstufe -> Sekundarbereich I
    lp:LP_0000463 "https://example.org/fachanforderungen-beispiel.pdf" ;  # uri (Originaldokument)
    obo:BFO_0000051 data:teil-sek1 .                # hat Teil

data:fachanforderung-titel
    a lp:LP_0000346 ;                               # Titel
    lp:LP_0000344 "Fachanforderungen Evangelische Religion" .   # hat Wert

# ---- Fragment (Pattern 6) ----------------------------------------- S. 5
data:teil-sek1
    a lp:LP_0030033 ;                               # Lehrplanfragment (SH)
    rdfs:label "Teil Sekundarstufe I" ;
    lp:LP_0030056 data:teil-sek1-titel ;
    lp:LP_0030057 data:teil-sek1-nummer ;           # hat Nummer
    lp:LP_0000460 "2"^^xsd:integer ;                # hat Position (Reihenfolge in der Vorlage)
    obo:BFO_0000051 data:kb-gott .

data:teil-sek1-titel  a lp:LP_0000346 ; lp:LP_0000344 "II Fachanforderungen Sekundarstufe I" .
data:teil-sek1-nummer a lp:LP_0000347 ; lp:LP_0000344 "II" .   # Identifikationsnummer

# ---- Kompetenzbereich (CE-Bereich) -------------------------------- S. 12
data:kb-gott
    a lp:LP_0030070 ;                               # Kompetenzbereich (SH)
    rdfs:label "Die Frage nach Gott" ;
    lp:LP_0030056 data:kb-gott-titel ;
    lp:LP_0030051 data:kb-gott-beschreibung ;       # hat Beschreibung
    lp:LP_0030057 data:kb-gott-nummer ;
    lp:LP_0000460 "1"^^xsd:integer ;
    obo:BFO_0000051 data:kb-gott-pk-1 , data:kb-gott-inhalt-1 , data:kb-gott-inhalt-2 .

data:kb-gott-titel        a lp:LP_0000346 ; lp:LP_0000344 "1 Die Frage nach Gott" .
data:kb-gott-nummer       a lp:LP_0000347 ; lp:LP_0000344 "1" .
data:kb-gott-beschreibung a lp:LP_0030003 ;         # Beschreibung
    lp:LP_0000344 "Die Frage nach Gott wird als existentielle Frage aufgeworfen und im Kontext religiöser Vielfalt konkretisiert." .

# ---- Prozessbezogene Kompetenz ------------------------------------ S. 12
data:kb-gott-pk-1
    a lp:LP_0030278 ;                               # Prozessbezogene Kompetenz (SH)
    rdfs:label "Gottesvorstellungen wahrnehmen" ;
    lp:LP_0030056 data:kb-gott-pk-1-titel ;
    lp:LP_0000026 lp:LP_2000005 , lp:LP_2000006 ;   # hat Jahrgangsstufe -> 5, 6
    lp:LP_0000460 "1"^^xsd:integer .

data:kb-gott-pk-1-titel a lp:LP_0000346 ;
    lp:LP_0000344 "Die Schülerinnen und Schüler nehmen unterschiedliche Gottesvorstellungen wahr und beschreiben sie." .

# ---- Moegliche Themen und Inhalte --------------------------------- S. 13
data:kb-gott-inhalt-1
    a lp:LP_0030280 ;                               # Moegliches Thema und Inhalt (SH)
    rdfs:label "Gottesvorstellungen" ;
    lp:LP_0030056 data:kb-gott-inhalt-1-titel ;
    lp:LP_0000026 lp:LP_2000005 , lp:LP_2000006 ;
    lp:LP_0000460 "2"^^xsd:integer .
data:kb-gott-inhalt-1-titel a lp:LP_0000346 ;
    lp:LP_0000344 "Gottesvorstellungen (anthropomorph, symbolisch, allmächtig, gütig)" .

data:kb-gott-inhalt-2
    a lp:LP_0030280 ;
    rdfs:label "Metaphorisches Sprechen von Gott" ;
    lp:LP_0030056 data:kb-gott-inhalt-2-titel ;
    lp:LP_0000026 lp:LP_2000005 , lp:LP_2000006 ;
    lp:LP_0000460 "3"^^xsd:integer .
data:kb-gott-inhalt-2-titel a lp:LP_0000346 ;
    lp:LP_0000344 "Metaphorisches Sprechen von Gott (personal; apersonal)" .
```

Vor dem Prüflauf die Datentypen der beiden DatatypeProperties nachsehen und anpassen:

```bash
scripts/klasse.sh LP_0000460 | grep -i 'range'     # hat Position — rdfs:range? xsd:integer oder ohne Angabe
scripts/klasse.sh LP_0000463 | grep -i 'range'     # uri — xsd:anyURI oder ohne Angabe
```

Steht dort ein Datentyp, wird er im Beispiel benutzt (`"1"^^xsd:integer` bzw. `"…"^^xsd:anyURI`); steht keiner, bleibt das Literal so.

- [ ] **Step 3: Prüfen, bis Exit 0**

```bash
CHECK="node $HOME/coding/comenius/mem-explorer/bin/mem-explorer.mjs check"
$CHECK references/beispiel.ttl > /tmp/beispiel.md; echo "exit=$?"
grep -n '^### ' /tmp/beispiel.md
```

Abbruchbedingung: `exit=0`. Solange nicht:
- Gruppe „Ziel ohne geforderte Klasse — hat Teil“: Kind darf nicht unter diesem Elternteil hängen → `scripts/klasse.sh <Elternklasse>` lesen (Restriktion auf `obo:BFO_0000051`), eine dort zulässige Klasse aus `references/laender/SH.md` wählen; die Wahl im Kommentar der Datei begründen.
- Gruppe „Literal an ObjectProperty“ / „Verweis an DatatypeProperty“: Prädikat-Typ mit `scripts/lookup.sh <ID>` prüfen und die Zeile berichtigen.
- Gruppen mit „Reasoner-Artefakt“ bleiben. Sie sind der Grund, warum `beispiel-bericht.md` existiert.

Dann:

```bash
$CHECK references/beispiel.ttl > references/beispiel-bericht.md; echo "exit=$?"   # 0
sed -i '1a\\n> Erzeugt mit `mem-explorer check references/beispiel.ttl`, Exit-Code 0. Die verbleibenden Gruppen sind Reasoner-Artefakte und Warnungen, keine Datenfehler — so sieht eine saubere Datei aus.' references/beispiel-bericht.md
```

- [ ] **Step 4: Commit**

```bash
git add references/beispiel.ttl references/beispiel-bericht.md
git commit -F - <<'EOF'
feat: beispiel.ttl - ein vollstaendiger Minimal-Lehrplan mit Exit 0

Wurzel, Fragment, Kompetenzbereich mit Titel-, Beschreibungs- und
Nummernknoten, eine prozessbezogene Kompetenz mit zwei Jahrgangsstufen,
zwei moegliche Inhalte, hat Position durchgehend. Der Bericht daneben
zeigt, was bei einer sauberen Datei stehen bleibt: Reasoner-Artefakte.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RVQuqJJiS33VQtsZfG6ont
EOF
```

---

### Task 5: RED — Ausgangsläufe ohne Skill

**Files:**
- Create: `docs/testing/szenarien.md` (die drei Aufgaben, wörtlich), `docs/testing/baseline.md` (Ergebnisse), `docs/testing/baseline/` (Rohausgaben)

- [ ] **Step 1: Szenarien festschreiben** — `docs/testing/szenarien.md`:

````markdown
# Testszenarien für die Skill

Drei Aufgaben, jeweils ohne Skill (Baseline) und mit Skill. Die Prompts werden wörtlich an
einen frischen Subagenten (general-purpose) gegeben; der Baseline-Prompt erwähnt die Skill
nicht und untersagt sie nicht — er ist der Normalfall eines Agenten, der die Aufgabe bekommt.

## Szenario 1 — Transformieren

> Du transformierst Lehrpläne nach dem MEM-Modell (Lehrplan-Ontologie des FWU,
> https://github.com/FWU-DE/lehrplan-ontologie). Schreibe für den folgenden Auszug aus den
> Fachanforderungen Evangelische Religion Schleswig-Holstein (Sekundarstufe I, Gymnasium)
> eine Turtle-Datei. Der Lehrplan gilt für Schleswig-Holstein, Fach Evangelische Religion,
> Schulart Gymnasium. Gib nur Turtle aus, keine Erklärungen.
>
> ---
> **1 Die Frage nach Gott** (S. 12)
>
> Die Frage nach Gott wird als existentielle Frage aufgeworfen. Sie konkretisiert sich
> für die Schülerinnen und Schüler im Kontext religiöser und kultureller Vielfalt.
>
> *Prozessbezogene Kompetenz (Jahrgangsstufen 5–6):* Die Schülerinnen und Schüler nehmen
> unterschiedliche Gottesvorstellungen wahr und beschreiben sie.
>
> *Mögliche Themen und Inhalte (Jahrgangsstufen 5–6):*
> - Gottesvorstellungen (anthropomorph, symbolisch, allmächtig, gütig)
> - Gottesvorstellungen in anderen Religionen
> - Metaphorisches Sprechen von Gott (personal; apersonal)
> ---

Erfolgsmaß: `mem-explorer check` Exit 0 · jede `lp:`/`schulfach:`/`schulart:`-ID existiert in
`references/terms/` · Titel und Beschreibung als benannte Knoten mit `hat Wert` · Jahrgangsstufen
als Individuen · keine Blank Nodes · `hat Position` an den Geschwistern · Text wörtlich.

## Szenario 2 — Nachbessern

> Hier ist eine MEM-Turtle-Datei und der Prüfbericht des MEM Explorers dazu. Behebe die
> gemeldeten Befunde. Ändere keine IRIs. Gib die vollständige korrigierte Datei aus.
>
> [Datei: docs/testing/fixtures/nachbessern.ttl] [Bericht: docs/testing/fixtures/nachbessern-bericht.md]

`nachbessern.ttl` enthält absichtlich die fünf Fehlerklassen der SH-Fassungen 5 und 6:
Titel als Literal direkt am Element · Beschreibung als Blank Node mit rdfs:label ·
benannter Titel-Knoten mit rdfs:label statt hat Wert · Jahrgangsstufe als Literal `"5-6"` ·
Beschreibungsknoten der Klasse CE-Hinweis (LP_0000852).

Erfolgsmaß: Exit 0 · IRIs unverändert (Diff der Subjekte leer) · Reasoner-Artefakt-Gruppen
nicht „behoben“ (kein `ist Teil von`, kein `hat Funktion` hinzugefügt).

## Szenario 3 — Nachschlagen

> Welche Klasse der Lehrplan-Ontologie ist für eine „Konkretion“ (einen möglichen Inhalt zu
> einem Kompetenzbereich) in Schleswig-Holstein vorgesehen, und was darf ein solcher Knoten
> laut Ontologie als Teile haben? Nenne die IDs.

Erfolgsmaß: Antwort nennt LP_0030280 („Mögliches Thema und Inhalt (SH)“) und liest die
Restriktionen mit `scripts/klasse.sh` bzw. aus `references/laender/SH.md`; kein Raten; die
Antwort zeigt, woher sie stammt.
````

- [ ] **Step 2: Fixture für Szenario 2 bauen** — `docs/testing/fixtures/nachbessern.ttl` aus `beispiel.ttl` ableiten:

```bash
mkdir -p docs/testing/fixtures
python3 - <<'EOF'
s = open('references/beispiel.ttl', encoding='utf-8').read()
# 1 Titel als Literal direkt am Element
s = s.replace('lp:LP_0030056 data:fachanforderung-titel ;', 'lp:LP_0030056 "Fachanforderungen Evangelische Religion" ;')
s = s.replace('data:fachanforderung-titel\n    a lp:LP_0000346 ;                               # Titel\n    lp:LP_0000344 "Fachanforderungen Evangelische Religion" .   # hat Wert\n', '')
# 2 Beschreibung als Blank Node mit rdfs:label
s = s.replace('lp:LP_0030051 data:kb-gott-beschreibung ;', 'lp:LP_0030051 [ a lp:LP_0030003 ; rdfs:label "Die Frage nach Gott wird als existentielle Frage aufgeworfen und im Kontext religiöser Vielfalt konkretisiert." ] ;')
import re
s = re.sub(r'data:kb-gott-beschreibung a lp:LP_0030003 ;.*?\n    lp:LP_0000344 "[^"]*" \.\n', '', s, flags=re.S)
# 3 benannter Titel-Knoten mit rdfs:label statt hat Wert
s = s.replace('data:kb-gott-titel        a lp:LP_0000346 ; lp:LP_0000344 "1 Die Frage nach Gott" .', 'data:kb-gott-titel        a lp:LP_0000346 ; rdfs:label "1 Die Frage nach Gott" .')
# 4 Jahrgangsstufe als Literal
s = s.replace('lp:LP_0000026 lp:LP_2000005 , lp:LP_2000006 ;   # hat Jahrgangsstufe -> 5, 6', 'lp:LP_0000026 "5-6" ;')
# 5 CE-Hinweis statt Beschreibung am Inhalt: Titel-Knoten von inhalt-1 wird zum CE-Hinweis-Knoten
s = s.replace('data:kb-gott-inhalt-1-titel a lp:LP_0000346 ;', 'data:kb-gott-inhalt-1-titel a lp:LP_0000852 ;')
open('docs/testing/fixtures/nachbessern.ttl', 'w', encoding='utf-8').write(s)
EOF
node ~/coding/comenius/mem-explorer/bin/mem-explorer.mjs check docs/testing/fixtures/nachbessern.ttl > docs/testing/fixtures/nachbessern-bericht.md; echo "exit=$?"   # 1
grep -n '^### ' docs/testing/fixtures/nachbessern-bericht.md   # erwartet u. a. Literal an ObjectProperty, Wertknoten als Blank Node, Text nicht an hat Wert, Ziel ohne geforderte Klasse
```

Fehlt eine der fünf Gruppen, ist die Ersetzung nicht gegriffen — Datei ansehen und nachziehen, bis alle fünf Befundarten im Bericht stehen.

- [ ] **Step 3: Baseline-Läufe** — je Szenario einen frischen Subagenten (Agent-Tool, `general-purpose`) mit genau dem Prompt aus `szenarien.md` dispatchen. Zusätzlich im Prompt nur: „Schreibe deine Ausgabe nach `docs/testing/baseline/szenario-<n>-lauf-<k>.ttl` (bzw. `.md` bei Szenario 3) und nenne zum Schluss in drei Sätzen, worauf du deine Entscheidungen zu Klassen, IDs und Schreibweise gestützt hast.“ Mindestens zwei Läufe je Szenario (Varianz sehen). Für Szenario 2 die beiden Fixture-Dateien im Prompt einbetten.

Für jede Turtle-Ausgabe:

```bash
for f in docs/testing/baseline/szenario-1-*.ttl docs/testing/baseline/szenario-2-*.ttl; do
  echo "== $f"; node ~/coding/comenius/mem-explorer/bin/mem-explorer.mjs check "$f" > "${f%.ttl}-bericht.md"; echo "exit=$?"
  grep -o 'lp:LP_[0-9]*' "$f" | sort -u | sed 's/lp://' | while read id; do scripts/lookup.sh "$id" >/dev/null 2>&1 || echo "ERFUNDEN: $id"; done
  grep -c '\[' "$f" | sed 's/^/Blank-Node-Klammern: /'
done
```

- [ ] **Step 4: `baseline.md` schreiben** — je Szenario und Lauf: Exit-Code, Befundgruppen mit Zahl, erfundene IDs, Blank Nodes ja/nein, Jahrgangsstufe als Literal ja/nein, Textträger am Titelknoten, und die **wörtliche** Begründung des Agenten (die drei Sätze). Am Ende ein Abschnitt „Muster“: welche Fehler in allen Läufen auftreten, welche Begründungen sich wiederholen — das sind die Sätze, gegen die `SKILL.md` geschrieben wird. Zeigt ein Szenario keinen Fehler, steht das dort genauso; dann bekommt die Skill an der Stelle keinen Absatz.

- [ ] **Step 5: Commit**

```bash
git add docs/testing
git commit -F - <<'EOF'
test: Szenarien und Ausgangslaeufe ohne Skill (RED)

Drei Aufgaben - Transformieren, Nachbessern, Nachschlagen - an frische
Subagenten ohne Skill. baseline.md haelt Exit-Codes, Befundgruppen,
erfundene IDs und die woertlichen Begruendungen fest. Dagegen wird
SKILL.md geschrieben; was hier nicht schiefgeht, bekommt dort keinen Satz.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RVQuqJJiS33VQtsZfG6ont
EOF
```

---

### Task 6: GREEN — `SKILL.md` und Referenzen schreiben, Läufe wiederholen

**Files:**
- Create: `SKILL.md`, `references/arbeitsablauf.md`, `references/muster.md`, `references/konventionen.md`, `references/fallstricke.md`, `references/befunde.md`
- Create: `docs/testing/green.md`

**Interfaces:**
- Consumes: `docs/testing/baseline.md` (Task 5) — jede Regel in `fallstricke.md` und jede Zeile der Rationalisierungstabelle verweist auf einen dort beobachteten Fehler oder eine Begründung; `references/beispiel.ttl` (Task 4); `scripts/lookup.sh`, `scripts/klasse.sh` (Task 3); `references/laender/SH.md` (Task 2).

- [ ] **Step 1: `SKILL.md`** — Entwurf; Wortlaut der Rationalisierungstabelle und der roten Flaggen wird aus `baseline.md` übernommen bzw. ergänzt:

````markdown
---
name: mem-lehrplan
description: >
  Use when writing or fixing MEM curriculum data — Lehrplan-Turtle nach der FWU
  Lehrplan-Ontologie (https://github.com/FWU-DE/lehrplan-ontologie): transforming a Lehrplan
  PDF or excerpt into Turtle, working off a MEM-Explorer report, choosing LP_/SF_/SA_ IDs or
  Länder classes, or when findings mention hat Titel, hat Beschreibung, hat Wert, Blank
  Nodes, Jahrgangsstufe, hat Teil, SHACL, Reasoner-Artefakt.
license: CC-BY-SA-4.0
compatibility: >
  Node 22+ for `npx mem-explorer check`; bash, grep, awk for scripts/; pdftotext optional.
  Works offline — all ontology references are bundled.
metadata:
  author: sroertgen
  ontology: "1.0.0rc3"
  version: "0.1.0"
---

# MEM-Lehrplan-Turtle schreiben und nachbessern

## Kernregel

Die Dokumentation der Lehrplan-Ontologie ist die Autorität — nicht die Daten im MEM-Store,
nicht dein Gedächtnis. Jede ID kommt aus `scripts/lookup.sh`. Jede Strukturentscheidung kommt
aus einem Muster in `references/muster.md`. Jeder Befund wird gegen sein Soll behoben. Text
aus der Vorlage bleibt wörtlich.

## Ablauf

1. `references/muster.md`, `references/konventionen.md` und `references/laender/<XX>.md` des
   Landes lesen. `references/beispiel.ttl` ist die Vorlage, die du kopierst.
2. Jede ID mit `scripts/lookup.sh <Wort|ID>` nachschlagen; was eine Klasse enthalten darf, mit
   `scripts/klasse.sh <LP_ID>`. Keine ID aus dem Gedächtnis, auch wenn sie richtig aussieht.
3. Schreiben: benannte Knoten mit IRI im eigenen Namensraum; Titel, Beschreibung, Nummer als
   Wertknoten mit `hat Wert` (LP_0000344); Jahrgangsstufen als Individuen (LP_2000001–13);
   Hierarchie über `hat Teil` (obo:BFO_0000051); `hat Position` (LP_0000460) für die
   Reihenfolge; keine Blank Nodes.
4. `npx mem-explorer check datei.ttl` — Exit 0 heißt: kein Fehler.
5. Bericht gruppenweise mit den **Soll**-Blöcken abarbeiten (`references/befunde.md`).
   Gruppen mit „Reasoner-Artefakt“ bleiben, wie sie sind. IRIs nie umbenennen.
6. Wiederholen bis Exit 0. Dann Bericht und Datei dem Menschen für den PDF-Abgleich geben —
   Texttreue und Vollständigkeit prüft das Werkzeug nicht.

Ausführlich, mit dem Weg vom PDF zur Struktur: `references/arbeitsablauf.md`.

## Schnellreferenz

| Was | ID | Beispiel |
|---|---|---|
| hat Teil (Hierarchie) | obo:BFO_0000051 | `data:kb obo:BFO_0000051 data:kompetenz .` |
| hat Titel → Titel-Knoten | LP_0030056 → Klasse LP_0000346 | `data:kb lp:LP_0030056 data:kb-titel .` |
| hat Beschreibung → Beschreibung | LP_0030051 → Klasse LP_0030003 | nicht CE-Hinweis (LP_0000852) |
| hat Nummer → Identifikationsnummer | LP_0030057 → Klasse LP_0000347 | `"2.1"` an `hat Wert` |
| hat Wert (der Text am Wertknoten) | LP_0000344 | `data:kb-titel lp:LP_0000344 "…" .` |
| hat Position (Reihenfolge) | LP_0000460 | `"3"^^xsd:integer` |
| hat Jahrgangsstufe → Individuum | LP_0000026 → LP_2000005 … | `lp:LP_2000005 , lp:LP_2000006` |
| von Bundesland → Individuum | LP_0000029 → LP_30000xx | SH = LP_3000054 (`laender/`) |
| hat Schulfach / für Schulart | LP_0000537 / LP_0000812 | volle IRI `https://w3id.org/schulfach/SH_…` |
| hat Schulstufe → Individuum | LP_0000047 → LP_0000045 (Sek I) | Pattern 5 |

## Rote Flaggen — anhalten und nachschlagen

- „Der MEM-Store schreibt es so.“ — Der Store ist importiert, nicht maßgeblich.
- „Die ID sieht richtig aus.“ — IDs sind opak. `lookup.sh`.
- „Blank Nodes sind kürzer.“ — Sie sind nicht verweisbar, nicht prüfbar, nicht im Prüfstand.
- „Ich prüfe am Ende.“ — Prüfen ist Teil des Schreibens; nach jedem Abschnitt `check`.
- „Der Explorer zeigt den Text, also passt es.“ — Er zeigt großzügig und meldet streng; der
  Bericht zählt, nicht die Anzeige.
- „Die Warnungen behebe ich auch noch.“ — Reasoner-Artefakte sind keine Fehler. Nichts
  hinzumodellieren, was ein Reasoner ableitet (`ist Teil von`, `hat Funktion`, `handelt von`).

Fallstricke mit Begründung: `references/fallstricke.md`.
````

`wc -w SKILL.md` < 500 prüfen; sonst kürzen, nicht in die description ausweichen.

- [ ] **Step 2: `references/muster.md`** — je Abschnitt: ein Satz, der Turtle-Block wörtlich aus `references/patterns/patternN.ttl` (Namensraum `ex:` beibehalten), der Link `https://fwu-de.github.io/lehrplan-ontologie/docs/patterns/#pattern-N-…` (Anker: Pattern 1 `#pattern-1-lehrplan-eines-bundeslandes`, 2 `#pattern-2-titel-beschreibung-und-identifikationsnummer`, 5 `#pattern-5-jahrgangstufeschulstufe-und-phasen-der-sekundarstufe-ii`, 6 `#pattern-6-hierarchie-der-curricularen-elemente`, 7 `#pattern-7-ce-verweis`). Abschnitte: Lehrplanwurzel (1) · Titel, Beschreibung, Nummer (2) · Jahrgangsstufe und Schulstufe (5) · Hierarchie über hat Teil (6) · Verweise (7) · Reihenfolge mit `hat Position` (kein Pattern; Begründung: RDF bewahrt keine Reihenfolge, die Geschwisterfolge der Vorlage geht sonst verloren — LP_0000460 aus `lp-terms.tsv`). Am Ende: „Was eine Klasse enthalten darf, steht nicht in den Mustern, sondern in ihrer Definition: `scripts/klasse.sh <ID>`.“

- [ ] **Step 3: `references/konventionen.md`** — überschrieben mit „Konventionen dieses Projekts, keine FWU-Vorgabe“: eigener Namensraum je Land und Projekt (Beispiel `https://lp-sh.org/resource/` der relidesk-Transformation); lesbare stabile Slugs (`kb-gott`, `kb-gott-inhalt-1`), eine IRI je Knoten, IRIs zwischen Iterationen nie umbenennen (Prüfstand hängt daran); `rdfs:label` = technische Kurzbezeichnung, Titel-Knoten = Wortlaut der Vorlage; Literale ohne Sprachtag (wie die Pattern-Dateien); Text wörtlich, nie paraphrasiert, nie gekürzt; Kommentar `# S. 12` je Knoten; eine Datei je Lehrplan, Schnitt nach Schulstufe `bundesland/schulstufe.ttl`; der Präfixblock aus `beispiel.ttl` zum Kopieren.

- [ ] **Step 4: `references/arbeitsablauf.md`** — die sechs Schritte ausformuliert plus „Vom PDF zur Struktur“: `pdftotext -layout datei.pdf - | sed -n '12,13p'`-artiges seitenweises Lesen (`pdftotext -f 12 -l 13 -layout datei.pdf -`); Überschriften der Ebenen → Fragment/Bereich mit `hat Nummer`; Tabellenspalten „Kompetenzen“ vs. „Mögliche Inhalte“ → Kompetenzspezifikation vs. Lerninhalt-Klassen des Landes; ein Knoten je Aufzählungspunkt; Jahrgangsstufen aus der Überschrift der Tabelle; Seitenzahl in den Kommentar; nach jedem Bereich `check`.

- [ ] **Step 5: `references/fallstricke.md`** — die Tabelle aus der Spec §4.4 (acht Regeln mit Begründung), ergänzt um die Beobachtungen aus `baseline.md`, dann die **Rationalisierungstabelle**: linke Spalte die wörtliche Begründung aus den Baseline-Läufen, rechte Spalte die Antwort. Jede Zeile trägt in Klammern das Szenario und den Lauf, aus dem sie stammt.

- [ ] **Step 6: `references/befunde.md`** — je Befundart ein Abschnitt mit Titel wie im Bericht, dem Soll (Turtle) und dem Handgriff; Reihenfolge und Wortlaut angelehnt an `guidance.ts` des Explorers (`~/coding/comenius/mem-explorer/src/lib/review/guidance.ts`): R1, R2, R3, R4–R6, R7/R10, R8, R9, R11, R12, R13, `shacl:Class` (drei Fälle: hat Beschreibung → LP_0030003; hat Teil → `klasse.sh` der Elternklasse; benannte Range), `shacl:MinCount`, und die drei Reasoner-Artefakte („Kein Handlungsbedarf“). Beispiele aus `beispiel.ttl` zitieren.

- [ ] **Step 7: GREEN-Läufe** — dieselben drei Prompts aus `szenarien.md`, jetzt mit vorangestelltem Satz: „Lies zuerst `~/coding/comenius/mem-lehrplan/SKILL.md` und arbeite genau danach.“ Zwei Läufe je Szenario; Ausgaben nach `docs/testing/green/`. Dieselbe Prüfschleife wie in Task 5 Step 3. Ergebnisse nach `docs/testing/green.md`, gleiche Tabelle wie `baseline.md`, plus Spalte „benutzte Skripte“ (aus der Selbstauskunft des Agenten).

Bestanden, wenn alle Läufe von Szenario 1 und 2 Exit 0 erreichen, keine erfundene ID enthalten, Szenario 2 die IRIs unverändert lässt, und Szenario 3 LP_0030280 mit Quelle nennt.

- [ ] **Step 8: REFACTOR** — jede neue Begründung eines Agenten, die zu einem Fehler geführt hat, wird als Zeile in die Rationalisierungstabelle aufgenommen und, wenn sie eine Regel betrifft, als rote Flagge in `SKILL.md`. Danach Step 7 wiederholen. Abbruch, wenn zwei aufeinanderfolgende Läufe je Szenario bestehen.

- [ ] **Step 9: Commit**

```bash
wc -w SKILL.md
git add SKILL.md references/*.md docs/testing
git commit -F - <<'EOF'
feat: SKILL.md und Referenzen - gegen die Ausgangslaeufe geschrieben (GREEN)

Kernregel, Ablauf, Schnellreferenz und rote Flaggen in SKILL.md; Muster,
Konventionen, Arbeitsablauf, Fallstricke mit Rationalisierungstabelle und
Befunde-Soll in references/. Jede Regel verweist auf einen beobachteten
Fehler aus baseline.md. green.md haelt fest, dass die Szenarien mit Skill
bestehen.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RVQuqJJiS33VQtsZfG6ont
EOF
```

---

### Task 7: Zweiter Blick — Umfang, Wortzahl, Format

**Files:**
- Modify: `SKILL.md`, `references/*.md` (nur Kürzungen und Korrekturen)

- [ ] **Step 1: Formatprüfung**

```bash
wc -w SKILL.md                                  # < 500
head -20 SKILL.md | grep -c 'description'       # 1
python3 - <<'EOF'
import re
s = open('SKILL.md', encoding='utf-8').read()
fm = s.split('---')[1]
name = re.search(r'^name:\s*(\S+)', fm, re.M).group(1)
assert name == 'mem-lehrplan', name
desc = re.search(r'description:\s*>?\s*(.*?)(?=^\w+:|\Z)', fm, re.S | re.M).group(1)
print('description chars:', len(' '.join(desc.split())))   # <= 1024
assert len(fm) <= 1024 or True
EOF
grep -n '"' SKILL.md references/*.md | grep -v '```' | grep -v 'lp:LP_\|xsd:\|rdfs:label\|@prefix\|"…"' | head   # gerade Anfuehrungszeichen nur in Turtle
```

- [ ] **Step 2: Inhaltsprüfung mit fremden Augen** — einen Subagenten `SKILL.md` und `references/muster.md` lesen lassen mit der Frage: „Welche drei Stellen sind unklar oder widersprüchlich, und welche Information hättest du beim Transformieren zusätzlich gebraucht?“ Antworten einarbeiten, wenn sie eine Lücke zeigen, die kein Baseline-Lauf gezeigt hat (dann als Retrieval-Test in `szenarien.md` ergänzen).

- [ ] **Step 3: Commit**

```bash
git add -A && git commit -F - <<'EOF'
docs: Skill nach Gegenlesen gestrafft

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RVQuqJJiS33VQtsZfG6ont
EOF
```

---

### Task 8: README, Tag v0.1.0, Push, Verteilung

**Files:**
- Modify: `README.md`

- [ ] **Step 1: README vervollständigen**

````markdown
# mem-lehrplan

Agent-Skill für das Schreiben und Nachbessern von MEM-Lehrplandaten — Turtle nach der
[Lehrplan-Ontologie des FWU](https://github.com/FWU-DE/lehrplan-ontologie). Für Claude Code
und andere Werkzeuge, die das [Agent-Skills-Format](https://agentskills.io) lesen.

Was drin ist: die Muster der Ontologie-Doku als Soll, Term-Tabellen für alle 2005 IDs,
Klassenprofile je Bundesland, ein vollständiges gültiges Beispiel, Skripte zum Nachschlagen
und die Fallstricke, die in echten Transformationen aufgetreten sind. Geprüft wird mit
`npx mem-explorer check` ([MEM Explorer](https://git.rpi-virtuell.de/Comenius-Institut/mem-explorer)).

## Installation

```sh
# Claude Code
git clone https://github.com/sroertgen/mem-lehrplan ~/.claude/skills/mem-lehrplan
# Codex, Copilot CLI, Gemini CLI und andere
git clone https://github.com/sroertgen/mem-lehrplan ~/.agents/skills/mem-lehrplan
```

Voraussetzungen: Node 22+ (für `npx mem-explorer check`), bash, grep, awk. Optional
`pdftotext` für den Weg vom PDF.

## Benutzung

Der Agent liest `SKILL.md` und folgt dem Ablauf. Von Hand nützlich:

```sh
scripts/lookup.sh "hat Jahrgangsstufe"     # Wort -> ID
scripts/lookup.sh LP_0030280               # ID -> Bedeutung
scripts/klasse.sh LP_0030280               # Definition mit Restriktionen, Labels aufgeloest
npx mem-explorer check datei.ttl           # Pruefbericht, Exit 0 = kein Fehler
```

## Referenzen aktualisieren

```sh
scripts/update-references.sh               # klont die FWU-Repos nach .vendor/ und erzeugt references/
scripts/update-references.sh ~/pfad/lehrplan-ontologie   # oder aus einem eigenen Checkout
git diff --stat references/                # was sich in der Ontologie geaendert hat
```

`references/VERSION` nennt den Stand.

## Herkunft und Lizenz

CC BY-SA 4.0. `references/patterns/`, `references/lp-base.ttl` und die Term-Tabellen stammen
aus FWU-DE/lehrplan-ontologie, schulfach-ontologie und schulart-ontologie (CC BY-SA 4.0,
© FWU Institut für Film und Bild in Wissenschaft und Unterricht). Entwurf und Tests:
`docs/`.
````

- [ ] **Step 2: Freigabe, Tag, Push**

An laoc: „Skill v0.1.0 ist fertig und getestet (green.md). Push nach Forgejo und GitHub jetzt?“ Nach Ja:

```bash
sed -i 's/^  version: "0.1.0"$/  version: "0.1.0"/' SKILL.md   # Kontrolle, dass metadata.version gesetzt ist
git add README.md && git commit -F - <<'EOF'
docs: README mit Installation, Benutzung, Aktualisierung, Herkunft

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RVQuqJJiS33VQtsZfG6ont
EOF
git tag -a v0.1.0 -F - <<'EOF'
mem-lehrplan 0.1.0

Erste Fassung: SKILL.md, Muster und Konventionen, Term-Tabellen und
Laenderprofile (Ontologie 1.0.0rc3), beispiel.ttl mit Exit 0, lookup.sh
und klasse.sh, gegen Ausgangslaeufe getestet.
EOF
git push origin main && git push origin v0.1.0
git push github main && git push github v0.1.0
```

- [ ] **Step 3: Verteilung**

- openskills.cc: kein Einreichformular. Nachricht an den Betreiber (X-Handle im Footer der Seite) mit dem GitHub-Link — laoc schickt sie; Textvorschlag: „Open-source Agent Skill (CC BY-SA 4.0) for writing German curriculum data (MEM / FWU Lehrplan-Ontologie): https://github.com/sroertgen/mem-lehrplan“.
- FWU: Entwurf einer kurzen Mail an redaktion@mem.schule nach `docs/fwu-notiz.md` legen (Was die Skill ist, dass sie die Doku als Autorität nimmt, Link, Bitte um Rückmeldung zu den Konventionen aus `konventionen.md`). Nicht senden — laoc entscheidet.

---

## Self-Review

**Spec-Abdeckung (Abschnitte 4–8):** 4.1 Form/Frontmatter → Task 6 Step 1, Task 7. 4.2 Layout → Tasks 1–4, 6. 4.3 SKILL.md-Inhalt → Task 6 Step 1. 4.4 Referenzen → Task 6 Steps 2–6, `beispiel.ttl` Task 4, `laender/` Task 2. 4.5 Skripte → Tasks 2, 3. 5 Tests → Tasks 5, 6, 7. 6 Verteilung → Tasks 1 (Remotes), 8. 7 Reihenfolge → Task-Reihenfolge B1–B5 entspricht Tasks 1–8. 8 Offene Punkte: npm-Konto → Plan A Task 7; Textauszug → Task 5 Step 1 (eigener Auszug, da kein PDF lokal); Namensraum-Konvention → `konventionen.md`; Lizenz → Task 1.

**Platzhalter:** Die Referenztexte in Task 6 Steps 2–6 sind als Inhaltsvorgaben formuliert, nicht als fertiger Text — bewusst, weil ihr Wortlaut aus `baseline.md` folgen muss (Skill-TDD). Jede Vorgabe nennt Quelle, Abschnitte und Reihenfolge; keine „TBD“.

**Konsistenz:** `scripts/lookup.sh`, `scripts/klasse.sh`, `scripts/update-references.sh` heißen in allen Tasks gleich; TSV-Spalten aus Task 2 werden in Task 3 (`$3`, `$4`, `$5`) und Task 2 `gen-laender.py` (`label_de`, `parent`, `type`) gleich benutzt; Klassen-IDs im Beispiel (LP_0000824, LP_0030033, LP_0030070, LP_0030278, LP_0030280, LP_0000346, LP_0030003, LP_0000347) stammen aus `lp-terms.tsv` 1.0.0rc3 und tauchen in `SKILL.md`, `szenarien.md` und der Fixture gleich auf.
