import numpy as np


def lu_decomposition(A):
    """
    Performs LU decomposition of a square matrix A using Doolittle's method.
    L has ones on its diagonal.
    """
    n = A.shape[0]
    U = np.copy(A).astype(float)
    L = np.eye(n, dtype=float)

    for k in range(n - 1):
        if U[k, k] == 0:
            raise ValueError("Zero pivot encountered. Pivoting is required.")
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]

    return L, U


# Example usage
M = np.array([[6, 18, 3], [2, 12, 1], [4, 15, 3]])
V = np.array([3, 19, 0])

L, U = lu_decomposition(M)
print("L:\n", L)
print("U:\n", U)
print("Verification L@U:\n", L @ U)

# Forward substitution: L W = V
W = np.linalg.solve(L, V)
# Backward substitution: U X = W
X = np.linalg.solve(U, W)

print("W:", W)
print("X:", X)
