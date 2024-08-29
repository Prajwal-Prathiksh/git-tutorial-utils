"""
This module contains tests for the geometry module.
"""

from math import pi

import numpy as np
import pytest

from src.geometry import circle_circumference, rectangle_area, triangle_area


def test_rectangle_area():
    """Test the rectangle_area function."""
    assert rectangle_area(1, 2) == 2
    assert rectangle_area(0, 100) == 0
    with pytest.raises(ValueError):
        rectangle_area(-1, 1)


def test_triangle_area():
    """Test the triangle_area function."""
    assert triangle_area(1, 2) == 1
    assert triangle_area(0, 100) == 0
    with pytest.raises(ValueError):
        triangle_area(-1, 1)


def test_circle_circumference():
    """Test the circle_circumference function."""
    assert np.isclose(circle_circumference(1), 2 * pi)
    assert np.isclose(circle_circumference(0), 0)
    with pytest.raises(ValueError):
        circle_circumference(-1)


if __name__ == "__main__":
    pytest.main()
