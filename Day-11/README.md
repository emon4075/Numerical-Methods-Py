# Iterative Methods for Solving Linear Systems

This repository contains implementations of two popular iterative methods for solving systems of linear equations: the **Jacobi Method** and the **Gauss-Seidel Method**. Both methods are used to solve systems of the form **Ax = b** where A is a coefficient matrix, x is the unknown vector, and b is the constant vector.

## Table of Contents
- [Jacobi Method](#jacobi-method)
- [Gauss-Seidel Method](#gauss-seidel-method)
- [Comparison](#comparison)
- [Usage](#usage)

## Jacobi Method

### File: `Jacobi_Method.py`

The Jacobi method is an iterative algorithm for solving linear systems where each variable is updated simultaneously using values from the previous iteration.

#### Line-by-Line Explanation

**Line 1:** 
```python
import numpy as np
```
Imports the NumPy library for efficient numerical computations and array operations.

**Line 4:** 
```python
def jacobi(A, b, x0, tol=1e-6, max_iter=100):
```
Defines the main Jacobi function with parameters:
- `A`: Coefficient matrix (n×n)
- `b`: Right-hand side vector
- `x0`: Initial guess vector
- `tol`: Convergence tolerance (default: 1e-6)
- `max_iter`: Maximum number of iterations (default: 100)

**Lines 5-17:** 
```python
"""
Solves Ax = b using the Jacobi iterative method.
...
"""
```
Documentation string explaining the function's purpose, parameters, and return values.

**Line 18:**
```python
n = len(b)
```
Gets the dimension of the system (number of equations/unknowns).

**Line 19:**
```python
x = x0.copy()
```
Creates a copy of the initial guess to avoid modifying the original input.

**Line 20:**
```python
print(f"Iteration 0: x = {np.round(x, 6)}")
```
Prints the initial guess rounded to 6 decimal places.

**Line 22:**
```python
for k in range(1, max_iter + 1):
```
Main iteration loop starting from iteration 1.

**Line 23:**
```python
x_old = x.copy()
```
Stores the current solution for use in calculations and convergence checking.

**Line 24:**
```python
for i in range(n):
```
Inner loop to update each variable individually.

**Line 25:**
```python
sigma = sum(A[i, j] * x_old[j] for j in range(n) if j != i)
```
Calculates the sum of products A[i,j] * x[j] for all j ≠ i using values from the previous iteration.

**Lines 26-27:**
```python
if A[i, i] == 0:
    raise ValueError("Zero on diagonal, cannot proceed.")
```
Checks for zero diagonal elements, which would cause division by zero.

**Line 28:**
```python
x[i] = (b[i] - sigma) / A[i, i]
```
Updates the i-th variable using the Jacobi formula: x[i] = (b[i] - Σ(A[i,j]*x[j])) / A[i,i]

**Line 30:**
```python
print(f"Iteration {k}: x = {np.round(x, 6)}")
```
Prints the current iteration results.

**Line 32:**
```python
if np.linalg.norm(x - x_old, ord=np.inf) < tol:
```
Checks convergence using the infinity norm (maximum absolute difference).

**Lines 33-34:**
```python
print(f"\nConverged after {k} iterations.")
return x, k
```
If converged, prints success message and returns solution with iteration count.

**Lines 36-37:**
```python
print("\nMaximum iterations reached without convergence.")
return x, max_iter
```
If maximum iterations reached, returns the best approximation found.

**Lines 40-46:**
```python
A = np.array([[8.0, 5.0, 2.0], [2.0, 10.0, -2.0], [1.0, 3.0, 6.0]])
b = np.array([25.0, 20.0, 30.0])
x0 = np.array([0.0, 0.0, 0.0])
solution, iterations = jacobi(A, b, x0)
print("Final Jacobi Solution:", np.round(solution, 6))
```
Example usage demonstrating how to solve a 3×3 system with zero initial guess.

## Gauss-Seidel Method

### File: `Gauss_Seidel_Method.py`

The Gauss-Seidel method is similar to Jacobi but uses updated values immediately as they become available, typically leading to faster convergence.

#### Line-by-Line Explanation

**Line 1:**
```python
import numpy as np
```
Imports NumPy for numerical operations.

**Line 4:**
```python
def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
```
Defines the Gauss-Seidel function with the same parameter structure as Jacobi.

**Line 5:**
```python
n = len(b)
```
Gets the system dimension.

**Line 6:**
```python
x = x0.copy()
```
Creates a working copy of the initial guess.

**Line 8:**
```python
for k in range(1, max_iter + 1):
```
Main iteration loop.

**Line 9:**
```python
x_old = x.copy()
```
Stores previous iteration values for convergence checking.

**Line 11:**
```python
for i in range(n):
```
Loop through each variable to update.

**Line 12:**
```python
sum1 = np.dot(A[i, :i], x[:i])  # updated values
```
Calculates sum using already updated values from current iteration (indices 0 to i-1).

**Line 13:**
```python
sum2 = np.dot(A[i, i + 1 :], x[i + 1 :])  # old values
```
Calculates sum using old values from previous iteration (indices i+1 to n-1).

**Line 14:**
```python
x[i] = (b[i] - sum1 - sum2) / A[i, i]
```
Updates variable i using the Gauss-Seidel formula, immediately using new values.

**Line 16:**
```python
print(f"Iteration {k}: {x}")
```
Prints current iteration results.

**Line 18:**
```python
# check convergence
```
Comment indicating convergence check.

**Line 19:**
```python
if np.linalg.norm(x - x_old, ord=np.inf) < tol:
```
Convergence test using infinity norm.

**Lines 20-21:**
```python
print(f"\nConverged after {k} iterations.")
return x
```
Returns solution if converged.

**Lines 23-24:**
```python
print("\nDid not converge within max iterations.")
return x
```
Returns best approximation if maximum iterations reached.

**Lines 27-33:**
```python
A = np.array([[45.0, 2.0, 3.0], [-3.0, 22.0, 2.0], [5.0, 1.0, 20.0]])
b = np.array([58.0, 47.0, 67.0])
x0 = np.array([0.0, 0.0, 0.0])
solution = gauss_seidel(A, b, x0, tol=1e-6, max_iter=25)
print("\nFinal Solution:", solution)
```
Example usage with a different 3×3 system, demonstrating the method's application.

## Comparison

| Feature | Jacobi Method | Gauss-Seidel Method |
|---------|---------------|-------------------|
| **Update Strategy** | All variables updated simultaneously | Variables updated sequentially |
| **Memory Usage** | Requires storing previous iteration | Can overwrite values immediately |
| **Convergence Speed** | Generally slower | Usually faster convergence |
| **Parallelization** | Easily parallelizable | Sequential nature limits parallelization |

## Usage

Both methods are suitable for solving large sparse systems where direct methods become computationally expensive. Choose Jacobi for parallel computing environments and Gauss-Seidel for faster sequential convergence.

### Requirements
- Python 3.x
- NumPy library

### Running the Code
```bash
python Jacobi_Method.py
python Gauss_Seidel_Method.py
```

Both methods will display iteration-by-iteration progress and final solutions for their respective example systems.