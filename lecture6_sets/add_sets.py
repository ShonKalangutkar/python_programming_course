# File: add_set_items.py
# Topic: Adding Items to Sets

"""
This script demonstrates how to add new items to a Python set.
Although individual set items are unchangeable, you can add new items
using the add() method (for single items) or the update() method (for multiple items from an iterable).
Sets automatically handle duplicate values, ensuring only unique items are stored.
"""


# Initial set
my_set = {'apple', 'banana', 'cherry'}
print(f"\nInitial set: {my_set}")

# 1. add() - To add one item to a set
print("\n1. add(): Adds a single item to the set")
my_set.add('orange')
print(f"After add('orange'): {my_set}")
# Expected: {'apple', 'banana', 'cherry', 'orange'} (order may vary)

# Attempt to add a duplicate (it will be ignored)
my_set.add('apple')
print(f"After add('apple') (duplicate): {my_set}")
# Expected: No change, as 'apple' is already present.

# 2. update() - To add items from another set (or any iterable)
print("\n2. update(): Adds elements from another iterable to the set")
other_fruits = {'kiwi', 'melon', 'banana'} # 'banana' is a duplicate
print(f"Set to update with: {other_fruits}")
my_set.update(other_fruits)
print(f"After update(other_fruits): {my_set}")
# Expected: All unique elements from both sets combined. 'banana' will appear once.
# e.g., {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon'} (order may vary)

# 3. Add Any Iterable - The update() method is versatile
# You can add elements from any iterable object (tuples, lists, strings etc.).
print("\n3. update() with other iterables:")

# Add from a list
vegetables = ['carrot', 'potato', 'cherry'] # 'cherry' is a duplicate
print(f"List to update with: {vegetables}")
my_set.update(vegetables)
print(f"After update(vegetables list): {my_set}")
# e.g., {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'carrot', 'potato'}

# Add from a tuple
spices = ('cumin', 'turmeric', 'kiwi') # 'kiwi' is a duplicate
print(f"Tuple to update with: {spices}")
my_set.update(spices)
print(f"After update(spices tuple): {my_set}")
# e.g., {'apple', ..., 'cumin', 'turmeric'}

# Add from a string (adds individual characters)
word = "date"
print(f"String to update with: '{word}'")
my_set.update(word)
print(f"After update(string 'date'): {my_set}")
# This will add 'd', 'a', 't', 'e' as individual items if not already present.
# e.g., {'apple', ..., 'd', 'a', 't', 'e'}
