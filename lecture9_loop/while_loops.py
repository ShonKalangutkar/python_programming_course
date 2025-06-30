# File: while_loops.py
# Topic: Python While Loops

"""
This script demonstrates the usage of the 'while' loop in Python,
along with control flow statements like 'break', 'continue', and the 'else' block.

Key concepts covered:
-   Basic 'while' loop syntax and execution.
-   Importance of incrementing (or changing) the loop condition to avoid infinite loops.
-   'break' statement: Exiting the loop prematurely.
-   'continue' statement: Skipping the rest of the current iteration.
-   'else' block with 'while': Executing code when the loop condition becomes false (normal termination).
"""


# 1. The Basic While Loop
# Executes a set of statements as long as a condition is true.
# Remember to increment the controlling variable, or the loop will continue forever.
print("\n1. Basic 'while' loop:")
i = 1
while i < 5:
    print(f"  Current value of i: {i}")
    i += 1 # Increment i to eventually make the condition false
print("  Loop finished (i is no longer < 5).")


# 2. The break Statement
# With the 'break' statement, we can stop the loop even if the 'while' condition is true.
print("\n2. The 'break' statement (exiting early):")
j = 1
while j < 6:
    print(f"  Checking j: {j}")
    if j == 3:
        print("    Breaking loop because j is 3!")
        break # Exit the loop immediately
    j += 1
print("  Loop finished (due to break).")


# 3. The continue Statement
# With the 'continue' statement, we can stop the current iteration,
# and continue with the next iteration.
print("\n3. The 'continue' statement (skipping current iteration):")
k = 0
while k < 5:
    k += 1 # Increment first, so the condition is handled correctly for next iteration
    if k == 3:
        print(f"  Skipping iteration for k = {k} (continue).")
        continue # Skip the rest of this iteration, go to the next check
    print(f"  Processing k: {k}")
print("  Loop finished (after continue example).")


# 4. The else Statement with While Loop
# With the 'else' statement, we can run a block of code once when
# the condition no longer is true (i.e., the loop completed without a 'break').
print("\n4. The 'else' statement with 'while' loop:")
l = 0
while l < 3:
    print(f"  Looping, l is: {l}")
    l += 1
else: # This 'else' block executes because the loop finished normally
    print(f"  'else' block: l is no longer less than 3 (l={l}). Loop completed normally.")

print("\n5. 'else' block not executed if 'break' is used:")
m = 0
while m < 5:
    print(f"  Looping with potential break, m is: {m}")
    if m == 2:
        print("    Breaking loop, so 'else' will NOT execute.")
        break
    m += 1
else: # This 'else' block will NOT execute
    print(f"  'else' block: This message will NOT print.")
print("  Loop finished (due to break, so else was skipped).")
