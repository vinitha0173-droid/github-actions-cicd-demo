"""Unit tests for the application."""

from app import add_numbers


def test_add_positive_numbers():
    """Test addition of positive numbers."""
    assert add_numbers(2, 3) == 5


def test_add_zero():
    """Test addition with zero."""
    assert add_numbers(5, 0) == 5


def test_add_negative_numbers():
    """Test addition of negative numbers."""
    assert add_numbers(-2, -3) == -5
