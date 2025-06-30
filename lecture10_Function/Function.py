# File: python_functions.py
# Topic: Python Functions

"""
This script demonstrates the various aspects of defining and using functions in Python.
Functions are reusable blocks of code that perform a specific task.

Key concepts covered:
-   Creating and calling functions.
-   Passing arguments (parameters vs. arguments).
-   Different types of arguments:
    -   Positional arguments (default)
    -   Arbitrary Positional Arguments (*args)
    -   Keyword Arguments
    -   Arbitrary Keyword Arguments (**kwargs)
    -   Default Parameter Values
-   Passing various data types (e.g., lists) as arguments.
-   Returning values from functions.
-   The 'pass' statement for empty function definitions.
-   Advanced argument passing:
    -   Positional-Only Arguments (using /)
    -   Keyword-Only Arguments (using *)
    -   Combining positional-only and keyword-only arguments.
-   Recursion (functions calling themselves).
"""


# 1. Creating and Calling a Function
# In Python, a function is defined using the 'def' keyword.
print("\n1. Creating and Calling a Function:")
def greet():
    """This function prints a simple greeting."""
    print("  Hello from a function!")

# To call a function, use the function name followed by parentheses.
greet() # Calling the function

# 2. Arguments (Parameters vs. Arguments)
# Parameters are variables listed inside the parentheses in the function definition.
# Arguments are the values sent to the function when it is called.
print("\n2. Arguments (Parameters vs. Arguments):")

# Function with one argument (fname - parameter)
def print_full_name(fname): # fname is a parameter
    """This function takes a first name and prints a full name."""
    print(f"  Hello, {fname} Smith!")

print_full_name("John") # "John" is an argument
print_full_name("Alice") # "Alice" is an argument

# Number of Arguments: By default, functions must be called with the correct number of arguments.
def sum_two_numbers(num1, num2): # num1, num2 are parameters
    """This function takes two numbers and prints their sum."""
    print(f"  Sum of {num1} and {num2} is: {num1 + num2}")

sum_two_numbers(10, 20) # Correct number of arguments
# sum_two_numbers(5) # This would raise a TypeError: missing 1 required positional argument

# 3. Arbitrary Arguments, *args
# If you do not know how many arguments will be passed, add a '*' before the parameter name.
# The function will receive a TUPLE of arguments.
print("\n3. Arbitrary Arguments (*args):")
def print_friends(*names): # names will be a tuple of arguments
    """This function prints all friends passed as arguments."""
    print("  My friends are:")
    for name in names:
        print(f"    - {name}")

print_friends("Emily", "David", "Sophia")
print_friends("Michael")
print_friends() # Can be called with no arguments as well

# 4. Keyword Arguments
# You can send arguments with the key = value syntax.
# This way, the order of the arguments does not matter.
print("\n4. Keyword Arguments:")
def describe_car(brand, model, year):
    """This function describes a car using keyword arguments."""
    print(f"  Car details: Brand={brand}, Model={model}, Year={year}")

describe_car(brand="Toyota", model="Corolla", year=2020) # Order does not matter
describe_car(year=2023, brand="Honda", model="Civic") # Different order, same result

# 5. Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments will be passed, add '**' before the parameter name.
# The function will receive a DICTIONARY of arguments.
print("\n5. Arbitrary Keyword Arguments (**kwargs):")
def print_person_info(**info): # info will be a dictionary
    """This function prints arbitrary person information."""
    print("  Person Info:")
    for key, value in info.items():
        print(f"    {key.capitalize()}: {value}")

print_person_info(name="Charlie", age=40, occupation="Engineer")
print_person_info(city="Paris", country="France")

# 6. Default Parameter Value
# If we call the function without an argument for a parameter with a default value, it uses the default.
print("\n6. Default Parameter Value:")
def describe_country(country="Norway"): # "Norway" is the default value
    """This function describes a country, with Norway as default."""
    print(f"  I am from {country}.")

describe_country("Sweden") # Passed argument overrides default
describe_country() # Uses default value ("Norway")

# 7. Passing a List as an Argument
# Any data type can be passed as an argument. It retains its type inside the function.
print("\n7. Passing a List as an Argument:")
def print_fruits(fruit_list):
    """This function iterates and prints items from a list."""
    print("  My favorite fruits:")
    for fruit in fruit_list:
        print(f"    - {fruit}")

my_favorite_fruits = ["apple", "mango", "pineapple"]
print_fruits(my_favorite_fruits)

# 8. Return Values
# To let a function return a value, use the 'return' statement.
print("\n8. Return Values:")
def multiply(a, b):
    """This function multiplies two numbers and returns the result."""
    return a * b

result = multiply(5, 4)
print(f"  Result of multiply(5, 4): {result}") # Expected: 20

def get_full_name(first, last):
    """Returns a formatted full name."""
    return f"{first} {last}"

full_name = get_full_name("Jane", "Doe")
print(f"  Full name: {full_name}")

# 9. The pass Statement in Functions
# Function definitions cannot be empty. Use 'pass' if there's no content.
print("\n9. The 'pass' Statement in Functions:")
def empty_function():
    pass # This does nothing, but makes the function syntactically valid.
print("  'empty_function' was defined with 'pass' and can be called without error.")
empty_function()


# 10. Positional-Only Arguments (Python 3.8+)
# Arguments before '/' can ONLY be passed by position.
print("\n10. Positional-Only Arguments (using /):")
def create_user(username, password, /, email): # username, password are positional-only
    """Creates a user. Username and password must be positional, email can be positional or keyword."""
    print(f"  User created: Username={username}, Password={password}, Email={email}")

create_user("user123", "passABC", "user@example.com") # All positional
create_user("user456", "passDEF", email="another@example.com") # Positional for first two, keyword for email
# create_user(username="user789", password="passGHI", email="test@example.com")
# The above line would raise a TypeError because username and password are positional-only.
print("  (Attempting to call 'create_user' with 'username=' or 'password=' would cause a TypeError.)")

# 11. Keyword-Only Arguments (Python 3.0+)
# Arguments after '*' can ONLY be passed by keyword.
print("\n11. Keyword-Only Arguments (using *):")
def send_message(subject, *, body, recipient): # body, recipient are keyword-only
    """Sends a message. Subject can be positional/keyword, body and recipient must be keyword."""
    print(f"  Sending message: Subject='{subject}', Body='{body}', Recipient='{recipient}'")

send_message("Greetings", body="Hello there!", recipient="info@example.com")
send_message(subject="Meeting Agenda", recipient="team@company.com", body="Please review.")
# send_message("Reminder", "Don't forget!", "test@email.com")
# The above line would raise a TypeError because body and recipient are keyword-only.
print("  (Attempting to call 'send_message' with 'body' or 'recipient' as positional would cause a TypeError.)")

# 12. Combine Positional-Only and Keyword-Only
# Any argument BEFORE '/' are positional-only. Any argument AFTER '*' are keyword-only.
print("\n12. Combining Positional-Only and Keyword-Only Arguments:")
def configure_settings(param1, /, param2, *, param3, param4):
    """
    param1: positional-only
    param2: positional or keyword
    param3, param4: keyword-only
    """
    print(f"  Configured: param1={param1}, param2={param2}, param3={param3}, param4={param4}")

configure_settings(10, 20, param3=30, param4=40) # All valid
configure_settings(10, param2=20, param3=30, param4=40) # Mixed valid
# configure_settings(param1=10, param2=20, param3=30, param4=40) # TypeError: param1 is positional-only
# configure_settings(10, 20, 30, 40) # TypeError: param3, param4 are keyword-only
print("  (See comments in code for examples of invalid calls.)")

# 13. Recursion
# A function calling itself. Requires a base case to terminate.
print("\n13. Recursion: (Function calling itself)")
def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.
    Factorial of n (n!) = n * (n-1) * ... * 1
    Base case: factorial(0) = 1
    """
    if n == 0:
        return 1 # Base case: stops the recursion
    else:
        print(f"    Calculating {n} * factorial({n-1})") # For demonstration
        return n * factorial(n-1) # Recursive call

print("  Calculating factorial(4):")
fact_result = factorial(4)
print(f"  Factorial of 4 is: {fact_result}") # Expected: 24 (4*3*2*1)

# Example of a simpler recursion (summing numbers down to 0)
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(f"    Recursion step (k={k}): Result = {result}")
    else:
        result = 0
    return result

print("\n  Calculating sum using tri_recursion(6):")
sum_result = tri_recursion(6)
print(f"  Result of tri_recursion(6): {sum_result}") # Expected: 21 (6+5+4+3+2+1+0)
