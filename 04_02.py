class Rectangle:
    def __init__(self, base, height):
        self._base = base
        self._height = height

    def get_base(self):
        return self._base

    def set_base(self, base):
        self._base = base

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def rectangle_area(self):
        return self._base * self._height


my_rectangle = Rectangle(12, 10)
print("Area:", my_rectangle.rectangle_area())

print(my_rectangle.get_base())
my_rectangle.set_base(5)
print(my_rectangle.get_base())

print(my_rectangle.get_height())
my_rectangle.set_height(3)
print(my_rectangle.get_height())

print("New area:", my_rectangle.rectangle_area())  # Expect 15
