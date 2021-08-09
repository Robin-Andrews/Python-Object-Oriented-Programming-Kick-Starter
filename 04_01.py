class Rectangle:
    def __init__(self, base, height):
        self._base = base
        self._height = height

    def rectangle_area(self):
        return self._base * self._height


new_rectangle = Rectangle(12, 10)
print("Area:", new_rectangle.rectangle_area())
