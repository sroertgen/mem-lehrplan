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

LIT = r'"""(?:[^\\]|\\.)*?"""|"(?:[^"\\]|\\.)*"'

def literals(block, pred, lang=None):
    out, tag = [], (f"@{lang}" if lang else "")
    for m in re.finditer(re.escape(pred) + r'\s+((?:(?:' + LIT + r')(?:@[a-zA-Z-]+)?\s*,?\s*)+)', block):
        for lm in re.finditer(r'"""((?:[^\\]|\\.)*?)"""(@[a-zA-Z-]+)?|"((?:[^"\\]|\\.)*)"(@[a-zA-Z-]+)?', m.group(1)):
            val, l = (lm.group(1), lm.group(2)) if lm.group(1) is not None else (lm.group(3), lm.group(4))
            l = l or ""
            if lang and l != tag:
                continue
            val = val.replace('\\"', '"').replace("\\n", " ")
            val = re.sub(r'\s*\n\s*', ' ', val)
            out.append(val)
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
