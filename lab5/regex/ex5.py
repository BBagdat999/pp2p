import re
pattern = 'a.*b$'
x = input()
matches = re.findall(pattern, x)
print(x)