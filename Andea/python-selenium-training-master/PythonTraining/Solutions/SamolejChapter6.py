#Write a Python program to print a specified list after removing the 1th, 4th and 5th elements. The results should be sorted.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Black', 'Red', 'White']

#Adjust your solution for chapter 4, and allow user to put the list with ; as a delimiter. You should also remove white spaces from the input.

list = []

def inputIntoList():
    print ("Input new elements. You can separate them by semi-colon. Spaces will be deleted.")

    data = input()
    data = data.replace(' ', '')

    list= data.split(';')
    return list


def delete(length, list):
    if length >=6 :
        del list[5]
    if length >=5:
        del list[4]
    if length >=2:
        del list[1]




list.sort()

length = len(list)

list = inputIntoList()
print (list)
print ("List length:" + str(length) + "\n")

delete (length, list)

print (list)
print ("List length:" + str(len(list)))