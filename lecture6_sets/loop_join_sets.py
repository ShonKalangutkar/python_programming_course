# File: set_operations.py
# Topic: Looping and Joining Sets (Set Operations)

"""
This script demonstrates how to loop through set items and various methods
for joining/combining sets based on their elements.

Key operations covered:
-   Looping through sets.
-   Union (combines all unique elements).
-   Update (adds elements from another iterable to the current set).
-   Intersection (keeps only common elements/duplicates).
-   Difference (keeps elements unique to the first set).
-   Symmetric Difference (keeps elements unique to either set, excludes common).
"""


my_set = {'apple', 'banana', 'cherry', 'orange'}
print(f"\nInitial set for looping: {my_set}")

# 1. Loop Through a Set
# You can loop through the set items using a 'for' loop.
# Remember that the order of items in a set is not guaranteed.
print("\n1. Looping through set items:")
for fruit in my_set:
    print(f"- {fruit}")

print("\n--- Demonstrating Set Joining Operations ---")

# Define sample sets for joining operations
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = {'cherry', 'orange', 'kiwi'}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Set 3: {set3}")

# 2. Union - Combines all unique items from both (or more) sets.
# Returns a NEW set.
print("\n2. Union: Combines all unique items (union() method / | operator)")
set_union_method = set1.union(set2)
print(f"set1.union(set2): {set_union_method}") # Expected: all unique elements from set1 and set2

set_union_operator = set1 | set2
print(f"set1 | set2: {set_union_operator}") # Same result as union() method

# Joining multiple sets
set_multi_union_method = set1.union(set2, set3)
print(f"set1.union(set2, set3): {set_multi_union_method}")

set_multi_union_operator = set1 | set2 | set3
print(f"set1 | set2 | set3: {set_multi_union_operator}")

# Join a Set and a Tuple (union() allows other iterables)
my_set_union_tuple = set1.union(('grape', 'banana', 'lemon')) # 'banana' is a duplicate
print(f"set1.union(('grape', 'banana', 'lemon')): {my_set_union_tuple}")

# 3. update() - Inserts all items from another set (or iterable) into the CURRENT set.
# Modifies the original set, does NOT return a new set.
print("\n3. update(): Adds elements from another iterable to the CURRENT set")
set_to_update = {'cat', 'dog', 'fish'}
print(f"Set before update: {set_to_update}")
set_to_update.update({'bird', 'dog', 'hamster'}) # 'dog' is a duplicate
print(f"Set after update with another set: {set_to_update}")
# Expected: {'cat', 'dog', 'fish', 'bird', 'hamster'} (order may vary)

set_to_update_with_list = {'alpha', 'beta'}
print(f"Set before update with list: {set_to_update_with_list}")
set_to_update_with_list.update(['gamma', 'alpha', 'delta'])
print(f"Set after update with list: {set_to_update_with_list}")
# Expected: {'alpha', 'beta', 'gamma', 'delta'}

# 4. Intersection - Keeps ONLY the common items (duplicates).
# Returns a NEW set.
print("\n4. Intersection: Keeps ONLY the common items (intersection() / & operator)")
set_intersection_method = set1.intersection(set2)
print(f"set1.intersection(set2): {set_intersection_method}") # Expected: {'apple'}

set_intersection_operator = set1 & set2
print(f"set1 & set2: {set_intersection_operator}")

# intersection_update() - Keeps ONLY the common items, modifies the ORIGINAL set.
print("\n   intersection_update(): Modifies original set, keeping only common items")
set_for_intersection_update = {'A', 'B', 'C', 'D'}
print(f"Set before intersection_update: {set_for_intersection_update}")
set_for_intersection_update.intersection_update({'C', 'D', 'E', 'F'})
print(f"Set after intersection_update: {set_for_intersection_update}") # Expected: {'C', 'D'}

# True/1 and False/0 equivalence in set operations
set_num_bool1 = {1, True, 2, 0, False, 3}
set_num_bool2 = {0, 1, 4, 5}
print(f"\n   Set with numbers and booleans (1/True, 0/False equivalent):")
print(f"   set_num_bool1: {set_num_bool1}") # Will likely show {0, 1, 2, 3} as True/False are stored as 1/0
print(f"   set_num_bool2: {set_num_bool2}")
print(f"   set_num_bool1.intersection(set_num_bool2): {set_num_bool1.intersection(set_num_bool2)}") # Expected: {0, 1}

# 5. Difference - Keeps items from the FIRST set that are not in the other set(s).
# Returns a NEW set.
print("\n5. Difference: Keeps items unique to the FIRST set (difference() / - operator)")
set_difference_method = set1.difference(set2)
print(f"set1.difference(set2): {set_difference_method}") # Expected: {'banana', 'cherry'}

set_difference_operator = set1 - set2
print(f"set1 - set2: {set_difference_operator}")

# difference_update() - Modifies the ORIGINAL set, keeping only unique items from itself.
print("\n   difference_update(): Modifies original set, removing common items")
set_for_difference_update = {'X', 'Y', 'Z', 'W'}
print(f"Set before difference_update: {set_for_difference_update}")
set_for_difference_update.difference_update({'Z', 'A', 'B'})
print(f"Set after difference_update: {set_for_difference_update}") # Expected: {'X', 'Y', 'W'}

# 6. Symmetric Difference - Keeps all items EXCEPT the duplicates.
# Returns a NEW set.
print("\n6. Symmetric Difference: Keeps all items EXCEPT common ones (symmetric_difference() / ^ operator)")
set_symmetric_difference_method = set1.symmetric_difference(set2)
print(f"set1.symmetric_difference(set2): {set_symmetric_difference_method}")
# Expected: {'banana', 'cherry', 'google', 'microsoft'} (elements unique to either set)

set_symmetric_difference_operator = set1 ^ set2
print(f"set1 ^ set2: {set_symmetric_difference_operator}")

# symmetric_difference_update() - Modifies the ORIGINAL set, keeping all except common items.
print("\n   symmetric_difference_update(): Modifies original set, keeping all but duplicates")
set_for_symmetric_difference_update = {'alpha', 'beta', 'gamma'}
print(f"Set before symmetric_difference_update: {set_for_symmetric_difference_update}")
set_for_symmetric_difference_update.symmetric_difference_update({'gamma', 'delta', 'epsilon'})
print(f"Set after symmetric_difference_update: {set_for_symmetric_difference_update}")
# Expected: {'alpha', 'beta', 'delta', 'epsilon'} (gamma was common, so removed)
