# advent-of-code

## Running

To run the problem for a day, run the Python module like

```sh
poetry run python -m y2020.problem01
```

The solution code generally has no dependencies outside of the standard library
but for tests, formatting etc I'm using [poetry](https://python-poetry.org/) to
manage dependencies.

## Setting up new problem

To generate code for a new problem/day from a template, run:

```sh
./new_problem.sh <year> <day number>
```

This will create files in a directory named `y$YEAR/$DAY`.

## Tests

Run the tests (yes I wrote tests) with `tox` or `pytest` or to run them for just
one problem, `poetry run pytest <year>/<directory>`.

Install the pre-commit hooks to keep the code nicely formatted via
[pre-commit](https://pre-commit.com/) with `pre-commit install`.

To benchmark one of the modules with `timeit`, can run something like:

```sh
python -m timeit -s 'import y2021.problem15; inp = open("y2021/problem15/input").read(-1).strip()' 'y2021.problem15.part1(inp)'
1 loop, best of 5: 938 msec per loop
```
