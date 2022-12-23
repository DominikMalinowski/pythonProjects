import unittest
import DataManagment_2 as DM2
import os 

class Data_Managment_Test(unittest):
    def is_abs_path_test():
        os.path.isabs(DM2.new_folder_abspath) == True