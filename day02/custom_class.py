import numbers


# in python, we ONLY create CLASS for OBJECT
class Employee:
    is_human = True  # similar to static variable of Java
    planet = 'Earth'

    # now want to create constractor for Employee class
    # every single method need to have self keyword
    # every single variable in Python need to initialize !
    # name ,job_title, salary are instance variable for Employee class

    # no argument constractor
    #     def __init__(self):
    #         self.name = None
    #         self.job_title = None
    #         self.salary = None

    # the issue in here is because we did not define any default argument
    # now are time we need to filled out all the 3 argument otherwise we're going to get error

    #  def __init__(self, name, job_tite, salary):
    #    self.name = name
    #    self.job_title = job_title
    #    self.salary = salary

    # IN Java when we have multiple argument is a MUST to write all the field in parentheses but in Python is
    # optional, but you need to give default value to them
    # SO IN THIS ONE WE HAVE DEFAULT ARGUMENT WITH DATATYPE RESTRICT!
    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):  # this work method is using the instance variable
        print(f'{self.name} is working')

    # __str__()
    # like toString method in java
    # is a return method
    # is overriding
    # __dict__ is like map in java key and value
    # to get the dictionary of this class to get every object of the class

    def __str__(self):  # def keyword is for defining the function because is inside the class is  for defining method
        return f'{type(self).__name__}{self.__dict__}'
    # type(self).__name__ --> is give you the name of class name type will give class '--main--.Employee thats why we
    # add
    # .__name__ so just get a class name;


employee1 = Employee()

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Daniel')

print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

employee3 = Employee('Breanna', 'SDET')

print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

employee4 = Employee('Yulia', 'Python Developer', 150_000)
print(employee4.name)
print(employee4.job_title)
print(employee4.salary)

# print(Employee.name)
print(Employee.is_human)
print(Employee.planet)

employee1.work()  # need to called through object not the class
employee2.work()  # need to called through object not the class
employee3.work()  # need to called through object not the class
employee4.work()  # need to called through object not the class

print(employee1)  #
print(employee2)
print(employee3)
print(employee4)
