"""Minimum-sum combinations: choose M elements of x whose sum is as small as possible.

The DP table T has one row per prefix of x and one column per subset size:

    T[0][0] = 0,  T[0][m] = inf for m > 0
    T[n][m] = min(T[n-1][m], T[n-1][m-1] + x[n-1])

i.e. the best m-subset of the first n elements either skips element n or uses it alongside the
best (m-1)-subset of the rest. Values are argminsum numbers, whose min() returns one of its two
arguments, so backtracking can tell "skipped" from "used" by object identity.
"""

import argparse

from argminsum import argminsum, inf, min, zero


def minsumcomb(x, M):
    """Returns argminsum(val=chosen elements, cnfg={"subset size": M, "min sum": total}).

    If fewer than M elements exist, no subset qualifies: the min sum is inf and none are chosen.
    """
    if M < 0:
        raise ValueError("M must be non-negative")
    size = len(x)
    if M > size:
        # No subset qualifies. Handled up front because min() breaks an inf-vs-inf tie by returning
        # a fresh inf object, which backtracking would misread as "element used".
        return argminsum([], {"subset size": M, "min sum": inf.val})

    cols = M + 1
    rows = size + 1

    # Initialize the 2D list with 'inf' for all values
    two_d = [[inf] * cols for _ in range(rows)]
    two_d[0][0] = zero

    for r in range(1, rows):
        for c in range(cols):
            two_d[r][c] = two_d[r - 1][c]  # Exclude the current element
            if c > 0:
                # Include the current element and compute the minimum
                current = argminsum(x[r - 1], [])
                two_d[r][c] = min(two_d[r][c], two_d[r - 1][c - 1] + current)

    # Backtracking to find the solution subset
    subset = []
    s, m = size, M
    while s > 0 and m > 0:
        if two_d[s][m] is two_d[s - 1][m]:  # Current element excluded
            s -= 1
        else:  # Current element included
            subset.append(x[s - 1])
            s -= 1
            m -= 1

    cnfg = {
        "subset size": M,
        "min sum": two_d[size][M].val,  # Extract the minimum sum from the 2D list
    }

    S = argminsum(subset, cnfg)
    return S


def main():
    parser = argparse.ArgumentParser(description="Choose M numbers with the smallest sum.")
    parser.add_argument("numbers", type=float, nargs="+", help="the candidate numbers")
    parser.add_argument("-m", type=int, required=True, help="how many numbers to choose")
    args = parser.parse_args()

    result = minsumcomb(args.numbers, args.m)
    print(f"Chosen: {result.val}")
    print(f"Minimum sum: {result.cnfg['min sum']}")


if __name__ == "__main__":
    main()
