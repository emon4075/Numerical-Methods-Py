---

# Naive Gaussian Elimination in Python

This repository contains an implementation of **Naive Gaussian Elimination** in Python using NumPy.
The code solves a system of linear equations of the form:

```
A * x = b
```

where:

* `A` is a square coefficient matrix
* `b` is the right-hand-side vector
* `x` is the unknown vector to be solved

---

## How the Algorithm Works

Gaussian elimination proceeds in two phases:

1. **Forward Elimination** — Transform the matrix `A` into an upper triangular matrix by eliminating variables step-by-step.
2. **Back Substitution** — Solve for the unknowns starting from the last row and moving upward.

---

## Code Overview

```python
import numpy as np

def naive_gaussian_elimination(A, b):
    A = A.astype(float)       # Convert A to floats for division
    b = b.astype(float)       # Convert b to floats for division
    n = len(b)                # Number of equations

    # Forward elimination
    for k in range(n - 1):    # Loop over pivot rows
        for i in range(k + 1, n):  # Loop over rows below pivot
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]   # Update row in A
            b[i] -= factor * b[k]           # Update corresponding b value

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x
```

---

## Step-by-Step Example

We solve the system:

```
2x₁ +  1x₂ − 1x₃ =  8
-3x₁ − 1x₂ + 2x₃ = -11
-2x₁ + 1x₂ + 2x₃ = -3
```

### Initial Matrices

```
A =
[  2   1  -1 ]
[ -3  -1   2 ]
[ -2   1   2 ]

b =
[  8 ]
[ -11 ]
[  -3 ]
```

---

### **Eliminate First Column (x₁)**

* **Row 2:**
  Factor = -3 / 2 = **-1.5**
  Row₂ ← Row₂ − (Factor × Row₁)
  New Row₂: (0, 0.5, 0.5),  b₂ = 1

* **Row 3:**
  Factor = -2 / 2 = **-1**
  Row₃ ← Row₃ − (Factor × Row₁)
  New Row₃: (0, 2, 1),  b₃ = 5

After elimination:

```
A =
[ 2   1  -1 ]
[ 0 0.5 0.5 ]
[ 0   2   1 ]

b =
[ 8 ]
[ 1 ]
[ 5 ]
```

---

### **Eliminate Second Column (x₂)**

* **Row 3:**
  Factor = 2 / 0.5 = **4**
  Row₃ ← Row₃ − (Factor × Row₂)
  New Row₃: (0, 0, -1),  b₃ = 1

After elimination:

```
A =
[ 2   1  -1 ]
[ 0 0.5 0.5 ]
[ 0   0  -1 ]

b =
[ 8 ]
[ 1 ]
[ 1 ]
```

---

## **Back Substitution**

We now solve from the bottom up:

1. From Row 3:
   `-1 * x₃ = 1` → **x₃ = -1**

2. From Row 2:
   `0.5 * x₂ + 0.5 * (-1) = 1`
   `0.5 * x₂ - 0.5 = 1` → **x₂ = 3**

3. From Row 1:
   `2 * x₁ + 1 * 3 - 1 * (-1) = 8`
   `2 * x₁ + 3 + 1 = 8` → **x₁ = 2**

---

## **Final Solution**

```
x = [ 2, 3, -1 ]
```

---

## Example Usage

```python
A1 = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b1 = np.array([8, -11, -3])
print(naive_gaussian_elimination(A1, b1))
# Output: [ 2.  3. -1.]
```

---

## Notes

* This implementation does **not** use partial pivoting — it can fail if a pivot element is zero or very small.
* For more numerical stability, consider implementing **Gaussian Elimination with Partial Pivoting**.

---
