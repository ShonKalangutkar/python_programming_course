# File: membership_operators.py
# Topic: Membership Operators

"""
This script demonstrates the use of membership operators ('in' and 'not in') in Python.
Membership operators are used to test if a sequence (like a substring or an item)
is present within an object (like a string, list, tuple, set, or dictionary keys).
"""


# --- Example 1: 'in' operator with a string ---
my_string = "Hello, Python World!"
print(f"\nString: '{my_string}'")

print(f"'Python' in my_string: {'Python' in my_string}") # Expected: True
print(f"'Java' in my_string: {'Java' in my_string}")     # Expected: False
print(f"'World' in my_string: {'World' in my_string}")   # Expected: True (case-sensitive)
print(f"'world' in my_string: {'world' in my_string}")   # Expected: False (case-sensitive)

# --- Example 2: 'in' operator with a list ---
my_list = ['apple', 'banana', 'cherry', 'date']
print(f"\nList: {my_list}")

print(f"'banana' in my_list: {'banana' in my_list}") # Expected: True
print(f"'grape' in my_list: {'grape' in my_list}")   # Expected: False
print(f"'cherry' in my_list: {'cherry' in my_list}") # Expected: True

# --- Example 3: 'in' operator with a tuple ---
my_tuple = (10, 20, 30, 40, 50)
print(f"\nTuple: {my_tuple}")

print(f"30 in my_tuple: {30 in my_tuple}") # Expected: True
print(f"60 in my_tuple: {60 in my_tuple}") # Expected: False

# --- Example 4: 'in' operator with a set ---
my_set = {'red', 'green', 'blue'}
print(f"\nSet: {my_set}")

print(f"'green' in my_set: {'green' in my_set}") # Expected: True
print(f"'yellow' in my_set: {'yellow' in my_set}") # Expected: False

# --- Example 5: 'in' operator with a dictionary (checks keys by default) ---
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"\nDictionary: {my_dict}")

print(f"'name' in my_dict: {'name' in my_dict}")         # Expected: True (checks for key)
print(f"'Alice' in my_dict: {'Alice' in my_dict}")       # Expected: False (does NOT check for value by default)
print(f"'Alice' in my_dict.values(): {'Alice' in my_dict.values()}") # Expected: True (explicitly check values)
print(f"('name', 'Alice') in my_dict.items(): {('name', 'Alice') in my_dict.items()}") # Expected: True (checks key-value pair)

# --- Example 6: 'not in' operator ---
# Returns True if a sequence with the specified value is NOT present in the object.
print(f"\n--- Demonstrating 'not in' operator ---")

print(f"'xyz' not in my_string: {'xyz' not in my_string}") # Expected: True
print(f"'Python' not in my_string: {'Python' not in my_string}") # Expected: False

print(f"'grape' not in my_list: {'grape' not in my_list}") # Expected: True
print(f"'banana' not in my_list: {'banana' not in my_list}") # Expected: False
