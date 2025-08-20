import numpy as np


def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0.copy()

    for k in range(1, max_iter + 1):
        x_old = x.copy()

        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])  # updated values
            sum2 = np.dot(A[i, i + 1 :], x[i + 1 :])  # old values
            x[i] = (b[i] - sum1 - sum2) / A[i, i]

        print(f"Iteration {k}: {x}")

        # check convergence
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f"\nConverged after {k} iterations.")
            return x

    print("\nDid not converge within max iterations.")
    return x


# Example system
A = np.array([[45.0, 2.0, 3.0], [-3.0, 22.0, 2.0], [5.0, 1.0, 20.0]])
b = np.array([58.0, 47.0, 67.0])
x0 = np.array([0.0, 0.0, 0.0])

solution = gauss_seidel(A, b, x0, tol=1e-6, max_iter=25)
print("\nFinal Solution:", solution)
