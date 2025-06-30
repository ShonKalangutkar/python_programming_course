# File: python_polymorphism.py
# Topic: Python Polymorphism

"""
This script demonstrates the concept of Polymorphism in Python.
Polymorphism refers to the ability of methods, functions, or operators to
work differently based on the object or class they are applied to.

Key concepts covered:
-   Function Polymorphism: A single function/operator working on different data types.
-   Class Polymorphism (without inheritance): Multiple classes having methods with the same name.
-   Inheritance Class Polymorphism: Child classes overriding methods from a parent class,
    allowing a common interface for different implementations.
"""


# --- 1. Function Polymorphism ---
# An example of a Python function that can be used on different objects
# is the built-in len() function.
print("\n1. Function Polymorphism (e.g., len() function):")

# For strings, len() returns the number of characters.
my_string = "Hello World"
print(f"  Length of string '{my_string}': {len(my_string)}") # Expected: 11

# For tuples, len() returns the number of items.
my_tuple = (1, 2, 3, 4, 5)
print(f"  Length of tuple {my_tuple}: {len(my_tuple)}") # Expected: 5

# For dictionaries, len() returns the number of key/value pairs.
my_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(f"  Length of dictionary {my_dictionary}: {len(my_dictionary)}") # Expected: 3

# For lists, len() returns the number of items.
my_list = ["apple", "banana", "cherry"]
print(f"  Length of list {my_list}: {len(my_list)}") # Expected: 3
print("  The 'len()' function demonstrates polymorphism by working on various iterable types.")


# --- 2. Class Polymorphism (without Inheritance) ---
# We can have multiple independent classes with methods that have the same name.
print("\n2. Class Polymorphism (without Inheritance):")

class Car:
    def move(self):
        print("  The car drives on the road.")

class Boat:
    def move(self):
        print("  The boat sails on the water.")

class Plane:
    def move(self):
        print("  The plane flies in the sky.")

# Create objects of each class
my_car = Car()
my_boat = Boat()
my_plane = Plane()

# Put them in a list
vehicles = [my_car, my_boat, my_plane]

print("  Calling the 'move()' method on different vehicle objects:")
for vehicle in vehicles:
    vehicle.move() # The same 'move()' call behaves differently for each object type
print("  This shows polymorphism where different classes implement a common method name differently.")


# --- 3. Inheritance Class Polymorphism ---
# Child classes inherit properties and methods from a parent class,
# but can also override (provide their own implementation for) those methods.
print("\n3. Inheritance Class Polymorphism:")

class Vehicle: # Parent Class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"  {self.brand} {self.model} moves.")

class CarInherited(Vehicle): # Child Class, implicitly uses Vehicle's move()
    pass # Inherits move() from Vehicle

class BoatInherited(Vehicle): # Child Class, overrides move()
    def move(self):
        print(f"  {self.brand} {self.model} sails on the water.")

class PlaneInherited(Vehicle): # Child Class, overrides move()
    def move(self):
        print(f"  {self.brand} {self.model} flies through the air.")

# Create objects of parent and child classes
vehicle_obj = Vehicle("Generic", "Vehicle")
car_obj = CarInherited("Nissan", "Leaf")
boat_obj = BoatInherited("SeaRay", "Sundancer")
plane_obj = PlaneInherited("Boeing", "747")

# Put them in a list
fleet = [vehicle_obj, car_obj, boat_obj, plane_obj]

print("  Calling the 'move()' method on Vehicle and its child class objects:")
for item in fleet:
    item.move() # The same 'move()' call invokes different implementations

print("  Here, 'move()' is called on objects of different types (Vehicle, CarInherited, BoatInherited, PlaneInherited).")
print("  Each object responds to the 'move()' call in its own specific way,")
print("  either by inheriting the parent's method or by overriding it.")
