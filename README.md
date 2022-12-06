# advent-of-code

To run the problem for a day, run the Python module like

```sh
(cd 2020 && python -m problem01)
```

Run the tests (yes I wrote tests) with `tox` or `pytest` or to run them for just
one problem, `pytest <year>/<directory>`.

Install the pre-commit hooks to keep the code nicely formatted via
[pre-commit](https://pre-commit.com/) with `pre-commit install`.

To benchmark one of the modules with `timeit`, can run something like:

```sh
python -m timeit -s 'import y2021.problem15; inp = open("y2021/problem15/input").read(-1).strip()' 'y2021.problem15.part1(inp)'
1 loop, best of 5: 938 msec per loop
```
