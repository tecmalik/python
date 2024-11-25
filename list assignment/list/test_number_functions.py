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
		is_largest_function.is_largest(34)
