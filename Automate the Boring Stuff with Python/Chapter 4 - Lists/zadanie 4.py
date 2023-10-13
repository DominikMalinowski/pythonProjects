##
spam = ['jabłka', 'banany', 'tofu', 'koty']
newlist = []

def function(list):
    result = ''
    for i in spam[:-1]:
        result += str(i) + ', '
    result += 'i ' + list[-1]
    return result

print(function(spam))

##
grid = [['.','.','.','.','.','.',],
        ['.','0','0','.','.','.',],
        ['0','0','0','0','.','.',],
        ['0','0','0','0','0','.',],
        ['.','0','0','0','0','0',],
        ['0','0','0','0','0','.',],
        ['0','0','0','0','.','.',],
        ['.','0','0','.','.','.',],
        ['.','.','.','.','.','.',]]

for i in range(6):
        for row in grid:
                print(row[i],end='')
        print()