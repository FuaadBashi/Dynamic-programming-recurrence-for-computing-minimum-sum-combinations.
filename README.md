# Minimum-Sum Combinations — Dynamic Programming

An AIML 2024–2025 coursework implementation of a recurrence for selecting M elements with minimum sum. It uses a custom value type to carry the result and configuration.

## Try the function

Requires Python 3; no external dependencies.

```bash
git clone https://github.com/FuaadBashi/Dynamic-programming-recurrence-for-computing-minimum-sum-combinations..git
cd Dynamic-programming-recurrence-for-computing-minimum-sum-combinations.
python3 -c 'from main import minsumcomb; print(minsumcomb([11, 3, -5, 8, 2], 2))'
```

## Implementation

- [main.py](main.py): `minsumcomb(x, M)`, a dynamic-programming table followed by backtracking.
- [argminsum.py](argminsum.py): custom addition, minimum selection, and zero/infinity values.

For each element, the recurrence compares excluding it with including it in a subset of one fewer element. The table uses O(NM) entries.

The returned object has `.val` and `.cnfg` attributes. Input validation and equal-cost backtracking deserve further tests; the custom type does not define value equality, so the backtracking equality check currently compares object identity.
