"""

3. Create a python file named sum_of_even_odd:
        3.1 Write a program that can return the sum of even numbers between 1 to 100

        3.2 Write a program that can return the sum of odd numbers between 1 to 100

        3.3 write a program that can calculate the sum of all numbers between 1 to any given number
            ex:
                input: 100
                output: 5050

                input: 50
                output: 1275
"""

print('------------------3.1------------------------')


def sum_even_number() -> int:
    result = 0

    for i in range(1, 101):
        if i % 2 == 0:
            result += i
    return result


print(sum_even_number())

print('------------------3.2------------------------')


def sum_odd_number() -> int:
    result = 0

    for i in range(1, 101):
        if i % 2 != 0:
            result += i
    return result


print(sum_odd_number())

print('------------------3.3------------------------')


def sum_any_number(number: int):
    result = 0
    for i in range(1, number + 1):
        result += i
    return result


print(sum_any_number(50))
