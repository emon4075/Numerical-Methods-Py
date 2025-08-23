import numpy as np

A = np.array([[1, 1], [-2, 1], [2, 1]])
b = np.array([2, 1, 4])

# Factor A into Q and R
q, r = np.linalg.qr(A)

# Calculate Q^T * b
q_t_b = q.T @ b

# Solve Rx = Q^T * b for x
x = np.linalg.solve(r, q_t_b)

print("Q Matrix:\n", q)
print("R Matrix:\n", r)
print("Solution x:\n", x)
