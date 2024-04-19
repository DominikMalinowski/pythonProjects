
file = open("./testFiles/file-1.txt", 'w')
file.write('That is my first file!')
file.close()

file = open("./testFiles/file-1.txt")
print(file.read())
file.close()