def palindrome(word):
    return True if word == word[::-1] else False

print(palindrome(input()))