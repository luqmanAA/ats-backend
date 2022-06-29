
from cmath import pi

class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth

    def get_perimeter(self):
        return 2*(self.length+self.breadth)


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi*(self.radius**2)

    def get_perimeter(self):
        return 2*(pi*self.radius)


class Triangle:
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def get_area(self, base, height):
        return 0.5*base*height

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base*self.height

    def get_perimeter(self):
        return 2*(self.base + self.height)


rectangle = Rectangle(length=4, breadth=5)
circle = Circle(radius=7)
triangle = Triangle(a=4, b=5, c=6)
parallelogram = Parallelogram(base=5, height=8)


# print(rectangle.get_area())
# print(rectangle.get_perimeter())

# print(circle.get_area())
# print(circle.get_perimeter())

print(triangle.get_area(4,5))
print(triangle.get_perimeter())

# print(parallelogram.get_area())
# print(parallelogram.get_perimeter())
