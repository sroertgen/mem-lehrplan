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
