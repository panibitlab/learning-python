class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle with width: {self.width} & height: {self.height}"

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.perimeter() > other.perimeter()

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)


def reducer(rectangle):
    return rectangle.perimeter() * 0.1


