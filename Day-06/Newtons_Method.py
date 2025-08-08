import numpy as np


def newton_raphson_method(f, df, x_n, tolerance=1e-6, max_itr=50):
    x = x_n
    print(f"Iteration 0 x = {x:.7f}")
    for i in range(1, max_itr + 1):
        fx = f(x)
        if fx < tolerance:
            print(f"\nConverged After {i} Iterations")
            return x

        dfx = df(x)
        if dfx == 0:
            print("Derivative is Zero.")
            return None

        x = x - (fx / dfx)
        print(f"Iteration {i}: x = {x:.7f}")
    print("Try Increasing Maximum Iterations")
    return x


def my_function(x):
    return (x**2) - 2


def derivative_my_function(x):
    return 2 * x


root = newton_raphson_method(f=my_function, df=derivative_my_function, x_n=1.7)
print(f"Approximated Root: {root:.7f}")
