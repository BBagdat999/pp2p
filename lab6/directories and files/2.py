# Write a Python program to check for access to a specified path.
# Test the existence, readability, writability and executability of the specified path

import os

path = input()

if os.path.exists(path):
    print("Path exists.")
else:
    print("Path does not exist!")

if os.access(path, os.R_OK):
    print("File is readable.")
else:
    print("File is not readable.")

if os.access(path, os.W_OK):
    print("File is writable.")
else:
    print("File is not writable.")

if os.access(path, os.X_OK):
    print("File is executable.")
else:
    print("File is not executable.")