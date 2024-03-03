# Write a Python program with builtin function to multiply all the numbers in a list

from functools import reduce
from operator import mul

def multiply(numbers):
    result = reduce(mul, numbers)
    return result

num_list = map(int, input("Enter numbers separated by spaces: ").split())

result = multiply(num_list)

print("Result:", result)
