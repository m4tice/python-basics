"""
Library: numpy
"""

import numpy as np

# Create a numpy array
my_list = np.arange(1, 6)
print(". List:", my_list)

# Create a numpy array with a specific data type
my_list = np.arange(1, 6, dtype=float)
print(". List with float data type:", my_list)

# Create a numpy array with a specific shape
my_list = np.arange(0, 6).reshape(2, 3)
print(". List with shape (2, 3):", my_list)

# Create a random number
random_number = np.random.randint(1, 10)
print(". Random Number:", random_number)

# Create a random number with a specific shape
random_number = np.random.randint(1, 10, size=(2, 3))
print(". Random Number with shape (2, 3):", random_number)
