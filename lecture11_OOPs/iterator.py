# File: python_iterators.py
# Topic: Python Iterators

"""
This script demonstrates the concept of iterators in Python.
An iterator is an object that contains a countable number of values and can be traversed.
Technically, an iterator implements the iterator protocol, consisting of __iter__() and __next__() methods.

Key concepts covered:
-   Iterator vs. Iterable: Understanding the difference.
-   Getting an iterator from built-in iterable objects.
-   Looping through iterators using next() and for loops.
-   Creating a custom iterator class by implementing __iter__() and __next__().
-   Handling StopIteration to gracefully end the iteration.
"""


# --- 1. Iterator vs. Iterable ---
# Iterables: Objects that can return an iterator (e.g., lists, tuples, strings, dictionaries, sets).
# Iterators: Objects that actually do the iterating, providing the next element.

print("\n1. Iterator vs. Iterable:")
my_list = [10, 20, 30, 40] # This is an iterable (a container)
print(f"  my_list (iterable): {my_list}")

# Get an iterator from the list using iter()
my_iterator = iter(my_list) # my_iterator is now an iterator object
print(f"  my_iterator (iterator object): {my_iterator}") # Will show an iterator object

# --- 2. Looping Through an Iterator using next() ---
# We can use the next() function to get the next item from an iterator.
print("\n2. Looping through an iterator using next():")
print(f"  First item: {next(my_iterator)}")   # Expected: 10
print(f"  Second item: {next(my_iterator)}")  # Expected: 20
print(f"  Third item: {next(my_iterator)}")   # Expected: 30
print(f"  Fourth item: {next(my_iterator)}")  # Expected: 40

try:
    print(f"  Fifth item (will raise StopIteration): {next(my_iterator)}")
except StopIteration:
    print("  Caught StopIteration: No more items in the iterator.")


# --- 3. Looping Through an Iterable using a For Loop ---
# The 'for' loop implicitly gets an iterator from the iterable and calls next() on it
# until StopIteration is raised.
print("\n3. Looping through an iterable using a 'for' loop:")
my_tuple = ("apple", "banana", "cherry") # This is an iterable
for fruit in my_tuple:
    print(f"  Fruit: {fruit}")
print("  'for' loop implicitly handled iteration and StopIteration.")


# --- 4. Creating a Custom Iterator ---
# To create an object/class as an iterator, you must implement __iter__() and __next__().
print("\n4. Creating a Custom Iterator: 'MyNumbers'")

class MyNumbers:
    def __iter__(self):
        """
        The __iter__() method is called when an iterator is requested for an object.
        It must return the iterator object itself.
        It's also a good place to initialize the iteration state (e.g., a counter).
        """
        self.a = 1 # Initialize our counter
        return self

    def __next__(self):
        """
        The __next__() method returns the next item in the sequence.
        It should raise StopIteration when there are no more items.
        """
        # Our terminating condition: Stop when 'a' is greater than 5
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration # Signal that the iteration is complete

# Create an instance of our custom iterable class
my_numbers_obj = MyNumbers()

# Get an iterator from our custom object
my_custom_iterator = iter(my_numbers_obj)

print("\n  Using next() on our custom iterator:")
print(f"  {next(my_custom_iterator)}") # Expected: 1
print(f"  {next(my_custom_iterator)}") # Expected: 2
print(f"  {next(my_custom_iterator)}") # Expected: 3

# Demonstrate that it resets if you get a new iterator
print("\n  Using a 'for' loop on our custom iterable (implicit new iterator):")
for num in my_numbers_obj: # The for loop calls iter() on my_numbers_obj again
    print(f"  Custom number: {num}")
print("  'for' loop successfully iterated over custom object and handled StopIteration.")
