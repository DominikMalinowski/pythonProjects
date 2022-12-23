
# Input dictionaries
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}


final_dictionary = {}

# Function to add content from one dictionary to another
# parameters: base_dictionary - dictionary which will be appended
# parameters: added_dictionary - dictionary which content will be added to base_dictionary
# return: base_dictionary - dictionary containing content from both input dictionaries
def addToDictionary(base_dictionary, added_dictionary):

    for x, y in added_dictionary.items():
        base_dictionary[x] = y

    return base_dictionary

# Add second dictionary to first
final_dictionary = addToDictionary(dic1, dic2)

# Add third dictionary to previously created one
final_dictionary = addToDictionary(final_dictionary, dic3)

print(final_dictionary)