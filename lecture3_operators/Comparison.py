# File: comparison_operators.py
# Topic: Comparison Operators

"""
This script demonstrates the use of comparison operators in Python.
Comparison operators are used to compare two values and return a boolean result (True or False).
"""


# Define two variables for comparison
x = 10
y = 2

print(f"\nVariables defined: x = {x}, y = {y}")

# == (Equal to)
# Returns True if both operands are equal
print(f"\n{x} == {y} : {x == y} (Is x equal to y?)") # Expected: False
print(f"{x} == 10 : {x == 10} (Is x equal to 10?)") # Expected: True

# != (Not equal to)
# Returns True if both operands are not equal
print(f"\n{x} != {y} : {x != y} (Is x not equal to y?)") # Expected: True
print(f"{x} != 10 : {x != 10} (Is x not equal to 10?)") # Expected: False

# > (Greater than)
# Returns True if the left operand is greater than the right operand
print(f"\n{x} > {y} : {x > y} (Is x greater than y?)") # Expected: True
print(f"{y} > {x} : {y > x} (Is y greater than x?)") # Expected: False

# < (Less than)
# Returns True if the left operand is less than the right operand
print(f"\n{x} < {y} : {x < y} (Is x less than y?)") # Expected: False
print(f"{y} < {x} : {y < x} (Is y less than x?)") # Expected: True

# >= (Greater than or equal to)
# Returns True if the left operand is greater than or equal to the right operand
print(f"\n{x} >= {y} : {x >= y} (Is x greater than or equal to y?)") # Expected: True
print(f"{y} >= 2 : {y >= 2} (Is y greater than or equal to 2?)") # Expected: True

# <= (Less than or equal to)
# Returns True if the left operand is less than or equal to the right operand
print(f"\n{x} <= {y} : {x <= y} (Is x less than or equal to y?)") # Expected: False
print(f"{y} <= 2 : {y <= 2} (Is y less than or equal to 2?)") # Expected: True

print("\n--- End of Comparison Operators Demonstration ---")