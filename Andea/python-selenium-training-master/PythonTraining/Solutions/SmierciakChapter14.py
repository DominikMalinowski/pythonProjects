import json

class JsonObj:
#define constructor. Make arguments optional
    def __init__(self, filepath = "", jsonstring = ""):
        
#check if user haven't sourced two arguments at once. If so, raise exception
        if filepath != "" and jsonstring != "":
            raise Exception("Can't take JSON string and file path at once")

#check if user haven't sourced two arguments at once. If so, raise exception
        if filepath == "" and jsonstring == "":
            raise Exception("Not all arguments defined")

#write jsondata (dictionary) from file
        elif filepath != "":
            try:
                with open(filepath,"r") as file:
                    self.jsondata = json.load(file)
#File handler exception
            except FileNotFoundError:
                print("File not exists.")

#write jsondata (dictionary) from string
        elif jsonstring != "":
            self.jsondata = json.loads(jsonstring)

#method for writing json to another file. As argument take filepath/filename
    def writejson(self, newfilepath):
        with open(newfilepath, "x+") as outfile:
            try:
                json.dump(self.jsondata, outfile)
#catch exception if file already exists 
            except FileNotFoundError:
                print("File already exists.")

#method for printing json content
    def printjson(self):
        print(self.jsondata)


x = '{ "name":"John", "age":30, "city":"New York"}'
jsonobj = JsonObj(jsonstring=x)
jsonobj.writejson("test5.json")
jsonobj.printjson()
print(jsonobj.jsondata)

jsonobj2 = JsonObj(filepath="test.json")
jsonobj2.writejson("test6.json")
jsonobj2.printjson()
print(jsonobj2.jsondata)
