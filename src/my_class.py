import math 

class Shape:

    def area(self):
        pass


    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    # def __eq__(self, other):
    #     if not isinstance(other, Rectangle):
    #         return False
    #     return self.length == other.length and self.width == other.width

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return (self.width * 2) + (self.length * 2)
    

class Circle(Shape):

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

class Square(Rectangle):
    
    def __init__(self, length ) -> None:
        super().__init__(length, length)
