
from cmath import pi
import logging


class Shapes:

    def __init__(self, length) -> None:
        self.length = length

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class TwoDimension(Shapes):

    def __init__(self,length) -> None:
        super().__init__(length)

    

class ThreeDimension(Shapes):

    def __init__(self, length) -> None:
        super().__init__(length)


class Circle(TwoDimension):

    def __init__(self, length) -> None:
        super().__init__(length)
        self.radius = length
        
    def get_area(self):
        return pi*self.radius**2
    
    def get_perimeter(self):
        return 2*pi*self.radius


class Square(TwoDimension):

    def __init__(self, length) -> None:
        super().__init__(length)

    def get_area(self):
        return self.length**2
    
    def get_perimeter(self):
        return self.length * 4

class Triangle(TwoDimension):

    def __init__(self, length, b, c) -> None:
        super().__init__(length)
        self.side_a = length
        self.side_b = b
        self.side_c = c

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        semi_perimeter = self.get_perimeter()/2
        side_diff_1 = semi_perimeter - self.side_a
        side_diff_2 = semi_perimeter - self.side_b
        side_diff_3 = semi_perimeter - self.side_c
        return (semi_perimeter*(side_diff_1)*(side_diff_2)*(side_diff_3))**0.5 


class Sphere(ThreeDimension):

    def __init__(self, length) -> None:
        super().__init__(length)
        self.radius = length
    
    def get_area(self):
        return 4*pi*self.radius**2
    
    def get_volume(self):
        return (4/3)*2*pi*self.radius**3


class Cube(ThreeDimension):

    def __init__(self, length) -> None:
        super().__init__(length)

    def get_lateral_area(self):
        return 4 * self.length**2

    def get_total_area(self):
        return 6 * self.length**2

    def get_perimeter(self):
        return 12*self.length
    
    def get_volume(self):
        return self.length**3


class Tetrahedron(ThreeDimension):

    def __init__(self, length) -> None:
        super().__init__(length)

    def get_lateral_area(self):
        return 3*(3**0.5)/(4 * self.length**2)

    def get_total_area(self):
        return (3**0.5)*self.length**2

    def get_perimeter(self):
        return 6*self.length
    
    def get_volume(self):
        return ((2**0.5)/12)*self.length**3



circle = Circle(7)
square = Square(7)
triangle = Triangle(4,5,6)
cube = Cube(8)
tetra = Tetrahedron(4)

# print(circle.get_area())
# print(circle.get_perimeter())

# print(square.get_perimeter())

# print(triangle.get_perimeter())
# print(triangle.get_area())

# print(cube.get_total_area())

# print(tetra.get_total_area())


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Settingto %r' % (key, value))
        super().__setitem__(key, value)