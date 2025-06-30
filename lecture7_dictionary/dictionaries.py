# File: dictionaries.py
# Topic: Python Dictionaries

"""
This script demonstrates the fundamental characteristics and creation of Python Dictionaries.

Key characteristics of Dictionaries:
-   Ordered*: Items have a defined order, which will not change (Python 3.7+).
-   Changeable (Mutable): Items can be changed, added, or removed after creation.
-   No Duplicate Keys: Each key must be unique. If a key is duplicated, the last assignment wins.
-   Stored as key:value pairs.
-   Written with curly brackets {}.
-   Keys must be immutable (e.g., strings, numbers, tuples). Values can be any data type.

*Note: Dictionaries were unordered in Python 3.6 and earlier.
"""


# 1. Creating a Dictionary
# Dictionaries are created using curly brackets {} with key:value pairs.
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"] # Value can be a list
}
print(f"\n1. Created a dictionary 'my_dict': {my_dict}")
print(f"Type of my_dict: {type(my_dict)}") # Using type()

# 2. Dictionary Items - Ordered (Python 3.7+)
print("\n2. Dictionaries are Ordered (as of Python 3.7+):")
# The order in which items are inserted is maintained.
# This is hard to "demonstrate" definitively in code without repeated runs
# but it's a fundamental property.
print("   The order of items in 'my_dict' is preserved based on insertion.")
print("   (In Python 3.6 and earlier, dictionaries were unordered).")

# 3. Changeable - Changing, Adding, Removing items
print("\n3. Dictionaries are Changeable:")

# Change an item's value
my_dict["year"] = 2020
print(f"   After changing 'year': {my_dict}")

# Add a new item
my_dict["engine"] = "V8"
print(f"   After adding 'engine': {my_dict}")

# Add another item
my_dict["electric"] = False
print(f"   After adding 'electric': {my_dict}")

# 4. Duplicates Not Allowed (for keys)
# If you try to insert a duplicate key, the new value will overwrite the existing one.
print("\n4. Duplicates Not Allowed (for keys):")
duplicate_key_dict = {
    "name": "Alice",
    "age": 30,
    "name": "Bob" # This 'name' will overwrite the previous 'Alice'
}
print(f"   Dictionary with a duplicate key 'name': {duplicate_key_dict}")
# Expected: {'name': 'Bob', 'age': 30}

# 5. Dictionary Length (len() function)
print(f"\n5. Length of 'my_dict': {len(my_dict)} items") # Expected: 6

# 6. Dictionary Items - Data Types
# Values can be of any data type, keys must be immutable (strings, numbers, tuples).
mixed_value_dict = {
    "string_key": "some text",
    123: 456,           # Integer key
    True: False,        # Boolean key
    (1, 2): [7, 8, 9],  # Tuple key with list value
    "complex_value": {"nested": "dict"} # Nested dictionary as value
}
print(f"\n6. Dictionary with mixed data types (for values and keys): {mixed_value_dict}")
print(f"   Value of 'string_key': {mixed_value_dict['string_key']}")
print(f"   Value of (1, 2) key: {mixed_value_dict[(1, 2)]}")

# 7. The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
print("\n7. Creating dictionaries using the dict() constructor:")

# From keyword arguments
from_keywords = dict(brand="Volvo", model="XC60", year=2024)
print(f"   From keyword arguments: {from_keywords}")

# From a list of tuples (key-value pairs)
from_list_of_tuples = dict([("name", "Charlie"), ("age", 25)])
print(f"   From a list of tuples: {from_list_of_tuples}")

# From zipped lists (keys and values)
keys = ['city', 'population']
values = ['London', 9000000]
from_zipped = dict(zip(keys, values))
print(f"   From zipped lists: {from_zipped}")

