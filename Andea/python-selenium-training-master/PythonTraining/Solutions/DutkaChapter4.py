# remove 1st, 4th and 5th element in the list
def remove_items(list_):
    try:
        del list_[4]
        del list_[3]
        del list_[0]
    except IndexError:
        return
    sorted_list = list_.sort()
    return sorted_list


userInput = []
item = ''
# ask the user to enter elements and create list
print('Enter at least 5 items which will be added to the list. To end the process write \"q\":')
while item != 'q':
    item = input()
    if item == ' ':
        continue
    elif item != 'exit':
        print('Next item')
        userInput.append(item)
# count list's length
input_len = len(userInput)
print('Your list has ' + str(input_len) + ' elements and contains: ' + str(userInput))
# check if the list has a proper length and if so, use the function and remove elements
if input_len < 5:
    print('Your list is too short to remove elements')
else:
    remove_items(userInput)
    print('Your list after removing operation:' + str(userInput))

