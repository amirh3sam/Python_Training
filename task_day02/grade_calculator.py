"""
8. Create a python file named grade calculator, and Write a program for grade calculator:
    8.1. Ask the user "Enter your score"
            If user enters invalid score, terminate the program after displaying the error message "Invalid Entry"

    8.2 Display the grade of the student.
                    90 ~ 100 ==> A
                    80 ~ 89 ==> B
                    70 ~ 79 ==> C
                    60 ~ 69 ==> D
                    0 ~ 59 ==> F
    8.3 Ask the user would you like to continue
            If "yes" --> repeat the previous steps
            If "no" --> print "Thank you for using Cydeo Grade Calculator APP"

            If user enters an invalid entry, ask the user to re-enter until user provides a valid entry

"""

print('-------------------------8.1------------------------')


def Enter_score():
    score = int(input('Enter your score : '))
    while 0 <= score <= 100:
        score = int(input('Enter your score : '))


Enter_score()

print('-------------------------8.2------------------------')


def score_cal():
    score = int(input('Enter your score : '))
    while 0 <= score <= 100:
        if 0 <= score <= 100:

            if score >= 90:
              grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            else:
                grade = 'F'
            print(f"Your grade is: {grade}")
            break
        else:
            print("Invalid Entry: Please enter a score between 0 and 100.")


score_cal()

print('-------------------------8.3------------------------')


def more_request_score():
    while True:
        score = int(input('Enter your score: '))

        if 0 <= score <= 100:
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            else:
                grade = 'F'

            print(f"Your grade is: {grade}")

            answer = input('Would you like to continue (Yes/No)? ')
            if answer.lower() != 'yes':
                break
        else:
            print("Invalid Entry: Please enter a score between 0 and 100.")


more_request_score()