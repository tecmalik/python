from unittest import TestCase
import is_even_number_function

class IsEvenNumberFunction(TestCase):
	def test_if_is_even_number_function_exist(self):
		is_even_number_function.is_even(23)
	def test_if_is_even_number_function_returns_false(self):
		is_even_number_function.is_even(23)
		self.assertFalse
	def test_if_is_even_number_function_returns_true(self):
		is_even_number_function.is_even(2)
		self.assertTrue
	def test_if_is_even_number_function_returns_correct_value_(self):
		value = is_even_number_function.is_even(23)
		expected = False
		self.assertEqual(value,expected)
		value = is_even_number_function.is_even(2)
		expected = True
		self.assertEqual(value,expected)


import is_prime_function

class IsPrimeFunction(TestCase):
	def test_is_prime_function_exist(self):
		is_prime_function.is_prime_(22)
	def test_is_prime_function_returns_a_boolen(self):
		is_prime_function.is_prime_(22)
		self.assertFalse 
	def test_is_prime_function_returns_a_false(self):
		value = is_prime_function.is_prime_(22)
		expected = False
		self.assertEqual(value,expected)
	def test_is_prime_function_returns_a_true(self):
		value = is_prime_function.is_prime_(23)
		expected = True
		self.assertEqual(value,expected)


import is_largest_function

class IsLargestFunction(TestCase):
	def test_if_is_largest_function_exist(self):
		is_largest_function.is_largest([3,4,5])
	def test_if_is_largest_function_return_an_int(self):
		value = is_largest_function.is_largest([2,3,4,5])
		expected = 5
		self.assertEqual(value,expected)
	def test_if_is_largest_function_return_correct_vlue(self):
		value = is_largest_function.is_largest([2,3,4,5])
		expected = 5
		self.assertEqual(value,expected)



import reverse_of_list_function

class IsreverseOfList(TestCase):
	def test_reverse_of_list_function_exist(self):
		reverse_of_list_function.reverse_of_list([2,3])

	def test_reverse_of_list_function_return(self):
		value = reverse_of_list_function.reverse_of_list([2,3])
		expected = [3,2]
	def test_reverse_of_list_reverses(self):
		value = reverse_of_list_function.reverse_of_list([2,3])
		expected = [3,2]

	
		
import checking_element_function

class CheckingElement(TestCase):
	def test_checking_element_function_exist(self):
		checking_element_function.checking_element([2,3],2)
	
	def test_checking_element_function_returns_boolean(self):
		checking_element_function.checking_element([2,3],2)
		self.assertTrue

	def test_checking_element_function_returns_true(self):
		value = checking_element_function.checking_element([2,3] ,2)
		expected = True
		self.assertEqual(value,expected)
	def test_if_checking_element_function_returns_false(self):
		value = checking_element_function.checking_element([2,3] , 22)
		expected = False
		self.assertEqual(value,expected)


import element_with_even_position_function

class ElementWithEvenPosition(TestCase):
	def test_if_element_with_even_position_exist(self):
		element_with_even_position_function.element_with_even_position([2,3,4,5])

	def test_if_element_with_even_position_will_return_a_list(self):
		value = element_with_even_position_function.element_with_even_position([2,3,4,5,6])
		expected = ([4,6])
		self.assertEqual(value,expected)
	def test_if_element_with_even_position_will_return_a_correct_value(self):
		value = element_with_even_position_function.element_with_even_position([2,3,4,5,4,5,6])
		expected = ([4,4])
		self.assertEqual(value,expected)

	











