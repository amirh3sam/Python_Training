employee1 = {}  # empty dic
# collection of pair -->data structure key and value  key must be uniq and keep the order {key:value,key:value,...}
employee1['name'] = 'James'  # [newKey] = value and key and value can be any data type because python is dynamic
# dataType
employee1['name'] = 'Daniel'
employee1['age'] = 45
employee1['salary'] = 60_000

print(employee1)

employee2 = {
    'name': 'James',
    'age': 29,
    'salary': 80_000,
    'full_time': False
}

print(employee2)
print(employee2['name'])  # to get the value you can use get() method

employee2['salary'] += 10000
print(employee2)

employee2.update({'age': 40})  # to update the value {first need to pass the key  :  then the value} you want to or
# you can do update this way ==> employee2['salary'] += 10000
# update

print(employee2)

employee2['full_time'] = True

# employee2.update( {'full_time': True} )

print(employee2)

employee2.pop('full_time')  # for removing the key

print(employee2)

# print( help(dict.popitem) )

employee2.popitem()  # for LIFO last in first out ==> "last pair will remove"

print(employee2)

l = employee2.copy()  # create new dic object with same pairs keys and values

print(l)

print(employee2 is l)  # because create new dic in memory

print('--------- Iterating Dictionary -----------------')

employee3 = {
    'name': 'Shay',
    'age': 29,
    'salary': 110_000,
    'full_time': False,
    'job_title': 'Developer',
    'company': 'Apple Inc'
}

print(list(employee3.keys()))  # return you a list of Keys

for key in employee3.keys():    # with for loop you can get keys then we can print every single key and value
    print(f'{key} : {employee3[key]}')
# you can do this to employee3.get(key)
print('---------------------------------------')

values = list(employee3.values())     # if only you want the value ==> get original  list of value

print(values)

for value in employee3.values():  # with for loop you can print all the value
    print(value)

print('---------------------------------------')

for x in employee3.items():  # items(): returns a collection of tuples, in each tuple there will be two elements one
    # key and one value index 0 represent key and index 1 represent value of each pair
    # print(x)
    print(f'{x[0]} : {x[1]}')

print('---------------------Nested DIC ------------------')

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
    },

    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ['Biology', 'Programming']
    },

    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

print(students)
        # [dic][dic] = 2.5 will update to 2.5
students['A01']['gpa'] = 2.5

print(students)

# students['A02'].update( {'name': 'Daniel' , 'gender': 'Male'} ) or you can do like this :
students['A02']['name'] = 'Daniel'
students['A02']['gender'] = 'Male'

print(students)

students['A03']['subjects'][1] = 'Biology'

print(students['A03'])

print('---------------------------------------------')

for x in students.items():
    print(x[1])
    for y in x[1]:
        print(y)

print('---------------------------------------------')

for value in students.values():
    print(value)
    for item in value.items():
        print(item[1])
