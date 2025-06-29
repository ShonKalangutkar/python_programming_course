# File: list_methods.py
# Topic: Python List Methods

"""
This script demonstrates the usage of various built-in methods available for Python lists.
These methods allow you to perform common operations like adding, removing,
modifying, and inspecting list elements.
"""


# Initial list for demonstrations
my_list = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'cherry']
print(f"\nInitial list: {my_list}")

# 1. append() - Adds an element at the end of the list
print("\n1. append(): Adds an element to the end")
my_list.append('grape')
print(f"After append('grape'): {my_list}")
# Expected: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'cherry', 'grape']

# 2. insert() - Adds an element at the specified position
print("\n2. insert(): Adds an element at a specified index")
my_list.insert(1, 'blueberry') # Insert 'blueberry' at index 1
print(f"After insert(1, 'blueberry'): {my_list}")
# Expected: ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'kiwi', 'cherry', 'grape']

# 3. extend() - Add the elements of an iterable to the end of the current list
print("\n3. extend(): Appends elements from another iterable")
tropical_fruits = ['mango', 'pineapple']
my_list.extend(tropical_fruits)
print(f"After extend(['mango', 'pineapple']): {my_list}")
# Expected: ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'kiwi', 'cherry', 'grape', 'mango', 'pineapple']

# 4. remove() - Removes the item with the specified value (first occurrence)
print("\n4. remove(): Removes the first occurrence of a specified value")
my_list.remove('cherry')
print(f"After remove('cherry'): {my_list}")
# Expected: ['apple', 'blueberry', 'banana', 'orange', 'kiwi', 'cherry', 'grape', 'mango', 'pineapple'] (first 'cherry' removed)

# 5. pop() - Removes the element at the specified position (and returns it)
# If no index is specified, it removes and returns the last item.
print("\n5. pop(): Removes element at specified index (or last)")
popped_item = my_list.pop(3) # Remove element at index 3 ('orange')
print(f"After pop(3): {my_list} (Popped item: {popped_item})")
# Expected: ['apple', 'blueberry', 'banana', 'kiwi', 'cherry', 'grape', 'mango', 'pineapple']
# Popped item: 'orange'

last_popped_item = my_list.pop() # Remove the last item ('pineapple')
print(f"After pop(): {my_list} (Popped item: {last_popped_item})")
# Expected: ['apple', 'blueberry', 'banana', 'kiwi', 'cherry', 'grape', 'mango']
# Popped item: 'pineapple'

# 6. del keyword (Not a method, but commonly used for removal by index or slice)
# It's important to differentiate methods from statements like 'del'.
print("\n6. del keyword: Removes element by index or slice (not a method)")
del my_list[0] # Delete 'apple' at index 0
print(f"After del my_list[0]: {my_list}")
# Expected: ['blueberry', 'banana', 'kiwi', 'cherry', 'grape', 'mango']

# 7. clear() - Removes all the elements from the list
print("\n7. clear(): Removes all elements from the list")
temp_list = [1, 2, 3]
print(f"Temporary list before clear(): {temp_list}")
temp_list.clear()
print(f"Temporary list after clear(): {temp_list}")
# Expected: []

# 8. copy() - Returns a shallow copy of the list
print("\n8. copy(): Returns a shallow copy of the list")
original_list = ['A', 'B', 'C']
copied_list = original_list.copy()
print(f"Original list: {original_list}")
print(f"Copied list: {copied_list}")
print(f"Are they the same object? (original_list is copied_list): {original_list is copied_list}") # Expected: False
copied_list.append('D')
print(f"Original list after modifying copied_list: {original_list}") # Original remains unchanged
# Expected: ['A', 'B', 'C']

# 9. count() - Returns the number of elements with the specified value
print("\n9. count(): Returns the number of occurrences of a value")
my_new_list = ['red', 'blue', 'green', 'red', 'yellow', 'red']
print(f"List for count(): {my_new_list}")
red_count = my_new_list.count('red')
blue_count = my_new_list.count('blue')
orange_count = my_new_list.count('orange')
print(f"Count of 'red': {red_count}")   # Expected: 3
print(f"Count of 'blue': {blue_count}") # Expected: 1
print(f"Count of 'orange': {orange_count}") # Expected: 0

# 10. index() - Returns the index of the first element with the specified value
print("\n10. index(): Returns the index of the first occurrence of a value")
print(f"List for index(): {my_new_list}")
print(f"Index of 'blue': {my_new_list.index('blue')}") # Expected: 1
print(f"Index of 'red': {my_new_list.index('red')}")   # Expected: 0 (first occurrence)
# print(my_new_list.index('purple')) # This would raise a ValueError if item not found

# 11. reverse() - Reverses the order of the list (in-place)
print("\n11. reverse(): Reverses the order of the list")
print(f"List before reverse(): {my_new_list}")
my_new_list.reverse()
print(f"List after reverse(): {my_new_list}")
# Expected: ['red', 'yellow', 'red', 'green', 'blue', 'red']

# 12. sort() - Sorts the list alphanumerically (in-place)
print("\n12. sort(): Sorts the list (ascending by default)")
print(f"List before sort(): {my_new_list}")
my_new_list.sort() # Sorts alphabetically
print(f"List after sort(): {my_new_list}")
# Expected: ['blue', 'green', 'red', 'red', 'red', 'yellow']

# Sort descending
print(f"List before sort(reverse=True): {my_new_list}")
my_new_list.sort(reverse=True)
print(f"List after sort(reverse=True): {my_new_list}")
# Expected: ['yellow', 'red', 'red', 'red', 'green', 'blue']

