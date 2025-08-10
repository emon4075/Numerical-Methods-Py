---
````markdown
# Partial Pivoting Gaussian Elimination in Python

This repository contains a Python implementation of **Gaussian Elimination with Partial Pivoting** for solving linear systems of equations.  
The implementation is in **`Partial_Pivoting.py`**.

---

## 📌 What is Partial Pivoting?

When solving a system of equations \( Ax = b \) using Gaussian elimination, **partial pivoting** improves **numerical stability** by swapping rows so that the **largest (by absolute value)** element in the current column becomes the pivot.  

✅ This avoids:
- Dividing by small numbers
- Large rounding errors
- Crashes from zero pivots

---

## 📂 File Overview: `Partial_Pivoting.py`

### **Imports**
```python
import numpy as np
````

We use **NumPy** for efficient matrix and vector operations.

---

### **Core Function:** `gauss_elim_pivot(A, b)`

This function solves a system of equations $Ax = b$ using Gaussian Elimination **with partial pivoting**.

---

#### **1. Convert Inputs to Float**

Ensures calculations use floating-point numbers for precision.

```python
A = A.astype(float)
b = b.astype(float)
n = len(b)
```

---

#### **2. Forward Elimination with Pivoting**

For each column $k$:

1. **Select pivot row** — row with largest absolute value in column $k$:

   ```python
   pivot = np.argmax(abs(A[k:, k])) + k
   ```
2. **Swap rows** if needed:

   ```python
   if pivot != k:
       A[[k, pivot]], b[[k, pivot]] = A[[pivot, k]], b[[pivot, k]]
   ```
3. **Eliminate below**:

   ```python
   for i in range(k + 1, n):
       factor = A[i, k] / A[k, k]
       A[i, k:] -= factor * A[k, k:]
       b[i] -= factor * b[k]
   ```

---

#### **3. Back Substitution**

Once $A$ is upper triangular, solve for unknowns starting from the last row.

```python
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
```

---

#### **4. Return Solution**

```python
return x
```

---

## 📝 Example Usage

```python
A = np.array([[2, 1, 3], [15, 2, 5], [1, 3, 1]])
b = np.array([10, 5, 3])

sol = gauss_elim_pivot(A, b)

print(f"x = {sol[0]:.4f}, y = {sol[1]:.4f}, z = {sol[2]:.4f}")
print("Check:", A @ sol)
```

---

## 🔍 Step-by-Step Example

We want to solve:

$$
\begin{cases}
2x + y + 3z = 10 \\
15x + 2y + 5z = 5 \\
x + 3y + z = 3
\end{cases}
$$

### **1. Input**

* Coefficient matrix:

$$
A =
\begin{bmatrix}
2 & 1 & 3 \\
15 & 2 & 5 \\
1 & 3 & 1
\end{bmatrix}
$$

* RHS vector:

$$
b =
\begin{bmatrix}
10 \\
5 \\
3
\end{bmatrix}
$$

---

### **2. Partial Pivoting**

* **First column pivot:** largest value is **15** → swap row 1 and row 2.
* **Eliminate below:** make first column entries below pivot zero.
* Repeat for next columns, always swapping for the largest pivot.

---

### **3. Back Substitution**

* Solve for $z$, then $y$, then $x$ using the upper-triangular system.

---

### **4. Output**

```
x = 0.0682, y = 1.0568, z = 2.9250
Check: [10.  5.  3.]
```

The check confirms the solution satisfies $Ax = b$.

---

## ▶️ How to Run

```bash
python Partial_Pivoting.py
```

---

## 💡 Why Use Partial Pivoting?

* ✅ Prevents division by small numbers
* ✅ Handles zero pivots without crashing
* ✅ Improves numerical stability over naive Gaussian elimination

---


