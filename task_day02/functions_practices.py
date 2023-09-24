"""


1.Create a python file named functions_practices:
    1.1 Create a function that can check if a person is eligible to vote
                Ex:
                    eligibleToVote(19, "USA");

                output:
                    You are not eligible to vote!

    1.2 Create a function that can calculate the grade of the student based on the score

    1.3 Create a function that can if the given integer is positive, negative or zero

    1.4 Create a function that can check if a string is palindrome, the function
    should return true if the given string is palindrome.
"""

print('-------------------1.1---------------------')


def eligibleToVote(age: int, country: str):
    eligible = 'You are eligible to vote!'
    not_eligible = 'You are not eligible to vote!'
    if age >= 21 and country == 'USA':
        return eligible
    else:
        return not_eligible


print(eligibleToVote(19, 'USA'))
print('--------------------1.2------------')


def calculateGrade(grade: 'str') -> str:
    result = ""
    if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "F":
        if grade == "A":
            result += 'your score is between 90 to 100'
        elif grade == "B":
            result += 'your score is between 80 to 89'
        elif grade == "C":
            result += 'your score is between 70 to 79'
        elif grade == "D":
            result += 'your score is between 60 to 69'
        else:
            result += " You are Failed"


    else:
        result += "Invalid"
    return result


print(calculateGrade('D'))
print('--------------------1.3------------')


def positiveNegativeZero(number: int) -> str:
    result = ""
    if number > 0:
        result += 'your number is positive'
    elif number < 0:
        result += 'your number is negative'
    else:
        result += 'your number is zero'
    return result


print(positiveNegativeZero(0))

print('---------------1.4---------------------')


def is_palindrome(string: str):
    reversed = string[::-1]
    if reversed == string:
        return True
    else:
        return False


print(is_palindrome('radar'))
