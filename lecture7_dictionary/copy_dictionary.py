# File: copy_dictionary.py
# Topic: Copying Dictionaries

"""
This script demonstrates how to correctly copy a Python dictionary.
It explains why simple assignment creates a reference, not a copy,
and shows two common methods for making a shallow copy:
the copy() method and the dict() constructor.
"""


original_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "features": ["V8 Engine", "Manual Transmission"] # Example of a mutable value
}
print(f"\nOriginal dictionary 'original_dict': {original_dict}")

# 1. Incorrect Copying: Reference Assignment
# Simply typing new_dict = original_dict creates a reference, not a copy.
# Both variables will point to the SAME dictionary object in memory.
print("\n1. Incorrect Copying: Reference Assignment (dict2 = dict1)")
reference_dict = original_dict
print(f"  Reference dictionary 'reference_dict': {reference_dict}")
print(f"  Do they refer to the same object? (original_dict is reference_dict): {original_dict is reference_dict}") # Expected: True

# Now, modify the original_dict and observe reference_dict
original_dict["year"] = 1965
original_dict["features"].append("Leather Seats") # Modify the mutable list inside
print(f"  After modifying original_dict['year'] and 'features':")
print(f"    Original dictionary: {original_dict}")
print(f"    Reference dictionary: {reference_dict}")
# Expected: Both will show the changes because they are the same dictionary.

# 2. Correct Copying: Using the copy() method (Shallow Copy)
# The copy() method returns a new dictionary with the same key-value pairs.
# This is a "shallow" copy.
print("\n2. Correct Copying: Using the copy() method (Shallow Copy)")
copied_dict_method = original_dict.copy()
print(f"  Copied dictionary (via .copy()): {copied_dict_method}")
print(f"  Do they refer to the same object? (original_dict is copied_dict_method): {original_dict is copied_dict_method}") # Expected: False

# Now, modify the original_dict and observe copied_dict_method
original_dict["color"] = "red"
original_dict["features"].append("Power Steering") # This modifies the *same* list object
print(f"  After further modifying original_dict:")
print(f"    Original dictionary: {original_dict}")
print(f"    Copied dictionary (via .copy()): {copied_dict_method}")
# Expected: 'color' change only in original. 'features' list change in *both* because it's a shallow copy.
print("  Note: For shallow copies, mutable values (like lists) within the dictionary are still references.")
print("  If you modify the mutable object itself (e.g., append to a list), the change will reflect in both copies.")

# 3. Correct Copying: Using the dict() constructor (Shallow Copy)
# You can also make a copy by using the built-in dict() constructor.
# This also performs a "shallow" copy.
print("\n3. Correct Copying: Using the dict() constructor (Shallow Copy)")
copied_dict_constructor = dict(original_dict)
print(f"  Copied dictionary (via dict()): {copied_dict_constructor}")
print(f"  Do they refer to the same object? (original_dict is copied_dict_constructor): {original_dict is copied_dict_constructor}") # Expected: False

# Demonstrate modifications again
original_dict["brand"] = "Tesla"
original_dict["features"].append("Automatic Braking") # Modifies the list reference
print(f"  After further modifying original_dict:")
print(f"    Original dictionary: {original_dict}")
print(f"    Copied dictionary (via dict()): {copied_dict_constructor}")
# Expected: 'brand' change only in original. 'features' list change in *both*.

# If you need a deep copy (where nested mutable objects are also copied, not just referenced)
# you would use the 'deepcopy' function from the 'copy' module.
# import copy
# deep_copied_dict = copy.deepcopy(original_dict)
print("\n  For completely independent copies, especially with nested mutable objects, consider 'copy.deepcopy'.")
print("  (This requires importing the 'copy' module).")
