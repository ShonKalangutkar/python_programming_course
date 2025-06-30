# File: python_classes_objects.py
# Topic: Python Classes/Objects

"""
This script demonstrates the fundamental concepts of Python Classes and Objects.
Classes serve as blueprints, and objects are instances created from those blueprints.

Key concepts covered:
-   Creating a class using the 'class' keyword.
-   Creating objects (instances) from a class.
-   The __init__() function (constructor) for initializing object properties.
-   The __str__() function for defining an object's string representation.
-   Defining and calling object methods (functions within a class).
-   The 'self' parameter and its role in accessing object properties.
-   Deleting object properties using the 'del' keyword.
-   The 'pass' statement for empty class definitions.
"""


# 1. Create a Class
# To create a class, use the keyword 'class'.
print("\n1. Creating a Class:")
class MyFirstClass:
    # A simple class with a property
    x = 5
    pass # Using pass here for an empty class initially

print("  Class 'MyFirstClass' created.")

# 2. Create Object
# Now we can use the class to create objects (instances).
print("\n2. Creating an Object:")
p1 = MyFirstClass()
print(f"  Object 'p1' created from MyFirstClass. Its 'x' property: {p1.x}") # Accessing property

# 3. The __init__() Function
# This special function is always executed when the class is being initiated (when an object is created).
# Use it to assign values to object properties, or perform other necessary setup.
print("\n3. The __init__() Function (Constructor):")
class Person:
    def __init__(self, name, age):
        """
        The __init__ method (constructor) initializes object properties.
        'self' refers to the instance of the class being created.
        """
        self.name = name  # Assigns the 'name' argument to the object's 'name' property
        self.age = age    # Assigns the 'age' argument to the object's 'age' property
        print(f"    A new Person object created: {self.name}, {self.age} years old.")

# When creating an object from 'Person', __init__ is automatically called.
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(f"  Person1's name: {person1.name}, age: {person1.age}")
print(f"  Person2's name: {person2.name}, age: {person2.age}")


# 4. The __str__() Function
# Controls what should be returned when the class object is represented as a string (e.g., by print()).
# If not set, it returns a default memory address representation.
print("\n4. The __str__() Function:")
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        """
        Defines the string representation of a Car object.
        Called by str(), print(), or when converting object to string.
        """
        return f"Car(Brand: {self.brand}, Model: {self.model}, Year: {self.year})"

# Object without custom __str__ (to show default behavior)
class SimpleObject:
    def __init__(self, value):
        self.value = value
simple_obj = SimpleObject(100)
print(f"  Default __str__ for SimpleObject: {simple_obj}") # Shows memory address

# Object with custom __str__
my_car = Car("Toyota", "Camry", 2020)
print(f"  Custom __str__ for Car object: {my_car}") # Calls __str__ method
print(str(my_car)) # Explicitly calling str() also uses __str__


# 5. Object Methods
# Methods are functions that belong to the object (defined within the class).
print("\n5. Object Methods:")
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self): # This is a method
        """A method that makes the dog bark."""
        print(f"  {self.name} ({self.breed}) says Woof! Woof!")

    def describe(self): # Another method
        """Describes the dog."""
        print(f"  This is {self.name}, a {self.breed}.")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.describe() # Calling the describe method
my_dog.bark()     # Calling the bark method


# 6. The self Parameter
# 'self' is a reference to the current instance of the class.
# It is the first parameter of any instance method in the class.
# It does not *have* to be named 'self', but it's a strong convention.
print("\n6. The 'self' Parameter:")
class Robot:
    def __init__(this_robot, name): # 'this_robot' is used instead of 'self'
        this_robot.name = name
        print(f"    Robot '{this_robot.name}' activated.")

    def introduce(my_instance): # 'my_instance' is used instead of 'self'
        print(f"  Hello, my name is {my_instance.name}.")

robot1 = Robot("C-3PO")
robot1.introduce()

# Reverting to standard 'self' for clarity in subsequent examples.


# 7. Delete Object Properties
# You can delete properties on objects by using the 'del' keyword.
print("\n7. Deleting Object Properties:")
person3 = Person("Charlie", 45) # Create a new person object
print(f"  Person3 before deleting age: Name: {person3.name}, Age: {person3.age}")

del person3.age # Delete the 'age' property
try:
    print(f"  Person3's age after deletion: {person3.age}")
except AttributeError as e:
    print(f"  Error: Tried to access deleted property 'age': {e}")

# You can also delete the object itself (makes it unavailable for further use)
del person3 # Delete the entire object
try:
    print(person3.name)
except NameError as e:
    print(f"  Error: Tried to access deleted object 'person3': {e}")


# 8. The pass Statement in Class Definitions
# Class definitions cannot be empty. If you have a class definition with no content,
# put in the 'pass' statement to avoid getting an error.
print("\n8. The 'pass' Statement in Class Definitions:")
class EmptyClass:
    pass # Placeholder for an empty class

empty_obj = EmptyClass()
print("  'EmptyClass' defined with 'pass' and object 'empty_obj' created successfully.")

