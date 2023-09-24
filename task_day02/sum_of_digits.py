"""

6.Create a python file named sum_of_digits, Write a program that can return the sum of digits from a  string
             Ex:
                 input: A1B2C3

                 output: 6
"""

def sum_of_digits(string : str):
    number_of_digits = 0
    for char in string:
        if char.isdigit():
            number_of_digits += int(char)

    return number_of_digits


print(sum_of_digits('S4A2F9'))