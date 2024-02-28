import re
x = input()
pattern = re.compile(r'(?<=[a-z])([A-Z])')
space = re.sub(pattern, r' \1', x)
print(space)

