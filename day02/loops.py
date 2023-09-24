# no do while loop in Paython
s = 'Python Programming'


# for loop is used successive each successive value of a sequence or a data structure
# the built-in data structure: string, tuple, list , set, dictionary
# do not confuse this with for each loop in java

for each in s:
    print(each)
# here is going to give you each character of the string!
print('-----------------------')
3 # range is going to give you in sequence
for i in range(0, len(s)):
    print(s[i])

print('-----------------------')
# here do reverse string
for i in range(-len(s), 0):
    print(s[i])

print('-----------------------')
# another way to reverse the string
for i in reversed( range(0, len(s)) ):
    print(s[i])

print('-----------------------')

result = ''
# another way with slicing to reverse the string
for x in s[::-1]:
   result += x

print(result)

print('-----------------------')

# want to repeat something 10 times
for x in range(1, 11):
    print('Hello World')

print('-----------------------')

# while loop is when you do not know the number of iterations
num = int( input('Enter a positive number:\n'))

while num <= 0:
    num = int( input('Enter a positive number:\n')) # input return as string that why we need to cast int

print(f'You have entered {num}')

print('-----------------------')

answer = input('Enter yes or no:\n')

while not ( answer.lower() == 'yes' or answer.lower() =='no'): # if inside the () is not valid -- not is like ! in Java
    answer = input('Enter yes or no:\n')

print(f'You have entered {answer}')
