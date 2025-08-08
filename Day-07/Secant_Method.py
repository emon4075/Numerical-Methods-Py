def secant_method(f, x0, x1, tolerance=1e-8, max_itr=50):
    print(f"Iteration 0: x = {x0:.8f}")
    print(f"Iteration 1: x = {x1:.8f}")

    for i in range(2, max_itr + 1):
        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            print("Error: Can't Divide By Zero")
            return None

        xn = x1 - (fx1 * ((x1 - x0) / (fx1 - fx0)))
        print(f"Iteration {i}: x = {xn:.8f}")

        if abs(f(xn)) < tolerance:
            print(f"\nConverged! Root Found After {i} Iterations")
            return xn

        x0 = x1
        x1 = xn

    print("Try Increasing Max Iteration")
    return xn


def my_function(x):
    return x**2 - 2


x0 = 1.0
x1 = 2.0

root = secant_method(f=my_function, x0=x0, x1=x1)

if root:
    print(f"Final Approximation: {root:.8f}")
