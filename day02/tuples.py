# tuples is like array in Java

# you wanat to have only one data still have to add comma after that otherwise the data type will be string or int or
# float so for this example --> days = ("Monday",)

# tuple has only 2 method index() and count()

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", 1, 2, 3, 4, 5, 6, 7, True, False)

print(type(days))
print(len(days))

print(days)

# days[0] =  in 'Java' you can update the value of element for example index 0 ,but in Paython is not possible
# if you want to update the value you need to convert to set or list
# print(days)


print(days[0])  # to access the first element
print(days[-1])    # to access the last element

days = ('Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# work_days = days[1:-3]  if you  want to count from reverse mean from sunday
work_days = days[1:4]
print(work_days)

week_days = days[:-2] # start from beginning until friday

print(week_days)

weekend = days[-3:]  # get the last 3 index
print(weekend)

# == ,  is
# if you want the two tuples are have same contents  we use '=='
# if you want the two tuples referencing to the same object we use 'is'
# in java was different to see two data referencing to the same object we use ==
# in java instead 'is' we had equal operator

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 == tuple2)
print(tuple1 is tuple2)

# in Python, we can Merge two tuple
tuple3 = tuple1 + tuple2 # now has all the element of tuple1 and tuple2 and accept duplicate
print(tuple3)

tuple4 = tuple1 * 5
print(tuple4)

# with slice, we can use same expression to reverse the tuple
reversed_tuple1 = days[::-1]

print(reversed_tuple1)
# or another way to get reverse
reversed_tuple2 = tuple(reversed(days))
print(reversed_tuple2)

print(days)
# using index() method to get what index is for 'Wednesday'
print(days.index('Wednesday'))

numbers = (10, 10, 10, 10, 20, 30, 40, 50, 10)
# this count method is using to see how many 10 we have in this tuple
print(numbers.count(10))

print('-------------------------')
# so when they have indexes we can iterate with for loop
for x in days:
    print(x)

print('-------------------------')

for x in range(0, len(days)):
    print(x)

print('-------------------------')

for x in reversed(range(0, len(days))):
    print(x)

print('-------------------------')


# also we can have nested tuple !!
nested_tuple = ((1, 2, 3), (4, 5, 6, 7, 8), (9, 10))
# the lenight is 3 is counting number of tuple that are in the nested tuple
print(len(nested_tuple))

print('-------------------------')
# by using nested loop we can iterate the nested tuple
# x is 3 index that incldue 3 tuple and y is elements inside each tuple
for x in nested_tuple:
    print(x)
    for y in x:
        print(y)

print('-------------------------')

for i in range(0, len(nested_tuple)):
    for j in range(0, len(nested_tuple[i])):
        print(nested_tuple[i][j])  # i and j are index numbers now we get access to each element inside each tuple
