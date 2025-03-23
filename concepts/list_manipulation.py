"""
author: @guu8hc
purpose: list manipulation functions
"""
# Python has several built-in functions
# that can be used to perform specific tasks. These include:
list_any = any([True, False, True]) # Returns True if any element in the list is True
print(". List Any:", list_any)

list_all = all([True, False, True]) # Returns True if all elements in the list are True
print(". List All:", list_all)

list_enumerate = enumerate(["apple", "banana", "cherry"]) # Returns an enumerate object
print(". List Enumerate:", list(list_enumerate))
