"""
2. Create a python file named numbers, Write a program that asks user to enter
number for 5 times, and print how many positive and negative numbers user entered
            Ex:
                Inputs:
                    10
                    20
                    -1
                    0
                    3

                Output:
                    3 positive and 1 negative

"""


def numberOfPositiveAndNegative():
    positive_number = 0
    negative_number = 0

    print('Please Enter 5 number ')
    for i in range(0, 5):
        user_number = int(input('Enter your number : '))
        if user_number > 0:
            positive_number += 1
        elif user_number < 0:
            negative_number += 1

    print(f'{positive_number} positive and {negative_number} negative')


numberOfPositiveAndNegative()
