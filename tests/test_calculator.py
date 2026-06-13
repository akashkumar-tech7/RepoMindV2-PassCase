"""Tests for the calculator module."""
import pytest

from src.calculator import add, divide, is_even, multiply, subtract


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_basic(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(1, 5) == -4


class TestMultiply:
    def test_positive(self):
        assert multiply(4, 5) == 20

    def test_by_zero(self):
        assert multiply(99, 0) == 0


class TestDivide:
    def test_basic(self):
        assert divide(10, 2) == 5.0

    def test_division_by_zero_raises(self):
        with pytest.raises(ValueError, match="divide by zero"):
            divide(1, 0)


class TestIsEven:
    @pytest.mark.parametrize("n,expected", [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-5, False),
    ])
    def test_is_even(self, n, expected):
        assert is_even(n) == expected
