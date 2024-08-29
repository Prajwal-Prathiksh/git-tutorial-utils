"""
This module contains functions for geometry related operations.
"""

from math import pi

from .arithmetic import multiply


def rectangle_area(width: int | float, height: int | float) -> float:
    """Calculate the area of a rectangle."""
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return multiply(width, height)


def triangle_area(base: int | float, height: int | float) -> float:
    """Calculate the area of a triangle."""
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return multiply(0.5, multiply(base, height))


def circle_circumference(radius: int | float) -> float:
    """Calculate the circumference of a circle."""
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return multiply(2, multiply(pi, radius))


def circle_area(radius: int | float) -> float:
    """Calculate the area of a circle."""
    raise NotImplementedError(
        "circle_area is not implemented yet. Should be implmented only after src.arithmetic.power is implemented."
    )
