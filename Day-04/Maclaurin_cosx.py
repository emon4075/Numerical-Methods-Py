import math
import numpy as np
import matplotlib.pyplot as plt


def maclaurin_cos(x, n_terms):
    result = 0
    for n in range(n_terms + 1):
        term = (((-1) ** n) * (x ** (2 * n))) / math.factorial(2 * n)
        result += term
    return result


x_values = np.linspace(-10, 10, 200)

true_cos_values = np.cos(x_values)

n_terms = 10
approx_values = []

for x in x_values:
    approx_values.append(maclaurin_cos(x, n_terms))


plt.plot(x_values, true_cos_values, c="red", ls="--", label="True Cos")
plt.plot(x_values, approx_values, c="green", ls="-.", label="Approximate Cos")

plt.title(f"Maclaurin Series For Cos(x) of {n_terms} Terms")
plt.ylabel("f(x)")
plt.xlabel("x")
plt.grid()
plt.legend()
plt.show()
