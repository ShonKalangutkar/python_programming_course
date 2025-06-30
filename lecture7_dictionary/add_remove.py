# File: add_dictionary_items.py
# Topic: Adding Items to Dictionaries

"""
This script demonstrates how to add new key:value pairs to a Python dictionary.
It covers adding items using direct assignment with a new key
and using the update() method.
"""


# Initial dictionary
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(f"\nInitial dictionary 'my_dict': {my_dict}")

# 1. Adding Items by Using a New Key
# Adding an item to the dictionary is done by using a new index key and assigning a value to it.
print("\n1. Adding items by using a new index key (direct assignment):")
my_dict["color"] = "red" # Add a new key "color" with value "red"
print(f"  After adding 'color': {my_dict}")
# Expected: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

my_dict["engine"] = "V8" # Add another new key "engine"
print(f"  After adding 'engine': {my_dict}")
# Expected: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red', 'engine': 'V8'}


# 2. update() Method
# The update() method will update the dictionary with the items from a given argument.
# If the item (key) does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
print("\n2. Using the update() method (for adding multiple items or mixed add/change):")

# Adding multiple new items from another dictionary
my_dict.update({"horsepower": 300, "top_speed_mph": 150})
print(f"  After update with {{'horsepower': 300, 'top_speed_mph': 150}}: {my_dict}")
# Expected: Original items + new items

# Adding items from a list of tuples (key-value pairs)
my_dict.update([("status", "available"), ("mileage", 75000)])
print(f"  After update with [('status', 'available'), ('mileage', 75000)]: {my_dict}")
# Expected: Original items + new items

# Using keyword arguments with update()
my_dict.update(num_doors=2, has_ac=True)
print(f"  After update with keyword arguments: {my_dict}")
# Expected: Original items + new items

# Note: If a key passed to update() already exists, its value will be updated, not added again.
my_dict.update({"year": 1965, "color": "blue"}) # 'year' and 'color' already exist, so they are updated
print(f"  After update (mix of adding and updating existing): {my_dict}")

