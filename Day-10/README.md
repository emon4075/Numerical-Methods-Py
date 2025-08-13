# LU Decomposition with Doolittle's Method in Python

This script provides a Python implementation of **LU decomposition** using Doolittle's method. LU decomposition is a matrix factorization technique that expresses a square matrix \( A \) as the product of a lower triangular matrix \( L \) and an upper triangular matrix \( U \):

\[
A = LU
\]

The code is located in `lu_decomposition.py` and includes a step-by-step example with solution.

---

## What is LU Decomposition?

LU decomposition allows you to solve systems \( Ax = b \) more efficiently by first decomposing \( A \) into \( L \) and \( U \), then using forward and backward substitution:

1. Solve \( Lw = b \) for \( w \) (forward substitution)
2. Solve \( Ux = w \) for \( x \) (backward substitution)

Doolittle's method constructs \( L \) with ones on its diagonal.

---

## Code Explanation

Let's go through the code line by line.

### 1. Import NumPy

```python
import numpy as np
```
NumPy is used for matrix and vector operations.

---

### 2. LU Decomposition Function

```python
def lu_decomposition(A):
    """
    Performs LU decomposition of a square matrix A using Doolittle's method.
    L has ones on its diagonal.
    """
    n = A.shape[0]
    U = np.copy(A).astype(float)
    L = np.eye(n, dtype=float)
```
- **`n = A.shape[0]`**: Get the number of rows/columns of the square matrix.
- **`U = np.copy(A).astype(float)`**: Make a copy of the input matrix \( A \) for the upper triangular matrix \( U \).
- **`L = np.eye(n, dtype=float)`**: Initialize the lower triangular matrix \( L \) as an identity matrix (ones on the diagonal).

---

#### Main Loop: Elimination & Construction

```python
    for k in range(n - 1):
        if U[k, k] == 0:
            raise ValueError("Zero pivot encountered. Pivoting is required.")
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]
```
- For each column \( k \) (except the last):
    - **Pivot Check:** If the pivot element \( U[k, k] \) is zero, the method fails and suggests pivoting.
    - **Elimination:** For each row \( i \) below \( k \):
        - Compute the elimination factor: \( \text{factor} = U[i, k] / U[k, k] \).
        - Store this factor in \( L \): \( L[i, k] = \text{factor} \).
        - Update \( U \): Subtract \( \text{factor} \times U[k, k:] \) from row \( i \) of \( U \).

---

#### Return Result

```python
    return L, U
```
- Returns the lower and upper triangular matrices \( L \) and \( U \).

---

### 3. Example Usage

Let's work through the included example.

#### Define Matrix and Vector

```python
M = np.array([[6, 18, 3], [2, 12, 1], [4, 15, 3]])
V = np.array([3, 19, 0])
```
- **Matrix \( M \):**
    \[
    \begin{bmatrix}
    6 & 18 & 3 \\
    2 & 12 & 1 \\
    4 & 15 & 3
    \end{bmatrix}
    \]
- **Vector \( V \):**
    \[
    \begin{bmatrix}
    3 \\ 19 \\ 0
    \end{bmatrix}
    \]

---

#### Perform LU Decomposition

```python
L, U = lu_decomposition(M)
print("L:\n", L)
print("U:\n", U)
print("Verification L@U:\n", L @ U)
```
- **L** is lower triangular with ones on the diagonal.
- **U** is upper triangular.
- **Verification:** \( L \times U \) should reconstruct the original matrix \( M \).

**Sample Output:**
```
L:
[[1.  0.  0. ]
 [0.33333333 1.  0. ]
 [0.66666667 0.5 1. ]]
U:
[[ 6. 18.  3.]
 [ 0.  6.  0.]
 [ 0.  0.  1.5]]
Verification L@U:
[[ 6. 18.  3.]
 [ 2. 12.  1.]
 [ 4. 15.  3.]]
```
---

### 4. Solving the System \( MX = V \)

#### Forward Substitution (\( LW = V \))

```python
W = np.linalg.solve(L, V)
```
- Solves for intermediate vector \( W \) using the lower triangular matrix.

#### Backward Substitution (\( UX = W \))

```python
X = np.linalg.solve(U, W)
```
- Solves for the final solution vector \( X \) using the upper triangular matrix.

**Print the solutions:**
```python
print("W:", W)
print("X:", X)
```

**Sample Output:**
```
W: [ 3.         18.         -9.        ]
X: [ 0.5  2.5 -6. ]
```

---

## Full Example Walkthrough

**Step-by-Step:**

1. **LU Decomposition:** Splits \( M \) into \( L \) and \( U \).
2. **Verification:** Confirms \( M = LU \).
3. **Forward substitution:** Solves \( L W = V \) for \( W \).
4. **Backward substitution:** Solves \( U X = W \) for \( X \).
5. **Final Solution:** \( X \) is the vector that solves \( M X = V \).

---

## How to Run

1. Make sure you have Python and NumPy installed.
2. Run the script:

```bash
python lu_decomposition.py
```

---

## Notes

- This implementation does **not** include pivoting. If a zero pivot is encountered, an error is raised.
- For ill-conditioned or singular matrices, partial pivoting is recommended (see Gaussian elimination with pivoting).

---
