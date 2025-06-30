# File: accessing_tuple_items.py
# Topic: Accessing Tuple Items

"""
This script demonstrates various ways to access elements in Python tuples
using indexing, negative indexing, and slicing (ranges).
It also covers how to check if an item exists in a tuple.
"""


my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(f"\nInitial tuple 'my_tuple': {my_tuple}")

# 1. Accessing Items by Index
# Tuple items are indexed, starting from 0 for the first item.
print("\n1. Accessing items by positive index:")
print(f"Element at index 0: {my_tuple[0]}")  # Expected: 'apple'
print(f"Element at index 3: {my_tuple[3]}")  # Expected: 'orange'

# 2. Negative Indexing
# Negative indexing means starting from the end of the tuple.
# -1 refers to the last item, -2 refers to the second last item, etc.
print("\n2. Accessing items by negative index:")
print(f"Last element (index -1): {my_tuple[-1]}")   # Expected: 'mango'
print(f"Second last element (index -2): {my_tuple[-2]}") # Expected: 'melon'

# 3. Range of Indexes (Slicing)
# You can specify a range by indicating start:end.
# The slice includes the item at the start index but excludes the item at the end index.
# The return value will be a new tuple with the specified items.
print("\n3. Accessing items using a range of positive indexes (slicing):")
print(f"Elements from index 2 to 5 (exclusive): {my_tuple[2:5]}") # Expected: ('cherry', 'orange', 'kiwi')
# Note: The search starts at index 2 (included) and ends at index 5 (not included).

# 3.1. Range from the beginning
# By leaving out the start value, the range will start at the first item (index 0).
print(f"Elements from beginning up to index 4 (exclusive): {my_tuple[:4]}") # Expected: ('apple', 'banana', 'cherry', 'orange')

# 3.2. Range to the end
# By leaving out the end value, the range will go to the end of the tuple.
print(f"Elements from index 3 to the end: {my_tuple[3:]}") # Expected: ('orange', 'kiwi', 'melon', 'mango')

# 3.3. Full copy of the tuple
print(f"Full copy of the tuple using slicing: {my_tuple[:]}") # Expected: ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')


# 4. Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple.
print("\n4. Accessing items using a range of negative indexes:")
# Example: Returns the items from index -4 (included) to index -1 (excluded)
# -4 is 'orange', -1 is 'mango' (exclusive, so up to 'melon')
print(f"Elements from index -4 to -1 (exclusive): {my_tuple[-4:-1]}") # Expected: ('orange', 'kiwi', 'melon')
print(f"Elements from index -3 to the end: {my_tuple[-3:]}") # Expected: ('kiwi', 'melon', 'mango')


# 5. Check if Item Exists
# Use the 'in' keyword to determine if a specified item is present in a tuple.
print("\n5. Checking if an item exists in the tuple ('in' keyword):")
search_item1 = "cherry"
search_item2 = "grape"

print(f"Is '{search_item1}' in my_tuple? {search_item1 in my_tuple}") # Expected: True
print(f"Is '{search_item2}' in my_tuple? {search_item2 in my_tuple}") # Expected: False
