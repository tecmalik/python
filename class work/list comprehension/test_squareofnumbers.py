from unittest import TestCase
import squareofnumbers_function

class SquareofNumbers(TestCase):
	def test_if_squareofnumbers_function_exist(self):
		squareofnumbers_function.squareofnumbers(4)

	def test_if_squareofnumbers_function_returns_a_value(self):
		value = squareofnumbers_function.squareofnumbers(4)
		expected = [1,4,9,16]
		self.assertEqual(value, expected) 

	def test_if_numbersgreaterthan10_exixt(self):
		value = squareofnumbers_function.numbersgreaterthan10([1,5,12,15,8])
		expected = [12,15]
		self.assertEqual(value,expected)