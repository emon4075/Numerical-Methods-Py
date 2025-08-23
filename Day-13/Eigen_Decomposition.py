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
