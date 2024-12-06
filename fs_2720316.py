from argminsum import *


def minsumcomb(x, M):
    size = len(x)
    
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
        if two_d[s][m] == two_d[s - 1][m]:  # Current element excluded
            s -= 1
        else:  # Current element included
            subset.append(x[s - 1])
            s -= 1
            m -= 1

    cnfg = {
        "subset size": M,
        "min sum": two_d[size][M].val  # Extract the minimum sum from the 2D list
    }

    S = argminsum(subset, cnfg)
    return S