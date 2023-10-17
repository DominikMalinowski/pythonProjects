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

# 