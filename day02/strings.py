name = 'Python'

print(len(name))  # len give you length for string
print(name[0])  # to access to any index just put it inside []
print(name[len(name) - 1])

print(name[-1])  # to access last index number
print(name[-2])  # to access the second last index number

s = 'Java Programming Language'
# if we want to get Programming P is index 5 and g is on index 15
# to have g in our slice, we have to choose the next index that is 16 like java
s2 = s[5:16]  # --> Slicing is like substring in java [start:end]
# --> or you can do [start:] or [:end]
print(s2)

s3 = s[:4]  #

print(s3)

s4 = s[::-1]  # reverses the string after slicing

print(s4)

# Reverse method
s = 'Python Programming'

s5 = str(reversed(s))

print(type(s5))
reversed(s5)

print(s5)

s5 = s[::-1]

print(s5)

s5 = 'python Programming'

s6 = s5[7:]  # by default, it slices the string from index 7 to the last character

print(s6)

s7 = 'CYDEO SCHOOL'
# str(reversed(s7))

print('----------------------')

# print( help(str))


print('----------------------')

s = 'python programming language'

# s = s.capitalize() # only first character upper case
s = s.title()   # all first characters of the sentence upper case
print(s)

s = "            Python           "
s = s.strip()  # trim method of java

# we have 2 more lstrip and rstrip that remove only one side(left or right)

print(s)

s = 'JAVA'

print(s.index('A'))  # first index number like the same as Java
print(s.rindex('A'))  # last index number of character like Java

s = 'Java Java'

s = s.replace('Java', 'Python', 1) # like java, replace Python with Java
# that count 1 is only replace one Python with Java
print(s)

s = 'C# C# Python'
# if we want to replace the second one, we add space before C# to make it uniq
s = s.replace(' C#', ' Java')
print(s)

s = 'Java jAVA java JAVA Python Python'
# how many 'java' with have in these sentences
# lower is for ignoring the case sententiously
count_java = s.lower().count('java')
count_python = s.count('Python')

print(count_java)
print(count_python)

s1 = 'java'
s2 = 'JAVA'
# use == to compare the content of the two objects, so you need to
# use a lower or upper case then compare them
print(s1.lower() == s2.lower())  # ignore case

s = 'Java'

print(s[0].islower())  # boolean answer --> False
print(s[0].isupper()) # boolean answer--> True

s = 'a'

print(s.isalpha())  # boolean answer--> True

s = '1'

print(s.isdigit())  # boolean answer--> False

s = 'Cydeo School'

print(s.istitle())   # boolean answer--> True
