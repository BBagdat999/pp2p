import re
pattern = 'ab*'
x = input()
if re.fullmatch(pattern, x):
    print(x)
