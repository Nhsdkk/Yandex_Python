class Rectangle:

    def __init__(self, point1, point2):
        self.p1 = (min(point1[0], point2[0]), max(point1[1], point2[1]))
        self.p2 = (max(point1[0], point2[0]), min(point1[1], point2[1]))
        self.dx = abs(point1[0] - point2[0])
        self.dy = abs(point1[1] - point2[1])

    def area(self):
        return round(self.dx * self.dy, 2)

    def perimeter(self):
        return round(2 * (self.dx + self.dy), 2)

    def move(self, dx, dy):
        self.p1 = (self.p1[0] + dx, self.p1[1] + dy)
        self.p2 = (self.p2[0] + dx, self.p2[1] + dy)

    def get_pos(self):
        return round(self.p1[0], 2), round(self.p1[1], 2)

    def resize(self, width, height):
        self.dx = width
        self.dy = height
        self.p2 = (self.p1[0] + width, self.p1[1] - height)

    def get_size(self):
        return round(self.p2[0] - self.p1[0], 2), round(self.p1[1] - self.p2[1], 2)