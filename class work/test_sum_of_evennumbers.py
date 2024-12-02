from unittest import TestCase
import sum_of_evennumbers_function

class SumOfEvennumbers(TestCase):
	def test_if_sum_of_evennumbers_test_exist(self):
		sum_of_evennumbers_function.sum_of_evennumbers([2,3,4,5,6])
	def test_if_sum_of_evennumbers_will_return_a_value(self):
		value = sum_of_evennumbers_function.sum_of_evennumbers([2,7,9,17,19,2,8,10])
		expected = 22
		self.assertEqual(value, expected)
	def test_if_sum_of_evennumbers_will_return_a_correct_value(self):
		value = sum_of_evennumbers_function.sum_of_evennumbers([2,7,9,17,19,2,8,10])
		expected = 22
		self.assertEqual(value, expected)
	def test_if_sum_of_evennumbers_will_return_a_correct_positive_value(self):
		value = sum_of_evennumbers_function.sum_of_evennumbers([2,7,9,17,19,2,8,10])
		expected = 22
		self.assertEqual(value, expected)

			