

initial_list = 'Red; Green; White; Black; Pink; Yellow'


# Function to split string into list, and to strip white spaces for each element
# parameter: input_str - string containing unchanged initial list
# return: modified_list - list containing elements gathered from input without the whitespaces
def modifyInput (input_str):

    modified_list = (input_str.split(";"))

    for i in range(len(modified_list)):
        modified_list[i] = modified_list[i].strip()

    return modified_list

# Function to erase elements with specified index from the list
# parameter: input_list - list containing all elements
# return: input_list - list containing list without specified elements
def newList (input_list):
    erase_index = [1, 4, 5]
    elements_to_erase = []

    for j in erase_index:
        elements_to_erase.append(input_list[j])

    for i in elements_to_erase:
        input_list.remove(i)

    input_list.sort()

    return input_list

#
modified_list = modifyInput(initial_list)
new_list = newList(modified_list)

print(initial_list)
print(new_list)

