"""
This module contains tests for the arithmetic module.
"""

import pytest

from src.arithmetic import add, divide, multiply, subtract


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


if __name__ == "__main__":
    pytest.main()
