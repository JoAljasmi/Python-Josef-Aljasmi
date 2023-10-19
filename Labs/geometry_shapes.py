import math

# Base class for all shapes
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        try:
            # Attempt to move the shape by dx and dy
            self.x += dx
            self.y += dy
        except TypeError as e:
            # Handle any TypeError that occurs during the translation
            print(f"Please type a number: {e}")

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
    
# Subclass representing a rectangle
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        # Calculate and return the area of the rectangle
        return self.width * self.height

    def perimeter(self):
        # Calculate and return the perimeter of the rectangle
        return 2 * (self.width + self.height)

    def is_inside(self, point_x, point_y):
        # Check if a point is inside the rectangle
        return (
            self.x - self.width / 2 <= point_x <= self.x + self.width / 2 and
            self.y - self.height / 2 <= point_y <= self.y + self.height / 2
        )

    def is_square(self):
        # Check if the rectangle is a square 
        return self.width == self.height

    def __repr__(self):
        # Custom representation for the rectangle object 
        return f'Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})'

    def __str__(self):
        # Custom string representation for the rectangle object 
        return f'Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}'
    

# Subclass representing a circle
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        # Calculate and return the area of the circle
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Calculate and return the perimeter of the circle
        return 2 * math.pi * self.radius

    def is_inside(self, point_x, point_y):
        # Check if a point is inside the circle
        distance = math.sqrt((self.x - point_x) ** 2 + (self.y - point_y) ** 2)
        return distance <= self.radius

    def is_unit_circle(self):
        # Check if the circle is a unit circle 
        return self.radius == 1

    def __repr__(self):
        # Custom representation for the circle object 
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

    def __str__(self):
        # Custom string representation for the circle object 
        return f'Circle at ({self.x}, {self.y}) with radius {self.radius}'

if __name__ == "__main__":
    # Example of how to use the classes
    rectangle = Rectangle(0, 0, 4, 6)
    circle = Circle(0, 0, 3)

    print(rectangle)
    print(f'Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}')
    print(f'Is square: {rectangle.is_square()}')

    print(circle)
    print(f'Area: {circle.area()}, Perimeter: {circle.perimeter()}')
    print(f'Is unit circle: {circle.is_unit_circle()}')