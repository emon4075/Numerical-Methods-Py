import numpy as np


def jacobi(A, b, x0, tol=1e-6, max_iter=100):
    """
    Solves Ax = b using the Jacobi iterative method.

    Parameters:
    A (ndarray): Coefficient matrix (n x n)
    b (ndarray): Right-hand side vector (n,)
    x0 (ndarray): Initial guess (n,)
    tol (float): Tolerance for convergence
    max_iter (int): Maximum iterations

    Returns:
    x (ndarray): Approximate solution
    k (int): Iterations performed
    """
    n = len(b)
    x = x0.copy()
    print(f"Iteration 0: x = {np.round(x, 6)}")

    for k in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            sigma = sum(A[i, j] * x_old[j] for j in range(n) if j != i)
            if A[i, i] == 0:
                raise ValueError("Zero on diagonal, cannot proceed.")
            x[i] = (b[i] - sigma) / A[i, i]

        print(f"Iteration {k}: x = {np.round(x, 6)}")

        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f"\nConverged after {k} iterations.")
            return x, k

    print("\nMaximum iterations reached without convergence.")
    return x, max_iter


# Example usage:
A = np.array([[8.0, 5.0, 2.0], [2.0, 10.0, -2.0], [1.0, 3.0, 6.0]])

b = np.array([25.0, 20.0, 30.0])
x0 = np.array([0.0, 0.0, 0.0])

solution, iterations = jacobi(A, b, x0)
print("Final Jacobi Solution:", np.round(solution, 6))
