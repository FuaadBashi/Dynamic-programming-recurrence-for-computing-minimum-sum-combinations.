# Minimum-Sum Combinations — Dynamic Programming

[![CI](https://github.com/FuaadBashi/Dynamic-programming-recurrence-for-computing-minimum-sum-combinations./actions/workflows/ci.yml/badge.svg)](https://github.com/FuaadBashi/Dynamic-programming-recurrence-for-computing-minimum-sum-combinations./actions/workflows/ci.yml)

Given numbers `x` and a size `M`, choose `M` of them with the smallest possible sum and report
which ones were chosen. It is solved with a dynamic-programming recurrence over an *argmin-sum*
number type that carries a value and a configuration together (AI and machine-learning
coursework, 2024–25).

```bash
$ python3 main.py 11 3 -5 8 2 -m 2
Chosen: [2.0, -5.0]
Minimum sum: -3.0
```

## The recurrence

Let `T[n][m]` be the smallest sum of `m` elements chosen from the first `n`:

```
T[0][0] = 0
T[0][m] = ∞                                   for m > 0
T[n][m] = min( T[n−1][m],                     skip element n
               T[n−1][m−1] + x[n−1] )         use element n
```

The table has `(N+1)(M+1)` entries, each filled in O(1), so the algorithm is **O(N·M)** in time
and space. The chosen elements are recovered by walking back from `T[N][M]`. Because the
argmin-sum `min` returns one of its two arguments, each step can tell "skipped" from "used" by
object identity.

## Verification

The tests check the DP against a brute-force search over every combination for 200 random inputs
(negatives, duplicates, empty lists, `M = 0` and `M = N`). They also check that chosen elements
come from the input without reuse, and that asking for more elements than exist returns no
solution.

## Files

- [main.py](main.py): `minsumcomb(x, M)` and a small CLI.
- [argminsum.py](argminsum.py): the argmin-sum number type: addition, `min`, `zero` and `inf`.
- [tests/](tests): pytest suite.

## Run the tests

```bash
pip install pytest ruff
pytest
ruff format --check . && ruff check .
```
