import numpy as np
import matplotlib.pyplot as plt

# Known Data Points
x_data = [1, 2, 3]
y_data = [20, 120, 125]

# Point(s) Where We Want to Find the Value(s)
x_new = [1.2, 1.3, 1.66, 1.9, 2.5]

# Perform Linear Interpolation
y_new = np.interp(x_new, x_data, y_data)

print(f"Interpolated Value at X = {x_new} is Y = {y_new}")


# Plot the Straight Line
plt.plot(x_data, y_data, c="blue", ls="--", label="Linear Interpolation Line")

# Plot the Original Data Points
plt.plot(x_data, y_data, marker="o", ls="None", label="Original Data Points")

# Plot the New Interpolated Point
plt.plot(
    x_new,
    y_new,
    c="red",
    ls="None",
    marker="o",
    label=f"Interpolated Point ({x_new}, {y_new})",
)

# Add Titles and Labels
plt.title("Linear Interpolation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()
