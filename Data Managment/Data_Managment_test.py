import unittest
import data_managment_2 as DM2
import os

class Data_Managment_Test(unittest.TestCase):
	
	def is_abs_path_test(self):
		if os.path.isabs(DM2.new_folder_abspath) == True:
			print('ok1')
		else: 
			print('test has failed!')

        
	def is_path_exist_test(self):
		if os.path.exists(DM2.new_folder_path) == True:
			print('ok2')
		else:
			print("Test failed")
