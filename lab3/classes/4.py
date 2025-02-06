import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


p1 = Point(0, 0)
p2 = Point(3, 4)

print("Point 1:", p1.show())
print("Point 2:", p2.show())
print("Distance:", p1.dist(p2))

p1.move(5, 5)
print("Point 1 after moving:", p1.show())