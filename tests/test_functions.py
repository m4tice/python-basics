"""
author: @guu8hc
purpose: test functions in the package
"""

from concepts.functions import add_numbers_basic, add_numbers_pro

def test_add_numbers_basic():
    """
    assert that add_numbers_basic returns the correct sum
    """
    assert add_numbers_basic(1, 2) == 3

def test_add_numbers_pro():
    """
    assert that add_numbers_pro returns the correct sum
    """
    assert add_numbers_pro(1, 2) == 3
