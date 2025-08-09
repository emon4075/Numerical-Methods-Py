import numpy as np


def naive_gaussian_elimination(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Forward elimination
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1 :], x[i + 1 :])) / A[i, i]

    return x


# Example usage
A1 = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b1 = np.array([8, -11, -3])
print(naive_gaussian_elimination(A1, b1))

A2 = np.array([[4, 2], [1, -3]])
b2 = np.array([10, -8])
print(naive_gaussian_elimination(A2, b2))
