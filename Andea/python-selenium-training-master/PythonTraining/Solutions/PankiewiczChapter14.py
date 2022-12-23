# V 1.0 - 22.05.2019
"""
Write a method that:
1. Takes JSON file name and json content as arguments
2. Creates a new JSON file in Solutions directory using given data

Write a second method that:
1. Takes JSON file name (or path) as an argument
2. Print content of given JSON file
"""
# import json to work with Json files (java Script object notifications)
import json

j1_name = ('AP_json_file.json')
# create dictionary (json format)
j1_content = {"Profile data":
                  [{"person": "Jan Kowalski", "phone": "null", "sex": "male"},
                   {"person": "Anna Nowak", "phone": "234567890", "sex": "female"}]}


def met_1(j1_name, j1_content):
    with open(j1_name, 'w') as f:
        # creates write variable. 'json.dumps' means we take content from json to variable
        # intent gives two indents after each level in json file
        write_content = json.dumps(j1_content, indent=2)
        # using 'write' function for 'write_content' variable
        f.write(write_content)


def met_2(j1_name):
    with open(j1_name, 'r') as n:
        # creates read variable
        read_content = n.read()
        # load json string as python object
        python_obj = json.loads(read_content)
        # print string
        print(python_obj)


# call both functions for these arguments
met_1(j1_name, j1_content)
met_2(j1_name)