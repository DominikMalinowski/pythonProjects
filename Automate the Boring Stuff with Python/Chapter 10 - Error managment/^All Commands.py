# raise custom exception
def exception():
    raise Exception('Error placeholder')

exception()

# saving raised exeption 
import trackeback 

try:
    raise Exception('Placeholder')
except: 
    errorFile = open('errorInfo.txt','w')
    errorFile.write(trackeback.format_exc())
    errorFile.close()

# assertion 
