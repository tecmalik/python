from unittest import TestCase
import tigernuts1
	
	
class TestGetSum(TestCase):
	def test_if_get_even_sum_exist(self):
		tigernuts1.get_even_sum([123])
		
	def test_if_get_even_sum_will_return_a_value(self):
		number = [1,2,3,4,5]
		value = tigernuts1.get_even_sum(number)
		expected = 6
		self.assertEqual(value,expected)

	def test_if_get_even_sum_will_return_a__correct_value(self):
		number = [1,2,3,4,5]
		value = tigernuts1.get_even_sum(number)
		expected = 6
		self.assertEqual(value,expected) 