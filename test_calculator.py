"""
Unit tests for the calculator functions.
"""

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """Test cases for the addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    """Test cases for the subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    """Test cases for the multiplication function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6

def test_divide():
    """Test cases for the division function, including zero-division handling."""
    assert divide(6, 2) == 3
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):  # Expecting an error for division by zero
        divide(5, 0)

