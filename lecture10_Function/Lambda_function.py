# File: python_lambda.py
# Topic: Python Lambda Functions

"""
This script demonstrates the concept and usage of Python lambda functions.
Lambda functions are small, anonymous functions defined with the 'lambda' keyword.

Key characteristics:
-   Anonymous: They don't have a name like regular functions defined with 'def'.
-   Single Expression: They can only have one expression, whose result is implicitly returned.
-   Any Number of Arguments: Can take multiple arguments.

Syntax: lambda arguments : expression
"""


# 1. Basic Lambda Function Syntax
# A lambda function that adds 10 to the argument passed in.
print("\n1. Basic Lambda Function Syntax:")
add_ten = lambda a : a + 10
print(f"  add_ten(5): {add_ten(5)}")     # Expected: 15
print(f"  add_ten(12): {add_ten(12)}")   # Expected: 22

# Lambda function with multiple arguments
multiply_two_numbers = lambda a, b : a * b
print(f"  multiply_two_numbers(4, 5): {multiply_two_numbers(4, 5)}") # Expected: 20

# Lambda function with no arguments (less common but possible)
greet_lambda = lambda : "Hello from lambda!"
print(f"  greet_lambda(): {greet_lambda()}")

# Lambda function that checks a condition
is_even = lambda num : "Even" if num % 2 == 0 else "Odd"
print(f"  is_even(4): {is_even(4)}")     # Expected: Even
print(f"  is_even(7): {is_even(7)}")     # Expected: Odd


# 2. Why Use Lambda Functions? (As Anonymous Functions Inside Another Function)
# The power of lambda is often seen when used as a small, one-time function
# that you don't need to formally define with 'def'.
# A common use case is when a function takes another function as an argument,
# or returns a function.

print("\n2. Using Lambda Functions within another function (function factory):")

def my_multiplier_factory(n):
    """
    This function takes a number 'n' and returns a lambda function.
    The returned lambda function will multiply its input 'a' by 'n'.
    """
    return lambda a : a * n

# Use the factory to create a function that always doubles the number
doubler = my_multiplier_factory(2)
print(f"  Using the 'doubler' function (created with lambda):")
print(f"    doubler(11): {doubler(11)}") # Expected: 22
print(f"    doubler(5): {doubler(5)}")   # Expected: 10

# Use the same factory to create a function that always triples the number
tripler = my_multiplier_factory(3)
print(f"  Using the 'tripler' function (created with lambda):")
print(f"    tripler(11): {tripler(11)}") # Expected: 33
print(f"    tripler(5): {tripler(5)}")   # Expected: 15

# You can create and use both in the same program
quadrupler = my_multiplier_factory(4)
print(f"  Using the 'quadrupler' function (created with lambda):")
print(f"    quadrupler(10): {quadrupler(10)}") # Expected: 40

# Another common use case: with built-in functions like sort(), map(), filter()
print("\n3. Lambda with built-in functions (e.g., sort):")
points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}, {'x': 1, 'y': 2}]
print(f"  Original list of points: {points}")

# Sort the list of dictionaries based on the 'y' value
points.sort(key=lambda p : p['y'])
print(f"  Sorted by 'y' value: {points}") # Expected: [{'x': 4, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 3}]

# Sort the list of dictionaries based on the 'x' value
points.sort(key=lambda p : p['x'])
print(f"  Sorted by 'x' value: {points}") # Expected: [{'x': 1, 'y': 2}, {'x': 2, 'y': 3}, {'x': 4, 'y': 1}]

