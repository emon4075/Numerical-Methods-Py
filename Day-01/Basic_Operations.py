import math

# For Exploring the "math" Module
# help(math)
# print(dir(math))

# Simple Arithmetic
print("2 + 3 =", 2 + 3)
print("2 * 3 =", 2 * 3)
print("2 ** 3 =", 2**3)
print("20 - 3 =", 20 - 3)
print("20 / 3 =", 20 / 3)

# Order of Operations with Parentheses
print("(3 * 4) / (2**2 + 4/2) =", (3 * 4) / (2**2 + 4 / 2))

# Using Math Module Functions
print("Square root of 9 =", math.sqrt(9))
print("cos(pi/3) =", math.cos(math.pi / 3))
print("e^log(10) =", math.exp(math.log(10)))
print("e^log10(10) =", math.exp(math.log(10, 10)))

# Special Values
print("1 / infinity =", 1 / math.inf)
print("2 * infinity =", 2 * math.inf)
print("infinity / infinity =", math.inf / math.inf)

# Complex Numbers
print("Complex Number 2 + 5j = ", 2 + 5j)
print("Another Way to Represent =", complex(2, 5))
