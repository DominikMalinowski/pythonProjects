
import logging

# logging.basicConfig(format= '%(asctime)s: %(levelname)s: %(message)s', datefmt='%d-%m-%Y,%H:%M:%S',level=logging.DEBUG)


class Logger():
    def test_log(self):
        logger = logging.getLogger(Logger.__name__)
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # formatter = logging.Formatter(format= '%(asctime)s: %(levelname)s: %(message)s', datefmt='%d-%m-%Y,%H:%M:%S')
        formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s', datefmt='%d-%m-%Y,%H:%M:%S')
        console_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)

        logger.debug('Debug message') 
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')

t = Logger()
t.test_log()
