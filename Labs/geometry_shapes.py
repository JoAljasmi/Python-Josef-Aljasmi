import math

# Base class for all shapes
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        # Method to move the shape by dx and dy
        self.x += dx
        self.y += dy

    def area(self):
        # Method to calculate the area of the shape 
        pass

    def perimeter(self):
        # Method to calculate the perimeter of the shape 
        pass

    def is_inside(self, point_x, point_y):
        # Method to check if a given point is inside the shape 
        pass

    def __eq__(self, other):
        # Custom equality operator (==) for comparing shapes based on area
        return self.area() == other.area()

    def __lt__(self, other):
        # Custom less than operator (<) for comparing shapes based on area
        return self.area() < other.area()

    def __le__(self, other):
        # Custom less than or equal to operator (<=) for comparing shapes based on area
        return self.area() <= other.area()

    def __gt__(self, other):
        # Custom greater than operator (>) for comparing shapes based on area
        return self.area() > other.area()

    def __ge__(self, other):
        # Custom greater than or equal to operator (>=) for comparing shapes based on area
        return self.area() >= other.area()

    def __repr__(self):
        # Custom representation for the shape object 
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    def __str__(self):
        # Custom string representation for the shape object 
        return f'{self.__class__.__name__} at ({self.x}, {self.y})'