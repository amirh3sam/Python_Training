import numbers


# from day02.utility import className


class Shape:  # this is a base class still can create object from it

    def __init__(self):  # this is constractor just set the name
        self.name = type(self).__name__

    def area(self) -> numbers:  # first way to achieve abstraction but is optional (base class abstraction)
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side


# now the area is optional to override it or not override it

square = Square(5)

print(square)
print(square.area())
