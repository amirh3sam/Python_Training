import math
import numbers

from abc import ABC, abstractmethod

# import abc

"""
abc: module name (built in module)
ABC: Abstract class in abc module
abstractmethod: annotations that can be given to abstract methods
"""


class Volume(ABC):

    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):  # by create class Square(shape):  immediately get warning to need to add abstract method in here
    # you can create this class abstract by add ABC -->class Square(Shape , ABC): but you can not create
    # object from this child class
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side  # here you can give different body for the abstract method with pass


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self) -> numbers:
        return math.pow(self.radius) * math.pi


class Rectangle(Shape):

    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self) -> numbers:
        return self.width * self.length


class Cube(Shape, Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass


class Cylinder(Shape, Volume):
    # right click /Generate /implement methods
    def area(self) -> numbers:
        pass

    def volume(self):
        pass


square1 = Square(5)

print(square1)
print(square1.area())
