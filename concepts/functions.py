"""
Concept: Functions / Function Annotations and Type Hints
Level: Beginner
"""

# Python has several built-in functions that can be used to perform specific tasks. These include:
list_any = any([True, False, True]) # Returns True if any element in the list is True
print(". List Any:", list_any)

list_all = all([True, False, True]) # Returns True if all elements in the list are True
print(". List All:", list_all)

list_enumerate = enumerate(["apple", "banana", "cherry"]) # Returns an enumerate object
print(". List Enumerate:", list(list_enumerate))

# Python also allows you to define your own functions using the 'def' keyword.
# You can also specify the data types of the input parameters and return value using function annotations and type hints.
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

print(". Add Numbers Basic:", add_numbers_basic(1, 2))
print(". Add Numbers Pro  :", add_numbers_pro(1, 2))
