#Using re module, find all e-mail adresses in given string.
#Hint: .findall method doesn't work well with groups in regular expressions :)

import re

#text
text = """
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""


#create new list, with text (without spaces and new lines, each word = new element)
def inputIntoList(text):
    text = text.replace('\n', '')
    list= text.split(' ')
    return list



#parameters
eRegEx = re.compile(r'[\w\.-]+@[\w\.-]+')


list = inputIntoList(text)
newlist = []

#search all emails
length = len(list)
for i in range(length):
    if eRegEx.search(list[i]):
        newlist.append(eRegEx.search(list[i]))
    i += 1
 

# In this example, we know that our pattern will be found in the string, so we know that a Match object will be returned. 
# Knowing that newlist contains a Match object and not the null value None, we can call group() on newlist to return the match. 

length = len(newlist)
for i in range(length):
    newlist[i]= newlist[i].group()


print(newlist)
