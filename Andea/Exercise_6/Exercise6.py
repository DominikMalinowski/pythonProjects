"""
adjust your solution for chapter 4, and allow user to put the list with ; as a delimiter.
You should also remove white spaces from the imput.
"""

colors_list = "Red ; Green ; White ; Black ; Pink ; Yellow"
elements = [1, 4, 5]


def remove_element_modified(input_list, removed_elements):

    # removing all white spaces from input
    input_list = input_list.replace(' ', '')

    # splitting input list with ';' symbol
    input_list = input_list.split(";")

    # code to remove 1st, 4th and 5th element
    for i in reversed(removed_elements):
        input_list.remove(input_list[i])

    # sorting edited list
    input_list.sort()

    # printing finished list
    print(input_list)


remove_element_modified(colors_list, elements)

