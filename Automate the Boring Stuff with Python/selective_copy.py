#! python 3

import shutil, os
path = ('C:\\Users\\DELL\\Desktop\\pythonProject\\venv')
exten = ('.exe')


def selective_copy(path, extension):
    # TODO: going through dic tree
    for folders, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(exten):
                # TODO: copy finded files to backup catalog
                backup = path + '\\backup'
                if not os.path.exists(backup):
                    os.makedirs(backup)
                shutil.copy(filename,backup)

selective_copy(path, exten)