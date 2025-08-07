import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange


def runge_function(x):
    """The function that causes the Runge phenomenon."""
    return 1 / (1 + 25 * x**2)


# 1. Define the parameters
num_points = 15  # A high number of points triggers the effect
x_data = np.linspace(-1, 1, num_points)  # Evenly spaced points
y_data = runge_function(x_data)

# 2. Perform Lagrange interpolation using SciPy
poly = lagrange(x_data, y_data)

# 3. Create points for a smooth plot
x_plot = np.linspace(-1, 1, 200)
y_poly_plot = poly(x_plot)  # The oscillating interpolated curve
y_exact_plot = runge_function(x_plot)  # The true curve

# 4. Plot the results
plt.plot(x_plot, y_exact_plot, "k--", label="True Runge Function")
plt.plot(x_plot, y_poly_plot, "c-", label=f"Lagrange Polynomial (n={num_points})")
plt.plot(x_data, y_data, "ro", label="Data Points")

plt.title("Runge Phenomenon Demonstration")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
