import json

# Name of new jsom file to be created
json_file = 'NewJson.json'

# Content of new json file
json_content = {"name": "Zophie", "isCat": "true", "miceCaught": 0,
"felineIQ": "null"}

# Function to create json file
# parameter json_file - string containing name of json file
# parameter json_content - content of the json file
def createJson(json_file, json_content):
    new_json = open(json_file, 'w')
    new_json.write(json.dumps(json_content))
    new_json.close()
    #content = new_file.read()

# Function to print content of the json file
# parameter json_file - string containing name of the json file
def printJson(json_file):
    new_json = open(json_file)
    print(json.loads(new_json.read()))
    new_json.close()


createJson(json_file, json_content)
printJson(json_file)




