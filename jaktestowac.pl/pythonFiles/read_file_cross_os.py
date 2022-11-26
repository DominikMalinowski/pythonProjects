#
# path = "./testFiles/fileToRead.txt"
import os.path

path = os.path.join('testFiles', 'fileToRead.txt')
file = open(path)
print(file.read())
file.close()

