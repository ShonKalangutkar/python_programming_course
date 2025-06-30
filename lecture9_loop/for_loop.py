# File: for_loops.py
# Topic: Python For Loops

"""
This script demonstrates the usage of the 'for' loop in Python,
along with control flow statements like 'break', 'continue',
the 'range()' function, 'else' block, nested loops, and the 'pass' statement.

Key concepts covered:
-   Iterating over sequences (lists, strings, etc.).
-   'break' statement: Exiting the loop prematurely.
-   'continue' statement: Skipping the rest of the current iteration.
-   'range()' function: Generating sequences of numbers for looping a specified number of times.
-   'else' block with 'for': Executing code when the loop finishes normally.
-   Nested loops: Loops inside other loops.
-   'pass' statement: Placeholder for empty loop blocks.
"""


# 1. Basic For Loop (Iterating over a List)
# A 'for' loop is used for iterating over a sequence.
print("\n1. Basic 'for' loop (iterating over a list):")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(f"  Current fruit: {x}")

# 2. Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters.
print("\n2. Looping through a string:")
name = "Python"
for char in name:
    print(f"  Character: {char}")

# 3. The break Statement
# With the 'break' statement, we can stop the loop before it has looped through all the items.
print("\n3. The 'break' statement (exiting early):")
for fruit in fruits:
    print(f"  Checking fruit: {fruit}")
    if fruit == "banana":
        print("    Breaking loop because we found 'banana'!")
        break # Exit the loop immediately
print("  Loop finished (due to break).")

# 4. The continue Statement
# With the 'continue' statement, we can stop the current iteration of the loop,
# and continue with the next.
print("\n4. The 'continue' statement (skipping current iteration):")
for fruit in fruits:
    if fruit == "banana":
        print(f"  Skipping 'banana' (continue).")
        continue # Skip the rest of this iteration, go to the next item
    print(f"  Processing fruit: {fruit}") # 'banana' will not be printed here
print("  Loop finished (after continue example).")

# 5. The range() Function
# Used to loop through a set of code a specified number of times.
# It returns a sequence of numbers.

# Default range(stop): Starts from 0, increments by 1, ends before 'stop'.
print("\n5.1. range(stop):")
for i in range(5): # This will loop for i = 0, 1, 2, 3, 4
    print(f"  Range (default): {i}")

# range(start, stop): Specifies a starting value.
print("\n5.2. range(start, stop):")
for i in range(2, 7): # This will loop for i = 2, 3, 4, 5, 6
    print(f"  Range (start, stop): {i}")

# range(start, stop, step): Specifies the increment value.
print("\n5.3. range(start, stop, step):")
for i in range(0, 10, 2): # This will loop for i = 0, 2, 4, 6, 8
    print(f"  Range (start, stop, step): {i}")

for i in range(10, 0, -1): # Counting backwards
    print(f"  Range (counting backwards): {i}")

# 6. Else in For Loop
# The 'else' keyword in a 'for' loop specifies a block of code to be executed
# when the loop is finished normally (i.e., without a 'break' statement).
print("\n6. 'else' in 'for' loop:")
for i in range(3):
    print(f"  Looping normally: {i}")
else: # This 'else' block will execute
    print("  'else' block: Loop finished without a 'break'.")

print("\n7. 'else' block not executed if 'break' is used:")
for i in range(5):
    print(f"  Checking 'break' condition: {i}")
    if i == 2:
        print("    Breaking loop, 'else' will NOT execute.")
        break
else: # This 'else' block will NOT execute
    print("  'else' block: This message will NOT print.")
print("  Loop finished (due to break, so else was skipped).")


# 8. Nested Loops
# A nested loop is a loop inside another loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop".
print("\n8. Nested Loops:")
adj = ["red", "big", "tasty"]
fruits_nested = ["apple", "banana", "cherry"]

for adjective in adj: # Outer loop
    for fruit_item in fruits_nested: # Inner loop
        print(f"  {adjective} {fruit_item}")
# Expected output: "red apple", "red banana", "red cherry", etc.

# 9. The pass Statement
# 'for' loops cannot be empty. If you have a 'for' loop with no content,
# put in the 'pass' statement to avoid getting an error.
print("\n9. The 'pass' Statement (for empty blocks):")
for item in []:
    pass # This loop does nothing, but 'pass' makes it syntactically valid.
print("  'pass' statement allows for empty 'for' loop blocks without errors.")
