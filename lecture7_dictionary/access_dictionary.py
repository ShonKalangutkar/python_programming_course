# File: accessing_dictionary_items.py
# Topic: Accessing Dictionary Items

"""
This script demonstrates various methods for accessing data within a Python dictionary.
It covers direct key access, the get() method, retrieving keys, values, and items views,
and checking for key existence.
"""

my_car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red",
    "engine": "V8"
}
print(f"\nInitial dictionary 'my_car': {my_car}")

# 1. Accessing Items by Key Name (using square brackets [])
# This is the most common way to access a dictionary's value.
print("\n1. Accessing items by key name (square brackets []):")
model_name = my_car["model"]
print(f"  Model: {model_name}") # Expected: Mustang
brand_name = my_car["brand"]
print(f"  Brand: {brand_name}") # Expected: Ford

# Trying to access a non-existent key with [] will raise a KeyError
try:
    non_existent = my_car["price"]
except KeyError as e:
    print(f"  ERROR: Attempted to access non-existent key 'price' with []: {e}")


# 2. Accessing Items using the get() method
# The get() method provides a safer way to access items, as it returns None
# if the key does not exist, instead of raising an error.
print("\n2. Accessing items using the get() method:")
year_value = my_car.get("year")
print(f"  Year: {year_value}") # Expected: 1964

# Key not found with get() - returns None by default
price_value = my_car.get("price")
print(f"  Price (key not found): {price_value}") # Expected: None

# get() with a default value if key is not found
miles_value = my_car.get("miles", "Not Available")
print(f"  Miles (key not found, with default): {miles_value}") # Expected: Not Available


# 3. Get Keys (keys() method)
# The keys() method returns a view object that displays a list of all the keys.
# This view is dynamic; any changes to the dictionary will be reflected in the keys view.
print("\n3. Getting dictionary keys (keys() method):")
car_keys = my_car.keys()
print(f"  Keys: {list(car_keys)}") # Convert to list for clear printing

# Demonstrate view property: add a new item and see it reflected
my_car["transmission"] = "automatic"
print(f"  After adding 'transmission' to dictionary: {my_car}")
print(f"  Updated keys view: {list(car_keys)}") # 'transmission' is now included

# 4. Get Values (values() method)
# The values() method returns a view object that displays a list of all the values.
# This view is also dynamic.
print("\n4. Getting dictionary values (values() method):")
car_values = my_car.values()
print(f"  Values: {list(car_values)}")

# Demonstrate view property: change an item and see it reflected
my_car["color"] = "blue"
print(f"  After changing 'color' in dictionary: {my_car}")
print(f"  Updated values view: {list(car_values)}") # 'blue' is now included

# 5. Get Items (items() method)
# The items() method returns a view object that displays each item as a tuple (key, value) in a list.
# This view is also dynamic.
print("\n5. Getting dictionary items (items() method):")
car_items = my_car.items()
print(f"  Items: {list(car_items)}")

# Demonstrate view property: remove an item and see it reflected
del my_car["engine"]
print(f"  After removing 'engine' from dictionary: {my_car}")
print(f"  Updated items view: {list(car_items)}") # 'engine' pair is gone

# 6. Check if Key Exists (using the 'in' keyword)
# Use the 'in' keyword to determine if a specified key is present in a dictionary.
print("\n6. Checking if a key exists ('in' keyword):")
check_key1 = "model"
check_key2 = "price"

print(f"  Is '{check_key1}' in my_car? {check_key1 in my_car}") # Expected: True
print(f"  Is '{check_key2}' in my_car? {check_key2 in my_car}") # Expected: False
