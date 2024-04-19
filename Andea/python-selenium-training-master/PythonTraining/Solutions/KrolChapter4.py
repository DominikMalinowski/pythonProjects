# Function that removes specified list values and sort them
def list_converter(user_list):
    try:
        del user_list[5]
        del user_list[4]
        del user_list[1]
    except IndexError:
        try:
            del user_list[4]
            del user_list[1]
        except:
            try:
                del user_list[1]
            except:
                print('Yor list has only single element')
    user_list.sort(key=str.lower)
    print(user_list)


# Variables
number = 1
ulist = []

# Ask user for a list
while True:
    print('Please provide ' + str(number) + ' list value (if you don\'t want to put any more  provide q)')
    answer = input()
    if answer == 'q':
        break
    else:
        ulist.append(str(answer))
        number += 1

list_converter(ulist)
