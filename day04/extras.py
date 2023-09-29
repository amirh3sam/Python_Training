from functools import reduce

print('------------------closure-----------------')  # is uniq only for python a function inside another function

# nested function
def display_message():
    def method():
        print('Hello World')
        print('I Love Python')

    method()
    method()
    method()
    method()


display_message() # called the out method will print inner one 4 times

print('------------')


def display_palindromes(strings: list):
    def is_palindrome(s: str) -> bool:
        return s[::-1].lower() == s.lower()

    for s in strings:
        if is_palindrome(s):
            print(s)


print('-----------------------map-------------')

nums = [10, 20, 30, 40, 50, 60, 70, 80]

nums = list(map(lambda x: x * 10, nums))  # update every single element by multiply by 10
# map ( lambda argument name  : body of the function ,data structure )
#map(    lambda       x       :  x*10  , nums )   =>at end retun map objcet so we need to constract list() to get a list
print(nums)

names = ['Java', 'JAVA', 'java', 'ruby', 'swift', 'CyDeO', 'javaSCRipt']

names = list(map(lambda s: str(s).upper(), names))   # need change argument to str to be able to called s.upper that
# why we use constructor str ()

print(names)

dictionary = {'x': 100, 'y': 200, 'z': 300}

dictionary = dict(map(lambda t: (t[0], t[1] * 10), dictionary.items()))   # lambda work with tuple first and second
# index times 10
# t[1]  second element and multiply by 10
             # ==> return map object thats why we need to constructor to dic object
print(dictionary)

print('--------------------filter------------------') # is for similar list comprehension

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# nums = [ x for x in nums if x % 5 ==0]

nums = list(filter(lambda x: x % 5 == 0, nums))

print(nums)


names = ['Java', 'JAVA', 'java', 'ruby', 'swift', 'CyDeO', 'javaSCRipt']

# names = [a for a in names if not a.lower().startswith('j')]

names = list( filter(lambda x: not str(x).lower().startswith('j'), names ) )

print(names)


print('--------------------reduce------------------')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print( reduce( lambda x, y: x+y , list1) )


list2 = ['Java', 'Python', 'C#', 'Ruby']

print(  reduce( lambda x, y: f'{x} {y}' , list2 )  )


