# File: set_methods.py
# Topic: Python Set Built-in Methods

"""
This script demonstrates the usage of various built-in methods available for Python sets.
These methods allow you to add, remove, compare, and combine set elements efficiently.
"""


# --- Sample Sets for Demonstrations ---
set_a = {'apple', 'banana', 'cherry', 'date'}
set_b = {'cherry', 'date', 'elderberry', 'fig'}
set_c = {'apple', 'banana'} # A subset of set_a
set_d = {'grape', 'honeydew'} # Disjoint from set_a

print(f"\nInitial Sets for demonstration:")
print(f"  set_a = {set_a}")
print(f"  set_b = {set_b}")
print(f"  set_c = {set_c}")
print(f"  set_d = {set_d}")

# 1. add() - Adds an element to the set
print("\n1. add(): Adds an element to the set")
my_set_add = {'cat', 'dog'}
print(f"  Before add('bird'): {my_set_add}")
my_set_add.add('bird')
print(f"  After add('bird'): {my_set_add}")
my_set_add.add('cat') # Adding a duplicate, no effect
print(f"  After add('cat') (duplicate): {my_set_add}")

# 2. clear() - Removes all the elements from the set
print("\n2. clear(): Removes all elements from the set")
my_set_clear = {1, 2, 3}
print(f"  Before clear(): {my_set_clear}")
my_set_clear.clear()
print(f"  After clear(): {my_set_clear}")

# 3. copy() - Returns a copy of the set
print("\n3. copy(): Returns a shallow copy of the set")
my_set_copy = set_a.copy()
print(f"  Original set_a: {set_a}")
print(f"  Copied set: {my_set_copy}")
print(f"  Are they the same object? (set_a is my_set_copy): {set_a is my_set_copy}") # Expected: False
my_set_copy.add('guava')
print(f"  Original set_a after modifying copy: {set_a}") # original is unchanged

# 4. difference() (-) - Returns a new set with items in the first set but not in others
print("\n4. difference() (-): Items in first set, not in others")
set_diff_method = set_a.difference(set_b)
print(f"  set_a.difference(set_b): {set_diff_method}") # Expected: {'apple', 'banana'}
set_diff_operator = set_a - set_b
print(f"  set_a - set_b: {set_diff_operator}") # Same result

# 5. difference_update() (-=) - Removes items in this set that are also in another
print("\n5. difference_update() (-=): Removes common items from THIS set")
my_set_diff_update = {'X', 'Y', 'Z', 'W'}
print(f"  Before difference_update: {my_set_diff_update}")
my_set_diff_update.difference_update({'Z', 'A', 'B'})
print(f"  After difference_update({'Z', 'A', 'B'}): {my_set_diff_update}") # Expected: {'X', 'Y', 'W'}
my_set_diff_update_op = {'P', 'Q', 'R', 'S'}
print(f"  Before -=: {my_set_diff_update_op}")
my_set_diff_update_op -= {'R', 'T'}
print(f"  After -= {'R', 'T'}: {my_set_diff_update_op}") # Expected: {'P', 'Q', 'S'}

# 6. discard() - Remove the specified item (no error if not found)
print("\n6. discard(): Removes item, no error if not found")
my_set_discard = {'one', 'two', 'three'}
print(f"  Before discard('two'): {my_set_discard}")
my_set_discard.discard('two')
print(f"  After discard('two'): {my_set_discard}")
my_set_discard.discard('four') # Item not present, no error
print(f"  After discard('four') (not found): {my_set_discard}")

# 7. intersection() (&) - Returns a new set with ONLY the common items
print("\n7. intersection() (&): Keeps ONLY common items")
set_intersect_method = set_a.intersection(set_b)
print(f"  set_a.intersection(set_b): {set_intersect_method}") # Expected: {'cherry', 'date'}
set_intersect_operator = set_a & set_b
print(f"  set_a & set_b: {set_intersect_operator}")

# 8. intersection_update() (&=) - Modifies original set, keeping only common items
print("\n8. intersection_update() (&=): Modifies original, keeping only common items")
my_set_intersect_update = {'red', 'green', 'blue'}
print(f"  Before intersection_update: {my_set_intersect_update}")
my_set_intersect_update.intersection_update({'green', 'yellow', 'red'})
print(f"  After intersection_update: {my_set_intersect_update}") # Expected: {'red', 'green'}
my_set_intersect_update_op = {'alpha', 'beta', 'gamma'}
print(f"  Before &=: {my_set_intersect_update_op}")
my_set_intersect_update_op &= {'beta', 'delta'}
print(f"  After &= {'beta', 'delta'}: {my_set_intersect_update_op}") # Expected: {'beta'}

# 9. isdisjoint() - Returns True if two sets have no common items
print("\n9. isdisjoint(): Checks if two sets have NO common items")
print(f"  set_a: {set_a}, set_b: {set_b}")
print(f"  set_a.isdisjoint(set_b): {set_a.isdisjoint(set_b)}") # Expected: False ('cherry', 'date' are common)
print(f"  set_a: {set_a}, set_d: {set_d}")
print(f"  set_a.isdisjoint(set_d): {set_a.isdisjoint(set_d)}") # Expected: True (no common items)

# 10. issubset() (<=, <) - Checks if another set contains this set
print("\n10. issubset() (<=, <): Checks if this set is a subset of another")
print(f"  set_c: {set_c}, set_a: {set_a}")
print(f"  set_c.issubset(set_a): {set_c.issubset(set_a)}") # Expected: True (all elements of c are in a)
print(f"  set_c <= set_a: {set_c <= set_a}") # Same as issubset()

# Proper subset (<): Returns True if all items in this set are present in other, and the other set has more items.
print(f"  set_c < set_a (proper subset): {set_c < set_a}") # Expected: True
print(f"  set_a < set_a (proper subset): {set_a < set_a}") # Expected: False (not strictly smaller)

# 11. issuperset() (>=, >) - Checks if this set contains another set
print("\n11. issuperset() (>=, >): Checks if this set is a superset of another")
print(f"  set_a: {set_a}, set_c: {set_c}")
print(f"  set_a.issuperset(set_c): {set_a.issuperset(set_c)}") # Expected: True (a contains all elements of c)
print(f"  set_a >= set_c: {set_a >= set_c}") # Same as issuperset()

# Proper superset (>): Returns True if all items in other set are present in this set, and this set has more items.
print(f"  set_a > set_c (proper superset): {set_a > set_c}") # Expected: True
print(f"  set_a > set_a (proper superset): {set_a > set_a}") # Expected: False

# 12. pop() - Removes a random element from the set (and returns it)
print("\n12. pop(): Removes and returns a random element")
my_set_pop = {'pen', 'pencil', 'eraser', 'ruler'}
print(f"  Before pop(): {my_set_pop}")
popped_item = my_set_pop.pop()
print(f"  After pop(): {my_set_pop} (Removed: {popped_item})")
# Item removed is random due to set's unordered nature.

# 13. remove() - Removes the specified item (raises KeyError if not found)
print("\n13. remove(): Removes specified item (raises KeyError if not found)")
my_set_remove = {'keyboard', 'mouse', 'monitor'}
print(f"  Before remove('mouse'): {my_set_remove}")
my_set_remove.remove('mouse')
print(f"  After remove('mouse'): {my_set_remove}")
try:
    my_set_remove.remove('speaker') # Item not present
except KeyError as e:
    print(f"  ERROR: Tried to remove 'speaker' which is not in set: {e}")

# 14. symmetric_difference() (^) - Returns a new set with items NOT common to both
print("\n14. symmetric_difference() (^): Items unique to either set (excluding common)")
set_sym_diff_method = set_a.symmetric_difference(set_b)
print(f"  set_a.symmetric_difference(set_b): {set_sym_diff_method}")
# Expected: {'apple', 'banana', 'elderberry', 'fig'}
set_sym_diff_operator = set_a ^ set_b
print(f"  set_a ^ set_b: {set_sym_diff_operator}")

# 15. symmetric_difference_update() (^=) - Modifies original, keeping items not common
print("\n15. symmetric_difference_update() (^=): Modifies original, keeping unique items from both")
my_set_sym_diff_update = {'monday', 'tuesday', 'wednesday'}
print(f"  Before symmetric_difference_update: {my_set_sym_diff_update}")
my_set_sym_diff_update.symmetric_difference_update({'wednesday', 'thursday', 'friday'})
print(f"  After symmetric_difference_update: {my_set_sym_diff_update}")
# Expected: {'monday', 'tuesday', 'thursday', 'friday'} (wednesday was common, so removed)
my_set_sym_diff_update_op = {'jan', 'feb', 'mar'}
print(f"  Before ^=: {my_set_sym_diff_update_op}")
my_set_sym_diff_update_op ^= {'mar', 'apr'}
print(f"  After ^= {'mar', 'apr'}: {my_set_sym_diff_update_op}") # Expected: {'jan', 'feb', 'apr'}

# 16. union() (|) - Returns a new set containing all unique items from all sets
print("\n16. union() (|): Returns a new set with all unique items")
set_union_method_full = set_a.union(set_b, set_c)
print(f"  set_a.union(set_b, set_c): {set_union_method_full}")
set_union_operator_full = set_a | set_b | set_c
print(f"  set_a | set_b | set_c: {set_union_operator_full}")

# 17. update() (|=) - Updates the set with the union of this set and others
print("\n17. update() (|=): Updates THIS set with the union of itself and others")
my_set_update = {'alpha', 'beta'}
print(f"  Before update: {my_set_update}")
my_set_update.update({'gamma', 'beta', 'delta'})
print(f"  After update: {my_set_update}") # Expected: {'alpha', 'beta', 'gamma', 'delta'}
my_set_update_op = {'north', 'south'}
print(f"  Before |=: {my_set_update_op}")
my_set_update_op |= {'east', 'west', 'north'}
print(f"  After |= {'east', 'west', 'north'}: {my_set_update_op}") # Expected: {'north', 'south', 'east', 'west'}
