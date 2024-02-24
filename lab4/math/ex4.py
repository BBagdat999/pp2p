def parallelogram_area(base, height):
    return base * height

base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = parallelogram_area(base_length, height)

print("Expected Output:", area)
