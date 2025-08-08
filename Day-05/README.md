# Day-05: Bisection Method for Root Finding

**File:** `Bisection_Method.py`

This file demonstrates the implementation of the Bisection Method, a numerical technique for finding roots (zeros) of continuous functions. The method is based on the Intermediate Value Theorem and uses a divide-and-conquer approach to narrow down the location of a root.

## Mathematical Background

The Bisection Method finds roots of equations f(x) = 0 by:
1. Starting with an interval [a, b] where f(a) and f(b) have opposite signs
2. Repeatedly bisecting the interval and keeping the half where the sign change occurs
3. Continuing until the interval is smaller than a specified tolerance

**Requirements:** The function must be continuous, and f(a) × f(b) < 0 (opposite signs at endpoints).

---

## Code Explanation:

### Import Statement
```python
import math
```
- **Line 1:** Import the math module for mathematical functions
  - Needed for `math.exp()` (exponential function) and `math.log()` (natural logarithm)

### Bisection Method Function Definition
```python
def bisection_method(f, a, b, tolerance):
    if f(a) * f(b) >= 0:
        print(f"Signs are Not Opposite at [{a, b}]")
        return None
```
- **Line 4:** Define the main bisection function with parameters:
  - `f`: The function for which we want to find the root
  - `a`: Left endpoint of the initial interval
  - `b`: Right endpoint of the initial interval  
  - `tolerance`: Stopping criterion (how close to the actual root)

- **Line 5:** Check the fundamental requirement of bisection method
  - `f(a) * f(b) >= 0` means both function values have the same sign
  - If true, there's no guaranteed root in the interval [a, b]

- **Line 6:** Display error message if the sign condition fails
  - Shows the problematic interval endpoints

- **Line 7:** Return `None` to indicate failure (no root found)

### Main Bisection Loop
```python
    while ((b - a) / 2.0) > tolerance:
        mid_point = (a + b) / 2.0
```
- **Line 8:** Continue the bisection process while the interval is larger than tolerance
  - `(b - a) / 2.0`: Half the current interval width
  - When this becomes ≤ tolerance, we've found our root with desired precision

- **Line 9:** Calculate the midpoint of the current interval
  - `mid_point = (a + b) / 2.0`: Arithmetic mean of the interval endpoints
  - This is our current best estimate of the root location

### Interval Update Logic
```python
        if f(mid_point) == 0 or f(a) * f(mid_point) < 0:
            b = mid_point
        else:
            a = mid_point
```
- **Line 11:** Check two conditions for updating the interval:
  - **First condition:** `f(mid_point) == 0`
    - If true, we've found the exact root
  - **Second condition:** `f(a) * f(mid_point) < 0`
    - If true, f(a) and f(mid_point) have opposite signs
    - This means the root lies in the left half of the interval [a, mid_point]

- **Line 12:** Update the right endpoint
  - `b = mid_point`: The root is in [a, mid_point], so make mid_point the new right boundary

- **Line 13-14:** Handle the alternative case
  - If neither condition in line 11 is true, then f(mid_point) and f(b) must have opposite signs
  - `a = mid_point`: The root is in [mid_point, b], so make mid_point the new left boundary

### Return Final Result
```python
    return (a + b) / 2.0
```
- **Line 15:** Return the final root approximation
  - After the loop ends, the interval [a, b] is smaller than tolerance
  - The midpoint of this small interval is our best root approximation

### Target Function Definition
```python
def my_function(x):
    return (2 * math.exp(-2 * x)) - (math.exp(-x))
```
- **Line 18-19:** Define the specific function whose root we want to find
  - Mathematical form: f(x) = 2e^(-2x) - e^(-x)
  - This is equivalent to: f(x) = e^(-x)(2e^(-x) - 1)
  - Setting f(x) = 0: 2e^(-2x) = e^(-x)
  - Dividing by e^(-x): 2e^(-x) = 1
  - Therefore: e^(-x) = 1/2
  - Taking natural log: -x = ln(1/2) = -ln(2)
  - So the exact root is: x = ln(2) ≈ 0.693147

### Parameter Setup
```python
initial_a = 0.0
initial_b = 1.0
tol = 0.00001
```
- **Line 22:** Set the left endpoint of the initial interval
  - `initial_a = 0.0`: Starting point of our search interval

- **Line 23:** Set the right endpoint of the initial interval  
  - `initial_b = 1.0`: Ending point of our search interval
  - The interval [0, 1] should contain the root ln(2) ≈ 0.693

- **Line 24:** Set the tolerance (precision requirement)
  - `tol = 0.00001`: Stop when the interval width is ≤ 0.00001
  - This gives approximately 5 decimal places of accuracy

### Method Execution
```python
root = bisection_method(f=my_function, a=initial_a, b=initial_b, tolerance=tol)
```
- **Line 26:** Execute the bisection method with our parameters
  - `f=my_function`: Pass our target function
  - `a=initial_a, b=initial_b`: Use the interval [0, 1]
  - `tolerance=tol`: Use the specified precision
  - Store the result in `root` variable

### Results Display
```python
if root:
    print(f"The Approximate Root is: {root:.7f}")
    print(f"The Real Root is: {math.log(2):.7f}")
```
- **Line 28:** Check if a root was found
  - `if root:` evaluates to `True` if root is not `None`

- **Line 29:** Display the approximate root found by bisection method
  - `{root:.7f}`: Format to 7 decimal places for precision comparison

- **Line 30:** Display the exact analytical root for comparison
  - `math.log(2)`: Natural logarithm of 2 (the exact solution)
  - `{math.log(2):.7f}`: Also formatted to 7 decimal places

## Expected Output

When you run this code, you should see output similar to:
```
The Approximate Root is: 0.6931458
The Real Root is: 0.6931472
```

The slight difference shows the numerical approximation error, which is within our specified tolerance.

## Algorithm Analysis

### Convergence Properties:
- **Always converges** if the initial interval contains a root
- **Linear convergence** rate (relatively slow but reliable)
- **Guaranteed accuracy** bounded by the tolerance parameter

### Number of Iterations:
The number of iterations required is approximately: `log₂((b-a)/tolerance)`

For this example: `log₂((1-0)/0.00001) = log₂(100000) ≈ 16.6`

So approximately 17 iterations are needed.

### Advantages:
1. **Robust**: Always works if initial conditions are met
2. **Simple**: Easy to understand and implement
3. **Guaranteed**: Convergence is mathematically certain

### Disadvantages:
1. **Slow**: Linear convergence (other methods like Newton's are faster)
2. **Requires sign change**: Need f(a) and f(b) to have opposite signs
3. **Single root**: Only finds one root per interval

## Verification

To verify the solution, substitute x = ln(2) into the original function:
- f(ln(2)) = 2e^(-2ln(2)) - e^(-ln(2))
- f(ln(2)) = 2e^(ln(1/4)) - e^(ln(1/2))  
- f(ln(2)) = 2(1/4) - (1/2)
- f(ln(2)) = 1/2 - 1/2 = 0 ✓

This confirms that x = ln(2) is indeed the exact root.

## Experimentation

Try modifying the parameters to see different behaviors:

1. **Different tolerance:** Change `tol` to see how it affects accuracy and iterations
2. **Different interval:** Try [0.5, 0.8] (still contains the root)
3. **Bad interval:** Try [0, 0.5] (doesn't contain root) to see the error handling
4. **Different function:** Replace `my_function` with other continuous functions

## Mathematical Insight

The Bisection Method demonstrates how mathematical theorems (Intermediate Value Theorem) can be transformed into practical computational algorithms for solving equations that have no algebraic solutions.