# File: modifying_tuples.py
# Topic: Modifying Tuples (Workarounds for Immutability)

"""
This script demonstrates the workarounds for "modifying" immutable Python tuples.
Since tuples are unchangeable (immutable), direct modification, addition, or
removal of items is not possible. However, you can convert a tuple to a mutable
type (like a list), perform operations, and then convert it back to a tuple.
Additionally, you can concatenate tuples to effectively "add" items.
"""


# Initial tuple
my_tuple = ("apple", "banana", "cherry")
print(f"\nInitial tuple: {my_tuple}")

# Attempting direct modification (will result in an error)
print("\n--- Attempting Direct Modifications (will cause errors) ---")
try:
    my_tuple[1] = "blueberry"
    print("This line will not be reached.")
except TypeError as e:
    print(f"ERROR: Cannot change item directly: {e}")

try:
    my_tuple.append("grape")
    print("This line will not be reached.")
except AttributeError as e:
    print(f"ERROR: Cannot append directly: {e}")

try:
    my_tuple.remove("apple")
    print("This line will not be reached.")
except AttributeError as e:
    print(f"ERROR: Cannot remove directly: {e}")


# --- Workarounds for Changing, Adding, and Removing Items ---

## 1. Changing Tuple Values (via List Conversion)
# You can convert the tuple into a list, change the list,
# and convert the list back into a tuple.
print("\n--- 1. Changing Tuple Values (via List Conversion) ---")
print(f"Original tuple: {my_tuple}")

# Convert tuple to list
temp_list = list(my_tuple)
print(f"Converted to list: {temp_list}")

# Modify the list
temp_list[1] = "blueberry"
print(f"List after changing item at index 1: {temp_list}")

# Convert list back to tuple
my_tuple = tuple(temp_list)
print(f"Tuple after change (converted back): {my_tuple}")
# Expected: ('apple', 'blueberry', 'cherry')


## 2. Adding Items to a Tuple

### 2.1. Adding Items (via List Conversion)
# Similar to changing, convert to a list, add, then convert back.
print("\n--- 2.1. Adding Items (via List Conversion) ---")
print(f"Current tuple: {my_tuple}")

temp_list = list(my_tuple)
temp_list.append("kiwi")
my_tuple = tuple(temp_list)
print(f"Tuple after adding 'kiwi' (via list conversion): {my_tuple}")
# Expected: ('apple', 'blueberry', 'cherry', 'kiwi')

### 2.2. Adding Tuple to a Tuple (Concatenation)
# You can add tuples to tuples, effectively creating a new tuple with more items.
print("\n--- 2.2. Adding Tuple to a Tuple (Concatenation) ---")
print(f"Current tuple: {my_tuple}")

new_item_tuple = ("mango",) # Remember the comma for a single-item tuple
my_tuple = my_tuple + new_item_tuple
print(f"Tuple after adding ('mango',) (concatenation): {my_tuple}")
# Expected: ('apple', 'blueberry', 'cherry', 'kiwi', 'mango')

more_items_tuple = ("grape", "pineapple")
my_tuple = my_tuple + more_items_tuple
print(f"Tuple after adding ('grape', 'pineapple') (concatenation): {my_tuple}")
# Expected: ('apple', 'blueberry', 'cherry', 'kiwi', 'mango', 'grape', 'pineapple')


## 3. Removing Items from a Tuple (via List Conversion)
# Since tuples are unchangeable, you cannot remove items directly.
# Use the list conversion workaround.
print("\n--- 3. Removing Items (via List Conversion) ---")
print(f"Current tuple: {my_tuple}")

temp_list = list(my_tuple)
temp_list.remove("cherry") # Remove 'cherry'
print(f"List after removing 'cherry': {temp_list}")
my_tuple = tuple(temp_list)
print(f"Tuple after removing 'cherry' (converted back): {my_tuple}")
# Expected: ('apple', 'blueberry', 'kiwi', 'mango', 'grape', 'pineapple')

# You can also use 'del' on the entire tuple to delete it from memory.
# This is not removing an item, but deleting the whole tuple variable.
print("\n--- Deleting the Entire Tuple Variable ---")
print(f"Tuple before deleting the variable: {my_tuple}")
del my_tuple
try:
    print(my_tuple) # This will cause a NameError
except NameError as e:
    print(f"ERROR: Variable 'my_tuple' no longer exists: {e}")
