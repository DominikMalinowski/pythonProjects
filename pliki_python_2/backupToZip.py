#! python3
# backupToZip.py - creating incremented backup for specific directory

import zipfile, os
def backupToZip(path):
    # covering path to absolute path
    path = os.path.abspath(path)

    number = 1
    while True:
        zipFileName = os.path.basename(path) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1

    # TODO creating .zip file
    print('Creating .zip file %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # TODO getting through all dictionary and compressing all files
    for foldername, subfolders, filenames in os.walk(path):
        print('Dodawanie plików w %s ...' %(foldername))
        # adding current dictionary to catalog
        backupZip.write(foldername)
        # adding all files in catalog to .zip archive
        for filename in filenames:
            newBase = os.path.basename(path) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # in archive there's only archive files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
