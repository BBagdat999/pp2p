class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y, sep = ", ")
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    
    def dist(self, p):
        return ((self.x - p.x) ** 2 + ((self.y - p.y) ** 2)) * (0.5)
    
p1 = Point(3, 4)
p1.show()
p1.move(5, 6)
p1.show()
p1.move(1, 2)

center = Point(0, 0)
print(f"distance between 2 points = {p1.dist(center)}")
p1.show()