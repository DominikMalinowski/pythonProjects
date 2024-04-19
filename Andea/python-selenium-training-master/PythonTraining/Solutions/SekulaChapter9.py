import os, shutil, zipfile

#checking if files exists
try:
    #creating files
    file1=open('f1.txt', 'x')
    file2=open('f2.txt', 'x')
except:
    print('File exists')


#copy files
shutil.copy('f1.txt', 'f1-copy.txt')
shutil.copy('f2.txt', 'f2-copy.txt')

#closing files
file1.close()
file2.close()

#removing files
os.remove('f1.txt')
os.remove('f2.txt')

#creating zip file
zf=zipfile.ZipFile('example.zip', 'w')

zf.write('f1-copy.txt')
zf.write('f2-copy.txt')

zf.close()
