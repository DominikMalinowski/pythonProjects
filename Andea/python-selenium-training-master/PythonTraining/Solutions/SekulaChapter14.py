import json

data={'name':'Krzysiek', 'surname': 'Sekula' , 'phone number':'123456789' , 'email':'ksekula@asd.com' , 'login':'ksekula' , 'password':'qweasdzxc'}
filename='personaldata.json'

#write data to json
def jsonwrite(filename, data):
    #creating json
    f=open(filename, 'w')
    #changing data format to json format
    stringtojson=json.dumps(data)
    #writing and closing json
    f.write(stringtojson)
    f.close()


#read data from json
def jsonread(data):
    #opening json
    f=open(filename, 'r')
    #reading data from json 
    text=f.read()
    #changing data format to [python
    string_from_json=json.loads(text)
    print(string_from_json)
    f.close()


jsonwrite(filename, data)
jsonread(filename)