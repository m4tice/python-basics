"""
Concept: Control Flow and Conditional Statements
Level: Beginner
"""

# Python has several control flow and conditional statements that are used to control the flow of a program. These include:

# Example 1: if statement
print("Example 1: if statement")
condition_met: bool = True

if condition_met:
    print(". This statement is True")
else:
    print(". This statement is False") # This will never be printed


# Example 2: if-elif-else statement
print("\nExample 2: if-elif-else statement")
number = 1

if 1 == number:
    print(". Number is 1")
elif 2 == number:
    print(". Number is 2")
else:
    print(". Number is not 1 or 2")


# Example 3: nested if statement
print("\nExample 3: nested if statement")
condition_1_is_met: bool = True
condition_2_is_met: bool = False

if condition_1_is_met and condition_2_is_met:
    print(". Both conditions are True")
elif condition_1_is_met or condition_2_is_met:
    print(". At least one condition is True")
else:
    print(". Neither condition is True")
