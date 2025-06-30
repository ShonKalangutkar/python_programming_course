# File: loop_dictionaries.py
# Topic: Looping Through Dictionaries

"""
This script demonstrates various methods for iterating through items in a Python dictionary.
It covers looping through keys, values, and key-value pairs.
"""


my_car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}
print(f"\nInitial dictionary 'my_car': {my_car}")

# 1. Loop Through a Dictionary (Default: Iterating over Keys)
# When you loop through a dictionary directly, the return value is the keys of the dictionary.
print("\n1. Looping directly through a dictionary (iterates over keys):")
for x in my_car:
    print(f"- Key: {x}")

# 2. Loop Through Keys and Access Values
# You can use the retrieved key to access its corresponding value inside the loop.
print("\n2. Looping through keys and accessing values inside the loop:")
for x in my_car:
    print(f"- Key: {x}, Value: {my_car[x]}")

# 3. Loop Through Values (using values() method)
# The values() method returns a view object that displays a list of all the values.
print("\n3. Looping through values (using .values() method):")
for value in my_car.values():
    print(f"- Value: {value}")

# 4. Loop Through Items (using items() method)
# The items() method returns a view object that displays each item as a tuple (key, value) in a list.
# This allows for convenient unpacking of key and value in the loop.
print("\n4. Looping through key-value pairs (using .items() method):")
for key, value in my_car.items():
    print(f"- Key: {key}, Value: {value}")

# Example with different variable names
print("\n   Example of .items() with different variable names:")
for k, v in my_car.items():
    print(f"   {k} --> {v}")
