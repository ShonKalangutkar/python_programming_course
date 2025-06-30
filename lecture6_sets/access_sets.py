# File: accessing_set_items.py
# Topic: Accessing Set Items

"""
This script demonstrates how to "access" items in a Python set.
Since sets are unordered and unindexed, direct access by index or key is not possible.
Instead, you can iterate through the set or check for the presence of an item.
"""


my_set = {'apple', 'banana', 'cherry', 'orange', 'kiwi'}
print(f"\nInitial set 'my_set': {my_set}")

# 1. Cannot Access Items by Index or Key
# Sets do not support indexing or key-based access.
print("\n1. IMPORTANT: Cannot access set items by index or key:")
try:
    print(f"Attempting to access element at index 0: {my_set[0]}")
except TypeError as e:
    print(f"   ERROR: {e} - Sets are unindexed, so direct access like my_set[0] is not allowed.")

# 2. Loop Through the Set (Using a for loop)
# This is the primary way to process each item in a set.
# Note: The order of items when looping is not guaranteed to be the same every time.
print("\n2. Looping through set items using a 'for' loop:")
for fruit in my_set:
    print(f"- {fruit}")

# 3. Check if Item Exists (using the 'in' keyword)
# This is the most efficient way to determine if a specified item is present in a set.
print("\n3. Checking if an item exists in the set ('in' keyword):")
search_item1 = "cherry"
search_item2 = "grape"

print(f"Is '{search_item1}' in my_set? {search_item1 in my_set}") # Expected: True
print(f"Is '{search_item2}' in my_set? {search_item2 in my_set}") # Expected: False
