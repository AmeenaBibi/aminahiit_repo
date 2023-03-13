class Rectangle:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def area(self):
        print(f'area = {self.width * self.height}')

    def perimeter(self):
        print(f'perimeter = {2 * (self.width + self.height)}')

    def scale(self, n):
        self.width = float(n * self.width)
        self.height = float(n * self.height)
        print(f'scale = {self.width, self.height}')


rec = Rectangle(10.4, 5)
rec.area()
rec.perimeter()
rec.scale(2)
rec.area()
