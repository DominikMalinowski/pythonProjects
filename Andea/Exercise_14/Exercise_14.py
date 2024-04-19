"""
Write a method that:
1. Takes JSON file name and json content as arguments
2. Creates a new JSON file in Solutions directory using given data

Write a second method that:
1. Takes JSON file name (or path) as an argument
2. Print content of given JSON file
"""
json_new_file = 'new_json.json'
jsonString = '{"name": "Sophie", "isCat": true, "miceCaught":0, "felineIQ":null}'

import json 

def create_JSON(JSON_file, JSON_content):
    new_JSON = open(JSON_file,'w')
    new_JSON.write(json.dumps(JSON_content))
    new_JSON.close()

def JSON_print(JSON):
    jsonData = json.loads(JSON)
    print(jsonData)

create_JSON(json_new_file, jsonString)
JSON_print(jsonString)