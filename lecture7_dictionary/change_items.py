# File: change_dictionary_values.py
# Topic: Changing Dictionary Values

"""
This script demonstrates how to modify the values associated with keys
in a Python dictionary.
It covers direct assignment using the key and the update() method.
"""


# Initial dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}
print(f"\nInitial dictionary 'car': {car}")

# 1. Change Values by Referring to Key Name
# You can change the value of a specific item by referring to its key name.
print("\n1. Changing values by referring to key name:")
car["year"] = 2020 # Change the value associated with the "year" key
print(f"  After changing 'year' to 2020: {car}")
# Expected: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}

car["color"] = "blue" # Change the value associated with the "color" key
print(f"  After changing 'color' to 'blue': {car}")
# Expected: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'blue'}


# 2. update() Method
# The update() method will update the dictionary with the items from the given argument.
# If a key exists, its value is updated. If a key does not exist, it is added.
# The argument can be another dictionary or an iterable of key:value pairs.
print("\n2. Using the update() method:")

# Update with another dictionary
car.update({"engine": "V8", "year": 2024}) # "year" will be updated, "engine" will be added
print(f"  After update with {{'engine': 'V8', 'year': 2024}}: {car}")
# Expected: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024, 'color': 'blue', 'engine': 'V8'}

# Update with an iterable of key:value pairs (e.g., a list of tuples)
car.update([("seats", 4), ("color", "black")]) # "seats" added, "color" updated
print(f"  After update with [('seats', 4), ('color', 'black')]: {car}")
# Expected: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024, 'color': 'black', 'engine': 'V8', 'seats': 4}

# Update with keyword arguments (another common way)
car.update(is_electric=False, brand="Tesla") # New key 'is_electric', 'brand' updated
print(f"  After update with keyword arguments: {car}")
# Expected: {'brand': 'Tesla', 'model': 'Mustang', 'year': 2024, 'color': 'black', 'engine': 'V8', 'seats': 4, 'is_electric': False}

