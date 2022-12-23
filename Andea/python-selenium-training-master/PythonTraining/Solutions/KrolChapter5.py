# Dictionaries:
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

# Final dictionary:
dic4={}


def append_dictionary(dictionary1, dictionary2):
    dictionary1.update(dictionary2)


print('List of dictionaries for concatenate:\n' + str(dic1) + '\n' + str(dic2) + '\n' + str(dic3))

append_dictionary(dic4, dic1)
append_dictionary(dic4, dic2)
append_dictionary(dic4, dic3)


print('Concatenate of the dictionary results as:\n' + str(dic4))