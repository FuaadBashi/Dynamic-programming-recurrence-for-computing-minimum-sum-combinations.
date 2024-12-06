# Dynamic-programming-recurrence-for-computing-minimum-sum-combinations.
to implement, in Python, the recurrence. For an input data list of length N, [x1,...,xN], it finds a combination of M elements of smallest sum in S⋆ 


This repository contains the solution to the AIML 2024-2025 coursework assignment, which implements a dynamic programming recurrence to compute the minimum sum combination of `M` elements from an input list of numerical values. The implementation adheres to the specifications outlined in the provided coursework instructions.

## Problem Overview

The task is to compute the minimum sum combination \( S^\star \) of `M` elements from a given input list \( x \), using the recurrence:

\[
S^\star_{n,m} = \text{min} \left( S^\star_{n-1,m}, S^\star_{n-1,m-1} + x_n \right)
\]

### Example

For an input list `x = [11, 3, -5, 8, 2]` and `M = 2`, the minimum sum combination at \( S^\star_{5,2} \) is `-3`, corresponding to the subset `[-5, 2]`.

---

## Function Details

The implementation is contained in a single Python file and includes the following function:

```python
S = minsumcomb(x, M)
```

### Parameters:
- `x`: A Python list of numerical values.
- `M`: A positive integer representing the number of elements to select.

### Returns:
- `S`: A list of lists as defined by the `argminsum` type in the course's `argminsum.py` module, representing the minimum sum combinations.

---

## Usage

To test the function:

1. Import the function into your testing script:
   ```python
   from yourfile.py import minsumcomb
   ```

2. Call the function with appropriate inputs:
   ```python
   x = [11, 3, -5, 8, 2]
   M = 2
   result = minsumcomb(x, M)
   print(result)
   ```

---
