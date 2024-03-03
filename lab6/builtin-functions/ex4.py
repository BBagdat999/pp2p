import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

input_number = int(input("Enter the number: "))
input_milliseconds = int(input("Enter the number of milliseconds to wait: "))
square_root = calculate_square_root(input_number, input_milliseconds)
print(f"Square root of {input_number} after {input_milliseconds} milliseconds is {square_root}")