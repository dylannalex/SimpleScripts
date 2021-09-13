from math import sqrt


def roots(a, b, c):
    """a*x**2 + b*x + c = 0"""
    root = sqrt(b ** 2 - 4 * a * c)
    denominator = 2 * a
    return (-b + root) / denominator, (-b - root) / denominator


# Equation: 2x**2 - 10x + 6 = 0
print(roots(2, -10, 6))

# Equation: -6x**2 + 7x - 1 = 0
print(roots(-6, 7, -1))
