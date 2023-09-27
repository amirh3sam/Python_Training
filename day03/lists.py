groceries_list = ['Eggs', 'Milk', 'Rice']  # create the list name = ['str','str' ,int ,int ]

groceries_list.append('Chicken')  # append method is for add one element at the time
groceries_list.extend(('Beef', 'Oranges', 'Onion'))  # the extend method allow to insert data structure so need to
# be only one element and should be datastructure (tuple,set,list)  that's why here we give a tuple with 3 elements

print(len(groceries_list))  # list are ordered
print(groceries_list)

groceries_list[-2] = 'Cherry'
print(groceries_list)
# you can access the element and reassign it (orange is second last element = -2 )
# in Python for list if after you type the slicing " groceries_list[-2:] " and after that add " = " will not do slicing
# it
# will do only range of indexing

# you do this groceries_list[-2:] = 'Cherry' what happen is going to add cherry at the end one character at a time
# ['Eggs', 'Milk', 'Rice', 'Chicken', 'Beef', 'C', 'h', 'e', 'r', 'r', 'y']
# so when you have a list like this is better to add tuple or list not string -->groceries_list[-2:] = ( tuple or list)


print('------------------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers_list)
# want to update 30 ,40 ,50  60 --> 300 , 4000 ,5 ,6000
numbers_list[2:-2] = [300, 4000, 5, 60000]  # we have to update multiple at the time so give range if index from
# starting to ending of the list  but make sure you have to choose index element 70 to 60 be included that's why is -2
print(numbers_list)

print('------------------------------------')
# now we want to do slicing
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

list1 = characters[2: -3]  # create new list and add the slicing in it from c to f
# if you wana give both forward index direction  you can do this [2 : len(characters)-3]
print(list1)
# or you can do list this
list12 = characters[2: 6]
print(list12)
list2 = characters[:4]  # from beginning to index 4
print(list2)

list3 = characters[2:]  # from index 2 to the end of list
print(list3)
# in this case I try to add element to index 2 , 3 and 4, but I am giving more element  what happens is they will add
# and shift the others
characters[2:5] = ['C', "D", 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']  # more than the range adding element

print(characters)

print('------------------------------------')
# iterate the list is exact same to do iterate tuple
names = ['Conor', 'Steve', 'Hazel', 'Breanna']

for x in names:
    print(x)

print('------------------------------------')
# in this example I want to update the list
nums = [10, 20, 30, 40, 50, 60]

for i in range(len(nums)):
    nums[i] = int(nums[i] / 5)  # the / operator give you float that why we add int (  )

print(nums)

print('------------------------------------')

nums = [10, 20, 30, 40, 50, 60]

for i in reversed(range(len(nums))):
    print(nums[i])

print('------------------------------------')

for x in nums[::-1]:  # this slicing creat new list and reversing it too
    print(x)

print('------------------------------------')

for x in reversed(nums):
    print(x)

print('------------------------------------')

i = 0

while i < len(nums):
    print(nums[i])
    i += 1

print('------------------------------------')

for i in range(1, 6):
    i += 2  # number increase by 2
    print(i)

print('------------------------------------')

nums = [60, 500, 10, 20, 15, 5, 0]

# nums.sort() ---> ascending order

nums.sort(reverse=True)  # it will reverse ascending order --> descending order

print(nums)

print('------------------------------------')

list1 = [10, 20, 30, 40]

# list1 = list( reversed(list1) ) # we use list (    ) constractor function here

list1.reverse()

print(list1)

print('------------------------------------')

tuple_elements = ('Java', 'Python', 'C#', 'Ruby')

list_elements = list(tuple_elements)  # convert tuple to list
list_elements[-2] = 'C++'
list_elements.append('SWIFT')

print(list_elements)

tuple_elements = tuple(list_elements)  # cast the list to tuple

print(tuple_elements)

print('------------------------------------')

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

print(list1 is list2)  # in list, it will return false the two object referencing the same object

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)

print(tuple1 is tuple2)  # but in tuple, it will return True, the two object referencing the same object
# THE REASON is the tuple is immutable just like the string when you have string literal the is only one objet memory
# located in the string pool since the tuple is immutable there is guaranty  the those element will not change so if
# you have two tuple object that has exact same contents gonna one objet will locate in python memory
# but list is changeable when you create list could be change later that is why even if they have exact same contents
# for each going to be memory located

print('------------------------------------')

groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend(('Beef', 'Oranges', 'Onion'))

print(groceries_list)

groceries_list.remove('Beef')  # is going to remove one object at the time

print(groceries_list)

groceries_list.pop()  # if you want to remove element by the index the default is last index when you are not giving
# any argument

print(groceries_list)

groceries_list.pop(1)  # now we give arg  -- >  that element index = 1 will remove

print(groceries_list)

groceries_list.insert(2, 'Apple')  # different between append and insert : append just add after last element but
# insert you can add in specific element  --> at index 2 add Apple and chicken shift to right

print(groceries_list)

print(groceries_list.index('Eggs'))

nums = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]

print(nums.count(1))  # how many 1 we have in this list

print('--------------- List Comprehensions -------------------------')

nums = []

for x in range(1, 51):  # numbers range from 1 to 50
    nums.append(x)

print(nums)  # now contents element 1 to 50

print('------------------------------------')

"""
divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)
"""
# another way to create new list  that after to loop add it to new list that only divisible by 5
# new_list = [var_name for var_name in iterable if condition]

divisible_by_5 = tuple([x for x in nums if x % 5 == 0]) # if you want to your comprehensions getting tuple
# just cast it to tuple ( )  if instead  [   ] use  (  ) and do not want to cast to tuple you will get hash code so
# you need to first  do the list [    ]  then cast it to tuple ( [     ] ) then you gonna have tuple

print(divisible_by_5)

print('------------------------------------')

even_nums = [x for x in nums if x % 2 == 0]
odd_numbers = [x for x in nums if x % 2 != 0]

print(even_nums)
print(odd_numbers)

print('------------------------------------')

names = ['Python', 'Java', 'Java', 'JavaScript', 'java', 'JaVA', 'Ruby']

names = [x for x in names if x.lower() != 'java']

print(names)
