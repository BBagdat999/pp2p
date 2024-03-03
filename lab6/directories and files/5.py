# Write a Python program to write a list to a file.

my_list = ["apple", "banana", "orange", "kiwi"]

file_path = input("Enter a name for the file: ")

with open(file_path, "w") as file:
    for item in my_list:
        file.write(item + "\n")

print("List has been written to the file:", file_path)
