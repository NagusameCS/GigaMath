# GigaMath

GigaMath is a comprehensive Python library that provides a wide range of mathematical functions across various domains including algebra, calculus, trigonometry, statistics, geometry, linear algebra, complex numbers, and number theory. 

## Features

- Algebra: addition, subtraction, multiplication, division, power, square root, factorial, greatest common divisor (GCD), least common multiple (LCM)
- Calculus: derivative, integral, definite integral
- Trigonometry: sine, cosine, tangent, arcsine, arccosine, arctangent
- Statistics: mean, median, standard deviation, variance
- Geometry: area of a circle, perimeter of a rectangle, volume of a sphere
- Linear Algebra: matrix addition, matrix multiplication, determinant, inverse matrix
- Complex Numbers: complex addition, complex multiplication, magnitude, phase
- Number Theory: prime check, prime factors, Fibonacci sequence

## Installation

You can install the GigaMath library using pip:

```bash
pip install git+https://github.com/NagusameCS/GigaMath.git
```

## Usage
After installation, you can import and use the various mathematical functions provided by GigaMath. Below are some examples of how to use the library:

```bash
import GigaMath as gm

# Algebra
print(gm.add(5, 3))            # Output: 8
print(gm.sqrt(16))             # Output: 4.0

# Calculus
print(gm.derivative('x**2', 'x'))   # Output: '2*x'
print(gm.definite_integral('x', 'x', 0, 1))   # Output: 0.5

# Trigonometry
print(gm.sin(3.14159/2))       # Output: 1.0

# Statistics
print(gm.mean([1, 2, 3, 4, 5]))   # Output: 3.0

# Geometry
print(gm.area_circle(5))       # Output: 78.53981633974483

# Linear Algebra
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
print(gm.matrix_add(matrix1, matrix2))   # Output: [[6, 8], [10, 12]]

# Complex Numbers
print(gm.complex_add(1+2j, 3+4j))   # Output: (4+6j)

# Number Theory
print(gm.is_prime(29))   # Output: True
```
