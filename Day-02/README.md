# Numerical Methods in Python - Day 02

This repository contains implementations of fundamental numerical methods concepts, focusing on error analysis and approximation techniques. This README explains two important Python scripts that demonstrate different types of errors in numerical computations.

## 1. Taylors_Series_Truncation_Error.py

This script demonstrates **truncation error** by approximating the sine function using Taylor series expansion and comparing it with the true value.

### Detailed Line-by-Line Explanation:

#### Import Statements
```python
import math
import numpy as np
```
- `math`: Provides mathematical functions including `sin()` and `factorial()`
- `numpy`: Used for mathematical constants like π (pi)

#### Taylor Series Approximation Function
```python
def taylor_approximation(x_value, num_terms):
    approx_val = 0
    for n in range(num_terms):
        term = (((-1) ** n) * (x_value ** (2 * n + 1))) / math.factorial(2 * n + 1)
        approx_val += term
    return approx_val
```

**Function Purpose**: Calculates the Taylor series approximation of sin(x) using a specified number of terms.

**Mathematical Background**: The Taylor series for sin(x) is:
```
sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + x⁹/9! - ...
```

**Line-by-Line Breakdown**:
- `approx_val = 0`: Initializes the approximation sum to zero
- `for n in range(num_terms):`: Loops through each term (0 to num_terms-1)
- `term = (((-1) ** n) * (x_value ** (2 * n + 1))) / math.factorial(2 * n + 1)`:
  - `(-1) ** n`: Alternating signs (+, -, +, -, ...)
  - `x_value ** (2 * n + 1)`: Odd powers of x (x¹, x³, x⁵, x⁷, ...)
  - `math.factorial(2 * n + 1)`: Factorial of odd numbers (1!, 3!, 5!, 7!, ...)
- `approx_val += term`: Adds each term to the running sum
- `return approx_val`: Returns the final approximation

#### Main Execution
```python
x_point = np.pi / 2
true_sin_val = math.sin(x_point)
```
- `x_point = np.pi / 2`: Sets the evaluation point to π/2 (90 degrees)
- `true_sin_val = math.sin(x_point)`: Calculates the true value of sin(π/2) = 1

```python
print(f"\nTrue sin({x_point:.2f}): {true_sin_val}")
```
- Displays the true value of sin(π/2) with 2 decimal places for the angle

#### Error Analysis Loop
```python
num_term_list = [1, 3, 5, 7, 9]
for terms in num_term_list:
    approx_sin_val = taylor_approximation(x_point, terms)
    truc_error = abs(true_sin_val - approx_sin_val)
    print(f"Approximation With {terms} terms: {approx_sin_val:.8f}, Trucation Error: {truc_error:.8f}")
```

**Purpose**: Demonstrates how truncation error decreases as more terms are included.

**Line-by-Line**:
- `num_term_list = [1, 3, 5, 7, 9]`: List of different numbers of terms to test
- `for terms in num_term_list:`: Iterates through each term count
- `approx_sin_val = taylor_approximation(x_point, terms)`: Calculates approximation with current number of terms
- `truc_error = abs(true_sin_val - approx_sin_val)`: Computes absolute truncation error
- `print(...)`: Displays the approximation and error with 8 decimal places

**Key Concept**: **Truncation Error** occurs when we stop an infinite series after a finite number of terms. As we include more terms, the approximation becomes more accurate and the truncation error decreases.

---

## 2. Inherent_Error.py

This script demonstrates **inherent error** (also called input error) by showing how measurement errors propagate through calculations.

### Detailed Line-by-Line Explanation:

#### Input Values
```python
true_length = 10.12345
measured_length = 10.12
```
- `true_length`: The actual, exact length value
- `measured_length`: The measured value with limited precision (measurement error)

**Real-world Context**: In practice, we can never measure quantities with perfect accuracy due to instrument limitations, human error, and environmental factors.

#### Area Calculations
```python
true_area = true_length**2
measured_area = measured_length**2
```
- `true_area`: Calculates the true area using the exact length (10.12345² = 102.484...)
- `measured_area`: Calculates the area using the measured length (10.12² = 102.4144)

**Important Note**: The error in the input (length measurement) gets amplified when we perform operations like squaring.

#### Error Analysis
```python
inherent_error_in_area = abs(true_area - measured_area)
```
- Calculates the absolute difference between true and computed areas
- This represents how the initial measurement error propagated through the calculation

#### Results Display
```python
print(f"True Area: {true_area:.8f} m^2")
print(f"Measured Area: {measured_area:.8f} m^2")
print(f"Error in Area due to Inherent Error: {inherent_error_in_area:.8f}")
```
- Displays all values with 8 decimal places to clearly show the error magnitude
- Shows how a small input error (0.00345 in length) leads to a larger error in the computed area

**Key Concept**: **Inherent Error** is the error present in the input data itself. This error propagates through calculations and can be amplified depending on the mathematical operations performed.

---
