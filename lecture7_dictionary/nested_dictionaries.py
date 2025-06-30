# File: nested_dictionaries.py
# Topic: Nested Dictionaries

"""
This script demonstrates the concept of nested dictionaries in Python,
where a dictionary can contain other dictionaries as its values.
It covers creation, accessing items, and looping through nested structures.
"""


# 1. Creating Nested Dictionaries

# Method A: Direct creation
print("\n1.1. Creating a nested dictionary (direct creation):")
myfamily_direct = {
    "child1": {
        "name": "Emil",
        "year": 2004,
        "hobbies": ["painting", "reading"]
    },
    "child2": {
        "name": "Tobias",
        "year": 2007,
        "hobbies": ["gaming", "coding"]
    },
    "child3": {
        "name": "Linus",
        "year": 2011,
        "hobbies": ["sports", "music"]
    }
}
print(f"  Nested dictionary 'myfamily_direct': {myfamily_direct}")

# Method B: Adding existing dictionaries into a new dictionary
print("\n1.2. Creating a nested dictionary (by combining existing dictionaries):")
child1_dict = {
    "name": "Emil",
    "year": 2004
}
child2_dict = {
    "name": "Tobias",
    "year": 2007
}
child3_dict = {
    "name": "Linus",
    "year": 2011
}

myfamily_combined = {
    "child1": child1_dict,
    "child2": child2_dict,
    "child3": child3_dict
}
print(f"  Nested dictionary 'myfamily_combined': {myfamily_combined}")

# 2. Access Items in Nested Dictionaries
# To access items, you chain the key names, starting from the outer dictionary.
print("\n2. Accessing items in nested dictionaries:")
print(f"  Name of child1: {myfamily_direct['child1']['name']}") # Expected: Emil
print(f"  Year of child2: {myfamily_direct['child2']['year']}") # Expected: 2007
print(f"  First hobby of child1: {myfamily_direct['child1']['hobbies'][0]}") # Accessing an item in a list within a nested dict

# You can also assign the nested dictionary to a variable first for readability
child2_info = myfamily_direct["child2"]
print(f"  Hobbies of child2 (via temp variable): {child2_info['hobbies']}") # Expected: ['gaming', 'coding']

# 3. Loop Through Nested Dictionaries
# You can loop through the outer dictionary and then loop through the inner dictionaries.
print("\n3. Looping through nested dictionaries:")
print("  --- Family Members Details ---")
for child_key, child_data in myfamily_direct.items():
    print(f"\n  Child ID: {child_key}")
    for detail_key, detail_value in child_data.items():
        print(f"    {detail_key.capitalize()}: {detail_value}")
