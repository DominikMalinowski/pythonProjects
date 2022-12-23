#! python 3
import os

def big_file_display(path,size):

    for folderName, subFolders, fileNames in os.walk(path):
        for fileName in fileNames:
            if os.path.getsize(fileName) >= size:
                print(fileName + ' - waga: ' + str(os.path.getsize(fileName)))
                print('path: ' + os.path.abspath(fileName) + '\n')
            else:
                continue

path_1 = ('C:\\Users\\DELL\\Desktop\\pythonProject\\pliki_python_2')

big_file_display(path_1, 1000)