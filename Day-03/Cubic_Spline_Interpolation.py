import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x_data = np.array([1, 3, 5, 8])
y_data = np.array([2, 3, 9, 10])

cs = CubicSpline(x_data, y_data)

x_smooth = np.linspace(x_data.max(), x_data.min(), 100)
y_smooth = cs(x_smooth)

plt.plot(x_smooth, y_smooth, c="green", label="Cubic Spline Interpolation")
plt.plot(x_smooth, y_smooth, marker="o", ms=2, ls="None", c="red", label="Data Points")
plt.title("Cubic Spline Interpolation")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid()
plt.show()

x = 4
y = cs(x)
print(f"Interpolated Value at {x} is : {y:.4f}")
