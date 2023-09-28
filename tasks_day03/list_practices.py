"""

1. Create a python file named list_practices:

		1.1 Write a program that can move all the zeros to the last indexes of ArrayList
	            Ex:
	                list: [1,0,2,0,3,0,4,0]

	            output:
	                [1, 2, 3, 4, 0, 0, 0, 0]

"""


def zero_to_end(numbers: list):
    new_list_no_zero = [each for each in numbers if each != 0]

    for number in numbers:
        if number == 0:
            new_list_no_zero.append(number)

    print(new_list_no_zero)


zero_to_end([1, 0, 2, 0, 3, 0, 4, 0])

"""

	    1.2 write a program that can multiply each odd number by 2
		            ex: 
		            	list = [1,2,3,4,5];

		                output: [2,2,6,4,10]"""


def multiple_odd(numbers: list):
    new_list = [each for each in numbers if each % 2 != 0]
    doubled_list = []
    for number in new_list:
        doubled_list.append((number * 2))
    new_list.extend(doubled_list)
    print(doubled_list)


multiple_odd([1, 2, 3, 4, 5])
""""
  1.3 Write a program that can remove all the names "Ahmed" from a list of strings
				Ex:
	                list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]

	            output:
	            	["John", "Daniel", "James", "Muhammed"]"""


def remove_ahmad(names: list):
    new_list = [each for each in names if each != 'Ahmed']

    print(new_list)


remove_ahmad(["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"])

""""

1.4 Write a program that can display the palindrome strings from a list of String
				Ex:
					words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']

					output:
						Anna
						Level"""




def is_palindrome(word):
    # Remove spaces and convert the word to lowercase for a case-insensitive check
    cleaned_word = word.replace(" ", "").lower()
    # Check if the cleaned word is the same when reversed
    return cleaned_word == cleaned_word[::-1]


def display_palindromes(words):
    newlist = []
    for word in words:
        if is_palindrome(word):
            newlist.append(word)

    print(newlist)


display_palindromes(['Java', 'Anna', 'python', 'Cydeo', 'Level'])

"""1.5 Write a program that can display the common elements of two lists:
				Ex:
					list1 = [1,2,3,4,5]
					list2 = [4,5,6,7,8]

					Output:
						4
						5
"""

"""


1.6 Write a program that can remove the duplicated elements from a list
				Ex:
					elements = [1,2,3,4,5,1,2,3,4,5]

					Output:
						[1, 2, 3, 4, 5]

					Notes: Do Not use Set
"""

""""



1.7 Write a program that can remove string elements from a list if the first and last characters 
of the string are same
				ex:
					list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}

				output:
					["Lan", "Ebrahim", "Farida"]

"""

"""
		1.8  Write a program that can display the unique elements of an arrayList:
					ex:
						list = [1, 1, 2, 3, 3, 4, 5, 5]

					output:
						[2, 4]
"""
