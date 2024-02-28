import re
camel = input()
pattern = re.compile(r'(?<!^)(?=[A-Z])')
snake= re.sub(pattern, '_', camel).lower()
print(snake)