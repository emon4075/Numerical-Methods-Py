import math


def fixed_point_iteration(g, x_0, tolerance=1e-6, max_itr=50):
    x_current = x_0
    print(f"Iteration 0: x = {x_current:.6f}")

    for itr in range(1, max_itr + 1):
        x_previous = x_current
        x_current = g(x_previous)
        print(f"Iteration {itr}: x = {x_current:.6f}")

        if abs(x_current - x_previous) < tolerance:
            print(f"Convergence Achieved After {itr} Iterations.")
            return x_current

    print("Failed To Converge")
    return None


def my_function(x):
    return 1 + (1 / x)


initial_guess = 2
root = fixed_point_iteration(g=my_function, x_0=initial_guess)

if root:
    print(f"\nThe Calculated Root is Approximately: {root:.6f}")
