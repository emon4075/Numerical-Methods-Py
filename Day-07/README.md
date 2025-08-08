# Secant Method for Root Finding

**File:** `Secant_Method.py`

The Secant Method is a root-finding algorithm that serves as a modification of Newton's Method. It approximates the derivative using secant lines instead of requiring the exact derivative, making it useful when the derivative is difficult to compute or unavailable.

## Mathematical Background

The Secant Method uses the formula:
```
x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))
```

This formula approximates the derivative f'(x_n) ≈ (f(x_n) - f(x_{n-1})) / (x_n - x_{n-1}), which is the slope of the secant line through the two most recent points.

**Key Differences from Newton's Method:**
- Requires two initial guesses instead of one
- Uses finite difference approximation instead of exact derivative
- Converges slower than Newton's (superlinear vs. quadratic) but faster than bisection
- More robust when derivatives are hard to compute

---

## Code Explanation:

### Main Secant Method Function
```python
def secant_method(f, x0, x1, tolerance=1e-8, max_itr=50):
    print(f"Iteration 0: x = {x0:.8f}")
    print(f"Iteration 1: x = {x1:.8f}")
```
- **Line 1:** Define the secant method function with parameters:
  - `f`: The target function for which we want to find roots
  - `x0`: First initial guess (starting point 1)
  - `x1`: Second initial guess (starting point 2)
  - `tolerance=1e-8`: Stopping criterion (default: 0.00000001, more precise than previous methods)
  - `max_itr=50`: Maximum number of iterations to prevent infinite loops

- **Line 2:** Display the first initial guess (iteration 0)
  - `:.8f`: Format to 8 decimal places for high precision tracking

- **Line 3:** Display the second initial guess (iteration 1)
  - Both initial guesses are needed before the secant formula can be applied

### Main Iteration Loop
```python
    for i in range(2, max_itr + 1):
        fx0 = f(x0)
        fx1 = f(x1)
```
- **Line 5:** Start the iteration loop from 2 (since we already have iterations 0 and 1)
  - The secant method needs two previous points to calculate the next one

- **Line 6:** Calculate the function value at the first point
  - `fx0 = f(x0)`: This is f(x_{n-1}) in the secant formula

- **Line 7:** Calculate the function value at the second point
  - `fx1 = f(x1)`: This is f(x_n) in the secant formula

### Division by Zero Check
```python
        if fx1 - fx0 == 0:
            print("Error: Can't Divide By Zero")
            return None
```
- **Line 9:** Check for the critical failure condition
  - `fx1 - fx0 == 0` means f(x_n) = f(x_{n-1})
  - This would make the denominator of the secant formula zero
  - Occurs when both points have the same function value (horizontal secant line)

- **Line 10:** Display error message for division by zero case

- **Line 11:** Return `None` to indicate method failure
  - The method cannot proceed when the secant line is horizontal

### Secant Formula Application
```python
        xn = x1 - (fx1 * ((x1 - x0) / (fx1 - fx0)))
        print(f"Iteration {i}: x = {xn:.8f}")
```
- **Line 13:** Apply the secant method formula
  - `x1 - (fx1 * ((x1 - x0) / (fx1 - fx0)))`: Complete secant formula
  - **Breaking it down:**
    - `(x1 - x0)`: Difference in x-coordinates
    - `(fx1 - fx0)`: Difference in function values
    - `(x1 - x0) / (fx1 - fx0)`: Slope of secant line (approximate derivative)
    - `fx1 * ((x1 - x0) / (fx1 - fx0))`: Newton-like step using secant slope
    - `x1 - ...`: Subtract step from current point to get next approximation

- **Line 14:** Display the new approximation
  - Shows the current iteration number and calculated x-value

### Convergence Check
```python
        if abs(f(xn)) < tolerance:
            print(f"\nConverged! Root Found After {i} Iterations")
            return xn
```
- **Line 16:** Check if convergence has been achieved
  - `abs(f(xn)) < tolerance`: Check if function value is close enough to zero
  - Uses absolute value to handle both positive and negative function values

- **Line 17:** Announce successful convergence
  - `\n`: Adds blank line for better output formatting
  - Shows the total number of iterations needed

- **Line 18:** Return the converged root value

### Point Update for Next Iteration
```python
        x0 = x1
        x1 = xn
```
- **Line 20:** Update the first point for the next iteration
  - `x0 = x1`: The old second point becomes the new first point

- **Line 21:** Update the second point for the next iteration
  - `x1 = xn`: The newly calculated point becomes the new second point
  - This maintains the "sliding window" of two points needed for the secant method

### Non-Convergence Handling
```python
    print("Try Increasing Max Iteration")
    return xn
```
- **Line 23:** Handle case where maximum iterations are reached
  - Suggests increasing max_itr if convergence wasn't achieved within the limit

- **Line 24:** Return the last calculated value
  - Even if not converged, this might be close to the actual root

### Target Function Definition
```python
def my_function(x):
    return x**2 - 2
```
- **Line 27-28:** Define the specific function for root finding
  - Mathematical form: f(x) = x² - 2
  - Same function used in Newton's method for comparison
  - Roots are at x = ±√2 ≈ ±1.414213562

### Initial Guesses Setup
```python
x0 = 1.0
x1 = 2.0
```
- **Line 31:** Set the first initial guess
  - `x0 = 1.0`: Starting point 1, below the positive root √2

- **Line 32:** Set the second initial guess
  - `x1 = 2.0`: Starting point 2, above the positive root √2
  - Having points on opposite sides of the root often helps convergence

### Method Execution
```python
root = secant_method(f=my_function, x0=x0, x1=x1)
```
- **Line 34:** Execute the secant method
  - Pass the target function and both initial guesses
  - Uses default tolerance (1e-8) and maximum iterations (50)

### Results Display
```python
if root:
    print(f"Final Approximation: {root:.8f}")
```
- **Line 36-37:** Display the final result if successful
  - `if root:` checks if a valid result was returned (not None)
  - Shows the final root approximation to 8 decimal places for high precision

## Expected Output

When you run this code, you should see output similar to:
```
Iteration 0: x = 1.00000000
Iteration 1: x = 2.00000000
Iteration 2: x = 1.33333333
Iteration 3: x = 1.40000000
Iteration 4: x = 1.41379310
Iteration 5: x = 1.41421143
Iteration 6: x = 1.41421356

Converged! Root Found After 6 Iterations
Final Approximation: 1.41421356
```

The exact root is √2 ≈ 1.41421356..., showing excellent accuracy.

## Algorithm Analysis

### Convergence Properties:
- **Superlinear convergence** (approximately φ ≈ 1.618 order, where φ is the golden ratio)
- **Faster than bisection** but **slower than Newton's method**
- **More robust than Newton's** when derivatives are unavailable or expensive

### Advantages:
1. **No derivative required** - only needs function evaluations
2. **Generally stable** - less likely to fail than Newton's method
3. **Good convergence rate** - faster than linear methods
4. **Simple implementation** - straightforward formula

### Disadvantages:
1. **Needs two initial guesses** instead of one
2. **Slower than Newton's method** when derivatives are available
3. **Can fail** if secant lines become horizontal
4. **No convergence guarantee** like bisection method

## Comparison with Other Methods

| Method | Initial Points | Derivative Needed | Convergence Rate | Robustness |
|--------|----------------|-------------------|------------------|------------|
| **Bisection** | 2 (with sign change) | No | Linear | High |
| **Newton's** | 1 | Yes | Quadratic | Medium |
| **Secant** | 2 | No | Superlinear (~1.618) | Medium-High |
| **Fixed Point** | 1 | No | Linear | Low-Medium |

## When to Use Secant Method

**Choose Secant Method when:**
- Derivative is difficult or expensive to compute
- You need faster convergence than bisection
- You have good initial guesses available
- Newton's method is unstable for your function

**Avoid Secant Method when:**
- Derivative is easily available (use Newton's instead)
- You need guaranteed convergence (use bisection)
- Function evaluations are very expensive
- You only have one good initial guess

## Mathematical Insight

The Secant Method demonstrates how numerical methods can adapt mathematical concepts (replacing derivatives with finite differences) to create practical algorithms. It shows the trade-off between computational requirements (no derivative needed) and convergence speed (slower than Newton's but faster than simpler methods).
