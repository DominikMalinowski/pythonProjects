
# Content:
# - if statement
# - else statement
# - elif statement
# - 'while' loop 
# - breaking infinity loop
# - continue the loop 
# - for and in range
# - range arguments 
# - exiting the programm 


# if statement
data = True

if data == True:
    print('Yes')

# else statement
data = False

if data == True:
    print('Yes')
else:
    print('No')

# elif statement
data = '50/50'

if data == True:
    print('Yes')
elif data == '50/50':
    print('Maybe')
else:
    print('No')

# 'while' loop 
counter = 0
while counter < 5:
    print('Add one')
    counter += 1

# breaking infinity loop
while True:
    print('To infinity and beyond')
    break

# continue the loop 
while True:
    print('Provide data')
    data = input()
    if data != 'stop':
        continue
    print('Terminated')
    break

# for and in range
for i in range(5):
    print('dot')

# range arguments 
for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)

# exiting the programm 
import sys

while True:
    print('Type "exit" to close program')
    data = input()
    if data == 'exit':
        sys.exit()
    else:
        print(data)