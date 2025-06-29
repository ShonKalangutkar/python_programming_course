# File: accessing_list_items.py
# Topic: Accessing List Items

"""
This script demonstrates various ways to access elements in Python lists
using indexing, negative indexing, and slicing (ranges).
It also covers how to check if an item exists in a list.
"""


fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(f"\nInitial list 'fruits': {fruits}")

# 1. Accessing Items by Index
# List items are indexed, starting from 0 for the first item.
print("\n1. Accessing items by positive index:")
print(f"Element at index 0: {fruits[0]}")  # Expected: 'apple'
print(f"Element at index 3: {fruits[3]}")  # Expected: 'orange'

# 2. Negative Indexing
# Negative indexing means starting from the end of the list.
# -1 refers to the last item, -2 refers to the second last item, etc.
print("\n2. Accessing items by negative index:")
print(f"Last element (index -1): {fruits[-1]}")   # Expected: 'mango'
print(f"Second last element (index -2): {fruits[-2]}") # Expected: 'melon'

# 3. Range of Indexes (Slicing)
# You can specify a range by indicating start:end.
# The slice includes the item at the start index but excludes the item at the end index.
print("\n3. Accessing items using a range of positive indexes (slicing):")
print(f"Elements from index 2 to 5 (exclusive): {fruits[2:5]}") # Expected: ['cherry', 'orange', 'kiwi']
# Note: The search starts at index 2 (included) and ends at index 5 (not included).

# 3.1. Range from the beginning
# By leaving out the start value, the range will start at the first item (index 0).
print(f"Elements from beginning up to index 4 (exclusive): {fruits[:4]}") # Expected: ['apple', 'banana', 'cherry', 'orange']

# 3.2. Range to the end
# By leaving out the end value, the range will go to the end of the list.
print(f"Elements from index 3 to the end: {fruits[3:]}") # Expected: ['orange', 'kiwi', 'melon', 'mango']

# 3.3. Full copy of the list
print(f"Full copy of the list using slicing: {fruits[:]}") # Expected: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']


# 4. Range of Negative Indexes
# Specify negative indexes to start the search from the end of the list.
print("\n4. Accessing items using a range of negative indexes:")
# Elements from 'orange' (index -4) to 'melon' (index -2 exclusive)
print(f"Elements from index -4 to -2 (exclusive): {fruits[-4:-1]}") # Expected: ['orange', 'kiwi', 'melon']
print(f"Elements from index -3 to the end: {fruits[-3:]}") # Expected: ['kiwi', 'melon', 'mango']


# 5. Check if Item Exists
# Use the 'in' keyword to determine if a specified item is present in a list.
print("\n5. Checking if an item exists in the list ('in' keyword):")
search_item1 = "cherry"
search_item2 = "grape"

print(f"Is '{search_item1}' in fruits? {search_item1 in fruits}") # Expected: True
print(f"Is '{search_item2}' in fruits? {search_item2 in fruits}") # Expected: False
