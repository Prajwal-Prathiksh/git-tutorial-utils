"""
This module contains tests for the arithmetic module.
"""

import numpy as np
import pytest

from src.arithmetic import add, divide, factorial, multiply, power, subtract


def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_subtract():
    """Test the subtract function."""
    assert subtract(1, 2) == -1
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2


def test_multiply():
    """Test the multiply function."""
    assert multiply(1, 2) == 2
    assert multiply(0, 0) == 0
    assert multiply(-1, 1) == -1


def test_divide():
    """Test the divide function."""
    assert divide(1, 2) == 0.5
    assert divide(0, 1) == 0
    assert divide(-1, 1) == -1


def test_divide_by_zero():
    """Test that divide raises a ZeroDivisionError when appropriate."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power():
    """Test the power function."""
    assert power(2, 3) == 8
    assert power(0, 0) == 1
    assert power(2, 0) == 1
    assert power(0, 2) == 0
    assert np.isclose(power(2, 0.5), np.sqrt(2))
    assert np.isclose(power(2, -1), 0.5)


def test_factorial():
    """Test the factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(0.5)  # type: ignore


if __name__ == "__main__":
    pytest.main()
