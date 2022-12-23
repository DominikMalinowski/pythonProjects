import unittest
import DataManagment_2 as DM2
import os 

class Data_Managment_Test(unittest.TestCase):
	def is_abs_path_test(new_folder_abspath):
		if os.path.isabs(DM2.new_folder_abspath) == True:
			print('ok')
		else: 
			print('test has failed!')

        
	def is_path_exist_test():
		if os.path.exists(DM2.new_folder_path) == True:
			pass
		else:
			print("Test failed")
