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