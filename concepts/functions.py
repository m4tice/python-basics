"""
Concept: Functions / Function Annotations and Type Hints
Level: Beginner
"""

# Python also allows you to define your own functions using the 'def' keyword.
# You can also specify the data types of the input parameters
# and return value using function annotations and type hints.

def add_numbers_basic(a, b):
    """
    this is a function docstring
    """
    return a + b

def add_numbers_pro(a: int, b: int) -> int:
    """
    This is a function docstring following reST style.

    :param a: this is a first param: int
    :param b: this is a second param: int
    :returns: this is a description of what is returned: int
    :raises keyError: raises an exception (optional)
    """
    return a + b

def subtract_numbers_basic(a: int, b: int) -> int:
    """
    This is a function docstring following reST style.

    :param a: this is a first param: int
    :param b: this is a second param: int
    :returns: this is a description of what is returned: int
    :raises keyError: raises an exception (optional)
    """
    return a - b
