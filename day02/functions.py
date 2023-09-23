"""

Java Methods:
    public static void method(parameter){

    }


"""
import numbers


# generic type of function used as void or return function
def display_message():  # is not retuning any value
    print('Hello Cydeo')
    print('Hello World')


display_message()


def value():  # this is return function but not permanent return function because you can add the return or not
    return 'Python Programming'


# you can assign it to the variable or pass it in to a print statement
print(value())


# this is not a generic function is for return function and should return int
def return_int() -> int:
    return 10.0


# on above 10.0 is float, but we ask for int if was java we get compile error
# paython give you warning, but it will run the code just tell you ,should be int you provide float
print(return_int())


# def square(num): no data type define in here
#   return num * num
# print(square(10))


def square(num: int):  # we want to make sure num is int
    return num * num


print(square(10))


# print( square('Java'))

# print( divide('C#', 'Python')) # get error because not be able to divide two strings
# ----------------------------------------------------
def add2(num1: int, num2: int):  # this function said had two argument and both should be int
    return num1 + num2


def add3(num1: int, num2: int) -> int:  # this function said had two argument and both should be int and return type
    # should be int too
    return num1 + num2


# --------------------------------------------

# there are "class numbers" that you need to import and called "numbers" you can add any numbers in this function now
def add(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


# you can pass int or float and return you int or float
print(add(10, 20))
print(add(10.5, 20.5))

print('------------------------------------------')


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 20, '+'))

print(calculate(100.5, 2.5, '/'))

print('---------------------------------------------------------')


# example of method overloading

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(10, 20))

print(sum(10, 20, 30))

print(sum(10, 20, 30, 40))


class test:  # method must create in class and has space before def
    def method(self):
        pass


print('----------------------------------------')


# one string and 4 more with any datatype
# just display the concatenation the result
# if we don't give c and d and e ='' empty(SET DEFAULT VALUE) we are going to get error
# so what we do is we give default arg so
# also arg has to give to all of them in order
# for example if you give default arg to third one your getting error on 4 and 5th one


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())


concat('Cydeo', 'School')
concat('Python', 3, 2.5)
concat('Python', 3, 2.5, True)
concat('Python', 3, 2.5, True, False)

"""
1. Declaring
2. parameters
3. restricting parameter' data type
4. setting default value to parameter
5. restricting return type

Dynamic Typing
"""
