class Rectangle:
    def __init__(self, point1, point2):
        self.p1 = (min(point1[0], point2[0]), max(point1[1], point2[1]))
        self.p2 = (max(point1[0], point2[0]), min(point1[1], point2[1]))
        self.dx = abs(point1[0] - point2[0])
        self.dy = abs(point1[1] - point2[1])
        self.center = (self.p1[0] + self.dx / 2, self.p1[1] - self.dy / 2)

    def area(self):
        return round(self.dx * self.dy, 2)

    def perimeter(self):
        return round(2 * (self.dx + self.dy), 2)

    def move(self, dx, dy):
        self.p1 = (self.p1[0] + dx, self.p1[1] + dy)
        self.p2 = (self.p2[0] + dx, self.p2[1] + dy)
        self.center = (self.center[0] + dx, self.center[1] + dy)

    def get_pos(self):
        return round(self.p1[0], 2), round(self.p1[1], 2)

    def resize(self, width, height):
        self.dx = width
        self.dy = height
        self.center = (self.p1[0] + self.dx / 2, self.p1[1] - self.dy / 2)
        self.p2 = (self.p1[0] + width, self.p1[1] - height)

    def scale(self, factor):
        self.p1 = (self.p1[0] - (factor - 1) * self.dx / 2, self.p1[1] + (factor - 1) * self.dy / 2)
        self.p2 = (self.p2[0] + (factor - 1) * self.dx / 2, self.p2[1] - (factor - 1) * self.dy / 2)
        self.dx *= factor
        self.dy *= factor

    def get_size(self):
        return round(self.p2[0] - self.p1[0], 2), round(self.p1[1] - self.p2[1], 2)

    def turn(self):
        self.dx , self.dy = self.dy, self.dx
        self.p1 = (self.center[0] - self.dx / 2, self.center[1] - self.dy / 2)
        self.p2 = (self.p1[0] + self.dx, self.p1[1] - self.dy)


# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.scale(2.0)
# print(rect.get_pos(), rect.get_size(), sep='\n')

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')