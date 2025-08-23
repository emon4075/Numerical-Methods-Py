import numpy as np

# Step 1: Define matrix A and vector b
A = np.array([[0, 1], [1, 1], [2, 1], [5, 1]])

b = np.array([0, 3, 3, 6])

# Step 2: Compute A^T A and A^T b
ATA = A.T @ A
ATb = A.T @ b

# Step 3: Solve for x = [c1, c2]
x_hat = np.linalg.solve(ATA, ATb)

c1, c2 = x_hat
print(f"The solution is c1 = {c1:.4f} and c2 = {c2:.4f}")
print(f"Best fit line: y = {c1:.4f}x + {c2:.4f}")

# Verify manually computed values
print(f"15/14 = {15/14:.4f}")
print(f"6/7 = {6/7:.4f}")
