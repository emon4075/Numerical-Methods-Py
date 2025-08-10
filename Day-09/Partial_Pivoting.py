import numpy as np


def gauss_elim_pivot(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Forward elimination with pivoting
    for k in range(n):
        # Find pivot row and swap
        pivot = np.argmax(abs(A[k:, k])) + k
        if pivot != k:
            A[[k, pivot]], b[[k, pivot]] = A[[pivot, k]], b[[pivot, k]]

        # Eliminate entries below pivot
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1 :], x[i + 1 :])) / A[i, i]

    return x


# Example system
A = np.array([[2, 1, 3], [15, 2, 5], [1, 3, 1]])
b = np.array([10, 5, 3])

sol = gauss_elim_pivot(A, b)

print(f"x = {sol[0]:.4f}, y = {sol[1]:.4f}, z = {sol[2]:.4f}")
print("Check:", A @ sol)
