
"""
input is like a scanner in JAVA,
and a type is always String in Paython and return you can use Type method to check the data type
--if you want to act like int you need to do casting
--best way is cast the input --> as soon as enter the value convert it int
age = int( input('Enter your age:\n') )
or other type!!

"""
import faker

# help method is display the documentation of the method
# print(  help(input)  )

name = input('Enter your name:\n')
age = int( input('Enter your age:\n') )
gpa = float(input('Enter your gpa:\n'))
boolean_value =  bool(input('Enter True or False:\n'))

print(name)
print( type(name) )

print( age )
print( type(age) )

print(gpa)
print( type(gpa))

print(boolean_value)
print( type(boolean_value))