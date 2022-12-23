""" Write a Python program to print a specified list after removing the 1th, 4th and 5th elements. The results should be sorted.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Black', 'Red', 'White'] """

def newlist(list):

    del list[5]
    del list[4]
    del list[1]
    list.sort()
    print(list)


list2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# check for another list
# list3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8' , '9']
newlist(list2)
