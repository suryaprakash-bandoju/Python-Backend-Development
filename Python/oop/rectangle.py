class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

r1 = Rectangle(5, 10)
print(r1.area())  # 50
print(r1.perimeter())  # 30
print(r1.is_square())  # False
print(r1)  # Rectangle(5x10)

r1.resize(5, 5)
print(r1.is_square())  # True
print(r1)  # Rectangle(5x5)

# These should raise errors:
# r2 = Rectangle(-5, 10)
# r3 = Rectangle(5, 0)
# r1.resize(0, 5)
