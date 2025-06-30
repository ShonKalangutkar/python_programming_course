# File: loop_tuples.py
# Topic: Looping Through Tuples

"""
This script demonstrates various methods for iterating through items in a Python tuple.
It covers using a for loop, looping by index numbers (with range() and len()),
and using a while loop.
"""


my_tuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon')
print(f"\nInitial tuple 'my_tuple': {my_tuple}")

# 1. Loop Through a Tuple (Using a for loop)
# This is the most common and Pythonic way to iterate directly over items.
print("\n1. Looping through items using a 'for' loop:")
for fruit in my_tuple:
    print(f"- {fruit}")

# 2. Loop Through the Index Numbers
# You can also loop by referring to their index number using range() and len().
print("\n2. Looping through items using 'for' loop with index numbers (range(len())):")
for i in range(len(my_tuple)):
    print(f"Index {i}: {my_tuple[i]}")

# 3. Using a While Loop
# You can loop through the tuple items by using a while loop.
# Use len() to determine the length, then start at 0 and refer to indexes.
# Remember to increase the index by 1 after each iteration.
print("\n3. Looping through items using a 'while' loop:")
i = 0
while i < len(my_tuple):
    print(f"Index {i}: {my_tuple[i]}")
    i += 1 # Important: increment the index
