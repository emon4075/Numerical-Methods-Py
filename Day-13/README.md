
# Eigendecomposition and Eigenvalue/Eigenvector Calculation in Python

This repository contains two Python scripts that demonstrate how to calculate eigenvalues and eigenvectors of a matrix and how to perform eigendecomposition using the NumPy library.

---

## 1. `Eigen_Value_Vector.py`

This script calculates the eigenvalues and eigenvectors of a given 2x2 matrix.

### Code

```python
import numpy as np

A = np.array(
    [
        [4, -2],
        [1, 1],
    ]
)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)
````

### Line-by-Line Explanation

  - **`import numpy as np`**: This line imports the NumPy library, which is essential for numerical operations in Python, especially for linear algebra. We give it the alias `np` for convenience.

  - **`A = np.array(...)`**: Here, we define a 2x2 matrix `A` using NumPy's `array` function. This matrix will be the subject of our calculations.

  - **`eigenvalues, eigenvectors = np.linalg.eig(A)`**: This is the core of the script.

      - `np.linalg.eig(A)` is a function from NumPy's linear algebra module (`linalg`) that computes the eigenvalues and right eigenvectors of a square matrix.
      - The function returns two values: a 1D array containing the eigenvalues and a 2D array containing the corresponding eigenvectors as columns.
      - We unpack these two results into the variables `eigenvalues` and `eigenvectors`.

  - **`print("Eigenvalues:", eigenvalues)`**: This line prints the calculated eigenvalues of matrix `A`.

  - **`print("\nEigenvectors:\n", eigenvectors)`**: This line prints the calculated eigenvectors. Each column in the output matrix corresponds to an eigenvector associated with the eigenvalue at the same index in the `eigenvalues` array.

-----

## 2\. `Eigen Decompositon`

This script demonstrates the concept of **eigendecomposition**. Eigendecomposition is the factorization of a matrix into a canonical form, representing it in terms of its eigenvalues and eigenvectors. The formula for eigendecomposition is:

$$
A = V \Lambda V^{-1}
$$Where:

- **A** is the original matrix.
- **V** is the matrix of eigenvectors.
- **Λ (Lambda)** is the diagonal matrix of eigenvalues.
- **V⁻¹** is the inverse of the eigenvector matrix.

This script calculates these components and then reconstructs the original matrix `A` to verify the formula.

### Code

```python
import numpy as np

A = np.array(
[
[4, -2],
[1, 1],
]
)

eigenvalues, eigenvectors = np.linalg.eig(A)

# A = V*Lambda*V^-1

V = eigenvectors
V_inverse = np.linalg.inv(V)
Lambda = np.diag(eigenvalues)

A_reconstructed = V @ Lambda @ V_inverse
print(f"Reconstructed Matrix:\n {A_reconstructed}")
```

### Line-by-Line Explanation

- **`import numpy as np`**, **`A = np.array(...)`**, and **`eigenvalues, eigenvectors = np.linalg.eig(A)`**: These lines are identical to the first script, setting up the matrix and calculating its eigenvalues and eigenvectors.

- **`V = eigenvectors`**: We assign the calculated `eigenvectors` matrix to a new variable `V` for clarity, following the standard notation in the eigendecomposition formula.

- **`V_inverse = np.linalg.inv(V)`**: We calculate the inverse of the eigenvector matrix `V` using `np.linalg.inv()`. This is the `V⁻¹` part of the formula.

- **`Lambda = np.diag(eigenvalues)`**: We create the diagonal matrix `Λ` (Lambda) from the `eigenvalues` array. The `np.diag()` function takes a 1D array and places its elements on the diagonal of a new 2D square matrix, with zeros everywhere else.

- **`A_reconstructed = V @ Lambda @ V_inverse`**: This line performs the matrix multiplication to reconstruct the original matrix. The `@` operator is used for matrix multiplication in NumPy. It calculates `V * Λ * V⁻¹`.

- **`print(f"Reconstructed Matrix:\n {A_reconstructed}")`**: This line prints the resulting matrix. If the calculations are correct, this reconstructed matrix will be identical (or very close, due to floating-point precision) to the original matrix `A`.

<!-- end list -->