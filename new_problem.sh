#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

name=$1
mkdir "$name"
touch "$name/__init__.py"
touch "$name/test_$name.py"

cat <<END >"$name/__main__.py"
from $name import *

if __name__ == "__main__":
    with open("$name/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", "TODO")

    print("part 2:", "TODO")
END
