class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r * 2 * 3.14


class Square:

    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s ** 2


c = Circle(2)
s = Square(3)

for shape in (c,s):
    print(shape.area())

