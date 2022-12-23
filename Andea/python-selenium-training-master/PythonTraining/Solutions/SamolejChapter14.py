"""
Write a method that:
1.Takes JSON file name and json content as arguments
2.Creates a new JSON file in Solutions directory using given data
Write a second method that:
1. Takes JSON file name( or path) as an argument
2. Print content of given JSON file
"""

import json

newJson = 'newJson.json'
dic = {'test1': 'test11', 'test2': 'test22'}

#save dictionary to json file
def createJson(newJson, dic):

    file = open(newJson, 'w')
    file.write(json.dumps(dic))
    file.close()


#reads data from json
def jsonread(data):
    file = open(newJson)
    print(json.loads(file.read()))
    file.close()


createJson(newJson,dic)
jsonread(newJson)