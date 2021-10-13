from typing import Callable
from math import sqrt


def derivative(f: Callable, a: float):
    """
    Returns f derivative at a point --> derivative(f, a) = f'(a)
    """
    dx = 1e-13
    return (f(a + dx) - f(a)) / dx


def f1(x):
    return x ** 2 + 3 * x


def f2(x):
    return sqrt(x ** 2) ** 2 + x


def main():
    for a in range(10):
        print(f"f1'({a}) = {derivative(f1, a)}\t\tf2'({a}) = {derivative(f2, a)}")


if __name__ == "__main__":
    main()
