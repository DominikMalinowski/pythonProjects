"""
Write a program that:
1. Creates a new file named 'data.txt' in the same directory as your program (check if it already doesn't exist) - use relative path!
2. Opens the file in write mode and writes three words (e.g. 'one', 'two', 'three') to it - each one in new line
3. Opens the file in read mode and reads all the lines, putting each word to list as a new element
4. Deletes the created file
"""

import os 

file_name = 'data2.txt'
content = 'one, \ntwo, \nthree'

def create_file(path, input_text):
    if os.path.exists(path) == True:
        print('File already exisit')
    else:
        with open (path, 'w') as open_file:
            open_file.write(input_text)
            open_file.close()

create_file(file_name, content)

#         # removing the file
# def file_remove(file_to_remove):
#     if os.path.exists(file_to_remove):
#         os.remove(file_to_remove)
#     else:
#         print('File to remove does not exist')