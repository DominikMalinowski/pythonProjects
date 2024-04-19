""" Adjust your solution for chapter 4, and allow user to put the list with ;
as a delimiter. You should also remove white spaces from the imput. """

def userlist(inputlist):

    # input a list separated by ; - moved out of function definition
    # inputlist = input('Enter a list element separated by ; ')

    # remove white spaces
    inputlist = inputlist.replace(" ","")
    print('\n' + 'White spaces have been removed: ', inputlist)

    inputlist = inputlist.split(";")
    print('Your list: ', inputlist)

    # remove empty element from the list
    list5 = list(filter(None, inputlist))
    print('Your list without empty element: ', list5)

    # remove 1 st, 4th and 5th elements from the list
    del list5[5]
    del list5[4]
    del list5[1]

    print('Your list without 1st, 4th and 5th elements: ', list5)

    # sort list
    list5.sort()
    print('Your sorted list: ',list5)

userinput = input('Enter a list element separated by ; ')
userlist(userinput)


