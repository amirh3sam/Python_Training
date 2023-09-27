class Person:

    def __init__(self, name: str = 'Unknown', age: int = 1):   # so here we give default value to name and age so if
        # you want to just give a name or just the age still will work
        self.__name = None  # name now has private access modifier default argument
        self.__age = None
        self.set_name(name)  # add setter inside the constractor, so we can set directly when create a object
        self.set_age(age)

    # now we're creating getter with condition
    def get_name(self) -> str:  # -> str because want to make sure must have a return method
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}') # manually will throw exception " rise
            # keyword" is like throw in Java

        return self.__name

    def set_name(self, name: str): # now we can to give condition to setter
        if type(name) != str:
            raise RuntimeError(f'Person name must be string')

        if name == '':
            raise RuntimeError(f'Person name can not be empty')

        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age):

        if age < 0 or age > 150:
            raise RuntimeError(f'Inavlid age {age}')
        self.__age = age

    def __str__(self): # this is like toString method in Java so if wana print the whole object print(person1)
        return f'{type(self).__name__}{str(self.__dict__).replace("_Person__", "")}'


person1 = Person()
# we try to access to name like person1.name() you will get error because we are outside of class that why we use
# get_name()
print(person1.get_name())
print(person1.get_age())

person2 = Person('James')

print(person2.get_name())
print(person2.get_age())

person3 = Person('Hazel', 27)  # now the setter check to make sure is pass the condition
# in Java, you can over loading constractor but in java can be only one constructor but if you want to have optional
# inside the (       ) you need to define the default value in constractor
print(person3.get_name())
print(person3.get_age())

print('------------------')

print(person1)
print(person2)
print(person3)
