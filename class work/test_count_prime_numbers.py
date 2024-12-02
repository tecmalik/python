from unittest import TestCase
import count_prime_numbers

class CountPrimeNumbers(TestCase):
	def test_if_count_prime_numbers_exist(self):
		value = count_prime_numbers.get_count_prime_numbers([10,3,7,1,9,4,2,8,5,6])
		ecpected = [True,False,False,False,False]


