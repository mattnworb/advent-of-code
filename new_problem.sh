#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <year> <day num>"
    exit 1
fi

# TODO: fix to allow specifying year too so this can be run from root dir
year=$1
day=$2
path="y${year}/problem${day}"
pkg="y${year}.problem${day}"

mkdir -p "${path}"
touch "${path}/input"
touch "${path}/__init__.py"
cat <<END >"${path}/__init__.py"
from typing import *

def part1(inp: str):
    pass

def part2(inp: str):
    pass
END

cat <<END >"${path}/__main__.py"
from ${pkg} import *

if __name__ == "__main__":
    with open("$path/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", "TODO")

    print("part 2:", "TODO")
END

cat <<END >"${path}/test_problem${day}.py"
from $pkg import *

def test_part1_example():
    pass

def test_part2_example():
    pass
END
