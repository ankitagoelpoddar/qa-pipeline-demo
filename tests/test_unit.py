# tests/test_unit.py
# Unit tests for our calculator

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import add, subtract, divide
import pytest

def test_add_two_positive_numbers():
    result = add(5, 3)
    assert result == 8                  # ✅ should pass

def test_subtract_gives_correct_result():
    result = subtract(10, 4)
    assert result == 6                  # ✅ should pass

def test_divide_normal():
    result = divide(10, 2)
    assert result == 5.0                # ✅ should pass

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):     # ✅ expects an error — should pass
        divide(10, 0)

def test_add_negative_numbers():
    result = add(-3, -7)
    assert result == -10                # ✅ should pass
