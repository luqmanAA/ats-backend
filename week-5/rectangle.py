
class Rectangle:

    def __init__(self, length = 1, width = 1) -> None:
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def _length(self, value):
        print("Setiing")
        if value < 0.0 or value > 20.0:
            raise ValueError("Length can only be between 0.1 and 20.0")
        self.__length = value

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def _width(self, value):
        if value < 0.0 or value > 20.0:
            raise ValueError("Width can only be between 0.1 and 20.0")
        self.__width = value

    def get_perimeter(self):
        '''
            Prints the perimeter of the rectangle class
        '''
        return 2*(self.length+self.width)

    def get_area(self):
        '''
            Prints the area of the rectangle class
        '''
        return self.length * self.width
    
rec = Rectangle(4,5)

print(rec.get_perimeter())