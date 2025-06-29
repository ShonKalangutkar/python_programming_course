# File: list_comprehension.py
# Topic: List Comprehension

"""
This script demonstrates the syntax and versatility of List Comprehension in Python.
List comprehension provides a concise way to create new lists based on existing iterables.

Syntax: new_list = [expression for item in iterable if condition == True]

Key benefits:
-   Shorter syntax compared to traditional for loops.
-   Often more readable for simple transformations and filtering.
-   Generally more efficient than traditional loops for list creation.
"""


fruits = ["apple", "banana", "cherry", "kiwi", "mango", "grape"]
print(f"\nOriginal list of fruits: {fruits}")

# 1. Basic List Comprehension (Filtering with a condition)
# Example: Create a new list containing only fruits with the letter "a" in their name.

# Without list comprehension:
print("\n1.1. Filtering without list comprehension:")
fruits_with_a = []
for x in fruits:
    if "a" in x:
        fruits_with_a.append(x)
print(f"Fruits with 'a' (traditional loop): {fruits_with_a}")

# With list comprehension:
print("\n1.2. Filtering with list comprehension:")
newlist_a = [x for x in fruits if "a" in x]
print(f"Fruits with 'a' (list comprehension): {newlist_a}")
# Expected: ['apple', 'banana', 'mango', 'grape']

# 2. The 'Condition' - Acting as a Filter
# The condition is optional and filters items that evaluate to True.

# Example: Exclude "apple" from the new list
print("\n2. Conditional filtering:")
fruits_no_apple = [x for x in fruits if x != "apple"]
print(f"Fruits without 'apple': {fruits_no_apple}")
# Expected: ['banana', 'cherry', 'kiwi', 'mango', 'grape']

# Example: Filter for fruits longer than 5 characters
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(f"Fruits with length > 5: {long_fruits}")
# Expected: ['banana', 'cherry', 'orange', 'kiwi' (if it was longer), 'mango', 'grape'] -> (banana, cherry, orange, mango, grape if 'orange' was in original)
# Correction based on initial list: ['banana', 'cherry', 'orange', 'mango'] (assuming 'orange' was initially in list for example)
# With current `fruits`: ['banana', 'cherry', 'mango']

# 3. The 'Iterable'
# The iterable can be any iterable object (list, tuple, set, string, etc.).

print("\n3. Using different iterables:")
my_tuple = ("car", "bike", "bus")
cars_only = [x for x in my_tuple if "car" in x]
print(f"From tuple {my_tuple}, items with 'car': {cars_only}") # Expected: ['car']

my_string = "programming"
vowels = [char for char in my_string if char in "aeiou"]
print(f"Vowels in '{my_string}': {vowels}") # Expected: ['o', 'a', 'i']

# 4. The 'Expression' - Manipulating the Outcome
# The expression is the current item, which can be manipulated before it's added to the new list.

# Example: Convert all fruit names to uppercase
print("\n4. Manipulating the 'expression':")
uppercase_fruits = [x.upper() for x in fruits]
print(f"All fruits in uppercase: {uppercase_fruits}")
# Expected: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO', 'GRAPE']

# Example: Add "fresh_" prefix to fruits
prefixed_fruits = ["fresh_" + x for x in fruits]
print(f"Fruits with 'fresh_' prefix: {prefixed_fruits}")

# Example: Return "long" or "short" based on fruit length
length_description = ["long" if len(x) > 5 else "short" for x in fruits]
print(f"Fruit length descriptions: {length_description}")
# Expected: ['short', 'long', 'long', 'short', 'short', 'short'] (based on current fruits)

# Example: Using else in the expression (condition is BEFORE the for loop)
# newlist = [expression IF condition ELSE another_expression FOR item IN iterable]
fruits_with_or_without_a = [x if "a" in x else "no 'a'" for x in fruits]
print(f"Fruits with 'a' or 'no 'a'' tag: {fruits_with_or_without_a}")
# Expected: ['apple', 'banana', 'no 'a'', 'no 'a'', 'mango', 'no 'a''] (based on current fruits)
# Note: kiwi and grape do not have 'a'
