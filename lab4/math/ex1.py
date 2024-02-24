import math

def degree_to_radian(deg):
    return deg * (math.pi / 180)

degree = float(input("Input degree: "))

radian = degree_to_radian(degree)

print("Output radian:", radian)