# Content:
# - change directory 
# - copy file 
# - copy file with all content
# - move file 
# - remove file/directory
# - save remove file/directory

# change directory 
import os 
os.chdir('{new path}')

# copy file 
import os 
import shutil
shutil.copy('{source}','{destination}')

# copy file with all content
import shutil
shutil.copytree('{source}','{destination}')

# move file 
import shutil
shutil.move('{source}','{destination}')

# remove file/directory
import os
os.unlink('{path}') # remove all data
os.rmdir('{path}') # remove only empty folders

# save remove file/directory
import send2trash
send2trash.send2trash('{path}')

# going through catalog file by file 
import os
for foldername in os.walk('{path}'):
    print(foldername)

# compress file 
import zipfile 
finished_zip = zipfile.ZipFile('{path}')

# extract zip file 
import zipfile 
finished_zip = zipfile.ZipFile('{path}')
extractedZip = finished_zip.extractall()

# adding files to compresed zip 
import zipfile 
finished_zip = zipfile.ZipFile('{path}')
extra_zip = zipfile.ZipFile(finished_zip, 'a')
extra_zip.write('{file_to_add}',compress_type=zipfile.ZIP_DEFLATED)
extra_zip.close()