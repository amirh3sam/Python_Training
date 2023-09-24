"""

4. Create a python file named factorial_number, Write a program that can return the factorial number of any given number

            Ex:
                input: 5
                output: 120

                    ( because: 5! = 5 * 4 * 3 * 2* 1 = 120 )

"""
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


print(factorial(5))