
name = 'James'
age = 36

print('My name is ' + name)
# the + opertaro is not recomanded in paython is better to use a format or f to do concatenation
print(str('My age is ') + str(age) )

print('My age is {}'.format(age))

print('My name is {} and I am {} years old'.format(name, age))
# this is the best and easy way to give a different type in print

# first type 'f' then start your string and by opening and closing {} that called "placeholder"
print(f'My name is {name} and I am {age} years old')
# so wih comma you can give a different type in print
print('Python', 3, 'is awesome:', True)






