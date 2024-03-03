# Write a Python program to copy the contents of a file to another file

import os

file_name = input("Enter the file name: ")

file_path = os.path.abspath(file_name)
if os.path.exists(file_path):
    print(f"{file_path} does not exist.")
    exit()

if os.access(file_path, os.W_OK):
    print(f"You do not have permission to delete {file_path}.")
    exit()
    
os.remove(file_path)
print(f"{file_path} has been deleted.")
