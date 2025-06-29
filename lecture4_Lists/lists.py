# File: lists.py
# Topic: Python Lists

"""
This script demonstrates the fundamental characteristics and operations of Python Lists.

Key characteristics of Lists:
-   Ordered: Items have a defined order which will not change. New items are added to the end.
-   Changeable (Mutable): Items can be changed, added, or removed after creation.
-   Allow Duplicates: Can contain multiple items with the same value.
-   Indexed: Items are accessed by their position (index), starting from 0.
-   Can hold items of different data types.
"""


# 1. Creating a List
# Lists are created using square brackets [].
fruits = ['apple', 'banana', 'cherry', 'apple', 'orange']
print("\n1. Created a list 'fruits':", fruits)

# 2. Accessing List Items (Ordered and Indexed)
# The first item has index [0], the second [1], etc.
print("\n2. Accessing list items:")
print(f"First element (index 0): {fruits[0]}")
print(f"Second element (index 1): {fruits[1]}")
print(f"Last element (using negative indexing): {fruits[-1]}")

# 3. List Length (len() function)
# To determine how many items a list has.
print(f"\n3. Length of 'fruits' list: {len(fruits)} items") # Expected: 5

# 4. Changeable (Modifying, Adding, Removing items)

# Change a specific item
fruits[1] = 'blueberry'
print(f"\n4.1. List after changing second element to 'blueberry': {fruits}")

# Append an item (adds to the end)
fruits.append('kiwi')
print(f"4.2. List after appending 'kiwi': {fruits}")

# Insert an item at a specific index
fruits.insert(2, 'grape') # Inserts 'grape' at index 2
print(f"4.3. List after inserting 'grape' at index 2: {fruits}")

# Remove an item by value
fruits.remove('apple') # Removes the first occurrence of 'apple'
print(f"4.4. List after removing 'apple' (first occurrence): {fruits}")

# Remove an item by index (pop())
removed_item = fruits.pop(3) # Removes item at index 3 ('orange')
print(f"4.5. List after popping item at index 3: {fruits} (Removed: {removed_item})")

# Delete an item using del keyword
del fruits[0] # Deletes the item at index 0 ('grape')
print(f"4.6. List after deleting item at index 0: {fruits}")

# Clear all items from the list
# fruits.clear()
# print(f"4.7. List after clearing all items: {fruits}")

# 5. Allowing Duplicates
# As seen in the initial list, 'apple' appeared twice.
print(f"\n5. Initial list allowing duplicates: {['red', 'blue', 'red']}")

# 6. List Items - Data Types
# Lists can contain items of different data types.
mixed_list = ["apple", 123, True, 3.14, ['nested', 'list']]
print(f"\n6. List with mixed data types: {mixed_list}")
print(f"Type of first element: {type(mixed_list[0])}")
print(f"Type of second element: {type(mixed_list[1])}")
print(f"Type of fifth element: {type(mixed_list[4])}")

# 7. Iterating through a List (common operation)
print("\n7. Iterating through the current 'fruits' list:")
for fruit in fruits:
    print(f"- {fruit}")

