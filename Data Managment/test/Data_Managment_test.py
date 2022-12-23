import unittest
import DataManagment_2 as DM2
import os 

class Data_Managment_Test():
    def is_abs_path_test():
        if os.path.isabs(DM2.new_folder_abspath) == True:
            print('ok')
        else: 
            print('test has failed!')


