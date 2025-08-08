import math


def bisection_method(f, a, b, tolerance):
    if f(a) * f(b) >= 0:
        print(f"Signs are Not Opposite at [{a, b}]")
        return None
    while ((b - a) / 2.0) > tolerance:
        mid_point = (a + b) / 2.0

        if f(mid_point) == 0 or f(a) * f(mid_point) < 0:
            b = mid_point
        else:
            a = mid_point
    return (a + b) / 2.0


def my_function(x):
    return (2 * math.exp(-2 * x)) - (math.exp(-x))


initial_a = 0.0
initial_b = 1.0
tol = 0.00001

root = bisection_method(f=my_function, a=initial_a, b=initial_b, tolerance=tol)

if root:
    print(f"The Approximate Root is: {root:.7f}")
    print(f"The Real Root is: {math.log(2):.7f}")
