from unittest import TestCase
import sum_of_list
	
	
class SumOfList(TestCase):
	def test_if_the_function_sum_of_list_exist_(self):
		number = [2,3,2,3,5,5]
		sum_of_list.get_sum_of_list(number)
	
	def test_if_the_function_sum_of_list_works_(self):
		number = [2,3,2,3,5,5]
		value = sum_of_list.get_sum_of_list(number)
		expected = 20
		self.assertEqual(value, expected)
		number = [-2,-3,-2,-3,-5,-5]
		value = sum_of_list.get_sum_of_list(number)
		expected = -20
		self.assertEqual(value, expected)
	def test_if_the_function_will_return_values_for_nagative(self):
		number = [-2,-3]
		value = sum_of_list.get_sum_of_list(number)
		expected = -5
		self.assertEqual(value, expected)
	def test_if_the_function_will_return_values_for_nagative_for_float(self):
		number = [-2.5,-3.5]
		value = sum_of_list.get_sum_of_list(number)
		expected = -6
		self.assertEqual(value, expected)