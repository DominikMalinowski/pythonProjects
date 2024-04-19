import os, shutil, zipfile

# Create a new files
file_1 = open('f1.txt', "w")
file_2 = open('f2.txt', "w")

# Copy files
shutil.copy('f1.txt', 'f1-copy.txt')
shutil.copy('f2.txt', 'f2-copy.txt')

# For removing file must be closed
file_1.close()
file_2.close()

os.remove('f1.txt')
os.remove('f2.txt')

# Create zip file
fileZip = zipfile.ZipFile('new_zip.zip', "w")
fileZip.write('f1-copy.txt', compress_type=zipfile.ZIP_DEFLATED)
fileZip.write('f2-copy.txt', compress_type=zipfile.ZIP_DEFLATED)