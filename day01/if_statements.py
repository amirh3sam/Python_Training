
"""
if statement Decision-Making
1- Single-if
2- if-Else
3- Multi Branch of
4- Nested if

 in Paython no more {} only space(Tab) before statements
 write if then the Condition then semi-column then next line give a space and then your statement
if condition:
    Statements
    # is better to use Tab because if you use one space and later on you gonna have multi if inside each need to
    count the number of space so use one tab then start write your statement
# any time you did not know your statement, and later you want to write it in you can use pass keyword
if condition:
    pass
    # so in this case your if statement is not going to get any error and also later you can add your statement
"""


if True:
    pass


# the first print statement with print if condiont is ture but second one because this is not space is not inside the if
# block
# if True:
#   print ('Python Programming')
#print ('Python Programming') by removing the space we get out of the block

if False:
    print('Python Programming')

print('Java Programming')

print('------------------------------------')

score = 70

if score >= 60:
    print('Congrats! you passed the exam')

"""
if(true){
}

"""
# also you can yous logical operator in condition as long as at the end you get boolean
s = 'Hello World'

if 'H' and 'W' in s:
    print(s, 'has', 'H and W')

print('------------------------------------')
# now you want to create condition for condition 2
if score >= 60:
    print('Passed')
else:
    print('Failed')

print('---------------------------------')
age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = "Not Eligible"

print(result)

print('---------------------------------')

# Ternary:

age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible'

print(result)

print('---------------------------------')


# like you are not able to change the order if elif and else
num = 100

result = None

if num > 0:
    result = "Positive"
elif num < 0:  # same with else if block of Java
    result = "Negative"
else:
    result = "Zero"

print(result)

print('---------------------------------')

num = 200
# Ternary: ONLY works with if and else block not with elif
result2 = 'Positive' if num >= 0 else 'Zero'

print(result2)

print('---------------------------------')
# in here we have pre-condition
score = -300

if 0 <= score <= 100:
    if score >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print('Invalid Score')

print('---------------------------------')

score = 95

if 0 <= score <= 100:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
else:
    print('Invalid Score')


"""
A score of a student is given, write a program that can calculate the grade of the student

    Possible grades are:
        1. A ( 90 ~ 100)
        2. B ( 80 ~ 90 )
        3. C ( 70 ~ 80 )
        4. D ( 60 ~ 70 )
        5. F ( less than 60)
"""


