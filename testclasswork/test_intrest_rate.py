from unittest import TestCase
import interest_rate


class InterestRate(TestCase):
	def test_if_the_interest_rate_finction_is_present(self):
		interest_rate.get_interest_rate(2,3,4)
	
	def test_if_the_interest_rate_is_will_produce_a_value(self):
		value = interest_rate.get_interest_rate(2,2,4)
		expected = round(value,4)
		self.assertEqual(value, expected)
	def test_if_the_interest_rate_is_will_produce_a_typ_error_with_a_string_as_first_input(self):
		value = interest_rate.get_interest_rate('a',2,4)
		expected = typeError
		self.assertEqual(value, expected)
	def test_if_the_montly_interest_is_will_produce_a_typ_error_with_a_string_as_second_input(self):
		value = interest_rate.get_interest_rate(2,'a',4)
		expected = typeError
		self.assertEqual(value, expected)
	def test_if_the_year_input_is_will_produce_a_typ_error_with_a_string_as_third_input(self):
		value = interest_rate.get_interest_rate(4,2,'a')
		expected = typeError
		self.assertEqual(value, expected)
	def test_if_the_interest_rate_is_will_produce_a_type_error_with_a_float(self):
		value = interest_rate.get_interest_rate(2.5,2,4)
		expected = round(value,4)
		self.assertEqual(value, expected)