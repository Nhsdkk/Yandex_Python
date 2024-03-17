class Rectangle:
    def __init__(self, point1, point2):
        self.dx = abs(point1[0] - point2[0])
        self.dy = abs(point1[1] - point2[1])

    def area(self):
        return round(self.dx * self.dy, 2)

    def perimeter(self):
        return round(2 * (self.dx + self.dy), 2)
