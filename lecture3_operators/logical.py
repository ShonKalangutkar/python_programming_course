# File: logical_operators.py
# Topic: Logical Operators

"""
This script demonstrates the use of logical operators (and, or, not) in Python.
Logical operators are used to combine conditional statements, returning a boolean result.
"""


# Define variables for conditional statements
x = 7
y = 15
z = 3

print(f"\nVariables defined: x = {x}, y = {y}, z = {z}")

# --- 'and' operator ---
# Returns True if both statements are True.
print("\n--- 'and' operator ---")

# Example 1: Both conditions are True
condition1_and_true = (x < 10) and (y > 10)
print(f"({x} < 10) and ({y} > 10): {condition1_and_true}") # Expected: True (True and True)

# Example 2: One condition is False
condition2_and_false = (x < 5) and (y > 10)
print(f"({x} < 5) and ({y} > 10): {condition2_and_false}") # Expected: False (False and True)

# Example 3: Both conditions are False
condition3_and_false = (x > 10) and (y < 5)
print(f"({x} > 10) and ({y} < 5): {condition3_and_false}") # Expected: False (False and False)

# --- 'or' operator ---
# Returns True if at least one of the statements is True.
print("\n--- 'or' operator ---")

# Example 1: Both conditions are True
condition1_or_true = (x < 10) or (y > 10)
print(f"({x} < 10) or ({y} > 10): {condition1_or_true}") # Expected: True (True or True)

# Example 2: One condition is True
condition2_or_true = (x < 5) or (y > 10)
print(f"({x} < 5) or ({y} > 10): {condition2_or_true}") # Expected: True (False or True)

# Example 3: Both conditions are False
condition3_or_false = (x > 10) or (y < 5)
print(f"({x} > 10) or ({y} < 5): {condition3_or_false}") # Expected: False (False or False)

# --- 'not' operator ---
# Reverses the result; returns False if the result is True, and True if the result is False.
print("\n--- 'not' operator ---")

# Example 1: Original condition is True
original_condition_true = (x < 10)
print(f"Original condition: ({x} < 10) is {original_condition_true}") # Expected: True
print(f"not ({x} < 10): {not original_condition_true}") # Expected: False

# Example 2: Original condition is False
original_condition_false = (x > 10)
print(f"Original condition: ({x} > 10) is {original_condition_false}") # Expected: False
print(f"not ({x} > 10): {not original_condition_false}") # Expected: True

# Example 3: Combining with 'and'
combined_and = (x < 5 and y < 10) # False and False -> False
print(f"({x} < 5 and {y} < 10) is {combined_and}") # Expected: False
print(f"not ({x} < 5 and {y} < 10): {not combined_and}") # Expected: True

# Example 4: Combining with 'or'
combined_or = (x > 5 or z > 10) # True or False -> True
print(f"({x} > 5 or {z} > 10) is {combined_or}") # Expected: True
print(f"not ({x} > 5 or {z} > 10): {not combined_or}") # Expected: False
