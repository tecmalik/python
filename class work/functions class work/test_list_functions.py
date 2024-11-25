from unittest import TestCase
import get_switched_list_function



class GetSwitchedList(TestCase):
	def test_if_get_switched_list_function_exist(self):
		get_switched_list_function.get_switched_list([232] , 1)
	
	def test_if_get_switched_list_function_takes_in_two_parameters_(self):
		get_switched_list_function.get_switched_list([232] , 2)
	def test_if_get_switched_list_function_returns_correct_value(self):
		value = get_switched_list_function.get_switched_list([12345] , 2)
		expected = [45123]
		self.assertEqual(value,expected)

	


import is_even_list_function
class IsEvenListFunction(TestCase):
	def test_if_is_even_list_function_exists(self):
		is_even_list_function.is_even_list([1,2,3,4])
	def test_if_is_even_list_function_returns_a_value(self):
		is_even_list_function.is_even_list([1,2,3,4])
		self.assertTrue
	def test_if_is_even_list_function_returns_a_list(self):
		value = is_even_list_function.is_even_list([1,2,3,4])
		expected =[False,True,False,True] 
		self.assertEqual(value,expected)
	def test_if_is_even_list_function_returns_a_correct_value(self):
		value = is_even_list_function.is_even_list([1,2,3,4,90])
		expected =[False,True,False,True,True] 
		self.assertEqual(value,expected)

import breaking_a_list_function
class BreakingA_List(TestCase):
	def test_if_breaking_a_list_exist(self):
		breaking_a_list_function.breaking_a_list([1,2,3,4,5])
	def test_if_breaking_a_list_will_return_a_value(self):
		value = breaking_a_list_function.breaking_a_list([1,2,3,4,5])
		expected = [[1,2,3],[4,5]]
		self.assertEqual(value,expected)



