from math import sqrt

class Shape:
    def describe(self):
        return "I am a shape."

class Polygon(Shape):
    def __init__(self, *sides):
        self.sides = sides

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calculate_area(self):
         s = (self.a + self.b + self.c) / 2
         S = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
         return S

triangle = Triangle(3, 4, 5)
print(triangle.calculate_area())
print(triangle.describe())