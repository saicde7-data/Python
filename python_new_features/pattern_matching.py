from typing import Union

# Define a simple class hierarchy
class Circle:
    def __init__(self, radius):
        self.radius = radius

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

# Function using pattern matching
def area(shape: Union[Circle, Square]) -> float:
    match shape:
        case Circle(radius=radius):
            return 3.14 * radius ** 2
        case Square(side_length=side_length):
            return side_length ** 2
        case _:
            raise ValueError("Unsupported shape")

# Example usage
circle = Circle(radius=5)
square = Square(side_length=4)

print(f"Area of circle: {area(circle)}")
print(f"Area of square: {area(square)}")

# Output
# Area of circle: 78.5
# Area of square: 16