"""
author: @guu8hc
CLI demonstration
"""
#pylint: disable=wrong-import-position
#pylint: disable=line-too-long

import os
import sys

# Add the root directory of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import argparse
from concepts.functions import add_numbers_basic, subtract_numbers_basic

def cli_app():
    """
    cli function
    """
    parser = argparse.ArgumentParser(description='Basic calculator')
    parser.add_argument('operation', type=str, help='Operation: add or subtract')
    parser.add_argument('operands', nargs='+', type=int, help='First number')
    args = parser.parse_args()

    result = None
    if args.operation == 'add':
        result = add_numbers_basic(*args.operands)
    elif args.operation == 'subtract':
        result = subtract_numbers_basic(*args.operands)
    else:
        result = "Invalid operation"

    print('Result:', result)

if __name__ == '__main__':
    cli_app()
