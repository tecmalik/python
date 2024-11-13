from unittest import TestCase
import multiplenumbersfunction

class TestMultipleNumbers(TestCase):
	def test_the_new_mutiple_Of_number_existance(self):
		multiplenumbersfunction.get_multiple(4,3)
		
	def test_multiple_numbers_function_if_it_returns_actual_value(self):
		value=multiplenumbersfunction.get_multiple(4,3)
		expected = 12
		self.assertEqual(value , expected)
		
	def test_multiple_numbers_function_if_passed_a_float_value(self):
		multiplenumbersfunction.get_multiple(4.4,3)
	
	
	
				
				