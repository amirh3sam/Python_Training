"""

21. Create a python file named number_to_words, Write a program that can convert user entered number (from 0~9) to words.

    NOTE: MUST use ternary
"""


user_number = int(input("Enter a number between 0 and 9: "))


number_words = (
    "Zero" if user_number == 0 else
    "One" if user_number == 1 else
    "Two" if user_number == 2 else
    "Three" if user_number == 3 else
    "Four" if user_number == 4 else
    "Five" if user_number == 5 else
    "Six" if user_number == 6 else
    "Seven" if user_number == 7 else
    "Eight" if user_number == 8 else
    "Nine" if user_number == 9 else
    "Invalid"
)

print(f"The number {user_number} is represented as: {number_words}")