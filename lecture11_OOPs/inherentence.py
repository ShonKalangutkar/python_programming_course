# File: python_inheritance.py
# Topic: Python Inheritance

"""
This script demonstrates the concept of Inheritance in Python,
a fundamental principle of Object-Oriented Programming (OOP).

Inheritance allows a class (child/derived class) to inherit all
the methods and properties from another class (parent/base class).

Key concepts covered:
-   Defining a Parent Class.
-   Defining a Child Class that inherits from a Parent.
-   Adding the __init__() method to a Child Class.
-   Using the super() function to automatically call the parent's __init__()
    and inherit its methods/properties.
-   Adding new properties specific to the Child Class.
"""


# --- 1. Create a Parent Class ---
# A Parent Class (also called Base Class) is the class being inherited from.
print("\n1. Creating a Parent Class: 'Person'")
class Person:
    def __init__(self, fname, lname):
        """Initializes a Person object with first and last name."""
        self.firstname = fname
        self.lastname = lname
        print(f"    Person created: {self.firstname} {self.lastname}")

    def printname(self):
        """Prints the full name of the person."""
        print(f"  {self.firstname} {self.lastname}")

# Create an object of the Parent Class
parent_person = Person("John", "Doe")
print("  Calling printname() from Parent Class object:")
parent_person.printname()

# --- 2. Create a Child Class ---
# A Child Class (also called Derived Class) inherits from another class.
# To create a child class, send the parent class as a parameter during definition.
print("\n2. Creating a Child Class: 'Student' (inherits from Person)")
class Student(Person): # Student inherits from Person
    pass # Use 'pass' for now, indicating no additional properties/methods yet

# Create an object of the Child Class
# Even with 'pass', Student objects inherit __init__ and printname from Person
student1 = Student("Mike", "Olsen")
print("  Calling printname() from Child Class object (inherited):")
student1.printname()


# --- 3. Add the __init__() Function to Child Class ---
# We want to add new properties to the child class, but still retain parent's initialization.
# Without calling parent's __init__, parent properties might not be initialized.
print("\n3. Adding __init__() to Child Class and calling Parent's __init__ explicitly:")
class Teacher(Person):
    def __init__(self, fname, lname, subject):
        # Call the parent's __init__ method using the parent's name
        Person.__init__(self, fname, lname)
        # Add new property specific to Teacher
        self.subject = subject
        print(f"    Teacher created: {self.firstname} {self.lastname}, Subject: {self.subject}")

    def teach(self):
        """A method specific to the Teacher class."""
        print(f"  {self.firstname} is teaching {self.subject}.")

teacher1 = Teacher("Ms.", "Davis", "Math")
print("  Teacher's name (inherited property):")
teacher1.printname() # Inherited method still works
print("  Teacher's subject (new property):")
teacher1.teach()     # New method works


# --- 4. Use the super() Function ---
# The super() function will make the child class inherit all methods and properties from its parent,
# without explicitly using the parent's name. It automatically refers to the parent class.
print("\n4. Using the super() function in Child's __init__:")
class GraduateStudent(Person):
    def __init__(self, fname, lname, student_id, field):
        # Using super() is the preferred way to call the parent's constructor.
        # No need to pass 'self' explicitly with super().
        super().__init__(fname, lname)
        self.student_id = student_id
        self.field_of_study = field
        print(f"    GraduateStudent created: {self.firstname} {self.lastname}, ID: {self.student_id}")

    def display_info(self):
        """Displays inherited and new properties."""
        print(f"  Name: {self.firstname} {self.lastname}, ID: {self.student_id}, Field: {self.field_of_study}")

grad_student = GraduateStudent("Alice", "Wonderland", "G12345", "Computer Science")
grad_student.printname() # Inherited method
grad_student.display_info() # New method displaying all info
