"""Tests for main module"""

import pytest

from src.main import add, greet


class TestGreet:
    """Test cases for greet function"""

    def test_greet_with_name(self):
        """Test greet returns correct message"""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_with_empty_string(self):
        """Test greet with empty string"""
        assert greet("") == "Hello, !"


class TestAdd:
    """Test cases for add function"""

    def test_add_positive_numbers(self):
        """Test add with positive numbers"""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Test add with negative numbers"""
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        """Test add with mixed positive and negative"""
        assert add(5, -3) == 2

    def test_add_zeros(self):
        """Test add with zeros"""
        assert add(0, 0) == 0
