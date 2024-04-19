# Content:
# - creating path
# - current working dictionary 
# - create new catalog 
# - absolute path and isabs()
# - relative path 
# - basename and dirname 
# - spilth path 
# - get size of all data in path 
# - list all folders in path 
# - check is path exist 
# - check is path leading to file/directory
# - opening file 
# - reading file 
# - opening file in 'write' mode
# - opening file in 'add' mode
# - opening file in 'read-only' mode


# creating path 
import os 
print(os.path.join('place','holder','path'))

# current working dictionary
import os 
print(os.getcwd())

# # create new catalog 
# import os 
# os.makedirs(r'C:\Users\dmalinowski\Desktop\Repo\new folder')

# absolute path and isabs()
import os
cwd = os.getcwd()
print('This is absolute path path: \n' + os.path.abspath(cwd))

# relative path 
import os
cwd = os.getcwd()
print('This is relative path: \n' + os.path.relpath(cwd,r'C:\Users\dmalinowski'))

# basename and directory 
import os 
cwd = os.getcwd()
print('This is base name for current working dictionary: \n' + os.path.basename(cwd))
print('This is directory name for current working dictionary: \n' + os.path.dirname(cwd))

# spilth path 
import os 
print(os.path.split(os.getcwd()))

# get size of all data in path 
import os 
print('Combined size of all files in path is: \n' + str(os.path.getsize(os.getcwd())))

# list all folders in path 
import os 
import pprint
pprint.pprint('This is list of all files/directory in path: \n' + str(os.listdir(os.getcwd())))

# check is path exist 
import os 
print(os.path.exists(os.getcwd()))

# check is path leading to file/directory
import os 
print(os.path.isfile(os.getcwd()))
print(os.path.isdir(os.getcwd()))

# opening file 
import os 
file_path = os.path.join(os.getcwd(),'Automate the Boring Stuff with Python\Chapter 8 - Read & write files\hello.txt')
opened_file = open(file_path)

# reading file 
import os 
file_path = os.path.join(os.getcwd(),'Automate the Boring Stuff with Python\Chapter 8 - Read & write files\hello.txt')
opened_file = open(file_path)
print(opened_file.read())
opened_file.readlines()

# opening file in 'write' mode
import os 
file_path = os.path.join(os.getcwd(),'Automate the Boring Stuff with Python\Chapter 8 - Read & write files\hello.txt')
opened_file = open(file_path, 'w')
opened_file.write('write text')
opened_file.close()

# opening file in 'add' mode
import os 
file_path = os.path.join(os.getcwd(),'Automate the Boring Stuff with Python\Chapter 8 - Read & write files\hello.txt')
opened_file = open(file_path, 'a')
opened_file.write('\n added text')
opened_file.close()

# opening file in 'read-only' mode
import os 
file_path = os.path.join(os.getcwd(),'Automate the Boring Stuff with Python\Chapter 8 - Read & write files\hello.txt')
opened_file = open(file_path, 'r')
print(opened_file.read())
opened_file.close()