import os
import shutil
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import Selenium.Utilities.Logger as ml

class FileHandler():
    """
    FileHandler class stores all methods that can be used for XML/PAS file handling
    e.g. upload new XML file, or check if XML/PAS file has been generated correctly
    """

    # Create logger object
    logsfl = ml.MESlogger()

    # Get needed, constant data
    FILES_PATH = os.path.dirname(os.getcwd()) + "\\Utilities\\Files"

    #QUEUE_PATH = jsonHandler.getDataFromConfiguration('QUEUE_PATH')
    #OUTPUT_PATH = jsonHandler.getDataFromConfiguration('OUTPUT_PATH')
    #PRINTER_SHARE_PATH = jsonHandler.getDataFromConfiguration('PRINTER_SHARE_PATH')

    def copyFile(self, folder_name, file_name, destination_path=None):
        """
        Copy file from one folder to another one.
        If destination_path is empty, file will be copied to the same folder.
        If not, file will be copied to destionation_path
        """
        try:
            if destination_path == None:
                shutil.copy(os.path.join(self.FILES_PATH, folder_name, file_name), os.path.join(self.FILES_PATH, folder_name, file_name + " - CopyTest.xml"))
                self.logsfl.info("New file has been created! Folder name: " + folder_name + ", File name: " + file_name + " - CopyTest.xml")
            else:
                shutil.copy(os.path.join(self.FILES_PATH, folder_name, file_name), os.path.join(destination_path, file_name))
                self.logsfl.info("File has been copied to Destination path (" + destination_path + ")! Folder name: " + folder_name + ", File name: " + file_name)
        except Exception as ex:
            self.logsfl.exception("File copying failed! Folder name: " + folder_name + ", File name: " + file_name + "\nException occured: " + str(ex))

    def deleteFile(self, folder_name, file_name):
        """ Delete given file """
        try:
            if os.path.exists(os.path.join(self.FILES_PATH, folder_name, file_name)):
                os.remove(os.path.join(self.FILES_PATH, folder_name, file_name))
                self.logsfl.info("File has been deleted! Folder name: " + folder_name + ", File name: " + file_name)
            else:
                self.logsfl.info("File deleting failed! Folder name: " + folder_name + ", File name: " + file_name)
        except:
            self.logsfl.exception("File deleting failed! Folder name: " + folder_name + ", File name: " + file_name)

    def checkIsFileGenerated(self, path, encoding='UTF-8', *strings_in_file):
        """
        It's a base method.
        Return True if proper file has been generated, False if not.
        Check if file has been generated in path by taking 3 newest
        files and looking for specific strings - from arguments
        """

        # Sorting files from path by time. Get files (and directories) and their dates and save into files variable
        files = sorted(os.listdir(path), key=lambda x: os.path.getctime(os.path.join(path, x)))

        # Check if it's file (not directory) and if yes then add to three_newest_file.
        # file_no variable is number of files currently stored in three_newest_files variable
        # file_number_on_list variable is number of file in the list, which will be checked. -1 means the newest one.
        three_newest_files = []
        file_no = 0
        file_number_on_list = -1
        while file_no < 3:
            if os.path.isfile(os.path.join(path, files[file_number_on_list])):
                three_newest_files.append((files[file_number_on_list]))
                file_number_on_list -= 1
                file_no += 1
            else:
                file_number_on_list -= 1

        # Check if one of three_newest_files is file that we are looking for (whether there are all required statements)
        # If yes - return True, if not - return False
        for file in three_newest_files:
            found_strings = 0
            for string in strings_in_file:
                with open(os.path.join(path, file), encoding=encoding) as myfile:

                    if string in myfile.read():
                        self.logsfl.info("Statement '" + string + "' has been found in the file: " + file)
                        found_strings += 1
                    else:
                        self.logsfl.info("Statement '" + string + "' has not been found in the file: " + file + ". Stop searching in this file")
                        break

            if found_strings == len(strings_in_file):
                self.logsfl.info("File has been generated! Name of file: " + file)
                return True

        return False
