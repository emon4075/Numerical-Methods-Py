# Day-04: Maclaurin Series Approximation for cos(x)

**File:** `Maclaurin_cosx.py`

This file demonstrates the implementation of the Maclaurin series (Taylor series centered at x=0) to approximate the cosine function. The Maclaurin series provides a polynomial approximation that becomes more accurate as more terms are included.

## Mathematical Background

The Maclaurin series for cos(x) is:
```
cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + x⁸/8! - ...
```

General term: `(-1)ⁿ × x^(2n) / (2n)!` for n = 0, 1, 2, 3, ...

---

## Code Explanation:

### Import Statements
```python
import math
import numpy as np
import matplotlib.pyplot as plt
```
- **Line 1:** `import math` - Provides mathematical functions like `factorial()` and the built-in `cos()`
- **Line 2:** `import numpy as np` - Used for creating arrays and numerical operations
- **Line 3:** `import matplotlib.pyplot as plt` - For creating visualizations and plots

### Maclaurin Series Function Definition
```python
def maclaurin_cos(x, n_terms):
    result = 0
    for n in range(n_terms + 1):
        term = (((-1) ** n) * (x ** (2 * n))) / math.factorial(2 * n)
        result += term
    return result
```
- **Line 6:** Define the function `maclaurin_cos` with parameters:
  - `x`: The input value for which to calculate cos(x)
  - `n_terms`: Number of terms to include in the series (degree of approximation)

- **Line 7:** Initialize `result = 0` to accumulate the sum of series terms

- **Line 8:** Start a loop from `n = 0` to `n = n_terms` (inclusive)
  - `range(n_terms + 1)` ensures we include exactly `n_terms + 1` terms (0 through n_terms)

- **Line 9:** Calculate each term of the Maclaurin series:
  - `(-1) ** n`: Alternating signs (+, -, +, -, ...)
    - n=0: (-1)⁰ = +1
    - n=1: (-1)¹ = -1  
    - n=2: (-1)² = +1
    - n=3: (-1)³ = -1
  - `x ** (2 * n)`: Powers of x are always even (0, 2, 4, 6, ...)
    - n=0: x⁰ = 1
    - n=1: x² 
    - n=2: x⁴
    - n=3: x⁶
  - `math.factorial(2 * n)`: Factorial of even numbers (0!, 2!, 4!, 6!, ...)
    - n=0: 0! = 1
    - n=1: 2! = 2
    - n=2: 4! = 24
    - n=3: 6! = 720

- **Line 10:** Add the calculated term to the running sum

- **Line 11:** Return the final approximated value

### Data Preparation
```python
x_values = np.linspace(-10, 10, 200)
```
- **Line 14:** Create an array of x-values for plotting
  - `np.linspace(-10, 10, 200)`: 200 evenly spaced points from -10 to 10
  - This range shows how the approximation performs over a wide interval

```python
true_cos_values = np.cos(x_values)
```
- **Line 16:** Calculate the true cosine values using NumPy's built-in function
  - `np.cos()` applies the cosine function element-wise to the entire array
  - These serve as the "ground truth" for comparison

### Approximation Calculation
```python
n_terms = 10
approx_values = []
```
- **Line 18:** Set the number of terms to use in the approximation
  - `n_terms = 10` means we'll use 11 terms total (n=0 through n=10)
  - More terms generally provide better accuracy but increase computation time

- **Line 19:** Initialize an empty list to store approximated values

```python
for x in x_values:
    approx_values.append(maclaurin_cos(x, n_terms))
```
- **Line 21-22:** Calculate Maclaurin approximation for each x-value
  - Loop through each x-value in the array
  - Call our custom `maclaurin_cos()` function for each point
  - Append the result to the `approx_values` list

### Visualization
```python
plt.plot(x_values, true_cos_values, c="red", ls="--", label="True Cos")
plt.plot(x_values, approx_values, c="green", ls="-.", label="Approximate Cos")
```
- **Line 25:** Plot the true cosine function
  - `c="red"`: Red color for the true function
  - `ls="--"`: Dashed line style
  - `label="True Cos"`: Legend label

- **Line 26:** Plot the Maclaurin approximation
  - `c="green"`: Green color for the approximation
  - `ls="-."`: Dash-dot line style (different from true function)
  - `label="Approximate Cos"`: Legend label

### Plot Formatting and Display
```python
plt.title(f"Maclaurin Series For Cos(x) of {n_terms} Terms")
plt.ylabel("f(x)")
plt.xlabel("x")
plt.grid()
plt.legend()
plt.show()
```
- **Line 28:** Set the plot title using f-string formatting
  - Dynamically includes the number of terms used
  - Makes it clear how many terms were used in the approximation

- **Line 29:** Label the y-axis as "f(x)" (function values)

- **Line 30:** Label the x-axis as "x" (input values)

- **Line 31:** Add a grid for easier value reading

- **Line 32:** Display the legend to distinguish between true and approximate functions

- **Line 33:** Show the complete plot

## Expected Results

When you run this code with 10 terms:

1. **Near x=0:** The approximation will be very accurate since Maclaurin series converge best near the center (x=0)

2. **Small |x| values:** Good approximation for roughly |x| < 5

3. **Large |x| values:** The approximation may deviate significantly from the true cosine, especially beyond |x| > 8

4. **Visual Comparison:** You'll see two curves that overlap closely near the origin but may diverge at the extremes

## Key Concepts Demonstrated

1. **Series Convergence:** More terms improve accuracy near the center
2. **Radius of Convergence:** Infinite for cos(x), but practical accuracy decreases with distance from center
3. **Computational Trade-offs:** More terms = better accuracy but slower computation
4. **Polynomial Approximation:** How smooth functions can be approximated by polynomials

## Experimentation

Try modifying `n_terms` to see how it affects accuracy:
- `n_terms = 5`: Fewer terms, less accurate at extremes
- `n_terms = 20`: More terms, better accuracy but slower computation
- `n_terms = 1`: Only first two terms (1 - x²/2), shows basic parabolic approximation

## Mathematical Insight

This implementation demonstrates how calculus concepts (infinite series) translate into practical computational methods for approximating transcendental functions.