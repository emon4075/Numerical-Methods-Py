import numpy as np
from scipy.interpolate import lagrange

# Data Points
x_points = np.array([0, 2, 3])
y_points = np.array([1, 5, 2])

# Point to Interpolate
x_to_find = 1.5

# Find the Lagrange Polynomial
polynomial = lagrange(x_points, y_points)

# Evaluate it at X
y_result = polynomial(x_to_find)

print(f"Data points (x): {x_points}")
print(f"Data points (y): {y_points}")
print(f"Lagrange Polynomial Equation is:{polynomial}")
print(f"For x = {x_to_find}, the interpolated y is: {y_result:.4f}")
