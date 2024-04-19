import json


def json_file_creation(json_name, json_arguments):
    with open(json_name, 'w') as f:  # Create an empty json file or replace existing one
        to_write = json.dumps(json_arguments)  # Change arguments to json format
        f.write(to_write)  # Write arguments to file
        f.close()


def print_json_file(json_name):
    with open(json_name) as f:  # Open existing json file
        to_read = f.read()  # Read the content
        print('Content of the file:\n' + to_read)  # Print content of the json file
        f.close()


# json file name
file_name = 'KK.json'

# json dictionary (as python dictionary)
json_dictionary = {"Animal data":
                       [{"name": "Zophie", "isCat": True, "isDog": False, "age": 5, "origin": None},
                        {"name": "Poppy", "isCat": False, "isDog": True, "age": 2, "origin": None}]}

# run functions
json_file_creation(file_name, json_dictionary)
print_json_file(file_name)
