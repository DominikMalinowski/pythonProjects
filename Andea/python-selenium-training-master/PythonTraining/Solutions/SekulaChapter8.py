import os

#checking if file exists
try:
    #creating file
    file=open('data.txt', 'x')
except:
    print('File exists')


#writing to file
file.write('one\ntwo\nthree')
file.close()

#open file in read mode
f=open('data.txt', 'r')

#reading from file
text=f.read()
#spliting string to list
content=text.split('\n')

#printing string list
print(content)
f.close()

#removing file
os.remove('data.txt')