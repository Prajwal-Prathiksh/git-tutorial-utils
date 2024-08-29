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


def multiply_or_power(
    a: int | float, b: int | float, power: bool = False
) -> int | float:
    """Multiply two numbers or raise a to the power of b."""
    if power:
        return a**b
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Divide two numbers."""
    return a / b


def factorial(n: int) -> int:
    """Calculate the factorial of n."""
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        return n * factorial(n - 1)
