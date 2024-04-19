""" Write a method that:
1. Takes JSON file name and json content as arguments
2. Creates a new JSON file in Solutions directory using given data

Write a second method that:
1. Takes JSON file name (or path) as an argument
2. Print content of given JSON file """

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

import json

filename = 'newfile.json'
data = {'name': ['Jan', 'Kowalski'], 'email': 'jan@Kowalski.pl'}


# method 1
# save directory to JSON file
def writeToJSONFile(filename, data):
    """
    :param filename:
    :param data:
    :return: stringToJson
    """
    with open(filename, 'w') as f:
        # dump() takes two positional arguments: (1) the data object to be serialized,
        # and (2) the file-like object to which the bytes will be written
        stringToJson = json.dumps(data)
        f.write(stringToJson)


#  method 2
# reads data from json file
def method2(file):
    """
    :param file:
    :return: data
    """
    with open(file) as json_file:
        # JSON string, can be parsed by using the json.loads() method
        data = json.load(json_file)
        json_file.close()
        print(data)

writeToJSONFile(filename, data)

method2("new.json")
