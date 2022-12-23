"""
JsonHandler.py is used to read data from json files.
Import it to the file, where getting data from json file is needed.
"""

import json
import os
from os.path import dirname
from dotmap import DotMap


CONFIGURATION_PATH = os.path.dirname(dirname(__file__)) + "\\Configuration"
UTILITIES_PATH = os.path.dirname(dirname(__file__)) + "\\Utilities"

def getDataFromJsonFile(file):
    file_name = file
    file_path = os.path.join(CONFIGURATION_PATH, file_name)

    with open(file_path) as opened_file:
        data = json.load(opened_file)

        map = DotMap(data)
        return map

def getDatabaseStatement(statement_name):
    """ Return value for given key from DatabaseStatements.json file """
    file_name = "DatabaseStatements.json"
    file_path = os.path.join(CONFIGURATION_PATH, file_name)

    with open(file_path) as opened_file:
        data = json.load(opened_file)

        statement = ""
        for element in data[statement_name]:
            statement += element

        return statement
