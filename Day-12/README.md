# Linear Algebra Methods for Least Squares Problems

This repository contains implementations of two fundamental methods for solving overdetermined linear systems and least squares problems: the **Least Squares Method** and the **QR Decomposition Method**. Both methods are used to find the best-fit solution when the system Ax = b has more equations than unknowns.

## Table of Contents
- [Least Squares Method](#normal-equation-method)
- [QR Decomposition Method](#qr-decomposition-method)
- [Comparison](#comparison)
- [Mathematical Background](#mathematical-background)
- [Usage](#usage)

## Least Squares Method

### File: `Least_Squares.py`

The Least Squares Method solves the least squares problem by using the formula: **x = (A^T A)^(-1) A^T b**. This method finds the best-fit line through a set of data points.

#### Line-by-Line Explanation

**Line 1:**
```python
import numpy as np
```
Imports the NumPy library for efficient matrix operations and linear algebra computations.

**Line 3:**
```python
# Step 1: Define matrix A and vector b
```
Comment indicating the first step: setting up the coefficient matrix and constant vector.

**Line 4:**
```python
A = np.array([[0, 1], [1, 1], [2, 1], [5, 1]])
```
Defines the coefficient matrix A (4×2). Each row represents a data point:
- Row 1: [0, 1] represents the point (x=0, coefficient for constant term=1)
- Row 2: [1, 1] represents the point (x=1, coefficient for constant term=1)
- Row 3: [2, 1] represents the point (x=2, coefficient for constant term=1)
- Row 4: [5, 1] represents the point (x=5, coefficient for constant term=1)

This matrix is set up to find a linear relationship y = c₁x + c₂.

**Line 6:**
```python
b = np.array([0, 3, 3, 6])
```
Defines the right-hand side vector b containing the y-values corresponding to each x-value:
- When x=0, y=0
- When x=1, y=3
- When x=2, y=3
- When x=5, y=6

**Line 8:**
```python
# Step 2: Compute A^T A and A^T b
```
Comment indicating the computation of matrices needed for the normal equation.

**Line 9:**
```python
ATA = A.T @ A
```
Computes A^T A (A transpose times A). The `@` operator performs matrix multiplication. This creates a 2×2 symmetric matrix that appears in the normal equation formula.

**Line 10:**
```python
ATb = A.T @ b
```
Computes A^T b (A transpose times b). This creates a 2×1 vector representing the right-hand side of the normal equation.

**Line 12:**
```python
# Step 3: Solve for x = [c1, c2]
```
Comment indicating the solution step for the coefficients.

**Line 13:**
```python
x_hat = np.linalg.solve(ATA, ATb)
```
Solves the normal equation (A^T A)x = A^T b for x using NumPy's linear solver. The result x_hat contains the optimal coefficients [c₁, c₂].

**Line 15:**
```python
c1, c2 = x_hat
```
Unpacks the solution vector into individual coefficients: c₁ (slope) and c₂ (y-intercept).

**Line 16:**
```python
print(f"The solution is c1 = {c1:.4f} and c2 = {c2:.4f}")
```
Prints the coefficients formatted to 4 decimal places.

**Line 17:**
```python
print(f"Best fit line: y = {c1:.4f}x + {c2:.4f}")
```
Displays the equation of the best-fit line in standard form.

**Line 19:**
```python
# Verify manually computed values
```
Comment indicating verification of results.

**Line 20:**
```python
print(f"15/14 = {15/14:.4f}")
```
Computes and displays 15/14 ≈ 1.0714, likely the theoretical value of c₁ for verification.

**Line 21:**
```python
print(f"6/7 = {6/7:.4f}")
```
Computes and displays 6/7 ≈ 0.8571, likely the theoretical value of c₂ for verification.

## QR Decomposition Method

### File: `QR_Factorization.py`

The QR decomposition method factors matrix A into an orthogonal matrix Q and an upper triangular matrix R, then solves the system using back substitution.

#### Line-by-Line Explanation

**Line 1:**
```python
import numpy as np
```
Imports NumPy for matrix operations and linear algebra functions.

**Line 3:**
```python
A = np.array([[1, 1], [-2, 1], [2, 1]])
```
Defines a 3×2 coefficient matrix A representing an overdetermined system:
- Row 1: [1, 1] represents the equation: 1·x₁ + 1·x₂ = b₁
- Row 2: [-2, 1] represents the equation: -2·x₁ + 1·x₂ = b₂  
- Row 3: [2, 1] represents the equation: 2·x₁ + 1·x₂ = b₃

**Line 4:**
```python
b = np.array([2, 1, 4])
```
Defines the right-hand side vector with corresponding values:
- First equation: x₁ + x₂ = 2
- Second equation: -2x₁ + x₂ = 1
- Third equation: 2x₁ + x₂ = 4

**Line 6:**
```python
# Factor A into Q and R
```
Comment indicating the QR factorization step.

**Line 7:**
```python
q, r = np.linalg.qr(A)
```
Performs QR decomposition of matrix A:
- `q`: Orthogonal matrix (3×2) where columns are orthonormal
- `r`: Upper triangular matrix (2×2) containing the factorization coefficients

The decomposition satisfies: A = QR

**Line 9:**
```python
# Calculate Q^T * b
```
Comment indicating the transformation of the right-hand side.

**Line 10:**
```python
q_t_b = q.T @ b
```
Computes Q^T b (Q transpose times b). This transforms the original right-hand side into a form compatible with the upper triangular system Rx = Q^T b.

**Line 12:**
```python
# Solve Rx = Q^T * b for x
```
Comment indicating the back substitution step.

**Line 13:**
```python
x = np.linalg.solve(r, q_t_b)
```
Solves the upper triangular system Rx = Q^T b for x using NumPy's linear solver. Since R is upper triangular, this is efficiently solved by back substitution.

**Line 15:**
```python
print("Q Matrix:\n", q)
```
Displays the orthogonal matrix Q, showing the orthonormal basis vectors.

**Line 16:**
```python
print("R Matrix:\n", r)
```
Displays the upper triangular matrix R, showing the factorization coefficients.

**Line 17:**
```python
print("Solution x:\n", x)
```
Displays the least squares solution vector x.

## Mathematical Background

### Least Squares Method
The normal equation approach minimizes ||Ax - b||² by solving:
```
(A^T A)x = A^T b
```
This method is direct but can be numerically unstable for ill-conditioned matrices.

### QR Decomposition Method
QR decomposition factors A = QR where:
- Q has orthonormal columns (Q^T Q = I)
- R is upper triangular

The least squares solution becomes:
```
Rx = Q^T b
```
This method is more numerically stable and preferred for most applications.

## Comparison

| Feature | Normal Equation | QR Decomposition |
|---------|-----------------|------------------|
| **Computational Complexity** | O(n³) | O(mn² - n³/3) |
| **Numerical Stability** | Can be unstable | More stable |
| **Memory Usage** | Requires A^T A | Requires Q and R storage |
| **Condition Number** | Squares condition number | Preserves condition number |
| **Recommended Use** | Small, well-conditioned problems | General purpose, larger problems |

## Usage

Both methods solve overdetermined linear systems (more equations than unknowns) by finding the least squares solution that minimizes the residual error.

### Requirements
- Python 3.x
- NumPy library

### Running the Code
```bash
python normal_equation_method.py
python qr_decomposition_method.py
```

### Applications
- **Curve Fitting**: Finding best-fit lines or polynomials through data points
- **Parameter Estimation**: Estimating model parameters from experimental data
- **Signal Processing**: Filtering and system identification
- **Machine Learning**: Linear regression and feature fitting

## Expected Output

### Least Squares Method
```
The solution is c1 = 1.0714 and c2 = 0.8571
Best fit line: y = 1.0714x + 0.8571
15/14 = 1.0714
6/7 = 0.8571
```

### QR Decomposition Method
```
Q Matrix:
[[ 0.33333333  0.66666667]
 [-0.66666667  0.33333333]
 [ 0.66666667  0.66666667]]

R Matrix:
[[ 3.          0.33333333]
 [ 0.          1.33333333]]

Solution x:
[1.25 0.75]
```

Both methods provide powerful tools for solving least squares problems with different computational and numerical characteristics.