import os


def create_new_file(pathname):
    """
    Function to check if given file exists, it not, it'll create it
    :param pathname: path of new file
    :return: print
    """
    if not os.path.exists(pathname):
        file = open(pathname, 'w+')
        file.write('one\ntwo\nthree')
        return print('File has been created: %s'% pathname)
    else:
        return print('File exists: %s' % pathname)


def remove_existed_file(pathname):
    """
    Function to check if given file exists, it not, it'll create it
    :param pathname: path of existed file
    :return: print
    """
    try:
        os.remove(pathname)
        return print('File has been removed successfully')
    except NameError:
        return print('File deletion failed')


path = '.\\data.txt'
create_new_file(path)

list_ = []
with open(path, 'r') as f:
    for i in f:
        x = i.split()
        list_.extend(x)
print('Show contents of the file:\n' + '\n' + str(list_))
remove_existed_file(path)

