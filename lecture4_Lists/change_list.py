# File: modifying_list_items.py
# Topic: Modifying List Items

"""
This script demonstrates how to change, update, and insert items in Python lists.
Lists are mutable, meaning their content can be altered after creation.
"""


# Initial list
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']
print(f"\nInitial list 'fruits': {fruits}")

# 1. Change Item Value
# To change the value of a specific item, refer to its index number.
print("\n1. Changing a single item's value:")
fruits[1] = 'blueberry' # Change 'banana' to 'blueberry'
print(f"List after changing item at index 1 to 'blueberry': {fruits}")
# Expected: ['apple', 'blueberry', 'cherry', 'orange', 'kiwi', 'melon']

# 2. Change a Range of Item Values
# To change values within a specific range, define a list with new values
# and assign it to the slice of the list.
print("\n2. Changing a range of item values:")
# Replace items from index 2 (inclusive) to 4 (exclusive) with new values
# Original slice: ['cherry', 'orange']
# New values: ['grape', 'strawberry', 'pineapple']
fruits[2:4] = ['grape', 'strawberry', 'pineapple']
print(f"List after changing items from index 2 to 4 (exclusive): {fruits}")
# Expected: ['apple', 'blueberry', 'grape', 'strawberry', 'pineapple', 'kiwi', 'melon']
# Note: The length of the list can change if the number of new values differs from the number of replaced items.

# Let's try another range change where length stays same or shrinks
another_list = ['A', 'B', 'C', 'D', 'E']
print(f"\n   Another example list: {another_list}")
another_list[1:4] = ['X', 'Y'] # Replace 'B', 'C', 'D' with 'X', 'Y'
print(f"   List after replacing 3 items with 2: {another_list}")
# Expected: ['A', 'X', 'Y', 'E']

# 3. Insert Items (insert() method)
# To insert a new list item without replacing any existing values, use the insert() method.
# The insert() method inserts an item at the specified index.
print("\n3. Inserting new items (insert() method):")

# Insert 'pear' at index 1 (before 'blueberry')
fruits.insert(1, 'pear')
print(f"List after inserting 'pear' at index 1: {fruits}")
# Expected (based on current fruits list): ['apple', 'pear', 'blueberry', 'grape', 'strawberry', 'pineapple', 'kiwi', 'melon']

# Insert 'fig' at the very end (equivalent to append if index is len(list))
fruits.insert(len(fruits), 'fig')
print(f"List after inserting 'fig' at the end: {fruits}")
