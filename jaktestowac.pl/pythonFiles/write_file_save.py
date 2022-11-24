

# file = open("./testFiles/fileToWrite.txt",'w')
import io

# file = open("./testFiles/fileToWrite.txt",'r')
# file.write('Hello jaktestowac.pl!')
# file.close()

try:
    file = open("./testFiles/fileToWrite.txt", 'r')
    file.write('Hello jaktestowac.pl!')
except io.UnsupportedOperation as UO:
    print(UO)
    print(f'Is file closed ? {file.closed}')
finally:
    print(f'Is file closed ? {file.closed}')
    file.close()
    print(f'Is file closed ? {file.closed}')

