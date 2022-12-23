def Chapter5(dict1, dict2):
    for x in dict2: #for all keys in dictionary 1
        dict1[x] = dict2[x] #create same key and assign its value
    return dict1 #return dictionary

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
newdict = Chapter5(dic1, dic2)
newdict = Chapter5(newdict, dic3)
print(newdict)