# Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path.

import os

path = input()
if os.path.exists(path):
    print("Basename: " + os.path.basename(path) + '\n' + "Dirname: " + os.path.dirname(path))
else:
    print("Path does not exist.")