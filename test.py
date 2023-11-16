

# turning off logging 
import logging
FORMAT = ' %(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.debug('Warning')

logging.disable(logging.DEBUG)
print('koniec')
logging.debug('Warning2')
logging.debug('Warning3')