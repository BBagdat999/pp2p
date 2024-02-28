import re
snake = input()
pattern = re.compile(r'(_\w)')
camel = re.sub(pattern, lambda x: x.group(1)[1:].upper(), snake)
print(camel)
