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