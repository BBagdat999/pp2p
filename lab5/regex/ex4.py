import re
pattern = '\b[A-Z][a-z]+\b'
x = input()
matches = re.findall(pattern, x)
print(x)
