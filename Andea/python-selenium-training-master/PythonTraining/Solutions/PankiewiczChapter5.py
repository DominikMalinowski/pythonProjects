# V 1.1 - 14.05.2019
"""
Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
#creating of new dictionaries
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

def margingDict():

    # creating of a new dictionary. If it is created by combining more, than one dictionary- we ned to put '**' before name of every component dictionary
    dic4 = {**dic1, **dic2, **dic3}

    #function will return new dictionary- "dic4"
    return(dic4)


#calling function
print(margingDict())