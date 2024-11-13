from unittest import TestCase 
import divide_or_square 

class TestDivideorsquare(TestCase):
	def test_that_divide_or_square_exist(self):
		divide_or_square.get_divide_or_square(4)
		
	def test_that_the_divide_or_square_will_return_an_error_with_string_input_(self):
		value = divide_or_square.get_divide_or_square('A')
		expected = TypeError
		self.assertEqual(value ,expected)
	def test_that_the_divide_or_square_will_return_square_for_numbers_divisible_by_5_(self):
		value = divide_or_square.get_divide_or_square(10)
		expected = 3.16
		self.assertEqual(value ,expected)

	def test_that_the_divide_or_square_will_return_rimender_for_numbers_not_divisible_by_5_(self):
		value = divide_or_square.get_divide_or_square(11)
		expected = 1
		self.assertEqual(value ,expected)

	def test_that_the_divide_or_square_will_return_a_value_with_nagative_numbers_divisible_by_(self):
		value = divide_or_square.get_divide_or_square(-10)
		expected = valueerror
		self.assertEqual(value ,expected)
		
	