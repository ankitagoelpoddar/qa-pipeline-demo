# tests/test_api.py
# Simulated API-style tests
# In a real project these would call actual HTTP endpoints
# Here we test the functions as if they were API responses

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import add, subtract, divide
import pytest

class TestAddEndpoint:

    def test_returns_correct_sum(self):
        response = add(100, 200)
        assert response == 300

    def test_handles_zero(self):
        response = add(0, 0)
        assert response == 0

class TestDivideEndpoint:

    def test_valid_division(self):
        response = divide(50, 5)
        assert response == 10.0

    def test_division_by_zero_returns_error(self):
        with pytest.raises(ValueError) as exc_info:
            divide(9, 0)
        assert "Cannot divide by zero" in str(exc_info.value)