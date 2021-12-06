#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <year> <day num>"
    exit 1
fi

year=$1
day=$2
padded_day=$(printf "%02d" "${day}")
path="y${year}/problem${padded_day}"
pkg="y${year}.problem${padded_day}"

mkdir -p "${path}"
touch "${path}/input"

#TODO: needs auth
#wget -O "${path}/input" "https://adventofcode.com/${year}/day/${day}/input"
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

    print("part 1:", part1(inp))

    print("part 2:", part2(inp))
END

cat <<END >"${path}/test_problem${padded_day}.py"
from $pkg import *

example = """"""

def test_part1_example():
    # TODO: populate
    assert part1(example)

def test_part2_example():
    # TODO: populate
    assert part2(example)
END
