# File: dictionary_methods.py
# Topic: Python Dictionary Built-in Methods

"""
This script demonstrates the usage of various built-in methods available for Python dictionaries.
These methods allow you to manipulate, query, and manage key-value pairs efficiently.
"""


# --- Sample Dictionaries for Demonstrations ---
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}

person_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(f"\nInitial Dictionaries for demonstration:")
print(f"  car_dict = {car_dict}")
print(f"  person_dict = {person_dict}")

# 1. clear() - Removes all the elements from the dictionary
print("\n1. clear(): Removes all elements from the dictionary")
my_dict_clear = {"a": 1, "b": 2, "c": 3}
print(f"  Before clear(): {my_dict_clear}")
my_dict_clear.clear()
print(f"  After clear(): {my_dict_clear}") # Expected: {}

# 2. copy() - Returns a copy of the dictionary
print("\n2. copy(): Returns a shallow copy of the dictionary")
car_copy = car_dict.copy()
print(f"  Original car_dict: {car_dict}")
print(f"  Copied car_copy: {car_copy}")
print(f"  Are they the same object? (car_dict is car_copy): {car_dict is car_copy}") # Expected: False
car_copy["year"] = 2020 # Modify copy
print(f"  car_dict after modifying car_copy: {car_dict}") # Original unchanged

# 3. fromkeys() - Returns a dictionary with the specified keys and a specified value
print("\n3. fromkeys(): Creates a dictionary from keys with an optional default value")
keys = ('key1', 'key2', 'key3')
default_value = 0
new_dict_fromkeys = dict.fromkeys(keys, default_value)
print(f"  dict.fromkeys({keys}, {default_value}): {new_dict_fromkeys}")
# Expected: {'key1': 0, 'key2': 0, 'key3': 0}

no_value_dict = dict.fromkeys(['a', 'b'])
print(f"  dict.fromkeys(['a', 'b']) (default None): {no_value_dict}")
# Expected: {'a': None, 'b': None}

# 4. get() - Returns the value of the specified key
print("\n4. get(): Returns the value for a key (or None/default if not found)")
model = car_dict.get("model")
print(f"  Value for 'model': {model}") # Expected: Mustang
color = car_dict.get("color", "Not specified") # Key exists, default not used
print(f"  Value for 'color' (with default): {color}")
price = car_dict.get("price", "N/A") # Key does not exist, default is returned
print(f"  Value for 'price' (with default): {price}")

# 5. items() - Returns a view object of all key-value pairs as tuples
print("\n5. items(): Returns a view of (key, value) pairs")
car_items = car_dict.items()
print(f"  car_dict.items(): {list(car_items)}") # Convert to list for clear printing
car_dict["engine"] = "V8" # Add a new item to demonstrate view property
print(f"  car_dict after adding 'engine': {car_dict}")
print(f"  Updated car_dict.items() view: {list(car_items)}") # View reflects change

# 6. keys() - Returns a view object of all the keys
print("\n6. keys(): Returns a view of all keys")
person_keys = person_dict.keys()
print(f"  person_dict.keys(): {list(person_keys)}")
person_dict["country"] = "USA" # Add item to demonstrate view property
print(f"  person_dict after adding 'country': {person_dict}")
print(f"  Updated person_dict.keys() view: {list(person_keys)}") # View reflects change

# 7. pop() - Removes the element with the specified key and returns its value
print("\n7. pop(): Removes a specified key-value pair and returns the value")
popped_year = car_dict.pop("year")
print(f"  After pop('year'): {car_dict} (Popped value: {popped_year})")
# Expected: {'brand': 'Ford', 'model': 'Mustang', 'color': 'red', 'engine': 'V8'} (year removed)

try:
    car_dict.pop("nonexistent_key")
except KeyError as e:
    print(f"  ERROR: Tried to pop 'nonexistent_key': {e}") # Raises KeyError if not found
popped_value_with_default = car_dict.pop("mileage", 0) # Returns default if key not found
print(f"  After pop('mileage', 0) (not found): {car_dict} (Popped value: {popped_value_with_default})")

# 8. popitem() - Removes the last inserted key-value pair (Python 3.7+), and returns it as a tuple
print("\n8. popitem(): Removes and returns the last inserted (key, value) pair")
# Note: In Python 3.6 and earlier, popitem() removed a random item.
last_item = person_dict.popitem()
print(f"  After popitem(): {person_dict} (Removed item: {last_item})")
# Expected: ('country', 'USA') or similar if order varied.

# 9. setdefault() - Returns the value of the specified key. If the key does not exist,
#                   it inserts the key with the specified value and returns that value.
print("\n9. setdefault(): Gets value for key, or inserts key with default if not found")
my_dict_setdefault = {"name": "Bob", "age": 25}
print(f"  Initial dict for setdefault: {my_dict_setdefault}")

# Key exists, returns current value (does not change it)
existing_city = my_dict_setdefault.setdefault("city", "London")
print(f"  setdefault('city', 'London') (key doesn't exist yet): {my_dict_setdefault} -> Value: {existing_city}")
# Expected: {'name': 'Bob', 'age': 25, 'city': 'London'}

# Key exists, returns existing value (does not update it)
existing_age = my_dict_setdefault.setdefault("age", 40)
print(f"  setdefault('age', 40) (key exists): {my_dict_setdefault} -> Value: {existing_age}")
# Expected: Value 25, dictionary remains unchanged.

# 10. update() - Updates the dictionary with the specified key-value pairs.
#                Adds new items if keys don't exist, updates values if keys exist.
print("\n10. update(): Updates with new key-value pairs (adds or modifies)")
print(f"  Before update: {car_dict}")
car_dict.update({"year": 2023, "horsepower": 450, "color": "blue"})
print(f"  After update({{ 'year': 2023, 'horsepower': 450, 'color': 'blue' }}): {car_dict}")
# Expected: 'year' and 'color' updated, 'horsepower' added.

# 11. values() - Returns a view object of all the values
print("\n11. values(): Returns a view of all values")
person_values = person_dict.values()
print(f"  person_dict.values(): {list(person_values)}")
person_dict["age"] = 31 # Modify value to demonstrate view property
print(f"  person_dict after changing 'age': {person_dict}")
print(f"  Updated person_dict.values() view: {list(person_values)}") # View reflects change

