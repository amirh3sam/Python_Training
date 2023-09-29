from typing import final  # to create final variable , method, class first you need to import this "typing"-> that has

# final
# make variable unchangeable and method not be able to override and class not be able to do inheritance
# and recommended to do give type final  --> pi: final =3.14  but if you reassign it will accept because is  a dynamic
# typing
pi: final = 3.14

pi = 3.5   # here show you warning but still will print


# if you want to create the class final use @final
@final
class Animal:
    pass


class Dog(Animal):   # here is give you warning because animal is final can not have subclass from it
    pass


class Employee:

    @final
    def work(self):
        print('Working')


class Driver(Employee):

    def work(self): # here try to do override manauly and you get this warning because implementation (` print(# 'Working')
#)should never change
        print('Driving')


class Person:

    def __init__(self, age: int):
        self.__age = age

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, value):
        raise RuntimeError(f' age is constant, can not be changed')


person1 = Person(10)

print(person1.person_age)

# person1.person_age = 100

print(person1.person_age)

print(person1.__age)
