import numpy as np
import matplotlib.pyplot as plt


def my_function(x):
    return (x**2) - 2


x_values = np.linspace(-10, 10, 200)
y_values = my_function(x_values)

plt.plot(x_values, y_values, ls="--", c="blue", label="Function F(X)")

plt.title("Approximating The Initial Guess")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
