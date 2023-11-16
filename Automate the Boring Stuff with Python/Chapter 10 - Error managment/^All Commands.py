# raise custom exception
def exception():
    raise Exception('Error placeholder')

exception()

# saving raised exeption 
import traceback

try:
    raise Exception('Placeholder')
except: 
    errorFile = open('errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()

# assertion 
value = 'Yes'
assert value == 'Yes','Assertion error is raised is assertion return false'

value = 'Nope'
assert value == 'Yes','Assertion error is raised is assertion return false'

# logging 
import logging
FORMAT = ' %(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

def count(n):
    logging.debug('Start')
    for i in range(n):
        logging.debug(f'Repeat numer: {i}')
    logging.debug('End')

count(5)

# turning off logging 
import logging
FORMAT = ' %(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.debug('Warning')

logging.disable(logging.DEBUG)
print('koniec')
logging.debug('Warning2')
logging.debug('Warning3')

