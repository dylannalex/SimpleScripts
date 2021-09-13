from math import sqrt


def roots(a, b, c):
    """a*x**2 + b*x + c = 0"""
    root = sqrt(b ** 2 - 4 * a * c)
    denominator = 2 * a
    return (-b + root) / denominator, (-b - root) / denominator
