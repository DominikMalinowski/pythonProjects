
# initial list
userInput = input("Put the list with ';' as a delimiter :")

# split and remove white spaces
inputList = [el.strip() for el in userInput.split(';')]
# remove 1, 4 and 5 element from the list

inputList = [x for (i,x) in enumerate(inputList) if i not in (1,4,5)]

# sort the list
inputList.sort()

# print the content of the list
print(inputList)

