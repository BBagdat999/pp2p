import re
pattern = '\b[a-z]+_[a-z]+\b'
x = input()
matches = re.findall(pattern, x)
print(x)