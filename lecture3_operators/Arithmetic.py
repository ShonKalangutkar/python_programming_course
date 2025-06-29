# File: arithmetic_operators.py
# Topic: Arithmetic Operators

"""
This script demonstrates the use of common arithmetic operators in Python.
Arithmetic operators are used with numeric values to perform mathematical operations.
"""


# Define two numeric variables
x = 20
y = 10

print(f"\nVariables defined: x = {x}, y = {y}")

# Addition (+)
# Adds values on either side of the operator.
result_add = x + y
print(f"\nAddition (x + y): {x} + {y} = {result_add}") # Expected: 30

# Subtraction (-)
# Subtracts right hand operand from left hand operand.
result_sub = x - y
print(f"Subtraction (x - y): {x} - {y} = {result_sub}") # Expected: 10

# Multiplication (*)
# Multiplies values on either side of the operator.
result_mul = x * y
print(f"Multiplication (x * y): {x} * {y} = {result_mul}") # Expected: 200

# Division (/)
# Divides left hand operand by right hand operand. Always returns a float.
result_div = x / y
print(f"Division (x / y): {x} / {y} = {result_div}") # Expected: 2.0

# Modulus (%)
# Divides left hand operand by right hand operand and returns the remainder.
result_mod = x % y
print(f"Modulus (x % y): {x} % {y} = {result_mod}") # Expected: 0 (20 divided by 10 has no remainder)

# Exponentiation (**)
# Performs exponential (power) calculation on operators.
result_exp = x ** 2 # x raised to the power of 2
print(f"Exponentiation (x ** 2): {x} ** 2 = {result_exp}") # Expected: 400 (20 * 20)
result_exp_xy = x ** y # x raised to the power of y (20^10)
print(f"Exponentiation (x ** y): {x} ** {y} = {result_exp_xy}") # Expected: 10240000000000

# Floor Division (//)
# Divides left hand operand by right hand operand and returns the integer part of the quotient.
# It truncates the decimal part.
result_floor_div = x // y
print(f"Floor Division (x // y): {x} // {y} = {result_floor_div}") # Expected: 2

# Example with non-even division for clarity of //
a = 21
b = 10
print(f"\nAnother example for Floor Division with {a} and {b}:")
print(f"Division ({a} / {b}): {a / b}")     # Expected: 2.1
print(f"Floor Division ({a} // {b}): {a // b}") # Expected: 2
