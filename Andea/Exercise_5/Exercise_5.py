"""
Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
result_dictionary = {}
   
def concatenate_dictionary(*dictionary):
    """ 
    Function combining any number of dictionaries into one 
    :param: dictionaries to combine
    :return: combined dictionary 
    """
    for dic in dictionary:
        result_dictionary.update(dic)
    return result_dictionary

print(concatenate_dictionary(dic1,dic2,dic3))