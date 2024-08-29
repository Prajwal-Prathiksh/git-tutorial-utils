"""
This module contains functions for arithmetic operations.

Python 3.6+ is required to run this module, since it uses type hints.
"""

from math import pow


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
    return pow(a, b)


def factorial(n: int) -> int:
    """Calculate the factorial of n."""
    raise NotImplementedError("factorial is not implemented yet")
