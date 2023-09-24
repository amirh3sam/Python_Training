"""
5. Create a python file named characters, write a program that can retive the digits, letters and special characters from a string
            Ex:
                input:
                    mn@#123Ab!

                output:
                    letters: mnAb
                    digits: 123
                    special chars: @#!
"""


def digit_letters_special_character(string: str):
    is_digits = ''
    is_special = ''
    is_letter = ''
    for char in string:
        if char.isdigit():
            is_digits += char
        elif char.isalpha():
            is_letter += char
        else:
            is_special += char

    print(f'letters:{is_letter}')
    print(f'digits:{is_digits}')
    print(f'special chars:{is_special}')


digit_letters_special_character('AB32#$')
