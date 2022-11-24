
path = './testFiles/file-1.txt'

with open(path,'w') as file:
    file.write('That is my first file!')

with open(path,'r') as file:
    print(file.read())

