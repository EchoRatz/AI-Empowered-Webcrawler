#!/usr/bin/env bash
set -euo pipefail

# always run from repo root
cd -- "$(dirname "$0")"

# pick python version (prefer 3.11)
for P in python3.11 python3.12 python3; do
  if command -v $P >/dev/null 2>&1; then
    PY=$P; break
  fi
done
[[ -z "${PY:-}" ]] && { echo "No suitable Python found"; exit 1; }

# create venv if missing
if [[ ! -d .venv ]]; then
  echo "[setup] creating venv with $PY..."
  $PY -m venv .venv
fi

# activate venv
source .venv/bin/activate

# upgrade pip/setuptools/wheel
python -m pip install --quiet --upgrade pip setuptools wheel

# install dependencies
if [[ -f requirements.txt ]]; then
  python -m pip install --quiet -r requirements.txt
fi

# make sure output folder exists
mkdir -p out

# run crawler with config
python redditCrawler.py --config "$(pwd)/config.yaml"
