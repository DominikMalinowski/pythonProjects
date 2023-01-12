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


# function taking multiple arguments
def concatenate_dictionaries(*dictionary):
    last_dic = {}
    for dic in dictionary:
        last_dic.update(dic)
    print(last_dic)


concatenate_dictionaries(dic1, dic2, dic3)
