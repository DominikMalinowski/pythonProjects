#  dictionaries to concatenate
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}


print('There are 3 dictionaries: \n' + str(dic3) + '\n' + str(dic1) + '\n and\n' + str(dic2))
print('Let\'s merge them together')
for x in range(2):
    print('~`!'*6)
    x = x+1

dic4 = {}
# update
for i, j in dic1.items():
    dic4.setdefault(i, j)
for i, j in dic2.items():
    dic4.setdefault(i, j)
for i, j in dic3.items():
    dic4.setdefault(i, j)

print('Merged dictionary: ' + str(dic4))