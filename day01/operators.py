# arithmetic: +, -, *, /, %

print(10 - 2)
print(10 + 2)

print(10 * 3)

print(10 / 3)

print(10 / 2)
# in java, what data type your will get is depended on what data type you have

# in python, it is different, you will always give you float here
print(10 % 3)

# if you want to get int need to cast to int like this example:
print(int(100 / 2))

# shorthand assignment operators: =, +=, -=, *=, /=, %=

a = 100

a = 200

print(a)

a += 100

print(a)

a -= 50

print(a)

a /= 2

print(a)

# logical operators: and, or, not
# in Java we use && and ||
s = 'Hello World'
# in paython, we can get a boolean result with and like this example
print('H' and 'W' in s)
# in java that what use and or for boolean
print(True and True)
print(True or False)

s = 'Java Python C# C++'

print('Java' or 'Ruby' in s)  # in here ONLY for OR operators when we have one of them True will print it in console

age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'

print(is_eligible) # going to give us True because both conditions are true

has_java = 'Java' in s  # here we are saying if Java is included in S ?!
print(has_java)

# !contains()
print('Python' not in s)

print(not False)
print(not True)  # !

print('----------------------------------')

s = 'Java'
s2 = 'Java'

print(s is s2)  # to check if two variables are referencing to the same objects ( == operator of java)
