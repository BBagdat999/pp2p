import re
pattern = 'ab{2, 3}'
x = input()
if re.fullmatch(pattern, x):
    print(x)
