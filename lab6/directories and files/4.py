# Write a Python program to count the number of lines in a text file.

import os

file_path = input("Enter the path to the text file: ")

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
else:
    with open(file_path, 'r') as file:
        line_count = 0
        
        for line in file:
            line_count += 1
        
        print(f"Number of lines in {file_path}: {line_count}")
