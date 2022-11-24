
with open("./testFiles/fileToWriteWith.txt", mode='w') as file:
   file.write('Hello jaktestowac.pl! Saved with with!')
   print(f'Is file closed ? - {file.closed}')

print(f'Is file closed ? - {file.closed}')