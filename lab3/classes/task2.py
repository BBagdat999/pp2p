class Shape:
    def __init__(self):
        self.area = 0
    
    def find_area(self):
        return self.area
    
class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
        self.area = self.length ** 2

s = Square(float(input('enter a length: ')))
print(f"Area equal to {s.find_area()} square meters")

