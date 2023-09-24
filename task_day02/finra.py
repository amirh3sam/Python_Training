"""

7. Create a python file named finra, Write a program which prints out the numbers from 1 to 100 but for numbers
 which are a multiple of both 3 and 5, print "FINRA" instead of the number,  for numbers which are a multiple of 3,
 print "FIN" instead of the number and for numbers which are a multiple of 5, print "RA" instead of the number.

    ex:
        output:
            1 2 FIN 4 RA FIN 7 8 FIN RA 11 FIN 13 14 FINRA 16 17 FIN
"""


def finra():

    result = ""
    for i in range(1,101):
        if i % 5 == 0 and i % 3 == 0:
            result += "FINRA"+' '
        elif i % 5 == 0 :
            result += "RA"+' '
        elif i % 3 == 0:
            result +="FIN"+' '
        else:
            result += str(i)+' '
    print(result.strip())
finra()