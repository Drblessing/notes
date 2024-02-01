"""
This module covers the tempfile module, which is used to create temporary files and directories.
"""
import tempfile
import os

# Creating a temporary file
with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as temp_file:
    # Write data to the file
    temp_file.write("Some temporary data")

    # Get the file name
    temp_file_name = temp_file.name
    print(f"Temporary file created at {temp_file_name}")

# You can now read from or write to the file outside the 'with' block
with open(temp_file_name, "r") as file:
    data = file.read()
    print(f"Data read from the file: {data}")

# When you're done with the file, you can delete it
os.remove(temp_file_name)
print("Temporary file deleted")

# Creating a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory created at {temp_dir}")
    # You can create files within this directory
    temp_file_path = os.path.join(temp_dir, "example.txt")
    with open(temp_file_path, "w") as file:
        file.write("This is inside the temporary directory")
        print(f"Temporary file created at {temp_file_path}")

    # Read the file
    with open(temp_file_path, "r") as file:
        print(file.read())

# The directory and all its contents are automatically deleted after the 'with' block
print("Temporary directory deleted")
