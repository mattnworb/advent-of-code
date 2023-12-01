# advent-of-code

To run the problem for a day, run the Python module like

```sh
python -m y2020.problem01
```

To generate code for a new problem/day from a template, run:

```sh
./new_problem.sh <year> <day number>
```

This will create files in a directory named `y$YEAR/$DAY`.

Run the tests (yes I wrote tests) with `tox` or `pytest` or to run them for just
one problem, `pytest <year>/<directory>`.

Install the pre-commit hooks to keep the code nicely formatted via
[pre-commit](https://pre-commit.com/) with `pre-commit install`.

To benchmark one of the modules with `timeit`, can run something like:

```sh
python -m timeit -s 'import y2021.problem15; inp = open("y2021/problem15/input").read(-1).strip()' 'y2021.problem15.part1(inp)'
1 loop, best of 5: 938 msec per loop
```

The `requirements.txt` file is generated with pip-compile from [pip-tools](https://pip-tools.readthedocs.io/en/latest/). To re-compile:

```
pip-compile --no-emit-index-url > requirements.txt
```
