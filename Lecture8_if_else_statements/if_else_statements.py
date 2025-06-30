# File: python_conditions.py
# Topic: Python Conditions and If Statements

"""
This script demonstrates Python's conditional statements (if, elif, else)
and related logical operators and control flow structures.

Key concepts covered:
-   Comparison Operators: ==, !=, <, <=, >, >=
-   Basic 'if' statement
-   Indentation for defining scope
-   'elif' keyword (else if)
-   'else' keyword (catch-all)
-   Short Hand If and Short Hand If...Else (Ternary Operators)
-   Logical Operators: 'and', 'or', 'not'
-   Nested If statements
-   The 'pass' statement for empty blocks
"""

print("--- Demonstrating Python Conditions and If Statements ---")

# --- Variables for examples ---
a = 50
b = 10
c = 50
d = 75
e = 25

print(f"\nVariables for examples: a={a}, b={b}, c={c}, d={d}, e={e}")

# 1. Comparison Operators and Basic If Statement
print("\n1. Basic 'if' statement with comparison operators:")
# Equals: a == b
if a == b:
    print(f"  a ({a}) is equal to b ({b})")

# Not Equals: a != b
if a != b:
    print(f"  a ({a}) is NOT equal to b ({b})")

# Less than: a < b
if a < b:
    print(f"  a ({a}) is less than b ({b})")

# Less than or equal to: a <= b
if a <= c: # a is equal to c
    print(f"  a ({a}) is less than or equal to c ({c})")

# Greater than: a > b
if a > b:
    print(f"  a ({a}) is greater than b ({b})")

# Greater than or equal to: a >= b
if a >= c: # a is equal to c
    print(f"  a ({a}) is greater than or equal to c ({c})")


# 2. Indentation
print("\n2. Indentation (defines scope):")
if a > b:
    print("  This line is inside the 'if' block.")
    print("  So is this one. Proper indentation is crucial.")
    if b < a: # Nested if, also needs indentation
        print("    This is a nested statement, indented further.")
print("  This line is outside the 'if' block, so it always executes.")


# 3. elif (Else If)
print("\n3. elif (Else If):")
if a > d: # 50 > 75 is False
    print(f"  a ({a}) is greater than d ({d})")
elif a == c: # 50 == 50 is True
    print(f"  a ({a}) and c ({c}) are equal.") # This will execute
elif a < b: # This condition will not be checked because the above elif was true
    print(f"  a ({a}) is less than b ({b})")
else:
    print("  No conditions above were true.")


# 4. else (Catch-all)
print("\n4. else (Catch-all):")
x_val = 100
y_val = 50
print(f"  Testing with x_val={x_val}, y_val={y_val}")
if x_val < y_val:
    print("  x_val is less than y_val")
elif x_val == y_val:
    print("  x_val is equal to y_val")
else: # This will execute
    print("  x_val is greater than y_val (caught by else).")

print("\n  Else without elif:")
x_val = 10
y_val = 20
print(f"  Testing with x_val={x_val}, y_val={y_val}")
if x_val > y_val:
    print("  x_val is greater than y_val")
else: # This will execute
    print("  x_val is not greater than y_val (caught by else).")


# 5. Short Hand If
print("\n5. Short Hand If (single statement):")
if a > b: print(f"  Short hand: a ({a}) is greater than b ({b})")


# 6. Short Hand If ... Else (Ternary Operators / Conditional Expressions)
print("\n6. Short Hand If ... Else (Ternary Operator):")
print_result = "a is greater" if a > b else "b is greater or equal"
print(f"  Result using ternary operator: {print_result}")

print_result_equal = "a and c are equal" if a == c else "a and c are NOT equal"
print(f"  Result for equality using ternary: {print_result_equal}")

# Multiple else statements on the same line (chaining ternary operators)
print_multi_condition = "A" if a > d else "B" if a == c else "C"
print(f"  Result chaining ternary operators: {print_multi_condition}")
# (a > d is False, a == c is True, so "B" is printed)


# 7. Logical Operators: and, or, not
print("\n7. Logical Operators:")
# and: Both conditions must be True
print("  --- 'and' operator ---")
if a > b and d > c: # (50 > 10 is True) AND (75 > 50 is True) -> True
    print(f"  Both 'a > b' ({a > b}) AND 'd > c' ({d > c}) are True.")

if a > d and d > c: # (50 > 75 is False) AND (75 > 50 is True) -> False
    print(f"  This line will NOT print (one condition is False).")

# or: At least one condition must be True