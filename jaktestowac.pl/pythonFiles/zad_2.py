
with open("./testFiles/file-2.txt", 'w') as file:
   file.write('That is my second file!')
with open("./testFiles/file-2.txt") as file:
   print(file.read())