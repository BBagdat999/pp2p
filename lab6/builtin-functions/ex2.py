# Write a Python program with builtin function that accepts a string and calculate the 
# number of upper case letters and lower case letters

def counter(string):
    cnt_up = sum(1 for char in string if char.isupper())
    cnt_low = sum(1 for char in string if char.islower())
    return cnt_up, cnt_low

st = input("Enter a string: ")
cnt_up, cnt_low = counter(st)

print(f"there are {cnt_up} uppercase letters and {cnt_low} lower case letters")