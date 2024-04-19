
try:
   with open("./testFiles/fileToWriteWith.txt", 'r') as file:
      file.write('Hello jaktestowac.pl! Saved with with!')
except Exception as e:
   print(f'Exception: {e}')
finally:
   print(f'In block "finally". Is file closed? {file.closed}')