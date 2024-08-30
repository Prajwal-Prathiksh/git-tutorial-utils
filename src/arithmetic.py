"""
This module contains functions for arithmetic operations.

Python 3.6+ is required to run this module, since it uses type hints.
"""


def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers."""
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract two numbers."""
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers."""
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Divide two numbers."""
    return a / b


def power(a: int | float, b: int | float) -> int | float:
    """Raise a to the power of b."""
    return a**b


def factorial(n: int) -> int:
    """Calculate the factorial of n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if isinstance(n, float):
        raise ValueError("n must be an integer")
    return 1 if n == 0 else n * factorial(n - 1)
