# File: sets.py
# Topic: Python Sets

"""
This script demonstrates the fundamental characteristics and creation of Python Sets.

Key characteristics of Sets:
-   Unordered: Items do not have a defined order; their order can change.
-   Unchangeable*: Individual items cannot be changed after creation.
-   Unindexed: Cannot be referred to by index or key.
-   No Duplicates: Automatically removes duplicate values.
-   Written with curly brackets {}.
-   Can hold items of different data types.

*Note: While individual set items are unchangeable, you can remove items from and add new items to the set.
"""


# 1. Creating a Set
# Sets are created using curly brackets {}.
my_set = {'apple', 'banana', 'cherry', 'apple', 'orange'} # 'apple' is duplicated, but only one will be stored
print(f"\n1. Created a set 'my_set': {my_set}")
print(f"Type of my_set: {type(my_set)}") # Using type()
# Expected output will show 'apple' only once, and order might vary.
# e.g., {'cherry', 'orange', 'apple', 'banana'}

# 2. Set Items - Unordered and Unindexed
# You cannot access items by index or key.
print("\n2. Sets are unordered and unindexed:")
try:
    print(f"Attempting to access element at index 0: {my_set[0]}") # This will raise a TypeError
except TypeError as e:
    print(f"   ERROR: Cannot access set items by index: {e}")

# 3. Set Items - Unchangeable (Immutability of elements)
# Attempting to change an individual item will result in an error.
print("\n3. Set items are unchangeable:")
# To demonstrate, we'd need to try to modify an item, which isn't a direct operation on a set.
# You can't do my_set[0] = 'grape' because it's unindexed.
# The concept here means you can't alter 'apple' to 'apricot' within the set directly.
print("   Individual items within a set cannot be changed directly.")
print("   (Unlike lists, you cannot modify a specific item in place).")


# 4. Duplicates Not Allowed
# Duplicate values are automatically ignored when creating a set.
print("\n4. Sets do not allow duplicate values:")
list_with_duplicates = [1, 2, 2, 3, 4, 4, 1, 5]
unique_numbers = set(list_with_duplicates)
print(f"Original list with duplicates: {list_with_duplicates}")
print(f"Set created from list (duplicates removed): {unique_numbers}")
# Expected: {1, 2, 3, 4, 5} (order may vary)

# 5. Get the Length of a Set (len() function)
print(f"\n5. Length of 'my_set': {len(my_set)} items") # Expected: 4 (since 'apple' was duplicated)

# 6. Set Items - Data Types
# Set items can be of any data type (as long as they are hashable).
# Mutable types like lists or dictionaries cannot be set items.
mixed_set = {"hello", 123, True, 3.14, (1, 2)} # Tuples are hashable
print(f"\n6. Set with mixed data types: {mixed_set}")
# The order of items when printed will vary.

# Attempt to add unhashable type (list)
try:
    mixed_set.add(['a', 'b'])
except TypeError as e:
    print(f"   ERROR: Cannot add mutable (unhashable) types like list to a set: {e}")


# 7. The set() Constructor
# It is also possible to use the set() constructor to make a set from an iterable.
print("\n7. Creating sets using the set() constructor:")
from_list = set(['grape', 'lemon', 'lime', 'grape'])
print(f"   From a list: {from_list}") # 'grape' duplicate removed

from_string = set("programming") # Each unique character becomes an item
print(f"   From a string: {from_string}")
# Expected: {'g', 'm', 'i', 'p', 'o', 'r', 'a', 'n'} (order will vary)

from_tuple = set(('cat', 'dog', 'cat', 'bird'))
print(f"   From a tuple: {from_tuple}")
