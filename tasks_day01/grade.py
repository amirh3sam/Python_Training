"""




18. Create a python file named grade, a variable named grade is given. write a program to print the following messages:
            'A': excellent
            'B': great job
            'C': good
            'D': passed
            'F': failed
            otherwise: invalid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT

"""


grade = "A"
result = ""

if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "F":
    if grade == "A":
        result += "excellent"
    elif grade == "B":
        result += "greate job"
    elif grade == "C":
        result += "good"
    elif grade == "D":
        result += "Passed"
    else:
        result += "Failed"


else:
    result += "Invalid"

print(result)