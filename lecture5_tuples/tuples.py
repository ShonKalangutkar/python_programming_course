# File: tuples.py
# Topic: Python Tuples

"""
This script demonstrates the fundamental characteristics and operations of Python Tuples.

Key characteristics of Tuples:
-   Ordered: Items have a defined order which will not change.
-   Unchangeable (Immutable): Items cannot be changed, added, or removed after creation.
-   Allow Duplicates: Can contain multiple items with the same value.
-   Indexed: Items are accessed by their position (index), starting from 0.
-   Can hold items of different data types.
-   Written with round brackets ().
"""


# 1. Creating a Tuple
# Tuples are created using round brackets ().
my_tuple = ('apple', 'banana', 'cherry', 'apple', 'orange')
print(f"\n1. Created a tuple 'my_tuple': {my_tuple}")
print(f"Type of my_tuple: {type(my_tuple)}") # Using type()

# 2. Tuple Items - Ordered and Indexed
# The first item has index [0], the second [1], etc.
print("\n2. Accessing tuple items (ordered and indexed):")
print(f"First element (index 0): {my_tuple[0]}")
print(f"Third element (index 2): {my_tuple[2]}")
print(f"Last element (using negative indexing): {my_tuple[-1]}")

# 3. Tuple Length (len() function)
print(f"\n3. Length of 'my_tuple': {len(my_tuple)} items") # Expected: 5

# 4. Unchangeable (Immutability)
# Attempting to change, add, or remove items will result in an error.
print("\n4. Tuples are unchangeable (immutable):")
try:
    my_tuple[1] = 'blueberry' # This will raise a TypeError
except TypeError as e:
    print(f"   Attempted to change item at index 1: {e}")

try:
    my_tuple.append('grape') # This will raise an AttributeError
except AttributeError as e:
    print(f"   Attempted to append an item: {e}")

try:
    my_tuple.remove('apple') # This will raise an AttributeError
except AttributeError as e:
    print(f"   Attempted to remove an item: {e}")

# 5. Allow Duplicates
# Since tuples are indexed, they can have items with the same value.
print(f"\n5. Tuples allow duplicate values: {('red', 'blue', 'red', 'green')}")

# 6. Create Tuple With One Item
# A single item needs a trailing comma to be recognized as a tuple.
single_item_tuple_correct = ("apple",)
print(f"\n6. Tuple with one item (correct way): {single_item_tuple_correct}")
print(f"   Type of single_item_tuple_correct: {type(single_item_tuple_correct)}") # Expected: <class 'tuple'>

single_item_not_tuple = ("apple") # Without comma, it's just a string
print(f"   Single item without comma (not a tuple): {single_item_not_tuple}")
print(f"   Type of single_item_not_tuple: {type(single_item_not_tuple)}") # Expected: <class 'str'>

# 7. Tuple Items - Data Types
# Tuple items can be of any data type.
mixed_tuple = ("hello", 123, True, 3.14, ['a', 'b'], {'key': 'value'})
print(f"\n7. Tuple with mixed data types: {mixed_tuple}")
print(f"   Type of first element: {type(mixed_tuple[0])}")
print(f"   Type of fifth element (a list): {type(mixed_tuple[4])}")

# 8. The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple from an iterable.
print("\n8. Creating tuples using the tuple() constructor:")
from_list = tuple(['kiwi', 'lemon', 'lime'])
print(f"   From a list: {from_list}")

from_string = tuple("Python")
print(f"   From a string: {from_string}") # Each character becomes an item

from_set = tuple({'x', 'y', 'z'}) # Note: sets are unordered, so tuple order may vary
print(f"   From a set: {from_set}")
