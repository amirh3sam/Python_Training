import os

path = 'C:/Users/amirh/OneDrive/Desktop/test.txt'  # if you text file is under files under day04, so you do not need
# day04 only 'files/Test.txt'

text_file = open(path, 'r')

print( text_file.read() ) # read the whole thing


text_file.close()  # need to close it otherwise keep the file open

"""
print(text_file.readline())   read one line only 
print(text_file.readline())
print(text_file.readline())
"""

print('----------------------------------')

path = 'files/Test2.txt'

text_file2= open(path, 'w') # now we can write something the Test.txt file

text_file2.write('This is a new text file\nPython created this file')

text_file2.close()

print('----------------------------------')

os.remove(path)   # also you can delete any file just need to import os and then os.remove('file_path') and its
# permanent

