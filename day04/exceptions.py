try:
    num = 10 / 0
    print(num)
except:
    print('Something went wrong')
else:  # only execute when the condition of this except is false
    print('Nothing went wrong')
finally:
    print('finally block')

print('Test Completed')

print('----------------------------')

tuple1 = (10, 20, 30, 40)

try:
    print(tuple1[2])            # try and else works together
except:  # after except you can mention the type of execution but if you get wrong type you will get error again
    print('The index number is too large')
else:
    print('The index number is valid')

print('---------------------------------------------')

try:
    raise FileNotFoundError('No such a file')
except SyntaxError:  # is only looking for SyntaxError
    print("It is a syntax error")
except OSError:  # is only looking for OSError
    print('It is an operating system error')
except ArithmeticError: # is only looking for ArithmeticError
    print('It is an arithmetic error')
finally:
    print('Finally block')


print('-------------------------------------')

raise LookupError('Invalid entry')



""" 
In Java
    throw: used for manually throwing exception
    throws: for exception handings (in method signature)
"""








