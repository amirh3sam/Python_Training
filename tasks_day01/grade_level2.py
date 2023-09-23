"""


14. Create a python file named grade_level2.  write a program that asks user to enter the grade level number,  determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

                    For Any Other grade: Invalid grade level given

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT

"""

grade_level = int(input("Enter your Grade level : "))
result = ""

if 1 <= grade_level <= 18:

    if 1 <= grade_level <= 5:
        result += "Elementary School"
    elif 6 <= grade_level <= 8:
        result += "Middle School"
    elif 9 <= grade_level <= 12:
        result += "High School"
    elif 13 <= grade_level <= 16:
        result += "College"
    else:
        result += "Grad School"

else:
    result = "Invalid grade level"

print(result)
