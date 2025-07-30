# Numerical Methods in Python - Day 01

This repository contains fundamental examples demonstrating floating-point arithmetic, precision issues, and basic mathematical operations in Python. These concepts are essential for understanding numerical methods and computational mathematics.

## Table of Contents
1. [Basic Operations](#1-basic-operations)
2. [Explore Floating Point Precision](#2-explore-floating-point-precision)
3. [Precision Spacing](#3-precision-spacing)
4. [Cumulative Rounding Error](#4-cumulative-rounding-error)

---

## 1. Basic Operations

**File**: `Basic_Operations.py`

This file demonstrates fundamental mathematical operations and the usage of Python's `math` module.

### Line-by-Line Explanation

```python
import math
```
- Imports Python's built-in `math` module, which provides access to mathematical functions and constants.

```python
# For Exploring the "math" Module
# help(math)
# print(dir(math))
```
- These commented lines show how to explore the `math` module:
  - `help(math)` would display detailed documentation
  - `dir(math)` would list all available functions and constants

### Simple Arithmetic Operations

```python
print("2 + 3 =", 2 + 3)
print("2 * 3 =", 2 * 3)
print("2 ** 3 =", 2**3)
print("20 - 3 =", 20 - 3)
print("20 / 3 =", 20 / 3)
```
- Demonstrates basic arithmetic operations:
  - Addition: `2 + 3 = 5`
  - Multiplication: `2 * 3 = 6`
  - Exponentiation: `2 ** 3 = 8` (2 raised to the power of 3)
  - Subtraction: `20 - 3 = 17`
  - Division: `20 / 3 = 6.666666666666667` (floating-point division)

### Order of Operations

```python
print("(3 * 4) / (2**2 + 4/2) =", (3 * 4) / (2**2 + 4 / 2))
```
- Demonstrates operator precedence and the use of parentheses
- Calculation: `(3 * 4) / (2**2 + 4/2) = 12 / (4 + 2) = 12 / 6 = 2.0`

### Math Module Functions

```python
print("Square root of 9 =", math.sqrt(9))
print("cos(pi/3) =", math.cos(math.pi / 3))
print("e^log(10) =", math.exp(math.log(10)))
print("e^log10(10) =", math.exp(math.log(10, 10)))
```
- `math.sqrt(9)`: Square root function returns `3.0`
- `math.cos(math.pi / 3)`: Cosine of π/3 radians (60 degrees) returns `0.5`
- `math.exp(math.log(10))`: e raised to the natural logarithm of 10, which equals `10.0`
- `math.exp(math.log(10, 10))`: e raised to the base-10 logarithm of 10, which equals `e^1 ≈ 2.718`

### Special Values

```python
print("1 / infinity =", 1 / math.inf)
print("2 * infinity =", 2 * math.inf)
print("infinity / infinity =", math.inf / math.inf)
```
- Demonstrates operations with infinity:
  - `1 / math.inf = 0.0`
  - `2 * math.inf = inf`
  - `math.inf / math.inf = nan` (Not a Number)

### Complex Numbers

```python
print("Complex Number 2 + 5j = ", 2 + 5j)
print("Another Way to Represent =", complex(2, 5))
```
- Shows two ways to create complex numbers in Python:
  - Direct notation: `2 + 5j`
  - Using the `complex()` function: `complex(2, 5)`
- Both represent the complex number 2 + 5i

---

## 2. Explore Floating Point Precision

**File**: `Explore_Floating_Point_Precision.py`

This file examines the internal representation and limitations of floating-point numbers in Python.

### Line-by-Line Explanation

```python
import sys, numpy as np
```
- Imports the `sys` module for system-specific parameters and `numpy` for numerical operations

```python
print("Python's float info: ")
print(sys.float_info)
```
- `sys.float_info` provides detailed information about Python's float implementation
- Displays properties like:
  - `max`: Maximum representable finite float value
  - `min`: Minimum representable normalized positive float value
  - `epsilon`: Difference between 1.0 and the least value greater than 1.0
  - `dig`: Maximum number of decimal digits that can be faithfully represented
  - `mant_dig`: Float precision in base-2 digits
  - `max_exp`, `min_exp`: Maximum and minimum exponents

This information is crucial for understanding the limitations of floating-point arithmetic.

---

## 3. Precision Spacing

**File**: `Precision_Spacing.py`

This file demonstrates floating-point precision issues and the concept of machine epsilon.

### Line-by-Line Explanation

```python
import numpy as np
```
- Imports NumPy for its precision-related functions

### Classic Precision Problem

```python
print("\nTesting Precision:")
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3?", (0.1 + 0.2) == 0.3)
```
- Demonstrates the famous floating-point precision issue
- `0.1 + 0.2` doesn't exactly equal `0.3` due to binary representation limitations
- Result: `0.1 + 0.2 = 0.30000000000000004` and `(0.1 + 0.2) == 0.3` is `False`

### Machine Epsilon at 1.0

```python
gap_at_one = np.spacing(1)
print(f"\nGap at 1.0: {gap_at_one}")
print(f"Is 1.0 == (1.0 + gap_at_one/2)? {1.0 == (1.0 + gap_at_one/2)}")
print(f"Is 1.0 == (1.0 + gap_at_one)? {1.0 == (1.0 + gap_at_one)}")
```
- `np.spacing(1)` returns the machine epsilon at 1.0 (smallest representable gap)
- Tests whether adding half and full epsilon to 1.0 can be distinguished:
  - Adding `gap_at_one/2` to 1.0 is still equal to 1.0 (rounds down)
  - Adding `gap_at_one` to 1.0 creates a distinguishable number

### Machine Epsilon at Large Numbers

```python
num = 1e9
gap_at_one = np.spacing(num)
print(f"\nGap at {num}: {gap_at_one}")
print(f"Is {num} == ({num} + {gap_at_one}/3)? {num == (num + gap_at_one/3)}")
print(f"Is {num} == ({num} + {gap_at_one})? {num == (num + gap_at_one)}")
```
- Demonstrates that machine epsilon increases with the magnitude of numbers
- At `1e9`, the spacing between representable numbers is much larger
- Shows that precision decreases as numbers get larger

---

## 4. Cumulative Rounding Error

**File**: `Cumulative_Rounding_Error.py`

This file demonstrates how small rounding errors can accumulate over many operations.

### Line-by-Line Explanation

```python
def add_and_subtract(iterations):
    result = 1
    for i in range(iterations):
        result += 1 / 3
    for i in range(iterations):
        result -= 1 / 3
    return result
```
- Defines a function that:
  - Starts with `result = 1`
  - Adds `1/3` a specified number of times
  - Subtracts `1/3` the same number of times
  - Mathematically, this should return exactly `1`

### Testing Cumulative Error

```python
print("\nCumulative Rounding Error: ")
print(f"1 + 1/3 - 1/3 = {1 + 1/3 - 1/3}")
print(f"add_and_substract(100) : {add_and_subtract(100)}")
print(f"add_and_substract(1000) : {add_and_subtract(1000)}")
print(f"add_and_substract(10000) : {add_and_subtract(10000)}")
```
- Tests the function with increasing iterations:
  - Single operation: `1 + 1/3 - 1/3` should equal `1.0`
  - 100 iterations: Small deviation from `1.0`
  - 1000 iterations: Larger deviation
  - 10000 iterations: Even larger deviation

The key insight is that each operation introduces a tiny rounding error, and these errors accumulate over many operations, leading to significant deviations from the expected mathematical result.

## Key Takeaways

1. **Floating-point arithmetic is not exact** - Binary representation cannot perfectly represent all decimal numbers
2. **Precision decreases with magnitude** - Larger numbers have larger gaps between representable values
3. **Cumulative errors matter** - Small errors can compound significantly over many operations
4. **Always use tolerance for comparisons** - Never use exact equality (`==`) for floating-point comparisons
5. **Understanding limitations is crucial** - Knowing these limitations helps in designing robust numerical algorithms

These concepts form the foundation for understanding more advanced numerical methods and the importance of error analysis in computational mathematics.