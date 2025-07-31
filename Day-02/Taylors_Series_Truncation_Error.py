import math
import numpy as np


def taylor_approximation(x_value, num_terms):
    approx_val = 0
    for n in range(num_terms):
        term = (((-1) ** n) * (x_value ** (2 * n + 1))) / math.factorial(2 * n + 1)
        approx_val += term
    return approx_val


x_point = np.pi / 2
true_sin_val = math.sin(x_point)

print(f"\nTrue sin({x_point:.2f}): {true_sin_val}")

num_term_list = [1, 3, 5, 7, 9]
for terms in num_term_list:
    approx_sin_val = taylor_approximation(x_point, terms)
    truc_error = abs(true_sin_val - approx_sin_val)
    print(
        f"Approximation With {terms} terms: {approx_sin_val:.8f}, Trucation Error: {truc_error:.8f}"
    )
