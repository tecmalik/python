from unittest import TestCase
import kala_function 

class KalaFunction(TestCase):
	def test_if_isEven_exist(self):
		kala_function.isEven(2)
	def test_if_isEven_will_return_a_boolen(self):
		value=kala_function.isEven(2)
		self.assertTrue
	def test_if_isEven_will_return_false(self):
		value = kala_function.isEven(3)
		expected = False
		self.assertEqual(value,expected)
	
	def test_if_isPrime_exist(self):
		kala_function.isEven(2)
	def test_if_isPrime_will_return_a_boolen(self):
		value=kala_function.isPrime(7)
		self.assertTrue
	def test_if_isPrime_will_return_false(self):
		value = kala_function.isPrime(4)
		expected = False
		self.assertEqual(value,expected)
	def test_if_isPrime_will_return_true(self):
		value = kala_function.isPrime(7)
		expected = True
		self.assertEqual(value,expected)
	
	def test_if_subtract_function_exist(self):
		kala_function.subtract(2,4)
	def test_if_subtract_will_return_a_value(self):
		value = kala_function.subtract(5,2)
		expected = 3
		self.assertEqual(value,expected)
	def test_if_subtract_will_return_a_pisitive(self):
		value = kala_function.subtract(5,2)
		expected = 3
		self.assertEqual(value,expected)
	def test_if_subtract_will_return_a_value_if_switched(self):
		value = kala_function.subtract(7,3)
		expected = 4
		self.assertEqual(value,expected)
		value = kala_function.subtract(3,7)
		expected = 4
		self.assertEqual(value,expected)
	
	def test_if_divide_function_exist(self):
		kala_function.divide(4,4)
	def test_if_divide_function_will_return_a_value(self):
		value = kala_function.divide(4,4)
		expected = 1.0
		self.assertEqual(value,expected)
	def test_if_divide_function_with_nagative_integers(self):
		value = kala_function.divide(-4,4)
		expected = -1.0
		self.assertEqual(value,expected)
	
	def test_if_divide_function_with_take_float_and_integers(self):
		value = kala_function.divide(-4.6,4)
		expected = -1.15
		self.assertEqual(value,expected)
	



	def test_if_factorOfNumber_function_exist(self):
		kala_function.factorOfNumber(10)
	def test_if_factorOfNumber_function_will_return_a_value(self):
		value = kala_function.factorOfNumber(10)
		expected = ([1,2,5,10])
		self.assertEqual(value,expected)
	def test_if_factorOfNumber_function_will_return_integer(self):
		value = kala_function.factorOfNumber(10)
		expected = ([1,2,5,10])
		self.assertEqual(value,expected)
	
	def test_if_factorOfNumber_function_returns_a_list(self):
		value = kala_function.factorOfNumber(12)
		expected = ([1,2,3,4,6,12])
		self.assertEqual(value,expected)

	def test_if_isSquare_function_exist(self):
		kala_function.isSquare(10)
	def test_if_isSquare_will_return_a_boolen(self):
		value=kala_function.isSquare(6)
		self.assertTrue
	def test_if_isSquare_will_return_false(self):
		value = kala_function.isSquare(7)
		expected = False
		self.assertEqual(value,expected)
	def test_if_isSquare_will_return_True(self):
		value = kala_function.isSquare(25)
		expected = True
		self.assertEqual(value,expected)




	