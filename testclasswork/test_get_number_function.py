from unittest import TestCase
import get_number_function

class GetNumber(TestCase):
	def test_if_get_number_function_exit(self):
		get_number_function.get_number(24 , [12,17,24,32,14])

	def test_if_get_number_function_returns_a_value_(self):
		value = get_number_function.get_number(24 , [12,17,24,32,14])
		expected = 2
		self.assertEqual(value, expected)

	def test_if_get_number_function_returns_a_correct_index_value_(self):
		value = get_number_function.get_number(24 , [12,17,24,32,14])
		expected = 2
		self.assertEqual(value, expected)
	def test_if_get_number_function_returns_a_value_(self):
		value = get_number_function.get_number( 24 , [12,17,24,32,14])
		expected = 2
		self.assertEqual(value, expected)
	

	
	def test_if_get_positive_nagative_numbers_exist(self):
		get_number_function.get_positive_nagative_numbers([15,34,-1,24,-7,9])
	def test_if_get_positive_nagative_numbers_returns_a_correct_value(self):
		value = get_number_function.get_positive_nagative_numbers([15,34,-1,24,-7,9])
		expected = 4,2,0
		self.assertEqual(value, expected)
	
