'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class rectangle():

    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return self.width*2 + self.length*2

my_rect = rectangle(10, 5)
print(my_rect.area(), my_rect.perimeter())

from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.pi = pi

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius

my_circle = Circle(5)
print(my_circle.area(), my_circle.circumference())



