from unittest import TestCase
import my_discount
	
class MyDiscount(TestCase):
	def test_if_my_discount_exist(self):
		my_discount.getmy_discount(5 , 6)
	
	def test_if_my_discount_returns_a_value_(self):
		value = my_discount.getmy_discount(150 , 15)
		expected = 127.5
		self.assertEqual(value,expected)

	def test_if_my_discount_returns_a_correct_value_(self):
		value = my_discount.getmy_discount(150 , 15)
		expected = 127.5
		self.assertEqual(value,expected)

	def test_if_my_discount_returns_a_correct_value_with_floats(self):
		value = my_discount.getmy_discount(150.67 , 15.5)
		expected = 127.316 
		self.assertEqual(value,expected)

	def test_if_my_discount_returns_a_correct_value_with_a_single_float_(self):
		value = my_discount.getmy_discount(150.5 , 15.5)
		expected =127.172
		self.assertEqual(value,expected)
	
	def test_if_my_discount_returns_a_correct_value_with_a_chr_(self):
		value = my_discount.getmy_discount('A' , 15.5)
		expected = None
		self.assertEqual(value,expected)