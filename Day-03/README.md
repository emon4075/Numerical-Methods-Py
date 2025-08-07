# Day-03: Interpolation Methods in Numerical Analysis

This directory contains Python implementations of various interpolation techniques commonly used in numerical methods. Each file demonstrates a different approach to interpolation, from simple linear methods to more sophisticated polynomial and spline techniques.

## Table of Contents
1. [Linear Interpolation](#1-linear-interpolation)
2. [Lagrange Interpolation](#2-lagrange-interpolation)
3. [Runge Phenomenon](#3-runge-phenomenon)
4. [Cubic Spline Interpolation](#4-cubic-spline-interpolation)

---

## 1. Linear Interpolation

**File:** `Linear_Interpolation.py`

Linear interpolation is the simplest form of interpolation that connects data points with straight lines. This method assumes a linear relationship between adjacent data points.

### Code Explanation:

```python
import numpy as np
import matplotlib.pyplot as plt
```
- **Line 1-2:** Import necessary libraries
  - `numpy`: For numerical operations and the interpolation function
  - `matplotlib.pyplot`: For creating visualizations

```python
# Known Data Points
x_data = [1, 2, 3]
y_data = [20, 120, 125]
```
- **Line 4-6:** Define the known data points
  - `x_data`: Independent variable values (input points)
  - `y_data`: Dependent variable values (output points)
  - These represent three points: (1,20), (2,120), (3,125)

```python
# Point(s) Where We Want to Find the Value(s)
x_new = [1.2, 1.3, 1.66, 1.9, 2.5]
```
- **Line 8-9:** Define the points where we want to interpolate
  - These are the x-values for which we want to estimate corresponding y-values
  - All values should be within the range of original data (1 to 3) for accurate interpolation

```python
# Perform Linear Interpolation
y_new = np.interp(x_new, x_data, y_data)
```
- **Line 11-12:** Execute the linear interpolation
  - `np.interp()`: NumPy's built-in linear interpolation function
  - Parameters: (points to interpolate, known x-points, known y-points)
  - Returns interpolated y-values corresponding to x_new

```python
print(f"Interpolated Value at X = {x_new} is Y = {y_new}")
```
- **Line 14:** Display the interpolation results
  - Shows both the input x-values and calculated y-values

```python
# Plot the Straight Line
plt.plot(x_data, y_data, c="blue", ls="--", label="Linear Interpolation Line")
```
- **Line 17-18:** Plot the interpolation line
  - Connects original data points with dashed blue lines
  - This shows the linear segments between each pair of adjacent points

```python
# Plot the Original Data Points
plt.plot(x_data, y_data, marker="o", ls="None", label="Original Data Points")
```
- **Line 20-21:** Plot the original data points
  - Uses circular markers (`"o"`) with no connecting lines (`ls="None"`)
  - Clearly shows the actual known data points

```python
# Plot the New Interpolated Point
plt.plot(
    x_new,
    y_new,
    c="red",
    ls="None",
    marker="o",
    label=f"Interpolated Point ({x_new}, {y_new})",
)
```
- **Line 23-30:** Plot the interpolated points
  - Red circular markers show where interpolation was performed
  - No connecting lines to distinguish from original data
  - Label includes the actual coordinate values

```python
# Add Titles and Labels
plt.title("Linear Interpolation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()
```
- **Line 32-38:** Format and display the plot
  - Add descriptive title and axis labels
  - Display legend to identify different plot elements
  - Add grid for easier value reading
  - Show the complete visualization

---

## 2. Lagrange Interpolation

**File:** `Lagrange_Interpolation.py`

Lagrange interpolation constructs a polynomial that passes exactly through all given data points. Unlike linear interpolation, this creates a single smooth curve through all points.

### Code Explanation:

```python
import numpy as np
from scipy.interpolate import lagrange
```
- **Line 1-2:** Import required libraries
  - `numpy`: For array operations
  - `scipy.interpolate.lagrange`: Specialized function for Lagrange polynomial construction

```python
# Data Points
x_points = np.array([0, 2, 3])
y_points = np.array([1, 5, 2])
```
- **Line 4-6:** Define the data points as NumPy arrays
  - `x_points`: Independent variable values
  - `y_points`: Corresponding dependent values
  - Points: (0,1), (2,5), (3,2)
  - NumPy arrays are required for SciPy functions

```python
# Point to Interpolate
x_to_find = 1.5
```
- **Line 8-9:** Specify the point for interpolation
  - We want to find the y-value when x = 1.5
  - This point lies between the first two data points

```python
# Find the Lagrange Polynomial
polynomial = lagrange(x_points, y_points)
```
- **Line 11-12:** Construct the Lagrange polynomial
  - `lagrange()` function creates a polynomial object
  - This polynomial passes exactly through all given points
  - The degree of polynomial = (number of points - 1)

```python
# Evaluate it at X
y_result = polynomial(x_to_find)
```
- **Line 14-15:** Evaluate the polynomial at the desired point
  - The polynomial object can be called like a function
  - Returns the interpolated y-value for the given x-value

```python
print(f"Data points (x): {x_points}")
print(f"Data points (y): {y_points}")
print(f"Lagrange Polynomial Equation is:{polynomial}")
print(f"For x = {x_to_find}, the interpolated y is: {y_result:.4f}")
```
- **Line 17-20:** Display comprehensive results
  - Show original data points for reference
  - Display the mathematical form of the polynomial
  - Show the final interpolated result rounded to 4 decimal places

---

## 3. Runge Phenomenon

**File:** `Runge_Phenomenon.py`

The Runge phenomenon demonstrates a critical problem with high-degree polynomial interpolation: using too many evenly spaced points can create unwanted oscillations, especially near the boundaries of the interpolation interval.

### Code Explanation:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
```
- **Line 1-3:** Import necessary libraries
  - `numpy`: For mathematical operations and array handling
  - `matplotlib.pyplot`: For visualization
  - `scipy.interpolate.lagrange`: For polynomial interpolation

```python
def runge_function(x):
    """The function that causes the Runge phenomenon."""
    return 1 / (1 + 25 * x**2)
```
- **Line 6-8:** Define the Runge function
  - This is a classic function known to exhibit the Runge phenomenon
  - Formula: f(x) = 1 / (1 + 25x²)
  - The function is smooth but becomes problematic for polynomial interpolation

```python
# 1. Define the parameters
num_points = 15  # A high number of points triggers the effect
x_data = np.linspace(-1, 1, num_points)  # Evenly spaced points
y_data = runge_function(x_data)
```
- **Line 10-13:** Set up the interpolation data
  - `num_points = 15`: Using many points increases polynomial degree and triggers oscillations
  - `np.linspace(-1, 1, 15)`: Creates 15 evenly spaced points from -1 to 1
  - `y_data`: Calculate corresponding y-values using the Runge function

```python
# 2. Perform Lagrange interpolation using SciPy
poly = lagrange(x_data, y_data)
```
- **Line 15-16:** Create the interpolating polynomial
  - Constructs a degree-14 polynomial (15 points - 1)
  - This high-degree polynomial will show oscillatory behavior

```python
# 3. Create points for a smooth plot
x_plot = np.linspace(-1, 1, 200)
y_poly_plot = poly(x_plot)  # The oscillating interpolated curve
y_exact_plot = runge_function(x_plot)  # The true curve
```
- **Line 18-21:** Prepare data for plotting
  - `x_plot`: 200 points for smooth curve visualization
  - `y_poly_plot`: Polynomial values (will show oscillations)
  - `y_exact_plot`: True function values (smooth curve)

```python
# 4. Plot the results
plt.plot(x_plot, y_exact_plot, "k--", label="True Runge Function")
plt.plot(x_plot, y_poly_plot, "c-", label=f"Lagrange Polynomial (n={num_points})")
plt.plot(x_data, y_data, "ro", label="Data Points")
```
- **Line 23-26:** Create the comparison plot
  - **Black dashed line:** True Runge function (smooth)
  - **Cyan solid line:** Interpolating polynomial (oscillating)
  - **Red circles:** Original data points used for interpolation

```python
plt.title("Runge Phenomenon Demonstration")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
```
- **Line 28-34:** Format and display the plot
  - Add descriptive title highlighting the phenomenon
  - Label axes appropriately
  - Show legend to distinguish between curves
  - Add grid for better readability
  - Display the final comparison

**Key Insight:** This visualization clearly shows how the high-degree polynomial interpolation creates large oscillations near the boundaries (-1 and 1), even though it passes exactly through all data points. This demonstrates why other methods like splines are often preferred for smooth interpolation.

---

## 4. Cubic Spline Interpolation

**File:** `Cubic_Spline_Interpolation.py`

Cubic spline interpolation addresses the problems of high-degree polynomial interpolation by using piecewise cubic polynomials. This method provides smooth interpolation without unwanted oscillations.

### Code Explanation:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
```
- **Line 1-3:** Import required libraries
  - `numpy`: For array operations and numerical computations
  - `matplotlib.pyplot`: For creating visualizations
  - `scipy.interpolate.CubicSpline`: Specialized function for cubic spline interpolation

```python
x_data = np.array([1, 3, 5, 8])
y_data = np.array([2, 3, 9, 10])
```
- **Line 5-6:** Define the data points
  - Four data points: (1,2), (3,3), (5,9), (8,10)
  - NumPy arrays are required for SciPy functions
  - These points show a non-linear relationship

```python
cs = CubicSpline(x_data, y_data)
```
- **Line 8:** Create the cubic spline object
  - `CubicSpline()` constructs piecewise cubic polynomials
  - Each segment between adjacent points uses a different cubic polynomial
  - Ensures smoothness by matching derivatives at connection points

```python
x_smooth = np.linspace(x_data.max(), x_data.min(), 100)
y_smooth = cs(x_smooth)
```
- **Line 10-11:** Generate smooth curve data
  - **Note:** There's likely an error here - should be `(x_data.min(), x_data.max())`
  - Creates 100 points for smooth visualization
  - `cs(x_smooth)`: Evaluate the spline at all interpolation points

```python
plt.plot(x_smooth, y_smooth, c="green", label="Cubic Spline Interpolation")
plt.plot(x_smooth, y_smooth, marker="o", ms=2, ls="None", c="red", label="Data Points")
```
- **Line 13-14:** Plot the interpolation results
  - **Green line:** Shows the smooth cubic spline curve
  - **Red dots:** Should show original data points, but there's a labeling error
  - `ms=2`: Sets marker size to 2 points

```python
plt.title("Cubic Spline Interpolation")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid()
plt.show()
```
- **Line 15-20:** Format and display the plot
  - Add descriptive title
  - Label both axes
  - Display legend (though there's a labeling issue in the code)
  - Add grid for easier value reading
  - Show the complete visualization

```python
x = 4
y = cs(x)
print(f"Interpolated Value at {x} is : {y:.4f}")
```
- **Line 22-24:** Demonstrate interpolation at a specific point
  - Choose x = 4 (between data points 3 and 5)
  - Evaluate the spline at this point
  - Display result rounded to 4 decimal places

**Key Advantages of Cubic Splines:**
- Smooth curves without oscillations
- Continuous first and second derivatives
- Local control (changing one point affects only nearby segments)
- More stable than high-degree polynomial interpolation

---

## Summary

This collection demonstrates the evolution of interpolation methods:

1. **Linear Interpolation:** Simple but creates sharp corners
2. **Lagrange Interpolation:** Smooth single polynomial but can oscillate
3. **Runge Phenomenon:** Shows the dangers of high-degree polynomial interpolation
4. **Cubic Spline:** Provides smooth, stable interpolation without oscillations

Each method has its appropriate use cases depending on the data characteristics and desired smoothness of the interpolated curve.

## Requirements

To run these scripts, you need:
- Python 3.x
- NumPy
- SciPy
- Matplotlib

Install dependencies using:
```bash
pip install numpy scipy matplotlib
```

## Usage

Run each file independently to see the interpolation method in action:
```bash
python Linear_Interpolation.py
python Lagrange_Interpolation.py
python Runge_Phenomenon.py
python Cubic_Spline_Interpolation.py
```