class Shape:
    def __init__(self):
        self.area = 0

    def find_area(self):
        return self.area

class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length = length
        self.width = width

    def findAreaOfRectangle(self):
        return self.length * self.width

a = float(input("enter a length: "))
b = float(input("enter a width: "))
r = Rectangle(a, b)
print(f"Area equal to {r.findAreaOfRectangle()} square meters")