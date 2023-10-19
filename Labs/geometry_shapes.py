import math

class Shape:
    """
    Base class for geometric shapes.

    Attributes:
        x (float): X-coordinate of the shape's center.
        y (float): Y-coordinate of the shape's center.
    """

    def __init__(self, x, y):
        """
        Initialize a shape with its center at (x, y).

        Args:
            x (float): X-coordinate of the shape's center.
            y (float): Y-coordinate of the shape's center.
        """
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        """
        Translate the shape by the specified amount.

        Args:
            dx (float): The amount to move the shape in the x-direction.
            dy (float): The amount to move the shape in the y-direction.

        Raises:
            TypeError: If dx or dy are not numeric values.
        """
        try:
            self.x += dx
            self.y += dy
        except TypeError as e:
            print(f"Translation error: {e}")

    def area(self):
        """
        Calculate and return the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass

    def is_inside(self, point_x, point_y):
        """
        Check if a given point is inside the shape.

        Args:
            point_x (float): X-coordinate of the point to check.
            point_y (float): Y-coordinate of the point to check.

        Returns:
            bool: True if the point is inside the shape, False otherwise.
        """
        pass

    def __eq__(self, other):
        """
        Custom equality operator for comparing shapes based on area.

        Args:
            other (Shape): Another shape object.

        Returns:
            bool: True if the areas of the two shapes are equal, False otherwise.
        """
        return self.area() == other.area()

    def __lt__(self, other):
        """
        Custom less than operator for comparing shapes based on area.

        Args:
            other (Shape): Another shape object.

        Returns:
            bool: True if the area of the current shape is less than the area of the other shape.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Custom less than or equal to operator for comparing shapes based on area.

        Args:
            other (Shape): Another shape object.

        Returns:
            bool: True if the area of the current shape is less than or equal to the area of the other shape.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Custom greater than operator for comparing shapes based on area.

        Args:
            other (Shape): Another shape object.

        Returns:
            bool: True if the area of the current shape is greater than the area of the other shape.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Custom greater than or equal to operator for comparing shapes based on area.

        Args:
            other (Shape): Another shape object.

        Returns:
            bool: True if the area of the current shape is greater than or equal to the area of the other shape.
        """
        return self.area() >= other.area()

    def __repr__(self):
        """
        Custom representation for the shape object (used for debugging).

        Returns:
            str: A string representation of the shape object.
        """
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    def __str__(self):
        """
        Custom string representation for the shape object (used for printing).

        Returns:
            str: A user-friendly string representation of the shape object.
        """
        return f'{self.__class__.__name__} at ({self.x}, {self.y})'


class Rectangle(Shape):
    """
    Subclass representing a rectangle.

    Attributes:
        width (float): Width of the rectangle.
        height (float): Height of the rectangle.
    """

    def __init__(self, x, y, width, height):
        """
        Initialize a rectangle with its center at (x, y), width, and height.

        Args:
            x (float): X-coordinate of the center of the rectangle.
            y (float): Y-coordinate of the center of the rectangle.
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def is_inside(self, point_x, point_y):
        """
        Check if a point is inside the rectangle.

        Args:
            point_x (float): X-coordinate of the point to check.
            point_y (float): Y-coordinate of the point to check.

        Returns:
            bool: True if the point is inside the rectangle, False otherwise.
        """
        return (
            self.x - self.width / 2 <= point_x <= self.x + self.width / 2 and
            self.y - self.height / 2 <= point_y <= self.y + self.height / 2
        )

    def is_square(self):
        """
        Check if the rectangle is a square (width equals height).

        Returns:
            bool: True if the rectangle is a square, False otherwise.
        """
        return self.width == self.height

    def __repr__(self):
        """
        Custom representation for the rectangle object (used for debugging).

        Returns:
            str: A string representation of the rectangle object.
        """
        return f'Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})'

    def __str__(self):
        """
        Custom string representation for the rectangle object (used for printing).

        Returns:
            str: A user-friendly string representation of the rectangle object.
        """
        return f'Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}'


class Circle(Shape):
    """
    Subclass representing a circle.

    Attributes:
        radius (float): Radius of the circle.
    """

    def __init__(self, x, y, radius):
        """
        Initialize a circle with its center at (x, y) and a given radius.

        Args:
            x (float): X-coordinate of the center of the circle.
            y (float): Y-coordinate of the center of the circle.
            radius (float): Radius of the circle.
        """
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate and return the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def is_inside(self, point_x, point_y):
        """
        Check if a point is inside the circle.

        Args:
            point_x (float): X-coordinate of the point to check.
            point_y (float): Y-coordinate of the point to check.

        Returns:
            bool: True if the point is inside the circle, False otherwise.
        """
        distance = math.sqrt((self.x - point_x) ** 2 + (self.y - point_y) ** 2)
        return distance <= self.radius

    def is_unit_circle(self):
        """
        Check if the circle is a unit circle (radius equals 1).

        Returns:
            bool: True if the circle is a unit circle, False otherwise.
        """
        return self.radius == 1

    def __repr__(self):
        """
        Custom representation for the circle object (used for debugging).

        Returns:
            str: A string representation of the circle object.
        """
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

    def __str__(self):
        """
        Custom string representation for the circle object (used for printing).

        Returns:
            str: A user-friendly string representation of the circle object.
        """
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