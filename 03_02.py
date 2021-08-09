class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def rectangle_area(self):
        return self.base * self.height


new_rectangle = Rectangle(12, 10)
print("Area:", new_rectangle.rectangle_area())
new_rectangle.base = 5
print("New area:", new_rectangle.rectangle_area())
