# File: remove_set_items.py
# Topic: Removing Items from Sets

"""
This script demonstrates various methods for removing items from a Python set.
-   remove(): Removes a specified item; raises an error if the item is not found.
-   discard(): Removes a specified item; does nothing if the item is not found.
-   pop(): Removes and returns a random item (due to sets being unordered).
-   clear(): Removes all elements from the set.
-   del: Deletes the entire set variable.
"""


# Initial set
my_set = {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon'}
print(f"\nInitial set: {my_set}")

# 1. remove() - Removes the specified item. Raises KeyError if not found.
print("\n1. remove(): Removes a specified item (raises KeyError if not found)")
my_set.remove('banana')
print(f"After remove('banana'): {my_set}")
# Expected: {'apple', 'cherry', 'orange', 'kiwi', 'melon'} (order may vary)

# Attempt to remove an item that does not exist (will cause an error)
try:
    my_set.remove('grape')
except KeyError as e:
    print(f"ERROR: Tried to remove 'grape' which is not in set: {e}")
print(f"Set after failed remove('grape'): {my_set}") # Set remains unchanged

# 2. discard() - Removes the specified item. Does NOT raise an error if not found.
print("\n2. discard(): Removes a specified item (does NOT raise error if not found)")
my_set.discard('orange')
print(f"After discard('orange'): {my_set}")
# Expected: {'apple', 'cherry', 'kiwi', 'melon'} (order may vary)

# Attempt to discard an item that does not exist (no error)
my_set.discard('grape')
print(f"After discard('grape') (not in set): {my_set}") # Set remains unchanged

# 3. pop() - Removes and returns a random item.
# Since sets are unordered, you cannot be sure which item will be removed.
print("\n3. pop(): Removes and returns a random item")
print(f"Set before pop(): {my_set}")
random_item = my_set.pop()
print(f"After pop(): {my_set} (Removed item: {random_item})")
# The removed item will be random, and the set will have one less item.

random_item_2 = my_set.pop()
print(f"After another pop(): {my_set} (Removed item: {random_item_2})")

# 4. clear() - Removes all elements from the set.
print("\n4. clear(): Removes all elements from the set")
my_set.clear()
print(f"After clear(): {my_set}")
# Expected: set() (an empty set)

# 5. del keyword - Deletes the entire set variable.
print("\n5. del keyword: Deletes the entire set variable")
another_set = {'red', 'green', 'blue'}
print(f"Another set before del: {another_set}")
del another_set
try:
    print(another_set) # This will cause a NameError
except NameError as e:
    print(f"ERROR: Variable 'another_set' no longer exists: {e}")
