import re
x = input()
pattern = '[A-Z][^A-Z]*'
split_strings = re.findall(pattern, x)
print(' '.join(split_strings))
