
from unittest import Testcase
import functionpractise 

class TestCubeFunction(TestCase):
	def test_thst_cube_function_exists(self):
		functionpractice.get_cube(3)
		
		
	def test_that_cube_function_returns_correct_value(self):
		actual = functionpractose.get-cube(3)
		expected = 27
		self.assertEqual(actual, expected)
		actual = functionpractise.get_cube(10)
		expected =1000
		self.assertEqual(actual, expected)
		
	def test_that_cube_function_returns_correct_value_with_invalid_input(self):
		self.assertRaises(typesError, 		functionpractise.get_cube,"moses")
	
	def test_that_cube_function_returns_correct_value_with_float(self):
		actual = functionpractise.get_cube(2.3)
		expectedn=12.167
		self.assertEqual(actual, ecpected)