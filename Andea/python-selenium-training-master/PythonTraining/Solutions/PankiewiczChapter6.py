# V 1.1 - 14.05.2019
"""
adjust your solution for chapter 4, and allow user to put the list with ; as a delimiter.
You should also remove white spaces from the imput.
"""

string1 = input("Type elements to the list, with ';' as a delimiter, and then press 'ENTER' : ")

#it removes all SPACES from string
string1 = string1.replace(" ", "")

#it creates string with content from string2 variable and its devides cells, where encounterrs ';' character
my_list = string1.split(";")

#deleting of empty elements from the list
my_list = list(filter(None, my_list))

print('\n' + "List with all of the elements, without sorting: ")
print(my_list)

#deleting of [5] element from the list
my_list.remove(my_list[5])
#deleting of [4] element from the list
my_list.remove(my_list[4])
#deleting of [1] element from the list
my_list.remove(my_list[1])

#sorting of the list
my_list.sort()


print('\n' + "List without 1,4 and 5 elements: ")
print(my_list)