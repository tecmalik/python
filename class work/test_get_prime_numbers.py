from unittest import TestCase
import get_prime_numbers_function

class GetPrimeNumbers(TestCase):
	def test_if_get_prime_numbers_exist(self):
		get_prime_numbers_function.get_prime_numbers(20)
	def test_if_get_prime_numbers_will_return_a_value(self):
		value = get_prime_numbers_function.get_prime_numbers(20)
		expected = ([2,3,5,7,11,13,17,19])
		self.assertEqual(value, expected)
