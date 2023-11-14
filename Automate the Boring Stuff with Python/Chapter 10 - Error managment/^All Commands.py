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
value = 'Yes'
assert value == 'Yes','Assertion error is raised is assertion return false'

value = 'Nope'
assert value == 'Yes','Assertion error is raised is assertion return false'

# logging 
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(sdctime)s - %(levelname)s - %(message)s')