# Day-06: Advanced Root Finding Methods

This directory contains Python implementations of advanced numerical methods for finding roots of equations. These methods build upon simpler techniques like the bisection method, offering faster convergence and different approaches to solving f(x) = 0.

## Table of Contents
1. [Fixed Point Iteration](#1-fixed-point-iteration)
2. [Newton's Method Initial Guess](#2-newtons-method-initial-guess)
3. [Newton's Method](#3-newtons-method)

---

## 1. Fixed Point Iteration

**File:** `Fixed_Point_Iteration.py`

Fixed Point Iteration is a method for finding roots by transforming the equation f(x) = 0 into the equivalent form x = g(x), then iteratively applying x_{n+1} = g(x_n) until convergence. The solution is called a "fixed point" because g(x*) = x*.

### Mathematical Background

To solve f(x) = 0, we rearrange it to x = g(x) form. For example:
- Original: x² - x - 1 = 0
- Rearranged: x = 1 + 1/x (so g(x) = 1 + 1/x)

### Code Explanation:

```python
import math
```
- **Line 1:** Import the math module for mathematical functions
  - Provides access to mathematical constants and functions if needed

### Main Function Definition
```python
def fixed_point_iteration(g, x_0, tolerance=1e-6, max_itr=50):
    x_current = x_0
    print(f"Iteration 0: x = {x_current:.6f}")
```
- **Line 4:** Define the fixed point iteration function with parameters:
  - `g`: The iteration function g(x) where we seek x = g(x)
  - `x_0`: Initial guess (starting point for iteration)
  - `tolerance=1e-6`: Stopping criterion (default: 0.000001)
  - `max_itr=50`: Maximum number of iterations to prevent infinite loops

- **Line 5:** Initialize the current x-value with the initial guess
  - `x_current`: Stores the current approximation of the fixed point

- **Line 6:** Display the initial guess (iteration 0)
  - `:.6f`: Format to 6 decimal places for consistent output

### Iteration Loop
```python
    for itr in range(1, max_itr + 1):
        x_previous = x_current
        x_current = g(x_previous)
        print(f"Iteration {itr}: x = {x_current:.6f}")
```
- **Line 8:** Start the iteration loop from 1 to max_itr (inclusive)
  - Each iteration applies the function g(x) to get closer to the fixed point

- **Line 9:** Store the current value as the previous value
  - Needed to calculate the change between iterations

- **Line 10:** Apply the iteration function to get the next approximation
  - `x_current = g(x_previous)`: Core of the fixed point method
  - This is the mathematical step: x_{n+1} = g(x_n)

- **Line 11:** Display the current iteration number and x-value
  - Shows the progress of convergence

### Convergence Check
```python
        if abs(x_current - x_previous) < tolerance:
            print(f"Convergence Achieved After {itr} Iterations.")
            return x_current
```
- **Line 13:** Check if convergence has been achieved
  - `abs(x_current - x_previous)`: Absolute difference between successive iterations
  - If this difference is smaller than tolerance, we've found our solution

- **Line 14:** Announce successful convergence
  - Shows how many iterations were needed

- **Line 15:** Return the converged value as the fixed point

### Non-Convergence Handling
```python
    print("Failed To Converge")
    return None
```
- **Line 17-18:** Handle the case where the method doesn't converge
  - If the loop completes without meeting the tolerance, convergence failed
  - Returns `None` to indicate failure

### Iteration Function Definition
```python
def my_function(x):
    return 1 + (1 / x)
```
- **Line 21-22:** Define the specific iteration function g(x)
  - Mathematical form: g(x) = 1 + 1/x
  - This comes from rearranging x² - x - 1 = 0 to x = 1 + 1/x
  - The fixed point satisfies: x = 1 + 1/x, or equivalently x² - x - 1 = 0

### Method Execution
```python
initial_guess = 2
root = fixed_point_iteration(g=my_function, x_0=initial_guess)
```
- **Line 25:** Set the starting point for iteration
  - `initial_guess = 2`: Choose x_0 = 2 as our starting approximation

- **Line 26:** Execute the fixed point iteration
  - Pass our iteration function and initial guess
  - Uses default tolerance and maximum iterations

### Results Display
```python
if root:
    print(f"\nThe Calculated Root is Approximately: {root:.6f}")
```
- **Line 28-29:** Display the result if convergence was successful
  - `if root:` checks if a valid result was returned (not None)
  - `\n`: Adds a blank line for better output formatting
  - Shows the final approximation to 6 decimal places

**Expected Result:** The golden ratio φ = (1 + √5)/2 ≈ 1.618034

---

## 2. Newton's Method Initial Guess

**File:** `Newtons_Method_Initial_Guess.py`

This file provides a visual tool for selecting an appropriate initial guess for Newton's method. By plotting the function, you can identify where roots might exist and choose a good starting point for the Newton-Raphson iteration.

### Mathematical Background

Newton's method requires a good initial guess to ensure convergence. A poor initial guess might:
- Lead to divergence
- Converge to a different root than intended
- Require many more iterations

Visualizing the function helps identify suitable starting points near the desired root.

### Code Explanation:

```python
import numpy as np
import matplotlib.pyplot as plt
```
- **Line 1:** Import NumPy for numerical arrays and mathematical operations
- **Line 2:** Import Matplotlib for creating plots and visualizations

### Function Definition
```python
def my_function(x):
    return (x**2) - 2
```
- **Line 5-6:** Define the target function for which we want to find roots
  - Mathematical form: f(x) = x² - 2
  - This function has roots at x = ±√2 ≈ ±1.414
  - We're looking for points where f(x) = 0

### Data Generation for Plotting
```python
x_values = np.linspace(-10, 10, 200)
y_values = my_function(x_values)
```
- **Line 9:** Create an array of x-values for plotting
  - `np.linspace(-10, 10, 200)`: 200 evenly spaced points from -10 to 10
  - This range is wide enough to show the function's behavior and both roots

- **Line 10:** Calculate corresponding y-values
  - `my_function(x_values)`: Apply the function to each x-value
  - Creates the data points needed to plot the curve

### Visualization
```python
plt.plot(x_values, y_values, ls="--", c="blue", label="Function F(X)")
```
- **Line 12:** Plot the function curve
  - `ls="--"`: Use dashed line style
  - `c="blue"`: Use blue color for the curve
  - `label="Function F(X)"`: Legend label for the plot

### Plot Formatting
```python
plt.title("Approximating The Initial Guess")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
```
- **Line 14:** Set the plot title
  - Clearly indicates the purpose: helping choose initial guess

- **Line 15:** Label the x-axis

- **Line 16:** Label the y-axis

- **Line 17:** Display the legend to identify the plotted function

- **Line 18:** Add a grid for easier value reading
  - Helps identify approximate x-coordinates where the function crosses y=0

- **Line 19:** Display the complete plot

### How to Use This Visualization:

1. **Identify Zero Crossings:** Look for points where the curve crosses the x-axis (y=0)
2. **Choose Nearby Points:** Select initial guesses close to these crossings
3. **Consider Slope:** Areas with steeper slopes generally provide better convergence
4. **Avoid Flat Regions:** Areas where the curve is nearly horizontal may cause problems

For f(x) = x² - 2:
- **Good initial guesses:** x₀ = 1.0 or x₀ = 1.5 (for positive root)
- **Good initial guesses:** x₀ = -1.0 or x₀ = -1.5 (for negative root)
- **Poor initial guesses:** x₀ = 0 (derivative is zero), x₀ = 10 (too far from roots)

---

## 3. Newton's Method

**File:** `Newtons_Method.py`

Newton's Method (also called Newton-Raphson Method) is one of the most powerful and widely-used root-finding algorithms. It uses both the function value and its derivative to rapidly converge to a root.

### Mathematical Background

Newton's method uses the formula:
```
x_{n+1} = x_n - f(x_n)/f'(x_n)
```

This formula comes from the linear approximation (tangent line) to the function at the current point.

### Code Explanation:

```python
import numpy as np
```
- **Line 1:** Import NumPy for numerical operations
  - Provides mathematical functions and array operations

### Main Newton-Raphson Function
```python
def newton_raphson_method(f, df, x_n, tolerance=1e-6, max_itr=50):
    x = x_n
    print(f"Iteration 0 x = {x:.7f}")
```
- **Line 4:** Define the Newton-Raphson function with parameters:
  - `f`: The target function f(x) for which we want to find roots
  - `df`: The derivative function f'(x)
  - `x_n`: Initial guess for the root
  - `tolerance=1e-6`: Stopping criterion (default: 0.000001)
  - `max_itr=50`: Maximum iterations to prevent infinite loops

- **Line 5:** Initialize the current x-value with the initial guess

- **Line 6:** Display the starting point (iteration 0)
  - `:.7f`: Format to 7 decimal places for high precision

### Newton-Raphson Iteration Loop
```python
    for i in range(1, max_itr + 1):
        fx = f(x)
        if fx < tolerance:
            print(f"\nConverged After {i} Iterations")
            return x
```
- **Line 7:** Start the iteration loop from 1 to max_itr

- **Line 8:** Calculate the function value at current x
  - `fx = f(x)`: This is f(x_n) in the Newton's formula

- **Line 9-11:** Check for convergence based on function value
  - If |f(x)| < tolerance, we're close enough to a root
  - The function value being near zero indicates we've found the root

### Derivative Check and Formula Application
```python
        dfx = df(x)
        if dfx == 0:
            print("Derivative is Zero.")
            return None

        x = x - (fx / dfx)
        print(f"Iteration {i}: x = {x:.7f}")
```
- **Line 13:** Calculate the derivative at current x
  - `dfx = df(x)`: This is f'(x_n) in Newton's formula

- **Line 14-16:** Check for zero derivative (critical failure condition)
  - If f'(x) = 0, the Newton's formula breaks down (division by zero)
  - This can happen at local maxima/minima or inflection points
  - Return `None` to indicate method failure

- **Line 18:** Apply Newton's formula to get the next approximation
  - `x = x - (fx / dfx)`: This is the core Newton-Raphson update
  - Mathematically: x_{n+1} = x_n - f(x_n)/f'(x_n)

- **Line 19:** Display the current iteration results
  - Shows the progression toward the root

### Non-Convergence Handling
```python
    print("Try Increasing Maximum Iterations")
    return x
```
- **Line 20-21:** Handle case where maximum iterations are reached
  - Suggests increasing max_itr if convergence wasn't achieved
  - Returns the last calculated value (might still be useful)

### Target Function and Its Derivative
```python
def my_function(x):
    return (x**2) - 2


def derivative_my_function(x):
    return 2 * x
```
- **Line 24-25:** Define the target function
  - Mathematical form: f(x) = x² - 2
  - Roots are at x = ±√2

- **Line 28-29:** Define the derivative function
  - Mathematical form: f'(x) = 2x
  - Derivative of x² - 2 is 2x (constant term disappears)

### Method Execution and Results
```python
root = newton_raphson_method(f=my_function, df=derivative_my_function, x_n=1.7)
print(f"Approximated Root: {root:.7f}")
```
- **Line 32:** Execute Newton's method
  - Use the defined function and its derivative
  - Start with initial guess x₀ = 1.7 (close to √2 ≈ 1.414)

- **Line 33:** Display the final result
  - Shows the approximated root to 7 decimal places

### Expected Behavior:

For f(x) = x² - 2 with x₀ = 1.7:
1. **Iteration 0:** x = 1.7000000
2. **Iteration 1:** x ≈ 1.4264706 (much closer to √2)
3. **Iteration 2:** x ≈ 1.4142857 (very close to √2)
4. **Iteration 3:** x ≈ 1.4142136 (extremely close to √2)

The method typically converges in just a few iterations due to its quadratic convergence rate.

---

## Comparison of Methods

| Method | Convergence Rate | Requirements | Advantages | Disadvantages |
|--------|------------------|--------------|------------|---------------|
| **Fixed Point** | Linear | x = g(x) form, \|g'(x)\| < 1 | Simple, guaranteed if convergent | Slow, may not converge |
| **Newton's** | Quadratic | Function and derivative | Very fast convergence | Needs derivative, can fail |

## Key Concepts Demonstrated

1. **Iteration vs. Direct Methods:** All methods use iterative approximation
2. **Convergence Criteria:** Different ways to determine when to stop
3. **Error Handling:** Managing cases where methods fail
4. **Visualization:** Using plots to understand function behavior
5. **Mathematical Transformation:** Converting problems to suitable forms

## Requirements

To run these scripts, you need:
- Python 3.x
- NumPy
- Matplotlib

Install dependencies using:
```bash
pip install numpy matplotlib
```

## Usage

Run each file independently:
```bash
python Fixed_Point_Iteration.py
python Newtons_Method_Initial_Guess.py  # Shows plot for choosing initial guess
python Newtons_Method.py
```

## Experimentation Suggestions

1. **Fixed Point:** Try different g(x) functions and initial guesses
2. **Newton's Method:** Experiment with different initial guesses to see convergence behavior
3. **Comparison:** Time both methods to see the speed difference
4. **Challenging Functions:** Try functions with multiple roots or difficult convergence properties

## Mathematical Insights

These implementations demonstrate how calculus concepts (derivatives, limits, convergence) translate into practical computational algorithms. Newton's method, in particular, shows the power of using derivative information to accelerate convergence dramatically.