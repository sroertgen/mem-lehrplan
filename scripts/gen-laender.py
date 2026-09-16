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
        groups = {bid: [] for bid, _ in BASES}; anon = []; other = []
        for r in classes:
            b = base_of(r["id"], lp)
            if b:
                groups[b].append(r)
            elif r["parent"]:
                other.append(r)
            else:
                anon.append(r)
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
                L += [f"### unter {title} ({bid})", "",
                      "| ID | Klasse | Hinweis (editorialNote) |", "|---|---|---|"]
                L += [f"| {r['id']} | {r['label_de']} | {r.get('note', '')} |" for r in groups[bid]] + [""]
        if anon:
            L += ["### Oberklasse ist ein anonymer OWL-Ausdruck", "",
                  "Für diese Klassen steht in der Tabelle keine benannte Oberklasse. Was sie "
                  "enthalten dürfen und wo sie hängen, zeigt `scripts/klasse.sh <ID>`. Für SHACL "
                  "sind sie unsichtbar (`rdfs:subClassOf*` endet im Blank Node); die Explorer-Regeln "
                  "greifen trotzdem.", "",
                  "| ID | Klasse | Hinweis (editorialNote) |", "|---|---|---|"]
            L += [f"| {r['id']} | {r['label_de']} | {r.get('note', '')} |" for r in anon] + [""]
        if other:
            L += ["### Weitere Klassen (Oberklasse außerhalb der Lehrplan-Hierarchie)", "",
                  "| ID | Klasse | Oberklasse |", "|---|---|---|"]
            for r in other:
                pid = r["parent"].split(",")[0]
                plabel = lp.get(pid, {}).get("label_de", "")
                L += [f"| {r['id']} | {r['label_de']} | {pid} „{plabel}“ |"]
            L += [""]
        if indiv:
            L += [f"## Individuen des Landes ({len(indiv)})", "", "| ID | Bezeichnung |", "|---|---|"]
            L += [f"| {r['id']} | {r['label_de']} |" for r in indiv] + [""]
        (out / f"{code}.md").write_text("\n".join(L), encoding="utf-8")
        print(f"{code}: {len(classes)} Klassen ({len(anon)} ohne benannte Oberklasse), {len(indiv)} Individuen")

if __name__ == "__main__":
    main()
