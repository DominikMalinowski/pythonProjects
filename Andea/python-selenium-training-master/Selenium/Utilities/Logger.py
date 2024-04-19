import inspect
import logging
import os
from os.path import dirname

def MESlogger(logLevel=logging.DEBUG):
    """
    Return logger.
    Create logger object in every file where it will be used
    """
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logLevel)

    # TODO: insert correct comment
    # projectPath = os.path.dirname(os.path.dirname(dirname(__file__))) + "\\"
    projectPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    file = logging.FileHandler(projectPath + "SeleniumLogs.log", mode='a')
    file.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    file.setFormatter(formatter)
    logger.addHandler(file)

    return logger