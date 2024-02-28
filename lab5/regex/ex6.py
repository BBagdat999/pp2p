import re
text = input()
pattern = '[ ,.]'
replaced_text = re.sub(pattern, ':', text)
print(replaced_text)    