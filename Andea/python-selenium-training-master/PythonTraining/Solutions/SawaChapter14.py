import json

# jsondata
nameJson = 'file_1.json'
jsonContent = {'Name': 'Pluto', 'Doge': 'True', 'Colour': 'Yellow', 'Owner': 'Mickey'}

# write data to json
def createJson():
    f = open(nameJson, 'w')
    f.write(json.dumps(jsonContent))
    f.close()


#reads data from json
def printJson():
    f = open(nameJson)
    print(json.loads(f.read()))
    f.close()

createJson()
printJson()