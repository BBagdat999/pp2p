# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import os 
    
# # for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
# #     file_name = i + '.txt'
    
# #     file_path = os.path.abspath(os.path.join('lab-6/File_handling', file_name))
    
# #     # Open the file in 'w' mode and write its absolute path to it
# #     with open(file_path, "w") as file:
# #         file.write(file_path)

# for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     file_name = i + '.txt'
    
#     file_path = os.path.abspath(os.path.join('lab-6/File_handling', file_name))
    
#     # Open the file in 'w' mode and write its absolute path to it
#     with open(file_path, "w") as file:
#         file.write(file_path)


A = ord('A')
for i in range(A, A + 26):
    k = chr(i) + ".txt"
    file_name = os.path.join(os.getcwd(), k)
    with open(file_name, 'w') as file:
        file.write(file_name)