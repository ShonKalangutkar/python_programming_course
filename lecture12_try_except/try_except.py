# File: python_error_handling.py
# Topic: Python Error Handling (Try...Except...Else...Finally, Raise)

"""
This script demonstrates Python's mechanisms for handling errors,
also known as exceptions. It covers the use of try, except, else,
finally blocks, and how to explicitly raise exceptions.

Key concepts covered:
-   The 'try' block: For code that might raise an error.
-   The 'except' block: For handling specific or general errors.
-   The 'else' block: For code to execute if no errors occur in 'try'.
-   The 'finally' block: For code that must always execute, regardless of errors.
-   Handling multiple specific exception types.
-   Raising custom exceptions using the 'raise' keyword.
"""


# --- 1. Basic Try...Except Block ---
# The 'try' block lets you test a block of code for errors.
# The 'except' block lets you handle the error.
print("\n1. Basic Try...Except Block:")

print("  Attempting to access an undefined variable:")
try:
    print(undefined_variable) # This line will cause a NameError
except:
    print("    An error occurred (generic except block caught it).")

print("  --- What happens WITHOUT a try block (program crashes): ---")
# Uncomment the following lines to see the program crash:
# print(f"  Before intentional crash.")
# print(1 / 0) # This will cause a ZeroDivisionError and crash the script
# print(f"  After intentional crash (this won't print).")
# print("  (Re-run with the above lines commented out to continue this script).")

# --- 2. Many Exceptions (Handling Specific Errors) ---
# You can define as many exception blocks as you want for special kinds of errors.
print("\n2. Handling Specific Exceptions:")

print("  Attempting division by zero and invalid type operation:")
try:
    result = 10 / 0 # ZeroDivisionError
    # result = "hello" + 5 # TypeError (if previous line didn't error)
    print(f"    Calculation result: {result}")
except ZeroDivisionError:
    print("    Caught a ZeroDivisionError: You cannot divide by zero!")
except TypeError:
    print("    Caught a TypeError: Operation with incompatible types!")
except Exception as e: # Generic catch-all for any other unexpected errors
    print(f"    Caught an unexpected error: {e}")

print("  Attempting to access a non-existent key in a dictionary:")
my_dict = {"name": "Alice"}
try:
    value = my_dict["age"] # KeyError
    print(f"    Value: {value}")
except KeyError:
    print("    Caught a KeyError: The dictionary key does not exist!")
except:
    print("    Caught an unknown error.")

# --- 3. The else Block ---
# The 'else' block is executed if no errors were raised in the 'try' block.
print("\n3. The 'else' Block:")

print("  Scenario A: No error in try block:")
try:
    num1 = 10
    num2 = 5
    division_result = num1 / num2
except ZeroDivisionError:
    print("    Error: Division by zero!")
else: # This block executes
    print(f"    No error occurred. Division result: {division_result}") # Expected: 2.0

print("  Scenario B: Error in try block (else will not execute):")
try:
    num1 = 10
    num2 = 0
    division_result = num1 / num2 # This will cause ZeroDivisionError
except ZeroDivisionError:
    print("    Error: Division by zero! (Else block will be skipped)")
else: # This block will NOT execute
    print(f"    This message will not print.")


# --- 4. The finally Block ---
# The 'finally' block, if specified, will be executed regardless of whether
# the 'try' block raises an error or not. It's often used for cleanup operations.
print("\n4. The 'finally' Block:")

print("  Scenario A: 'finally' with no error:")
try:
    print("    Inside try block (no error).")
except:
    print("    Inside except block (error caught).")
finally: # This always executes
    print("    Inside finally block (always runs).")

print("  Scenario B: 'finally' with an error:")
try:
    print("    Inside try block (about to raise error).")
    value = 1 / 0 # ZeroDivisionError
except ZeroDivisionError:
    print("    Inside except block (ZeroDivisionError caught).")
finally: # This always executes
    print("    Inside finally block (always runs, even after error).")


# --- 5. Raise an Exception ---
# As a Python developer, you can choose to throw (raise) an exception
# if a specific condition occurs.
print("\n5. Raising Exceptions with 'raise':")

def validate_age(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number (integer or float).")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age seems unusually high (max 150).")
    print(f"  Age {age} is valid.")

# Valid age
try:
    validate_age(30)
except (TypeError, ValueError) as e:
    print(f"  Error validating age: {e}")

# Invalid age (negative)
try:
    validate_age(-5)
except (TypeError, ValueError) as e:
    print(f"  Error validating age: {e}") # Expected: Age cannot be negative.

# Invalid age (too high)
try:
    validate_age(200)
except (TypeError, ValueError) as e:
    print(f"  Error validating age: {e}") # Expected: Age seems unusually high.

# Invalid age (wrong type)
try:
    validate_age("twenty")
except (TypeError, ValueError) as e:
    print(f"  Error validating age: {e}") # Expected: Age must be a number.

