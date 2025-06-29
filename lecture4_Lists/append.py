# File: add_list_items.py
# Topic: Adding Items to Lists

"""
This script demonstrates various methods to add elements to a Python list:
-   append(): Adds a single item to the end of the list.
-   insert(): Adds a single item at a specified index.
-   extend(): Adds all elements from another iterable (e.g., list, tuple, set)
              to the end of the current list.
"""


# Initial list
fruits = ['apple', 'banana', 'cherry']
print(f"\nInitial list 'fruits': {fruits}")

# 1. Append Items
# The append() method adds an item to the end of the list.
print("\n1. Appending items (append() method):")
fruits.append('orange')
print(f"List after appending 'orange': {fruits}")
# Expected: ['apple', 'banana', 'cherry', 'orange']

fruits.append('kiwi')
print(f"List after appending 'kiwi': {fruits}")
# Expected: ['apple', 'banana', 'cherry', 'orange', 'kiwi']

# 2. Insert Items
# The insert() method adds an item at a specified index, without replacing existing items.
print("\n2. Inserting items (insert() method):")
fruits.insert(1, 'grape') # Inserts 'grape' at index 1 (between 'apple' and 'banana')
print(f"List after inserting 'grape' at index 1: {fruits}")
# Expected: ['apple', 'grape', 'banana', 'cherry', 'orange', 'kiwi']

fruits.insert(len(fruits), 'mango') # Inserting at len(list) is equivalent to append
print(f"List after inserting 'mango' at the end (len(list) index): {fruits}")
# Expected: ['apple', 'grape', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

# 3. Extend List
# The extend() method appends elements from another list (or any iterable)
# to the end of the current list.
print("\n3. Extending list (extend() method):")
tropical_fruits = ['pineapple', 'papaya']
print(f"List to extend with: {tropical_fruits}")
fruits.extend(tropical_fruits)
print(f"List after extending with 'tropical_fruits': {fruits}")
# Expected: ['apple', 'grape', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'pineapple', 'papaya']

# 4. Add Any Iterable (using extend())
# The extend() method is flexible and can append elements from any iterable object.
print("\n4. Extending with other iterables (e.g., tuple, set):")

# Extend with a tuple
berries = ('strawberry', 'raspberry')
print(f"Tuple to extend with: {berries}")
fruits.extend(berries)
print(f"List after extending with 'berries' tuple: {fruits}")

# Extend with a set
unique_fruits = {'lemon', 'lime'} # Note: Set order is not guaranteed, but elements will be added
print(f"Set to extend with: {unique_fruits}")
fruits.extend(unique_fruits)
print(f"List after extending with 'unique_fruits' set: {fruits}")

# Extend with a string (iterates over characters)
# Be careful with strings, as it adds each character individually
print(f"\n   Caution: Extending with a string adds each character as an item.")
word = "date"
print(f"   String to extend with: '{word}'")
temp_list = ['temp_fruit']
temp_list.extend(word)
print(f"   Temporary list after extending with '{word}': {temp_list}")
# Expected: ['temp_fruit', 'd', 'a', 't', 'e']
