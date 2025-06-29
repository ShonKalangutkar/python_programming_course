# File: loop_lists.py
# Topic: Looping Through Lists

"""
This script demonstrates various methods for iterating through items in a Python list.
It covers using a for loop, looping by index numbers (with range() and len()),
using a while loop, and the concise syntax of list comprehension.
"""


fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']
print(f"\nInitial list 'fruits': {fruits}")

# 1. Loop Through a List (Using a for loop)
# This is the most common and Pythonic way to iterate directly over items.
print("\n1. Looping through items using a 'for' loop:")
for fruit in fruits:
    print(f"- {fruit}")

# 2. Loop Through the Index Numbers
# You can also loop by referring to their index number using range() and len().
print("\n2. Looping through items using 'for' loop with index numbers (range(len())):")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# 3. Using a While Loop
# You can loop through the list items using a while loop.
# Use len() to determine the length, then start at 0 and refer to indexes.
# Remember to increase the index by 1 after each iteration.
print("\n3. Looping through items using a 'while' loop:")
i = 0
while i < len(fruits):
    print(f"Index {i}: {fruits[i]}")
    i += 1 # Important: increment the index

# 4. Looping Using List Comprehension
# List Comprehension offers a concise syntax for creating new lists by
# looping through an existing list and performing an operation.
print("\n4. Looping using List Comprehension (for creating a new list):")

# Example: Create a new list with fruit names in uppercase
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(f"Original list: {fruits}")
print(f"Uppercase fruits (using list comprehension): {uppercase_fruits}")

# Example: Create a new list containing only fruits with 'a' in their name
a_fruits = [fruit for fruit in fruits if 'a' in fruit]
print(f"Fruits containing 'a' (using list comprehension): {a_fruits}")

# Note: While list comprehension is a loop, its primary purpose is
# to build a new list concisely, rather than just performing an action
# on each element. If you just need to perform an action, a regular
# 'for' loop is usually clearer.
print("\n   Note: List comprehension is primarily for building new lists efficiently.")
print("   If you just need to perform an action on each element, a simple 'for' loop is often preferred.")

