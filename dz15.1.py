import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_square = self.get_square() + other.get_square()
            return self._create_rectangle_with_area(new_square)
        raise ValueError("Can only add another Rectangle")

    def __mul__(self, n):
        if isinstance(n, (int, float)) and n > 0:
            new_square = self.get_square() * n
            return self._create_rectangle_with_area(new_square)
        raise ValueError("Can only multiply by a positive number")

    def _create_rectangle_with_area(self, area):
        # Залишимо ширину такою ж, а висоту обчислимо
        new_width = self.width
        new_height = area / new_width
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"

# Тестування
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("All tests passed!")
