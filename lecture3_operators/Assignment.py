# File: assignment_operators.py
# Topic: Assignment Operators

"""
This script demonstrates the use of various assignment operators in Python.
Assignment operators are used to assign values to variables.
They often combine an arithmetic or bitwise operation with an assignment.
"""


# = (Simple Assignment)
# Assigns the value on the right to the variable on the left.
x = 5
print(f"\nInitial assignment: x = 5 -> x is {x}") # Expected: x is 5

# += (Add and Assign)
# Adds the right operand to the left operand and assigns the result to the left operand.
# Equivalent to: x = x + 3
x += 3
print(f"After x += 3: x is {x}") # Expected: x is 8 (5 + 3)

# -= (Subtract and Assign)
# Subtracts the right operand from the left operand and assigns the result to the left operand.
# Equivalent to: x = x - 3
x -= 3
print(f"After x -= 3: x is {x}") # Expected: x is 5 (8 - 3)

# *= (Multiply and Assign)
# Multiplies the right operand with the left operand and assigns the result to the left operand.
# Equivalent to: x = x * 3
x *= 3
print(f"After x *= 3: x is {x}") # Expected: x is 15 (5 * 3)

# /= (Divide and Assign)
# Divides the left operand by the right operand and assigns the float result to the left operand.
# Equivalent to: x = x / 3
x /= 3
print(f"After x /= 3: x is {x}") # Expected: x is 5.0 (15 / 3)

# %= (Modulus and Assign)
# Divides the left operand by the right operand and assigns the remainder to the left operand.
# Equivalent to: x = x % 3
x %= 3
print(f"After x %= 3: x is {x}") # Expected: x is 2.0 (5.0 % 3 = 2.0)

# //= (Floor Divide and Assign)
# Divides the left operand by the right operand and assigns the integer part of the quotient to the left operand.
# Equivalent to: x = x // 3
x //= 3
print(f"After x //= 3: x is {x}") # Expected: x is 0.0 (2.0 // 3 = 0.0)

# **= (Exponentiate and Assign)
# Raises the left operand to the power of the right operand and assigns the result to the left operand.
# Equivalent to: x = x ** 3
x = 2 # Reset x to a meaningful integer for exponentiation
print(f"\nReset x to {x} for **=")
x **= 3
print(f"After x **= 3: x is {x}") # Expected: x is 8 (2 ** 3)

# Bitwise Assignment Operators (operate on binary representations)
print("\n--- Demonstrating Bitwise Assignment Operators ---")
a = 10  # Binary: 1010
b = 3   # Binary: 0011
print(f"Initial values for bitwise operations: a = {a} (binary: {bin(a)}), b = {b} (binary: {bin(b)})")

# &= (Bitwise AND and Assign)
# Performs a bitwise AND operation on the operands and assigns the result.
# Equivalent to: a = a & b
# 1010 & 0011 = 0010 (Decimal 2)
a &= b
print(f"After a &= b")