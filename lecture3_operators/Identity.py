# File: identity_operators.py
# Topic: Identity Operators

"""
This script demonstrates the use of identity operators (is, is not) in Python.
Identity operators are used to compare the memory location of two objects,
i.e., whether they refer to the exact same object in memory, not just if their values are equal.
"""


# --- Example 1: Comparing numbers (often optimized by Python) ---
# For small integers, Python often caches them, so 'is' might return True.
# For larger numbers, it's less likely.

x = 5
y = 5
z = 1000
a = 1000

print(f"\nComparing integers: x = {x}, y = {y}, z = {z}, a = {a}")
print(f"x is y: {x is y} (Do x and y refer to the same object?)")
print(f"x == y: {x == y} (Are x and y values equal?)")

print(f"\nz is a: {z is a} (Do z and a refer to the same object?)")
print(f"z == a: {z == a} (Are z and a values equal?)")

# --- Example 2: Comparing mutable objects (lists) ---
# Lists are mutable, and new lists are typically created in different memory locations.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1 # list3 now refers to the SAME object as list1

print(f"\nComparing lists:")
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1 -> {list3}")

print(f"list1 is list2: {list1 is list2} (Do list1 and list2 refer to the same object?)") # Expected: False (different memory locations)
print(f"list1 == list2: {list1 == list2} (Are list1 and list2 values equal?)") # Expected: True (values are the same)

print(f"\nlist1 is list3: {list1 is list3} (Do list1 and list3 refer to the same object?)") # Expected: True (list3 references list1)
print(f"list1 == list3: {list1 == list3} (Are list1 and list3 values equal?)") # Expected: True (values are the same)

# Modify list3 to see the effect on list1
list3.append(4)
print(f"\nAfter list3.append(4):")
print(f"list1: {list1}") # Expected: [1, 2, 3, 4] (because list1 and list3 are the same object)
print(f"list3: {list3}") # Expected: [1, 2, 3, 4]

# --- Example 3: is not operator ---
# Returns True if both variables are NOT the same object