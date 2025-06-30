# File: python_file_handling.py
# Topic: Python File Handling

"""
This script demonstrates various operations for handling files in Python,
including creating, reading, updating (appending/overwriting), and deleting files.
It also covers checking for file existence and deleting directories.

Key concepts covered:
-   The open() function with different modes ("r", "a", "w", "x", "t", "b").
-   Reading file content: read(), readline(), and looping through lines.
-   Best practice: Using the 'with' statement for automatic file closing.
-   Writing to files: appending ("a") and overwriting ("w").
-   Creating new files.
-   Deleting files and directories using the 'os' module.
-   Checking for file existence to prevent errors.
"""

import os # Import the os module for file/folder operations


# --- Global file names for demonstrations ---
DEMO_READ_FILE = "demofile_read.txt"
DEMO_WRITE_APPEND_FILE = "demofile_write_append.txt"
DEMO_OVERWRITE_FILE = "demofile_overwrite.txt"
DEMO_CREATE_EXCL_FILE = "demofile_exclusive_create.txt"
DEMO_FOLDER_TO_DELETE = "temp_empty_folder"

# --- Helper function to clean up files/folders before demonstrations ---
def cleanup_demo_files():
    files_to_clean = [
        DEMO_READ_FILE,
        DEMO_WRITE_APPEND_FILE,
        DEMO_OVERWRITE_FILE,
        DEMO_CREATE_EXCL_FILE
    ]
    for file_name in files_to_clean:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"  Cleaned up: {file_name}")
    if os.path.exists(DEMO_FOLDER_TO_DELETE):
        try:
            os.rmdir(DEMO_FOLDER_TO_DELETE)
            print(f"  Cleaned up: {DEMO_FOLDER_TO_DELETE}")
        except OSError as e:
            print(f"  Error cleaning up folder {DEMO_FOLDER_TO_DELETE}: {e}")

cleanup_demo_files() # Run cleanup at the start of the script

# --- Create a sample file for reading demonstrations ---
print("\n--- Setup: Creating a sample file for reading ---")
with open(DEMO_READ_FILE, "w") as f:
    f.write("Hello, this is line 1.\n")
    f.write("This is line 2.\n")
    f.write("And this is the final line, line 3.")
print(f"  Created '{DEMO_READ_FILE}' for reading demos.")

# --- File Open Modes ---
print("\n--- Understanding File Open Modes (r, a, w, x, t, b) ---")
print("  'r' (Read): Default. Opens for reading. Error if file doesn't exist.")
print("  'a' (Append): Opens for appending. Creates file if it doesn't exist.")
print("  'w' (Write): Opens for writing. Creates file if it doesn't exist. OVERWRITES existing content.")
print("  'x' (Create): Creates the specified file. Returns an error if the file exists.")
print("  't' (Text): Default. Text mode (for human-readable text files).")
print("  'b' (Binary): Binary mode (for non-text files like images, executables).")


# --- 1. Opening a File for Reading ('r' or 'rt' - default) ---
print(f"\n1. Opening '{DEMO_READ_FILE}' for reading:")

# Basic open and read (explicit close)
print("  a. Reading entire file content (explicit close):")
f = open(DEMO_READ_FILE, "r") # "r" is default, "rt" is also default
content = f.read()
print(f"    Content:\n'''\n{content}\n'''")
f.close() # Always close files!

# Reading specified number of characters
print("\n  b. Reading only parts of the file (first 10 characters):")
with open(DEMO_READ_FILE, "r") as f:
    part_content = f.read(10)
    print(f"    First 10 characters: '{part_content}'")

# Reading one line at a time
print("\n  c. Reading line by line using readline():")
with open(DEMO_READ_FILE, "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"    Line 1: '{line1.strip()}'") # .strip() removes trailing newline
    print(f"    Line 2: '{line2.strip()}'")

# Looping through lines (most memory efficient for large files)
print("\n  d. Looping through the file line by line (efficient):")
with open(DEMO_READ_FILE, "r") as f:
    for line_num, line in enumerate(f, 1):
        print(f"    Line {line_num}: '{line.strip()}'")


# --- 2. Using the 'with' statement ---
# The 'with' statement ensures the file is properly closed even if errors occur.
print("\n2. Using the 'with' statement (recommended for automatic closing):")
try:
    with open(DEMO_READ_FILE, "r") as f:
        print(f"  Successfully opened '{DEMO_READ_FILE}' with 'with' statement.")
        first_line = f.readline().strip()
        print(f"    Read first line: '{first_line}'")
    print("  File is automatically closed after 'with' block.")
except FileNotFoundError:
    print(f"  Error: '{DEMO_READ_FILE}' not found.")


# --- 3. Writing to an Existing File ---

# a. "a" - Append: will add content to the end of the file. Creates file if it doesn't exist.
print(f"\n3a. Writing to file (Append mode 'a') to '{DEMO_WRITE_APPEND_FILE}':")
# Ensure file exists before appending, or it will be created.
with open(DEMO_WRITE_APPEND_FILE, "w") as f:
    f.write("Initial content for append demo.\n")

with open(DEMO_WRITE_APPEND_FILE, "a") as f:
    f.write("This line is appended.\n")
    f.write("Another line appended.\n")
print(f"  Appended content to '{DEMO_WRITE_APPEND_FILE}'.")
with open(DEMO_WRITE_APPEND_FILE, "r") as f:
    print(f"  Current content of '{DEMO_WRITE_APPEND_FILE}':\n'''\n{f.read().strip()}\n'''")

# b. "w" - Write: will OVERWRITE any existing content. Creates file if it doesn't exist.
print(f"\n3b. Writing to file (Overwrite mode 'w') to '{DEMO_OVERWRITE_FILE}':")
# Create some initial content that will be overwritten
with open(DEMO_OVERWRITE_FILE, "w") as f:
    f.write("This content will be completely overwritten.\n")
    f.write("You will not see this after the next write.\n")
print(f"  Initial content in '{DEMO_OVERWRITE_FILE}'.")

with open(DEMO_OVERWRITE_FILE, "w") as f:
    f.write("New content has completely replaced the old content.\n")
print(f"  Overwritten content in '{DEMO_OVERWRITE_FILE}'.")
with open(DEMO_OVERWRITE_FILE, "r") as f:
    print(f"  Current content of '{DEMO_OVERWRITE_FILE}':\n'''\n{f.read().strip()}\n'''")


# --- 4. Create a New File ---
# "x" - Create: Creates the specified file. Returns an error if the file exists.
# "a" - Append: Creates a file if the specified file does not exists.
# "w" - Write: Creates a file if the specified file does not exists.
print("\n4. Creating New Files:")

print(f"  a. Creating with mode 'x' (exclusive creation): '{DEMO_CREATE_EXCL_FILE}'")
try:
    with open(DEMO_CREATE_EXCL_FILE, "x") as f:
        f.write("This file was created exclusively.")
    print(f"    Successfully created '{DEMO_CREATE_EXCL_FILE}'.")
except FileExistsError:
    print(f"    Error: '{DEMO_CREATE_EXCL_FILE}' already exists (cannot use 'x' mode).")

print(f"  b. Creating with mode 'a' (if not exists): '{DEMO_WRITE_APPEND_FILE}_new_a.txt'")
new_file_a = f"{DEMO_WRITE_APPEND_FILE}_new_a.txt"
if os.path.exists(new_file_a): os.remove(new_file_a) # Clean up if exists from prior runs
with open(new_file_a, "a") as f:
    f.write("This file was created by 'a' mode.\n")
print(f"    '{new_file_a}' created (or appended to) by 'a' mode.")

print(f"  c. Creating with mode 'w' (if not exists): '{DEMO_OVERWRITE_FILE}_new_w.txt'")
new_file_w = f"{DEMO_OVERWRITE_FILE}_new_w.txt"
if os.path.exists(new_file_w): os.remove(new_file_w) # Clean up if exists from prior runs
with open(new_file_w, "w") as f:
    f.write("This file was created by 'w' mode.\n")
print(f"    '{new_file_w}' created (or overwritten) by 'w' mode.")


# --- 5. Deleting a File ---
print("\n5. Deleting Files:")
file_to_delete = "temp_file_to_delete.txt"
with open(file_to_delete, "w") as f:
    f.write("This file will be deleted.")
print(f"  Created '{file_to_delete}' for deletion demo.")

# Check if file exists before deleting
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"  Successfully deleted '{file_to_delete}'.")
else:
    print(f"  Error: '{file_to_delete}' does not exist (cannot delete).")


# --- 6. Deleting a Folder ---
print("\n6. Deleting Folders:")
# Create an empty folder for deletion demo
if not os.path.exists(DEMO_FOLDER_TO_DELETE):
    os.makedirs(DEMO_FOLDER_TO_DELETE)
    print(f"  Created empty folder: '{DEMO_FOLDER_TO_DELETE}' for deletion demo.")

# Delete an empty folder using os.rmdir()
if os.path.exists(DEMO_FOLDER_TO_DELETE):
    try:
        os.rmdir(DEMO_FOLDER_TO_DELETE)
        print(f"  Successfully deleted empty folder: '{DEMO_FOLDER_TO_DELETE}'.")
    except OSError as e:
        print(f"  Error deleting folder '{DEMO_FOLDER_TO_DELETE}': {e}")
else:
    print(f"  Folder '{DEMO_FOLDER_TO_DELETE}' does not exist.")

# Try to delete a non-empty folder (will raise OSError)
non_empty_folder = "temp_non_empty_folder"
if not os.path.exists(non_empty_folder):
    os.makedirs(non_empty_folder)
    with open(os.path.join(non_empty_folder, "file_in_folder.txt"), "w") as f:
        f.write("content")
    print(f"  Created non-empty folder: '{non_empty_folder}'.")
try:
    os.rmdir(non_empty_folder)
    print(f"  Successfully deleted non-empty folder: '{non_empty_folder}'.")
except OSError as e:
    print(f"  Error deleting non-empty folder '{non_empty_folder}': {e}")
    print("  Note: os.rmdir() only deletes EMPTY directories.")
    import shutil
    print("  (Use 'shutil.rmtree(folder_name)' to delete non-empty folders.)")
    shutil.rmtree(non_empty_folder) # Clean up the non-empty folder for next run
    print(f"  Cleaned up non-empty folder: '{non_empty_folder}' using shutil.rmtree.")


# --- Final Cleanup ---
print("\n--- Final Cleanup of all demo files ---")
cleanup_demo_files()

